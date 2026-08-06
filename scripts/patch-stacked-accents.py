"""Lift the upper mark inside the fused stacked accents so its clearance over the
circumflex/breve stays constant across the weight axis.

The designers draw each Vietnamese stacked accent as one glyph holding two contours
(circumflex + hook/grave/acute/tilde).  As weight increases the lower mark gets much
wider but the upper mark is not raised to match, so the gap between them collapses -
for `choi` (used by e/a/o + hook above) it goes 46 -> 22 -> 10 units from Thin to
Black, which is what reads as a collision in the heavy weights.

Fix: translate the upper contour vertically, per master, so every master matches that
accent's own Thin clearance.  Thin is left untouched, so the designers' lightest-weight
intent is the reference.  Only node y-coordinates move - contour count, node count and
node order are unchanged, so master compatibility is preserved.
"""

import os
import re
import sys

import numpy as np
import glyphsLib
from PIL import Image
from drawbot_skia import drawbot as db

SRC = "sources/Onest.glyphs"
TMP = os.environ.get("TMPDIR", "/tmp")

ACCENTS = ["choi", "circumlfexhoi", "cflex", "cirkumflexgrave",
           "cacute.1", "circumflexacute", "ctilde", "circumlextilde",
           "aac", "abg",
           # drop 5 decomposed this one instead of moving the shared component,
           # so its private copy of the accent has to be lifted on its own.
           "Ecircumflexhoi"]

font = glyphsLib.load(open(SRC))
G = {g.name: g for g in font.glyphs}
MASTERS = [(m.id, m.name) for m in font.masters]


def layer(name, mid):
    for l in G[name].layers:
        if l.layerId == mid:
            return l
    return None


def contour_path(path, dy=0):
    bp = db.BezierPath()
    nodes = list(path.nodes)
    start = next(i for i, n in enumerate(nodes) if str(n.type) != "offcurve")
    nodes = nodes[start:] + nodes[:start]
    pt = lambda n: (n.position.x, n.position.y + dy)
    bp.moveTo(pt(nodes[0]))
    pending = []
    for i in range(1, len(nodes) + 1):
        n = nodes[i % len(nodes)]
        if str(n.type) == "offcurve":
            pending.append(pt(n))
        else:
            if len(pending) == 2:
                bp.curveTo(pending[0], pending[1], pt(n))
            elif len(pending) == 1:
                bp.qCurveTo(pending[0], pt(n))
            else:
                bp.lineTo(pt(n))
            pending = []
    bp.closePath()
    return bp


BOX = (-400, 300, 1000, 1400)
STEP = 2.0
W = int((BOX[2] - BOX[0]) / STEP)
H = int((BOX[3] - BOX[1]) / STEP)


def mask(bp):
    db.newDrawing()
    db.newPage(W, H)
    db.fill(1); db.rect(0, 0, W, H); db.fill(0)
    with db.savedState():
        db.scale(1 / STEP)
        db.translate(-BOX[0], -BOX[1])
        db.drawPath(bp)
    p = os.path.join(TMP, "_mask.png")
    db.saveImage(p)
    a = np.array(Image.open(p).convert("L")) < 128
    return a[::-1]


def clearance(accent, mid, dy=0):
    """Smallest vertical gap between the upper mark and the lower one.

    The two marks are the top-most contours, so this also works on a decomposed
    composite, where the base letter sits below them.
    """
    l = layer(accent, mid)
    ps = sorted(l.paths, key=lambda p: -max(n.position.y for n in p.nodes))
    upper = mask(contour_path(ps[0], dy))
    lower = mask(contour_path(ps[1]))
    best = None
    for x in range(W):
        u = np.where(upper[:, x])[0]
        d = np.where(lower[:, x])[0]
        if not len(u) or not len(d):
            continue
        gap = (u.min() - d.max()) * STEP
        if best is None or gap < best:
            best = gap
    return best


# ------------------------------------------------------------------ measure

lifts = {}
print("%-18s %-8s %8s %8s" % ("accent", "master", "clear", "lift"))
for accent in ACCENTS:
    if accent not in G:
        print("  %s missing, skipped" % accent)
        continue
    base = None
    for mid, mname in MASTERS:
        c = clearance(accent, mid)
        if c is None:
            print("%-18s %-8s   no vertical overlap" % (accent, mname))
            continue
        if base is None:          # first master (Thin) is the reference
            base = c
            lift = 0
        else:
            lift = max(0, int(round(base - c)))
        lifts[(accent, mid)] = lift
        print("%-18s %-8s %+8.0f %+8d" % (accent, mname, c, lift))
    print()

if os.path.exists(os.path.join(TMP, "_mask.png")):
    os.remove(os.path.join(TMP, "_mask.png"))

todo = {k: v for k, v in lifts.items() if v}
print("layers to patch: %d" % len(todo))
if not todo:
    sys.exit(0)

# ------------------------------------------------------------------ patch

lines = open(SRC).read().split("\n")
starts = [i for i, l in enumerate(lines) if l.startswith("glyphname = ")]
NODE = re.compile(r"^\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)(,[a-z]+)?\)(,?)$")

changed = 0
for (accent, mid), lift in todo.items():
    i = lines.index("glyphname = %s;" % accent)
    j = next((s for s in starts if s > i), len(lines))

    # locate the requested layer
    k = next(k for k in range(i, j) if lines[k] == 'layerId = "%s";' % mid)
    end = next((x for x in range(k + 1, j) if lines[x].startswith("layerId = ")), j)

    # collect every nodes=( ... ) run in this layer
    runs = []
    x = k
    while x < end:
        if lines[x] == "nodes = (":
            y = x + 1
            while lines[y] != ");":
                y += 1
            runs.append((x + 1, y))
            x = y
        x += 1
    if len(runs) < 2:
        sys.exit("%s/%s: expected 2 contours, found %d" % (accent, mid, len(runs)))

    def peak(run):
        lo, hi = run
        return max(float(NODE.match(lines[t]).group(2)) for t in range(lo, hi))

    # a decomposed composite also carries the base letter; the two accent contours
    # are the top-most ones, which is what clearance() measured as well
    upper, _lower = sorted(runs, key=peak, reverse=True)[:2]
    lo, hi = upper
    for t in range(lo, hi):
        m = NODE.match(lines[t])
        if not m:
            sys.exit("unparsed node line %d: %s" % (t + 1, lines[t]))
        nx, ny, typ, comma = m.group(1), float(m.group(2)), m.group(3) or "", m.group(4)
        ny = ny + lift
        ny = int(ny) if ny == int(ny) else ny
        lines[t] = "(%s,%s%s)%s" % (nx, ny, typ, comma)
        changed += 1

open(SRC, "w").write("\n".join(lines))
print("moved %d node lines" % changed)
