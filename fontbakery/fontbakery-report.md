## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[9] Onest-Medium.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three (U+0033): X=381.5,Y=1.0 (should be at baseline 0?)

	* S (U+0053): X=244.5,Y=705.5 (should be at cap-height 707?)

	* a (U+0061): X=288.5,Y=-1.0 (should be at baseline 0?)

	* j (U+006A): X=84.0,Y=-2.0 (should be at baseline 0?)

	* s (U+0073): X=335.5,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=251.0,Y=-1.0 (should be at baseline 0?)

	* section (U+00A7): X=362.0,Y=-0.5 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=100.0,Y=707.5 (should be at cap-height 707?)

	* uni00B3 (U+00B3): X=311.5,Y=707.5 (should be at cap-height 707?)

	* ordmasculine (U+00BA): X=112.0,Y=705.5 (should be at cap-height 707?)

	* ordmasculine (U+00BA): X=274.0,Y=705.0 (should be at cap-height 707?)

	* questiondown (U+00BF): X=156.0,Y=-1.0 (should be at baseline 0?)

	* Oslash (U+00D8): X=470.0,Y=705.0 (should be at cap-height 707?)

	* Oslash (U+00D8): X=294.0,Y=2.0 (should be at baseline 0?)

	* agrave (U+00E0): X=288.5,Y=-1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=288.5,Y=-1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=288.5,Y=-1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=288.5,Y=-1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=297.0,Y=706.0 (should be at cap-height 707?)

	* adieresis (U+00E4): X=288.5,Y=-1.0 (should be at baseline 0?)

	* aring (U+00E5): X=288.5,Y=-1.0 (should be at baseline 0?)

	* idieresis (U+00EF): X=-9.5,Y=707.5 (should be at cap-height 707?)

	* idieresis (U+00EF): X=78.0,Y=707.5 (should be at cap-height 707?)

	* idieresis (U+00EF): X=152.0,Y=707.5 (should be at cap-height 707?)

	* idieresis (U+00EF): X=239.5,Y=707.5 (should be at cap-height 707?)

	* eth (U+00F0): X=508.0,Y=706.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=392.5,Y=706.5 (should be at cap-height 707?)

	* otilde (U+00F5): X=393.5,Y=706.5 (should be at cap-height 707?)

	* amacron (U+0101): X=288.5,Y=-1.0 (should be at baseline 0?)

	* abreve (U+0103): X=288.5,Y=-1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=288.5,Y=-1.0 (should be at baseline 0?)

	* itilde (U+0129): X=209.5,Y=706.5 (should be at cap-height 707?)

	* ij (U+0133): X=307.0,Y=-2.0 (should be at baseline 0?)

	* jcircumflex (U+0135): X=84.0,Y=-2.0 (should be at baseline 0?)

	* Eng (U+014A): X=560.0,Y=-1.0 (should be at baseline 0?)

	* eng (U+014B): X=432.0,Y=-2.0 (should be at baseline 0?)

	* Sacute (U+015A): X=244.5,Y=705.5 (should be at cap-height 707?)

	* sacute (U+015B): X=335.5,Y=1.0 (should be at baseline 0?)

	* Scircumflex (U+015C): X=244.5,Y=705.5 (should be at cap-height 707?)

	* scircumflex (U+015D): X=335.5,Y=1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=244.5,Y=705.5 (should be at cap-height 707?)

	* scedilla (U+015F): X=335.5,Y=1.0 (should be at baseline 0?)

	* Scaron (U+0160): X=244.5,Y=705.5 (should be at cap-height 707?)

	* scaron (U+0161): X=335.5,Y=1.0 (should be at baseline 0?)

	* utilde (U+0169): X=384.5,Y=706.5 (should be at cap-height 707?)

	* uni0218 (U+0218): X=244.5,Y=705.5 (should be at cap-height 707?)

	* uni0219 (U+0219): X=335.5,Y=1.0 (should be at baseline 0?)

	* uni0237 (U+0237): X=84.0,Y=-2.0 (should be at baseline 0?)

	* tilde (U+02DC): X=95.5,Y=706.5 (should be at cap-height 707?)

	* tildecomb (U+0303): X=95.5,Y=706.5 (should be at cap-height 707?)

	* uni0405 (U+0405): X=241.0,Y=705.0 (should be at cap-height 707?)

	* uni040E (U+040E): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=242.0,Y=706.5 (should be at cap-height 707?)

	* uni0423 (U+0423): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=183.5,Y=1.5 (should be at baseline 0?)

	* uni043B (U+043B): X=17.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=17.0,Y=-1.0 (should be at baseline 0?)

	* uni0443 (U+0443): X=367.0,Y=-2.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=335.5,Y=1.0 (should be at baseline 0?)

	* uni0457 (U+0457): X=-9.5,Y=707.5 (should be at cap-height 707?)

	* uni0457 (U+0457): X=78.0,Y=707.5 (should be at cap-height 707?)

	* uni0457 (U+0457): X=152.0,Y=707.5 (should be at cap-height 707?)

	* uni0457 (U+0457): X=239.5,Y=707.5 (should be at cap-height 707?)

	* uni0458 (U+0458): X=84.0,Y=-2.0 (should be at baseline 0?)

	* quoteright (U+2019): X=192.0,Y=707.5 (should be at cap-height 707?)

	* arrowdown (U+2193): X=358.0,Y=-1.0 (should be at baseline 0?)

	* uni21BA (U+21BA): X=237.0,Y=0.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=704.5,Y=0.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<187.0,231.0>-<187.0,237.0>-<187.0,242.0>>

	* question (U+003F) contains a short segment B<<291.0,230.0>-<291.0,227.0>-<290.5,224.5>>

	* question (U+003F) contains a short segment B<<290.5,224.5>-<290.0,222.0>-<290.0,219.0>>

	* paragraph (U+00B6) contains a short segment L<<251.0,314.0>--<244.0,314.0>>

	* questiondown (U+00BF) contains a short segment B<<330.0,307.0>-<331.0,302.0>-<331.0,296.0>>

	* questiondown (U+00BF) contains a short segment B<<227.0,297.0>-<227.0,300.0>-<227.5,302.0>>

	* questiondown (U+00BF) contains a short segment B<<227.5,302.0>-<228.0,304.0>-<228.0,307.0>>

	* uni045E (U+045E) contains a short segment L<<87.0,-129.0>--<95.0,-129.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[9] Onest-SemiBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=276.0,Y=-1.0 (should be at baseline 0?)

	* three (U+0033): X=389.0,Y=2.0 (should be at baseline 0?)

	* f (U+0066): X=148.0,Y=708.5 (should be at cap-height 707?)

	* s (U+0073): X=337.5,Y=0.5 (should be at baseline 0?)

	* cent (U+00A2): X=245.0,Y=-1.0 (should be at baseline 0?)

	* cent (U+00A2): X=362.0,Y=-2.0 (should be at baseline 0?)

	* dieresis (U+00A8): X=468.5,Y=705.0 (should be at cap-height 707?)

	* dieresis (U+00A8): X=231.5,Y=705.0 (should be at cap-height 707?)

	* uni00B3 (U+00B3): X=317.5,Y=705.0 (should be at cap-height 707?)

	* Oslash (U+00D8): X=460.0,Y=708.0 (should be at cap-height 707?)

	* oslash (U+00F8): X=233.0,Y=1.0 (should be at baseline 0?)

	* sacute (U+015B): X=337.5,Y=0.5 (should be at baseline 0?)

	* scircumflex (U+015D): X=337.5,Y=0.5 (should be at baseline 0?)

	* scedilla (U+015F): X=337.5,Y=0.5 (should be at baseline 0?)

	* scaron (U+0161): X=337.5,Y=0.5 (should be at baseline 0?)

	* uni0219 (U+0219): X=337.5,Y=0.5 (should be at baseline 0?)

	* uni0405 (U+0405): X=242.5,Y=705.5 (should be at cap-height 707?)

	* uni040E (U+040E): X=115.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=115.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=240.5,Y=706.0 (should be at cap-height 707?)

	* uni0417 (U+0417): X=419.5,Y=705.5 (should be at cap-height 707?)

	* uni0423 (U+0423): X=115.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=115.0,Y=-1.0 (should be at baseline 0?)

	* uni0431 (U+0431): X=320.0,Y=706.5 (should be at cap-height 707?)

	* uni0437 (U+0437): X=186.0,Y=1.5 (should be at baseline 0?)

	* uni043B (U+043B): X=14.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=14.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=337.5,Y=0.5 (should be at baseline 0?)

	* quoteright (U+2019): X=204.5,Y=708.0 (should be at cap-height 707?)

	* quotedblright (U+201D): X=421.5,Y=708.5 (should be at cap-height 707?)

	* quotedblright (U+201D): X=204.5,Y=708.5 (should be at cap-height 707?)

	* uni20B4 (U+20B4): X=221.0,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=395.5,Y=707.5 (should be at cap-height 707?)

	* arrowdown (U+2193): X=365.0,Y=-2.0 (should be at baseline 0?)

	* uni21BA (U+21BA): X=236.5,Y=0.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=708.0,Y=0.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<304.0,239.0>-<303.0,235.0>-<303.0,232.0>>

	* question (U+003F) contains a short segment B<<303.0,232.0>-<303.0,229.0>-<303.0,225.0>>

	* paragraph (U+00B6) contains a short segment L<<243.0,314.0>--<233.0,314.0>>

	* questiondown (U+00BF) contains a short segment B<<220.0,289.0>-<221.0,292.0>-<221.0,295.0>>

	* questiondown (U+00BF) contains a short segment B<<221.0,295.0>-<221.0,298.0>-<221.0,302.0>>

	* uni045E (U+045E) contains a short segment L<<85.0,-114.0>--<95.0,-114.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[10] Onest-Thin.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* comma (U+002C): X=91.0,Y=-2.0 (should be at baseline 0?)

	* semicolon (U+003B): X=92.0,Y=-2.0 (should be at baseline 0?)

	* b (U+0062): X=244.0,Y=1.0 (should be at baseline 0?)

	* m (U+006D): X=222.0,Y=526.5 (should be at x-height 527?)

	* p (U+0070): X=250.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=147.0,Y=706.0 (should be at cap-height 707?)

	* braceright (U+007D): X=224.0,Y=706.0 (should be at cap-height 707?)

	* section (U+00A7): X=193.5,Y=2.0 (should be at baseline 0?)

	* section (U+00A7): X=344.5,Y=705.0 (should be at cap-height 707?)

	* uni00B2 (U+00B2): X=137.0,Y=707.5 (should be at cap-height 707?)

	* uni00B3 (U+00B3): X=136.5,Y=707.5 (should be at cap-height 707?)

	* ordmasculine (U+00BA): X=186.0,Y=708.0 (should be at cap-height 707?)

	* atilde (U+00E3): X=219.0,Y=708.0 (should be at cap-height 707?)

	* atilde (U+00E3): X=157.0,Y=709.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=271.0,Y=706.5 (should be at cap-height 707?)

	* otilde (U+00F5): X=279.0,Y=706.5 (should be at cap-height 707?)

	* Aogonek (U+0104): X=616.0,Y=1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=480.0,Y=1.0 (should be at baseline 0?)

	* Eogonek (U+0118): X=585.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=337.0,Y=1.0 (should be at baseline 0?)

	* uni0123 (U+0123): X=295.0,Y=705.0 (should be at cap-height 707?)

	* itilde (U+0129): X=70.0,Y=706.5 (should be at cap-height 707?)

	* Iogonek (U+012E): X=133.0,Y=1.0 (should be at baseline 0?)

	* iogonek (U+012F): X=114.0,Y=1.0 (should be at baseline 0?)

	* utilde (U+0169): X=261.0,Y=706.5 (should be at cap-height 707?)

	* Uogonek (U+0172): X=405.0,Y=1.0 (should be at baseline 0?)

	* uogonek (U+0173): X=329.0,Y=1.0 (should be at baseline 0?)

	* ogonek (U+02DB): X=271.0,Y=1.0 (should be at baseline 0?)

	* tilde (U+02DC): X=-23.0,Y=706.5 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-23.0,Y=706.5 (should be at cap-height 707?)

	* uni0312 (U+0312): X=-10.0,Y=705.0 (should be at cap-height 707?)

	* uni0328 (U+0328): X=19.0,Y=1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=228.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=237.0,Y=708.0 (should be at cap-height 707?)

	* uni0417 (U+0417): X=403.5,Y=2.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni0431 (U+0431): X=349.0,Y=709.0 (should be at cap-height 707?)

	* uni0437 (U+0437): X=172.0,Y=2.0 (should be at baseline 0?)

	* uni0440 (U+0440): X=250.0,Y=1.0 (should be at baseline 0?)

	* quotesinglbase (U+201A): X=92.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=242.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=92.0,Y=-2.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=371.5,Y=2.0 (should be at baseline 0?)

	* uni2713 (U+2713): X=373.0,Y=2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment L<<659.0,453.0>--<697.0,453.0>>

	* M (U+004D) contains a short segment L<<431.0,195.0>--<409.0,195.0>>

	* e (U+0065) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* r (U+0072) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* paragraph (U+00B6) contains a short segment L<<193.0,419.0>--<177.0,419.0>>

	* ae (U+00E6) contains a short segment B<<908.0,284.0>-<909.0,276.0>-<909.0,268.0>>

	* ae (U+00E6) contains a short segment B<<909.0,268.0>-<909.0,260.0>-<909.0,252.0>>

	* egrave (U+00E8) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* eacute (U+00E9) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* ecircumflex (U+00EA) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* edieresis (U+00EB) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* emacron (U+0113) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* ebreve (U+0115) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* edotaccent (U+0117) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* eogonek (U+0119) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* ecaron (U+011B) contains a short segment B<<523.0,282.0>-<524.0,275.0>-<524.0,267.5>>

	* Eng (U+014A) contains a short segment L<<467.0,-161.0>--<494.0,-161.0>>

	* oe (U+0153) contains a short segment B<<974.0,294.0>-<975.0,284.0>-<975.5,273.5>>

	* oe (U+0153) contains a short segment B<<975.5,273.5>-<976.0,263.0>-<976.0,252.0>>

	* racute (U+0155) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* uni0157 (U+0157) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* rcaron (U+0159) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* uni041C (U+041C) contains a short segment L<<431.0,195.0>--<409.0,195.0>>

	* uni0435 (U+0435) contains a short segment B<<523.0,279.0>-<524.0,272.0>-<524.0,265.5>>

	* uni0435 (U+0435) contains a short segment B<<524.0,265.5>-<524.0,259.0>-<524.0,252.0>>

	* uni043C (U+043C) contains a short segment L<<353.0,139.0>--<339.0,139.0>>

	* uni0451 (U+0451) contains a short segment B<<523.0,279.0>-<524.0,272.0>-<524.0,265.5>>

	* uni0451 (U+0451) contains a short segment B<<524.0,265.5>-<524.0,259.0>-<524.0,252.0>>

	* uni045E (U+045E) contains a short segment L<<86.0,-204.0>--<89.0,-204.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<104.0,177.0>--<102.0,707.0>>

	* exclam (U+0021): L<<143.0,707.0>--<141.0,177.0>>

	* exclamdown (U+00A1): L<<101.0,-181.0>--<103.0,349.0>>

	* exclamdown (U+00A1): L<<140.0,349.0>--<142.0,-181.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[9] Onest-Bold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=405.0,Y=709.0 (should be at cap-height 708?)

	* Q (U+0051): X=455.0,Y=-2.0 (should be at baseline 0?)

	* S (U+0053): X=253.5,Y=707.5 (should be at cap-height 708?)

	* f (U+0066): X=143.0,Y=707.0 (should be at cap-height 708?)

	* s (U+0073): X=339.5,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=371.0,Y=-1.0 (should be at baseline 0?)

	* section (U+00A7): X=373.0,Y=0.5 (should be at baseline 0?)

	* dieresis (U+00A8): X=372.0,Y=706.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=483.0,Y=706.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=129.0,Y=706.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=240.0,Y=706.0 (should be at cap-height 708?)

	* degree (U+00B0): X=69.0,Y=707.0 (should be at cap-height 708?)

	* questiondown (U+00BF): X=43.0,Y=1.0 (should be at baseline 0?)

	* Oslash (U+00D8): X=449.0,Y=710.0 (should be at cap-height 708?)

	* oslash (U+00F8): X=245.0,Y=-2.0 (should be at baseline 0?)

	* Sacute (U+015A): X=253.5,Y=707.5 (should be at cap-height 708?)

	* sacute (U+015B): X=339.5,Y=1.0 (should be at baseline 0?)

	* Scircumflex (U+015C): X=253.5,Y=707.5 (should be at cap-height 708?)

	* scircumflex (U+015D): X=339.5,Y=1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=253.5,Y=707.5 (should be at cap-height 708?)

	* scedilla (U+015F): X=339.5,Y=1.0 (should be at baseline 0?)

	* Scaron (U+0160): X=253.5,Y=707.5 (should be at cap-height 708?)

	* scaron (U+0161): X=339.5,Y=1.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=253.5,Y=707.5 (should be at cap-height 708?)

	* uni0219 (U+0219): X=339.5,Y=1.0 (should be at baseline 0?)

	* uni0405 (U+0405): X=243.5,Y=706.0 (should be at cap-height 708?)

	* uni0437 (U+0437): X=188.0,Y=2.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=353.5,Y=2.0 (should be at baseline 0?)

	* uni043B (U+043B): X=12.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=12.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=339.5,Y=1.0 (should be at baseline 0?)

	* quoteright (U+2019): X=217.5,Y=709.5 (should be at cap-height 708?)

	* quotedblright (U+201D): X=447.0,Y=709.0 (should be at cap-height 708?)

	* quotedblright (U+201D): X=217.5,Y=709.0 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=221.5,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=239.0,Y=707.5 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=399.0,Y=708.5 (should be at cap-height 708?)

	* uni21BA (U+21BA): X=236.0,Y=0.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<316.0,247.0>-<316.0,244.0>-<315.5,240.0>>

	* question (U+003F) contains a short segment B<<315.5,240.0>-<315.0,236.0>-<315.0,232.0>>

	* paragraph (U+00B6) contains a short segment L<<234.0,315.0>--<223.0,315.0>>

	* questiondown (U+00BF) contains a short segment B<<214.0,280.0>-<214.0,284.0>-<214.5,288.0>>

	* questiondown (U+00BF) contains a short segment B<<214.5,288.0>-<215.0,292.0>-<215.0,296.0>>

	* uni045E (U+045E) contains a short segment L<<84.0,-98.0>--<95.0,-98.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[10] Onest-ExtraBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam (U+0021): X=112.5,Y=1.0 (should be at baseline 0?)

	* dollar (U+0024): X=261.0,Y=2.0 (should be at baseline 0?)

	* dollar (U+0024): X=266.0,Y=710.0 (should be at cap-height 708?)

	* dollar (U+0024): X=408.0,Y=-1.0 (should be at baseline 0?)

	* eight (U+0038): X=223.5,Y=706.5 (should be at cap-height 708?)

	* eight (U+0038): X=404.0,Y=706.0 (should be at cap-height 708?)

	* Q (U+0051): X=454.5,Y=-2.0 (should be at baseline 0?)

	* asciicircum (U+005E): X=247.0,Y=710.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=353.0,Y=710.0 (should be at cap-height 708?)

	* g (U+0067): X=319.5,Y=-2.0 (should be at baseline 0?)

	* r (U+0072): X=271.0,Y=526.0 (should be at x-height 527?)

	* s (U+0073): X=179.5,Y=528.5 (should be at x-height 527?)

	* s (U+0073): X=341.5,Y=0.5 (should be at baseline 0?)

	* section (U+00A7): X=206.0,Y=1.0 (should be at baseline 0?)

	* section (U+00A7): X=212.5,Y=709.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=376.5,Y=707.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=497.0,Y=707.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=127.5,Y=707.0 (should be at cap-height 708?)

	* dieresis (U+00A8): X=248.0,Y=707.0 (should be at cap-height 708?)

	* uni00B2 (U+00B2): X=92.0,Y=707.0 (should be at cap-height 708?)

	* atilde (U+00E3): X=333.0,Y=707.5 (should be at cap-height 708?)

	* ntilde (U+00F1): X=344.0,Y=706.5 (should be at cap-height 708?)

	* ntilde (U+00F1): X=391.0,Y=707.0 (should be at cap-height 708?)

	* otilde (U+00F5): X=339.0,Y=706.5 (should be at cap-height 708?)

	* otilde (U+00F5): X=386.0,Y=707.0 (should be at cap-height 708?)

	* Aogonek (U+0104): X=672.0,Y=2.0 (should be at baseline 0?)

	* aogonek (U+0105): X=501.0,Y=2.0 (should be at baseline 0?)

	* ebreve (U+0115): X=249.0,Y=707.0 (should be at cap-height 708?)

	* ebreve (U+0115): X=346.0,Y=707.0 (should be at cap-height 708?)

	* Eogonek (U+0118): X=582.0,Y=2.0 (should be at baseline 0?)

	* eogonek (U+0119): X=368.0,Y=2.0 (should be at baseline 0?)

	* gcircumflex (U+011D): X=319.5,Y=-2.0 (should be at baseline 0?)

	* gbreve (U+011F): X=319.5,Y=-2.0 (should be at baseline 0?)

	* gbreve (U+011F): X=272.0,Y=707.0 (should be at cap-height 708?)

	* gbreve (U+011F): X=369.0,Y=707.0 (should be at cap-height 708?)

	* gdotaccent (U+0121): X=319.5,Y=-2.0 (should be at baseline 0?)

	* uni0123 (U+0123): X=319.5,Y=-2.0 (should be at baseline 0?)

	* itilde (U+0129): X=170.0,Y=706.5 (should be at cap-height 708?)

	* itilde (U+0129): X=217.0,Y=707.0 (should be at cap-height 708?)

	* ibreve (U+012D): X=83.0,Y=707.0 (should be at cap-height 708?)

	* ibreve (U+012D): X=180.0,Y=707.0 (should be at cap-height 708?)

	* Iogonek (U+012E): X=215.0,Y=2.0 (should be at baseline 0?)

	* iogonek (U+012F): X=189.0,Y=2.0 (should be at baseline 0?)

	* obreve (U+014F): X=252.0,Y=707.0 (should be at cap-height 708?)

	* obreve (U+014F): X=349.0,Y=707.0 (should be at cap-height 708?)

	* sacute (U+015B): X=341.5,Y=0.5 (should be at baseline 0?)

	* scircumflex (U+015D): X=341.5,Y=0.5 (should be at baseline 0?)

	* scedilla (U+015F): X=341.5,Y=0.5 (should be at baseline 0?)

	* scaron (U+0161): X=341.5,Y=0.5 (should be at baseline 0?)

	* utilde (U+0169): X=333.0,Y=706.5 (should be at cap-height 708?)

	* utilde (U+0169): X=380.0,Y=707.0 (should be at cap-height 708?)

	* ubreve (U+016D): X=246.0,Y=707.0 (should be at cap-height 708?)

	* ubreve (U+016D): X=343.0,Y=707.0 (should be at cap-height 708?)

	* Uogonek (U+0172): X=452.0,Y=2.0 (should be at baseline 0?)

	* uogonek (U+0173): X=371.0,Y=2.0 (should be at baseline 0?)

	* uni0219 (U+0219): X=341.5,Y=0.5 (should be at baseline 0?)

	* breve (U+02D8): X=245.5,Y=707.0 (should be at cap-height 708?)

	* breve (U+02D8): X=342.5,Y=707.0 (should be at cap-height 708?)

	* ring (U+02DA): X=184.0,Y=706.0 (should be at cap-height 708?)

	* ring (U+02DA): X=436.0,Y=706.0 (should be at cap-height 708?)

	* ring (U+02DA): X=350.0,Y=707.0 (should be at cap-height 708?)

	* ring (U+02DA): X=270.0,Y=707.0 (should be at cap-height 708?)

	* ogonek (U+02DB): X=310.0,Y=2.0 (should be at baseline 0?)

	* tilde (U+02DC): X=40.0,Y=706.5 (should be at cap-height 708?)

	* tilde (U+02DC): X=87.0,Y=707.0 (should be at cap-height 708?)

	* tildecomb (U+0303): X=40.0,Y=706.5 (should be at cap-height 708?)

	* tildecomb (U+0303): X=87.0,Y=707.0 (should be at cap-height 708?)

	* uni0306 (U+0306): X=-48.0,Y=707.0 (should be at cap-height 708?)

	* uni0306 (U+0306): X=49.0,Y=707.0 (should be at cap-height 708?)

	* uni0328 (U+0328): X=62.0,Y=2.0 (should be at baseline 0?)

	* uni0405 (U+0405): X=244.0,Y=706.5 (should be at cap-height 708?)

	* uni0417 (U+0417): X=438.0,Y=706.0 (should be at cap-height 708?)

	* uni041B (U+041B): X=8.0,Y=-2.0 (should be at baseline 0?)

	* uni041B (U+041B): X=8.0,Y=-2.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=359.0,Y=1.5 (should be at baseline 0?)

	* uni043B (U+043B): X=9.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=9.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=341.5,Y=0.5 (should be at baseline 0?)

	* quoteright (U+2019): X=230.5,Y=710.0 (should be at cap-height 708?)

	* quotedblright (U+201D): X=473.5,Y=709.5 (should be at cap-height 708?)

	* quotedblright (U+201D): X=230.5,Y=709.5 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=222.5,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=238.0,Y=707.5 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=401.5,Y=709.0 (should be at cap-height 708?)

	* uni21BA (U+21BA): X=235.0,Y=0.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=277.0,Y=-0.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<329.0,256.0>-<329.0,252.0>-<328.5,247.5>>

	* question (U+003F) contains a short segment B<<328.5,247.5>-<328.0,243.0>-<328.0,238.0>>

	* at (U+0040) contains a short segment B<<813.0,276.0>-<815.0,299.0>-<815.0,308.0>>

	* paragraph (U+00B6) contains a short segment L<<226.0,315.0>--<212.0,315.0>>

	* questiondown (U+00BF) contains a short segment B<<207.0,272.0>-<207.0,276.0>-<207.5,280.5>>

	* questiondown (U+00BF) contains a short segment B<<207.5,280.5>-<208.0,285.0>-<208.0,291.0>>

	* uni045E (U+045E) contains a short segment L<<82.0,-83.0>--<95.0,-83.0>>

	* Euro (U+20AC) contains a short segment B<<292.0,380.0>-<292.0,369.0>-<291.0,355.5>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni041B (U+041B): L<<119.0,434.0>--<121.0,708.0>>

	* uni21BA (U+21BA): L<<625.0,542.0>--<624.0,361.0>>

	* uni21BB (U+21BB): L<<325.0,361.0>--<324.0,542.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[9] Onest-Regular.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* comma (U+002C): X=128.0,Y=-2.0 (should be at baseline 0?)

	* three (U+0033): X=206.5,Y=0.5 (should be at baseline 0?)

	* three (U+0033): X=374.0,Y=0.5 (should be at baseline 0?)

	* S (U+0053): X=240.5,Y=705.0 (should be at cap-height 707?)

	* a (U+0061): X=297.5,Y=-0.5 (should be at baseline 0?)

	* j (U+006A): X=95.0,Y=-1.0 (should be at baseline 0?)

	* s (U+0073): X=333.5,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=257.0,Y=-2.0 (should be at baseline 0?)

	* section (U+00A7): X=356.5,Y=-1.0 (should be at baseline 0?)

	* agrave (U+00E0): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=297.5,Y=-0.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=297.5,Y=-0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=297.5,Y=-0.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aring (U+00E5): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aring (U+00E5): X=313.5,Y=707.5 (should be at cap-height 707?)

	* aring (U+00E5): X=250.5,Y=707.5 (should be at cap-height 707?)

	* eth (U+00F0): X=496.0,Y=709.0 (should be at cap-height 707?)

	* amacron (U+0101): X=297.5,Y=-0.5 (should be at baseline 0?)

	* abreve (U+0103): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aogonek (U+0105): X=297.5,Y=-0.5 (should be at baseline 0?)

	* uni0122 (U+0122): X=334.0,Y=-304.0 (should be at descender -305?)

	* uni0122 (U+0122): X=334.0,Y=-304.0 (should be at descender -305?)

	* ij (U+0133): X=301.0,Y=-1.0 (should be at baseline 0?)

	* jcircumflex (U+0135): X=95.0,Y=-1.0 (should be at baseline 0?)

	* uni0136 (U+0136): X=274.0,Y=-304.0 (should be at descender -305?)

	* uni0136 (U+0136): X=274.0,Y=-304.0 (should be at descender -305?)

	* uni0137 (U+0137): X=221.0,Y=-304.0 (should be at descender -305?)

	* uni0137 (U+0137): X=221.0,Y=-304.0 (should be at descender -305?)

	* uni013B (U+013B): X=287.0,Y=-304.0 (should be at descender -305?)

	* uni013B (U+013B): X=287.0,Y=-304.0 (should be at descender -305?)

	* uni013C (U+013C): X=71.0,Y=-304.0 (should be at descender -305?)

	* uni013C (U+013C): X=71.0,Y=-304.0 (should be at descender -305?)

	* uni0145 (U+0145): X=328.0,Y=-304.0 (should be at descender -305?)

	* uni0145 (U+0145): X=328.0,Y=-304.0 (should be at descender -305?)

	* uni0146 (U+0146): X=257.0,Y=-304.0 (should be at descender -305?)

	* uni0146 (U+0146): X=257.0,Y=-304.0 (should be at descender -305?)

	* eng (U+014B): X=442.0,Y=-1.0 (should be at baseline 0?)

	* uni0156 (U+0156): X=290.0,Y=-304.0 (should be at descender -305?)

	* uni0156 (U+0156): X=290.0,Y=-304.0 (should be at descender -305?)

	* uni0157 (U+0157): X=78.0,Y=-304.0 (should be at descender -305?)

	* uni0157 (U+0157): X=78.0,Y=-304.0 (should be at descender -305?)

	* Sacute (U+015A): X=240.5,Y=705.0 (should be at cap-height 707?)

	* sacute (U+015B): X=333.5,Y=1.0 (should be at baseline 0?)

	* Scircumflex (U+015C): X=240.5,Y=705.0 (should be at cap-height 707?)

	* scircumflex (U+015D): X=333.5,Y=1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=240.5,Y=705.0 (should be at cap-height 707?)

	* scedilla (U+015F): X=333.5,Y=1.0 (should be at baseline 0?)

	* Scaron (U+0160): X=240.5,Y=705.0 (should be at cap-height 707?)

	* scaron (U+0161): X=333.5,Y=1.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=240.5,Y=705.0 (should be at cap-height 707?)

	* uni0218 (U+0218): X=287.0,Y=-304.0 (should be at descender -305?)

	* uni0218 (U+0218): X=287.0,Y=-304.0 (should be at descender -305?)

	* uni0219 (U+0219): X=333.5,Y=1.0 (should be at baseline 0?)

	* uni0219 (U+0219): X=216.0,Y=-304.0 (should be at descender -305?)

	* uni0219 (U+0219): X=216.0,Y=-304.0 (should be at descender -305?)

	* uni021A (U+021A): X=246.0,Y=-304.0 (should be at descender -305?)

	* uni021A (U+021A): X=246.0,Y=-304.0 (should be at descender -305?)

	* uni0237 (U+0237): X=95.0,Y=-1.0 (should be at baseline 0?)

	* uni0326 (U+0326): X=-39.0,Y=-304.0 (should be at descender -305?)

	* uni0326 (U+0326): X=-39.0,Y=-304.0 (should be at descender -305?)

	* uni0405 (U+0405): X=240.5,Y=705.0 (should be at cap-height 707?)

	* uni040E (U+040E): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0430 (U+0430): X=297.5,Y=-0.5 (should be at baseline 0?)

	* uni0437 (U+0437): X=182.0,Y=1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=19.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=19.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=333.5,Y=1.0 (should be at baseline 0?)

	* uni0458 (U+0458): X=95.0,Y=-1.0 (should be at baseline 0?)

	* quotedblright (U+201D): X=368.5,Y=706.5 (should be at cap-height 707?)

	* quotedblright (U+201D): X=179.5,Y=706.5 (should be at cap-height 707?)

	* uni21BA (U+21BA): X=238.0,Y=1.0 (should be at baseline 0?)

	* uni21BB (U+21BB): X=701.5,Y=0.5 (should be at baseline 0?)

	* uni2713 (U+2713): X=373.0,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<191.0,213.0>-<190.0,218.0>-<190.0,223.5>>

	* question (U+003F) contains a short segment B<<190.0,223.5>-<190.0,229.0>-<190.0,234.0>>

	* at (U+0040) contains a short segment B<<531.5,-98.0>-<547.0,-97.0>-<561.5,-95.0>>

	* at (U+0040) contains a short segment B<<561.5,-95.0>-<576.0,-93.0>-<597.0,-89.0>>

	* paragraph (U+00B6) contains a short segment L<<260.0,314.0>--<255.0,314.0>>

	* questiondown (U+00BF) contains a short segment B<<321.0,313.0>-<322.0,308.0>-<322.0,302.5>>

	* questiondown (U+00BF) contains a short segment B<<322.0,302.5>-<322.0,297.0>-<322.0,292.0>>

	* ae (U+00E6) contains a short segment B<<883.0,272.0>-<883.0,262.0>-<882.5,252.0>>

	* ae (U+00E6) contains a short segment B<<882.5,252.0>-<882.0,242.0>-<881.0,232.0>>

	* oe (U+0153) contains a short segment B<<938.0,268.0>-<937.0,259.0>-<937.0,250.0>>

	* oe (U+0153) contains a short segment B<<937.0,250.0>-<937.0,241.0>-<936.0,232.0>>

	* uni045E (U+045E) contains a short segment L<<89.0,-145.0>--<95.0,-145.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[9] Onest-ExtraLight.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three (U+0033): X=371.5,Y=2.0 (should be at baseline 0?)

	* five (U+0035): X=233.5,Y=-1.5 (should be at baseline 0?)

	* a (U+0061): X=205.5,Y=525.0 (should be at x-height 527?)

	* b (U+0062): X=245.5,Y=1.5 (should be at baseline 0?)

	* i (U+0069): X=99.0,Y=709.0 (should be at cap-height 707?)

	* j (U+006A): X=137.0,Y=709.0 (should be at cap-height 707?)

	* m (U+006D): X=227.5,Y=526.5 (should be at x-height 527?)

	* uni00B2 (U+00B2): X=180.0,Y=705.0 (should be at cap-height 707?)

	* uni00B3 (U+00B3): X=185.0,Y=706.0 (should be at cap-height 707?)

	* edieresis (U+00EB): X=401.0,Y=709.0 (should be at cap-height 707?)

	* edieresis (U+00EB): X=186.0,Y=709.0 (should be at cap-height 707?)

	* eth (U+00F0): X=242.5,Y=705.0 (should be at cap-height 707?)

	* odieresis (U+00F6): X=408.0,Y=709.0 (should be at cap-height 707?)

	* odieresis (U+00F6): X=193.0,Y=709.0 (should be at cap-height 707?)

	* udieresis (U+00FC): X=392.0,Y=709.0 (should be at cap-height 707?)

	* udieresis (U+00FC): X=177.0,Y=709.0 (should be at cap-height 707?)

	* ydieresis (U+00FF): X=405.0,Y=709.0 (should be at cap-height 707?)

	* ydieresis (U+00FF): X=190.0,Y=709.0 (should be at cap-height 707?)

	* Aogonek (U+0104): X=625.0,Y=2.0 (should be at baseline 0?)

	* aogonek (U+0105): X=483.0,Y=2.0 (should be at baseline 0?)

	* cdotaccent (U+010B): X=276.0,Y=709.0 (should be at cap-height 707?)

	* edotaccent (U+0117): X=295.0,Y=709.0 (should be at cap-height 707?)

	* Eogonek (U+0118): X=587.0,Y=2.0 (should be at baseline 0?)

	* eogonek (U+0119): X=350.0,Y=2.0 (should be at baseline 0?)

	* gdotaccent (U+0121): X=304.0,Y=709.0 (should be at cap-height 707?)

	* uni0123 (U+0123): X=298.0,Y=708.0 (should be at cap-height 707?)

	* Iogonek (U+012E): X=146.0,Y=2.0 (should be at baseline 0?)

	* iogonek (U+012F): X=99.0,Y=709.0 (should be at cap-height 707?)

	* iogonek (U+012F): X=125.0,Y=2.0 (should be at baseline 0?)

	* Uogonek (U+0172): X=417.0,Y=2.0 (should be at baseline 0?)

	* uogonek (U+0173): X=339.0,Y=2.0 (should be at baseline 0?)

	* zdotaccent (U+017C): X=260.0,Y=709.0 (should be at cap-height 707?)

	* ogonek (U+02DB): X=287.0,Y=2.0 (should be at baseline 0?)

	* uni0307 (U+0307): X=1.0,Y=709.0 (should be at cap-height 707?)

	* uni0308 (U+0308): X=107.0,Y=709.0 (should be at cap-height 707?)

	* uni0308 (U+0308): X=-108.0,Y=709.0 (should be at cap-height 707?)

	* uni0312 (U+0312): X=-6.0,Y=708.0 (should be at cap-height 707?)

	* uni0328 (U+0328): X=32.0,Y=2.0 (should be at baseline 0?)

	* uni040E (U+040E): X=111.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=111.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=223.5,Y=0.5 (should be at baseline 0?)

	* uni0417 (U+0417): X=239.5,Y=708.0 (should be at cap-height 707?)

	* uni0423 (U+0423): X=111.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=111.0,Y=-1.0 (should be at baseline 0?)

	* uni0430 (U+0430): X=173.5,Y=1.0 (should be at baseline 0?)

	* uni0451 (U+0451): X=395.0,Y=709.0 (should be at cap-height 707?)

	* uni0451 (U+0451): X=180.0,Y=709.0 (should be at cap-height 707?)

	* wdieresis (U+1E85): X=514.0,Y=709.0 (should be at cap-height 707?)

	* wdieresis (U+1E85): X=299.0,Y=709.0 (should be at cap-height 707?)

	* uni20B4 (U+20B4): X=231.5,Y=-2.0 (should be at baseline 0?)

	* uni21BA (U+21BA): X=240.5,Y=-1.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=692.5,Y=-1.5 (should be at baseline 0?)

	* uni2713 (U+2713): X=373.0,Y=1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<196.0,207.0>-<196.0,211.0>-<196.0,215.5>>

	* question (U+003F) contains a short segment B<<196.0,215.5>-<196.0,220.0>-<196.0,224.0>>

	* M (U+004D) contains a short segment L<<437.0,192.0>--<409.0,192.0>>

	* paragraph (U+00B6) contains a short segment L<<215.0,384.0>--<203.0,384.0>>

	* questiondown (U+00BF) contains a short segment B<<306.0,321.0>-<306.0,317.0>-<306.0,312.5>>

	* questiondown (U+00BF) contains a short segment B<<306.0,312.5>-<306.0,308.0>-<306.0,304.0>>

	* ae (U+00E6) contains a short segment B<<900.0,280.0>-<900.0,271.0>-<900.0,262.5>>

	* ae (U+00E6) contains a short segment B<<900.0,262.5>-<900.0,254.0>-<900.0,245.0>>

	* oe (U+0153) contains a short segment B<<962.0,285.0>-<962.0,275.0>-<962.5,265.0>>

	* oe (U+0153) contains a short segment B<<962.5,265.0>-<963.0,255.0>-<963.0,245.0>>

	* uni041C (U+041C) contains a short segment L<<438.0,191.0>--<410.0,191.0>>

	* uni043C (U+043C) contains a short segment L<<356.0,138.0>--<339.0,138.0>>

	* uni045E (U+045E) contains a short segment L<<87.0,-184.0>--<91.0,-184.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[9] Onest-Light.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three (U+0033): X=373.0,Y=1.0 (should be at baseline 0?)

	* S (U+0053): X=238.5,Y=705.0 (should be at cap-height 707?)

	* s (U+0073): X=332.0,Y=0.5 (should be at baseline 0?)

	* y (U+0079): X=459.0,Y=2.0 (should be at baseline 0?)

	* y (U+0079): X=528.0,Y=-2.0 (should be at baseline 0?)

	* section (U+00A7): X=353.5,Y=-1.0 (should be at baseline 0?)

	* registered (U+00AE): X=240.0,Y=708.0 (should be at cap-height 707?)

	* ecircumflex (U+00EA): X=294.0,Y=706.0 (should be at cap-height 707?)

	* icircumflex (U+00EE): X=104.0,Y=706.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=172.5,Y=709.0 (should be at cap-height 707?)

	* ocircumflex (U+00F4): X=299.0,Y=706.0 (should be at cap-height 707?)

	* otilde (U+00F5): X=176.5,Y=709.0 (should be at cap-height 707?)

	* ucircumflex (U+00FB): X=286.0,Y=706.0 (should be at cap-height 707?)

	* yacute (U+00FD): X=459.0,Y=2.0 (should be at baseline 0?)

	* yacute (U+00FD): X=528.0,Y=-2.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=459.0,Y=2.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=528.0,Y=-2.0 (should be at baseline 0?)

	* ccircumflex (U+0109): X=276.0,Y=706.0 (should be at cap-height 707?)

	* gcircumflex (U+011D): X=302.0,Y=706.0 (should be at cap-height 707?)

	* uni0122 (U+0122): X=339.0,Y=-303.0 (should be at descender -305?)

	* uni0122 (U+0122): X=339.0,Y=-303.0 (should be at descender -305?)

	* itilde (U+0129): X=-18.5,Y=709.0 (should be at cap-height 707?)

	* ij (U+0133): X=75.5,Y=708.0 (should be at cap-height 707?)

	* ij (U+0133): X=149.0,Y=708.0 (should be at cap-height 707?)

	* ij (U+0133): X=294.5,Y=708.0 (should be at cap-height 707?)

	* ij (U+0133): X=369.0,Y=708.0 (should be at cap-height 707?)

	* jcircumflex (U+0135): X=137.0,Y=706.0 (should be at cap-height 707?)

	* uni0136 (U+0136): X=273.0,Y=-303.0 (should be at descender -305?)

	* uni0136 (U+0136): X=273.0,Y=-303.0 (should be at descender -305?)

	* uni0137 (U+0137): X=221.0,Y=-303.0 (should be at descender -305?)

	* uni0137 (U+0137): X=221.0,Y=-303.0 (should be at descender -305?)

	* uni013B (U+013B): X=288.0,Y=-303.0 (should be at descender -305?)

	* uni013B (U+013B): X=288.0,Y=-303.0 (should be at descender -305?)

	* uni013C (U+013C): X=69.0,Y=-303.0 (should be at descender -305?)

	* uni013C (U+013C): X=69.0,Y=-303.0 (should be at descender -305?)

	* uni0145 (U+0145): X=334.0,Y=-303.0 (should be at descender -305?)

	* uni0145 (U+0145): X=334.0,Y=-303.0 (should be at descender -305?)

	* uni0146 (U+0146): X=260.0,Y=-303.0 (should be at descender -305?)

	* uni0146 (U+0146): X=260.0,Y=-303.0 (should be at descender -305?)

	* uni0156 (U+0156): X=292.0,Y=-303.0 (should be at descender -305?)

	* uni0156 (U+0156): X=292.0,Y=-303.0 (should be at descender -305?)

	* uni0157 (U+0157): X=74.0,Y=-303.0 (should be at descender -305?)

	* uni0157 (U+0157): X=74.0,Y=-303.0 (should be at descender -305?)

	* Sacute (U+015A): X=238.5,Y=705.0 (should be at cap-height 707?)

	* sacute (U+015B): X=332.0,Y=0.5 (should be at baseline 0?)

	* Scircumflex (U+015C): X=238.5,Y=705.0 (should be at cap-height 707?)

	* scircumflex (U+015D): X=332.0,Y=0.5 (should be at baseline 0?)

	* scircumflex (U+015D): X=253.0,Y=706.0 (should be at cap-height 707?)

	* Scedilla (U+015E): X=238.5,Y=705.0 (should be at cap-height 707?)

	* scedilla (U+015F): X=332.0,Y=0.5 (should be at baseline 0?)

	* Scaron (U+0160): X=238.5,Y=705.0 (should be at cap-height 707?)

	* scaron (U+0161): X=332.0,Y=0.5 (should be at baseline 0?)

	* utilde (U+0169): X=163.5,Y=709.0 (should be at cap-height 707?)

	* uring (U+016F): X=320.5,Y=707.5 (should be at cap-height 707?)

	* uring (U+016F): X=251.5,Y=707.5 (should be at cap-height 707?)

	* wcircumflex (U+0175): X=414.0,Y=706.0 (should be at cap-height 707?)

	* ycircumflex (U+0177): X=459.0,Y=2.0 (should be at baseline 0?)

	* ycircumflex (U+0177): X=528.0,Y=-2.0 (should be at baseline 0?)

	* ycircumflex (U+0177): X=298.0,Y=706.0 (should be at cap-height 707?)

	* uni0218 (U+0218): X=238.5,Y=705.0 (should be at cap-height 707?)

	* uni0218 (U+0218): X=289.0,Y=-303.0 (should be at descender -305?)

	* uni0218 (U+0218): X=289.0,Y=-303.0 (should be at descender -305?)

	* uni0219 (U+0219): X=332.0,Y=0.5 (should be at baseline 0?)

	* uni0219 (U+0219): X=218.0,Y=-303.0 (should be at descender -305?)

	* uni0219 (U+0219): X=218.0,Y=-303.0 (should be at descender -305?)

	* uni021A (U+021A): X=248.0,Y=-303.0 (should be at descender -305?)

	* uni021A (U+021A): X=248.0,Y=-303.0 (should be at descender -305?)

	* tilde (U+02DC): X=-122.5,Y=709.0 (should be at cap-height 707?)

	* uni0302 (U+0302): X=0.0,Y=706.0 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-122.5,Y=709.0 (should be at cap-height 707?)

	* uni030A (U+030A): X=34.5,Y=707.5 (should be at cap-height 707?)

	* uni030A (U+030A): X=-34.5,Y=707.5 (should be at cap-height 707?)

	* uni0326 (U+0326): X=-36.0,Y=-303.0 (should be at descender -305?)

	* uni0326 (U+0326): X=-36.0,Y=-303.0 (should be at descender -305?)

	* uni0405 (U+0405): X=238.5,Y=705.0 (should be at cap-height 707?)

	* uni040E (U+040E): X=114.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=114.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=219.5,Y=1.5 (should be at baseline 0?)

	* uni0417 (U+0417): X=241.5,Y=707.5 (should be at cap-height 707?)

	* uni0423 (U+0423): X=114.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=114.0,Y=-1.0 (should be at baseline 0?)

	* uni0431 (U+0431): X=424.0,Y=709.0 (should be at cap-height 707?)

	* uni043B (U+043B): X=21.0,Y=-2.0 (should be at baseline 0?)

	* uni043B (U+043B): X=21.0,Y=-2.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=332.0,Y=0.5 (should be at baseline 0?)

	* uni0456 (U+0456): X=75.5,Y=708.0 (should be at cap-height 707?)

	* uni0456 (U+0456): X=149.0,Y=708.0 (should be at cap-height 707?)

	* uni0458 (U+0458): X=100.5,Y=708.0 (should be at cap-height 707?)

	* uni0458 (U+0458): X=175.0,Y=708.0 (should be at cap-height 707?)

	* ygrave (U+1EF3): X=459.0,Y=2.0 (should be at baseline 0?)

	* ygrave (U+1EF3): X=528.0,Y=-2.0 (should be at baseline 0?)

	* quotedblright (U+201D): X=345.5,Y=709.0 (should be at cap-height 707?)

	* quotedblright (U+201D): X=169.5,Y=709.0 (should be at cap-height 707?)

	* uni20B4 (U+20B4): X=225.5,Y=-0.5 (should be at baseline 0?)

	* uni21BA (U+21BA): X=239.0,Y=-0.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=696.5,Y=-0.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* nine (U+0039) contains a short segment B<<491.0,347.0>-<491.0,354.0>-<491.0,363.5>>

	* question (U+003F) contains a short segment B<<194.0,210.0>-<193.0,215.0>-<193.0,219.5>>

	* question (U+003F) contains a short segment B<<193.0,219.5>-<193.0,224.0>-<193.0,229.0>>

	* paragraph (U+00B6) contains a short segment L<<238.0,349.0>--<229.0,349.0>>

	* questiondown (U+00BF) contains a short segment B<<313.0,317.0>-<314.0,312.0>-<314.0,307.5>>

	* questiondown (U+00BF) contains a short segment B<<314.0,307.5>-<314.0,303.0>-<314.0,298.0>>

	* ae (U+00E6) contains a short segment B<<891.0,276.0>-<892.0,267.0>-<891.5,257.5>>

	* ae (U+00E6) contains a short segment B<<891.5,257.5>-<891.0,248.0>-<890.0,239.0>>

	* oe (U+0153) contains a short segment B<<950.0,277.0>-<950.0,267.0>-<950.0,257.5>>

	* oe (U+0153) contains a short segment B<<950.0,257.5>-<950.0,248.0>-<949.0,239.0>>

	* uni043C (U+043C) contains a short segment L<<359.0,136.0>--<338.0,136.0>>

	* uni045E (U+045E) contains a short segment L<<88.0,-165.0>--<93.0,-165.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[9] Onest-Black.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:registered_vendor_ids> had an error: ModuleNotFoundError: No module named 'bs4'
</div></details><details><summary>💔 <b>ERROR:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:hinting_stats> had an error: ModuleNotFoundError: No module named 'dehinter'
</div></details><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0403 (CYRILLIC CAPITAL LETTER GJE)


	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x040C (CYRILLIC CAPITAL LETTER KJE)


	- 0x040F (CYRILLIC CAPITAL LETTER DZHE)


	- 0x0409 (CYRILLIC CAPITAL LETTER LJE)


	- 0x040A (CYRILLIC CAPITAL LETTER NJE)


	- 0x040B (CYRILLIC CAPITAL LETTER TSHE)


	- 0x0402 (CYRILLIC CAPITAL LETTER DJE)


	- 0x0453 (CYRILLIC SMALL LETTER GJE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)


	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)


	- 0x045C (CYRILLIC SMALL LETTER KJE)


	- 0x045F (CYRILLIC SMALL LETTER DZHE)


	- 0x0459 (CYRILLIC SMALL LETTER LJE)


	- 0x045A (CYRILLIC SMALL LETTER NJE)


	- 0x045B (CYRILLIC SMALL LETTER TSHE)


	- 0x0452 (CYRILLIC SMALL LETTER DJE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam (U+0021): X=114.5,Y=2.0 (should be at baseline 0?)

	* exclam (U+0021): X=212.0,Y=2.0 (should be at baseline 0?)

	* dollar (U+0024): X=258.0,Y=709.0 (should be at cap-height 708?)

	* dollar (U+0024): X=419.0,Y=707.0 (should be at cap-height 708?)

	* three (U+0033): X=401.0,Y=706.5 (should be at cap-height 708?)

	* eight (U+0038): X=223.0,Y=706.5 (should be at cap-height 708?)

	* eight (U+0038): X=405.5,Y=706.5 (should be at cap-height 708?)

	* question (U+003F): X=172.5,Y=706.0 (should be at cap-height 708?)

	* Q (U+0051): X=453.5,Y=-2.0 (should be at baseline 0?)

	* asciicircum (U+005E): X=248.0,Y=709.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=365.0,Y=709.0 (should be at cap-height 708?)

	* d (U+0064): X=358.0,Y=525.5 (should be at x-height 527?)

	* q (U+0071): X=343.5,Y=2.0 (should be at baseline 0?)

	* s (U+0073): X=184.0,Y=1.0 (should be at baseline 0?)

	* s (U+0073): X=344.0,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=227.0,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=389.0,Y=1.0 (should be at baseline 0?)

	* section (U+00A7): X=206.0,Y=1.0 (should be at baseline 0?)

	* dieresis (U+00A8): X=511.5,Y=708.5 (should be at cap-height 708?)

	* dieresis (U+00A8): X=256.5,Y=708.5 (should be at cap-height 708?)

	* uni00B3 (U+00B3): X=105.5,Y=708.5 (should be at cap-height 708?)

	* questiondown (U+00BF): X=337.5,Y=-2.0 (should be at baseline 0?)

	* germandbls (U+00DF): X=468.5,Y=710.0 (should be at cap-height 708?)

	* atilde (U+00E3): X=363.0,Y=707.0 (should be at cap-height 708?)

	* ntilde (U+00F1): X=373.0,Y=707.0 (should be at cap-height 708?)

	* otilde (U+00F5): X=367.0,Y=707.0 (should be at cap-height 708?)

	* Aogonek (U+0104): X=679.0,Y=1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=504.0,Y=1.0 (should be at baseline 0?)

	* Eogonek (U+0118): X=580.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=366.0,Y=1.0 (should be at baseline 0?)

	* uni0123 (U+0123): X=391.5,Y=707.5 (should be at cap-height 708?)

	* itilde (U+0129): X=202.0,Y=707.0 (should be at cap-height 708?)

	* Iogonek (U+012E): X=225.0,Y=1.0 (should be at baseline 0?)

	* iogonek (U+012F): X=199.0,Y=1.0 (should be at baseline 0?)

	* sacute (U+015B): X=184.0,Y=1.0 (should be at baseline 0?)

	* sacute (U+015B): X=344.0,Y=1.0 (should be at baseline 0?)

	* scircumflex (U+015D): X=184.0,Y=1.0 (should be at baseline 0?)

	* scircumflex (U+015D): X=344.0,Y=1.0 (should be at baseline 0?)

	* scedilla (U+015F): X=184.0,Y=1.0 (should be at baseline 0?)

	* scedilla (U+015F): X=344.0,Y=1.0 (should be at baseline 0?)

	* scaron (U+0161): X=184.0,Y=1.0 (should be at baseline 0?)

	* scaron (U+0161): X=344.0,Y=1.0 (should be at baseline 0?)

	* utilde (U+0169): X=362.0,Y=707.0 (should be at cap-height 708?)

	* Uogonek (U+0172): X=455.0,Y=1.0 (should be at baseline 0?)

	* uogonek (U+0173): X=374.0,Y=1.0 (should be at baseline 0?)

	* uni0219 (U+0219): X=184.0,Y=1.0 (should be at baseline 0?)

	* uni0219 (U+0219): X=344.0,Y=1.0 (should be at baseline 0?)

	* ring (U+02DA): X=183.0,Y=710.0 (should be at cap-height 708?)

	* ring (U+02DA): X=449.0,Y=710.0 (should be at cap-height 708?)

	* ogonek (U+02DB): X=308.0,Y=1.0 (should be at baseline 0?)

	* tilde (U+02DC): X=67.0,Y=707.0 (should be at cap-height 708?)

	* tildecomb (U+0303): X=67.0,Y=707.0 (should be at cap-height 708?)

	* uni0312 (U+0312): X=66.5,Y=707.5 (should be at cap-height 708?)

	* uni0328 (U+0328): X=63.0,Y=1.0 (should be at baseline 0?)

	* uni0405 (U+0405): X=245.5,Y=706.5 (should be at cap-height 708?)

	* uni0417 (U+0417): X=447.0,Y=706.0 (should be at cap-height 708?)

	* uni041B (U+041B): X=7.0,Y=-1.0 (should be at baseline 0?)

	* uni041B (U+041B): X=7.0,Y=-1.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=365.0,Y=1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=7.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=7.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=184.0,Y=1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=344.0,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=223.0,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=237.0,Y=708.5 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=405.0,Y=710.0 (should be at cap-height 708?)

	* uni21BA (U+21BA): X=234.5,Y=0.5 (should be at baseline 0?)

	* uni21BA (U+21BA): X=680.0,Y=-0.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=272.5,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<342.0,265.0>-<341.0,261.0>-<340.5,255.5>>

	* question (U+003F) contains a short segment B<<340.5,255.5>-<340.0,250.0>-<340.0,244.0>>

	* at (U+0040) contains a short segment B<<808.5,285.0>-<810.0,305.0>-<810.0,312.0>>

	* s (U+0073) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* paragraph (U+00B6) contains a short segment L<<217.0,315.0>--<201.0,315.0>>

	* questiondown (U+00BF) contains a short segment B<<200.0,264.0>-<201.0,269.0>-<201.5,274.0>>

	* questiondown (U+00BF) contains a short segment B<<201.5,274.0>-<202.0,279.0>-<202.0,285.0>>

	* germandbls (U+00DF) contains a short segment B<<494.0,175.0>-<494.0,184.0>-<489.0,192.5>>

	* germandbls (U+00DF) contains a short segment B<<457.0,400.0>-<457.0,387.0>-<465.5,378.5>>

	* sacute (U+015B) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* scircumflex (U+015D) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* scedilla (U+015F) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* scaron (U+0161) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* tbar (U+0167) contains a short segment L<<257.0,210.0>--<257.0,201.0>>

	* uni0219 (U+0219) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* uni0424 (U+0424) contains a short segment L<<355.0,90.0>--<346.0,90.0>>

	* uni0424 (U+0424) contains a short segment L<<536.0,642.0>--<542.0,642.0>>

	* uni0455 (U+0455) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* uni045E (U+045E) contains a short segment L<<80.0,-67.0>--<95.0,-67.0>>

	* Euro (U+20AC) contains a short segment B<<308.0,374.0>-<308.0,365.0>-<307.5,355.5>>

	* Euro (U+20AC) contains a short segment B<<307.5,355.5>-<307.0,346.0>-<307.0,337.0>>

	* uni20B4 (U+20B4) contains a short segment B<<384.0,496.5>-<389.0,506.0>-<389.0,514.0>>

	* uni20B4 (U+20B4) contains a short segment B<<255.0,229.0>-<246.0,223.0>-<242.0,214.5>>

	* uni20B4 (U+20B4) contains a short segment B<<242.0,214.5>-<238.0,206.0>-<238.0,198.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 27 | 0 | 56 | 1091 | 46 | 894 | 0 |
| 1% | 0% | 3% | 52% | 2% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
