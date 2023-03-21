## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[16] Onest-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '300'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 539 among a set of 4 math glyphs.
The following math glyphs have a different width, though:

Width = 518:
plus, minus

Width = 441:
less, greater

Width = 508:
plusminus

Width = 459:
multiply

Width = 471:
divide

Width = 593:
approxequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three (U+0033): X=211.0,Y=707.5 (should be at cap-height 707?)

	* j (U+006A): X=105.0,Y=2.0 (should be at baseline 0?)

	* p (U+0070): X=257.5,Y=1.0 (should be at baseline 0?)

	* s (U+0073): X=188.5,Y=526.0 (should be at x-height 527?)

	* y (U+0079): X=466.0,Y=1.0 (should be at baseline 0?)

	* uni00B3 (U+00B3): X=230.5,Y=709.0 (should be at cap-height 707?)

	* atilde (U+00E3): X=142.0,Y=707.5 (should be at cap-height 707?)

	* atilde (U+00E3): X=295.0,Y=705.0 (should be at cap-height 707?)

	* atilde (U+00E3): X=389.5,Y=709.0 (should be at cap-height 707?)

	* adieresis (U+00E4): X=206.0,Y=705.5 (should be at cap-height 707?)

	* adieresis (U+00E4): X=136.5,Y=705.0 (should be at cap-height 707?)

	* adieresis (U+00E4): X=436.0,Y=705.5 (should be at cap-height 707?)

	* adieresis (U+00E4): X=367.0,Y=705.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=167.0,Y=707.5 (should be at cap-height 707?)

	* ntilde (U+00F1): X=320.0,Y=705.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=414.5,Y=709.0 (should be at cap-height 707?)

	* otilde (U+00F5): X=159.0,Y=707.5 (should be at cap-height 707?)

	* otilde (U+00F5): X=312.0,Y=705.0 (should be at cap-height 707?)

	* otilde (U+00F5): X=406.5,Y=709.0 (should be at cap-height 707?)

	* odieresis (U+00F6): X=217.0,Y=705.5 (should be at cap-height 707?)

	* odieresis (U+00F6): X=147.5,Y=705.0 (should be at cap-height 707?)

	* odieresis (U+00F6): X=447.0,Y=705.5 (should be at cap-height 707?)

	* odieresis (U+00F6): X=378.0,Y=705.0 (should be at cap-height 707?)

	* udieresis (U+00FC): X=211.0,Y=705.5 (should be at cap-height 707?)

	* udieresis (U+00FC): X=141.5,Y=705.0 (should be at cap-height 707?)

	* udieresis (U+00FC): X=441.0,Y=705.5 (should be at cap-height 707?)

	* udieresis (U+00FC): X=372.0,Y=705.0 (should be at cap-height 707?)

	* yacute (U+00FD): X=466.0,Y=1.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=466.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=367.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=355.0,Y=-1.0 (should be at baseline 0?)

	* uni0122 (U+0122): X=340.0,Y=-304.0 (should be at descender -305?)

	* itilde (U+0129): X=-32.0,Y=705.5 (should be at cap-height 707?)

	* ij (U+0133): X=317.0,Y=2.0 (should be at baseline 0?)

	* jcircumflex (U+0135): X=105.0,Y=2.0 (should be at baseline 0?)

	* uni0136 (U+0136): X=289.0,Y=-303.0 (should be at descender -305?)

	* uni0137 (U+0137): X=236.0,Y=-304.0 (should be at descender -305?)

	* uni013B (U+013B): X=299.0,Y=-303.0 (should be at descender -305?)

	* uni013C (U+013C): X=68.0,Y=-303.0 (should be at descender -305?)

	* uni0145 (U+0145): X=344.0,Y=-304.0 (should be at descender -305?)

	* uni0146 (U+0146): X=270.0,Y=-304.0 (should be at descender -305?)

	* uni0156 (U+0156): X=300.0,Y=-304.0 (should be at descender -305?)

	* uni0157 (U+0157): X=68.0,Y=-304.0 (should be at descender -305?)

	* utilde (U+0169): X=151.0,Y=707.5 (should be at cap-height 707?)

	* utilde (U+0169): X=304.0,Y=705.0 (should be at cap-height 707?)

	* utilde (U+0169): X=398.5,Y=709.0 (should be at cap-height 707?)

	* ycircumflex (U+0177): X=466.0,Y=1.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=288.0,Y=-304.0 (should be at descender -305?)

	* uni0219 (U+0219): X=223.0,Y=-304.0 (should be at descender -305?)

	* uni021A (U+021A): X=251.0,Y=-304.0 (should be at descender -305?)

	* uni021B (U+021B): X=179.0,Y=-304.0 (should be at descender -305?)

	* uni0237 (U+0237): X=105.0,Y=2.0 (should be at baseline 0?)

	* tilde (U+02DC): X=138.0,Y=707.5 (should be at cap-height 707?)

	* tilde (U+02DC): X=291.0,Y=705.0 (should be at cap-height 707?)

	* tilde (U+02DC): X=385.5,Y=709.0 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-419.0,Y=707.5 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-266.0,Y=705.0 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-171.5,Y=709.0 (should be at cap-height 707?)

	* uni0326 (U+0326): X=-329.0,Y=-304.0 (should be at descender -305?)

	* uni040E (U+040E): X=107.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=107.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=390.5,Y=708.5 (should be at cap-height 707?)

	* uni0417 (U+0417): X=227.5,Y=0.5 (should be at baseline 0?)

	* uni0423 (U+0423): X=107.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=107.0,Y=-1.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=334.0,Y=1.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=190.0,Y=-0.5 (should be at baseline 0?)

	* uni0451 (U+0451): X=178.0,Y=705.0 (should be at cap-height 707?)

	* uni0451 (U+0451): X=178.0,Y=705.0 (should be at cap-height 707?)

	* uni0451 (U+0451): X=408.0,Y=705.0 (should be at cap-height 707?)

	* uni0451 (U+0451): X=408.0,Y=705.0 (should be at cap-height 707?)

	* uni0458 (U+0458): X=105.0,Y=2.0 (should be at baseline 0?)

	* ygrave (U+1EF3): X=466.0,Y=1.0 (should be at baseline 0?)

	* uni21BA (U+21BA): X=246.5,Y=-2.0 (should be at baseline 0?)

	* uni21BB (U+21BB): X=681.0,Y=-2.0 (should be at baseline 0?)

	* uni27F5 (U+27F5): X=415.0,Y=-1.0 (should be at baseline 0?)

	* uni27F6 (U+27F6): X=956.0,Y=-1.0 (should be at baseline 0?) 

	* uniE003 (U+E003): X=265.0,Y=707.5 (should be at cap-height 707?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* nine (U+0039) contains a short segment B<<497.0,355.0>-<497.0,362.0>-<496.5,371.0>>

	* nine (U+0039) contains a short segment B<<496.5,371.0>-<496.0,380.0>-<496.0,387.0>>

	* AE (U+00C6) contains a short segment L<<433.0,647.0>--<427.0,647.0>>

	* germandbls (U+00DF) contains a short segment B<<431.0,281.5>-<444.0,277.0>-<453.0,274.0>>

	* aogonek (U+0105) contains a short segment L<<493.0,0.0>--<480.0,0.0>>

	* eogonek (U+0119) contains a short segment B<<367.0,1.0>-<364.0,0.0>-<361.0,0.0>>

	* eogonek (U+0119) contains a short segment B<<361.0,0.0>-<358.0,0.0>-<355.0,-1.0>>

	* Iogonek (U+012E) contains a short segment L<<157.0,0.0>--<153.0,0.0>>

	* iogonek (U+012F) contains a short segment L<<146.0,0.0>--<141.0,0.0>>

	* Eng (U+014A) contains a short segment L<<459.0,-132.0>--<484.0,-132.0>>

	* uni0162 (U+0162) contains a short segment L<<318.0,0.0>--<306.0,0.0>>

	* uni0162 (U+0162) contains a short segment L<<263.0,0.0>--<253.0,0.0>>

	* Uogonek (U+0172) contains a short segment B<<421.0,-167.0>-<432.0,-167.0>-<443.0,-165.0>>

	* Uogonek (U+0172) contains a short segment B<<443.0,-165.0>-<454.0,-163.0>-<464.0,-158.0>>

	* uni0414 (U+0414) contains a short segment L<<27.0,60.0>--<37.0,60.0>>

	* uniE009 (U+E009) contains a short segment B<<538.0,355.0>-<538.0,362.0>-<537.5,371.0>> 

	* uniE009 (U+E009) contains a short segment B<<537.5,371.0>-<537.0,380.0>-<537.0,387.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<102.0,195.0>--<100.0,707.0>>

	* exclam (U+0021): L<<164.0,707.0>--<162.0,195.0>>

	* exclamdown (U+00A1): L<<161.0,330.0>--<163.0,-182.0>> 

	* exclamdown (U+00A1): L<<99.0,-182.0>--<101.0,330.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[16] Onest-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '800'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 554 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 604:
plus

Width = 499:
less

Width = 576:
equal

Width = 498:
greater

Width = 594:
plusminus

Width = 597:
multiply

Width = 567:
divide

Width = 585:
minus

Width = 648:
approxequal

Width = 582:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=262.0,Y=1.0 (should be at baseline 0?)

	* dollar (U+0024): X=266.0,Y=710.0 (should be at cap-height 708?)

	* dollar (U+0024): X=410.0,Y=709.0 (should be at cap-height 708?)

	* ampersand (U+0026): X=389.5,Y=2.0 (should be at baseline 0?)

	* Q (U+0051): X=456.5,Y=-1.5 (should be at baseline 0?)

	* S (U+0053): X=247.5,Y=707.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=222.0,Y=709.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=332.0,Y=709.0 (should be at cap-height 708?)

	* a (U+0061): X=283.5,Y=1.5 (should be at baseline 0?)

	* h (U+0068): X=291.0,Y=525.5 (should be at x-height 527?)

	* braceleft (U+007B): X=269.5,Y=0.5 (should be at baseline 0?)

	* section (U+00A7): X=213.5,Y=708.5 (should be at cap-height 708?)

	* Aring (U+00C5): X=364.0,Y=969.0 (should be at ascender 970?)

	* Aring (U+00C5): X=364.0,Y=969.0 (should be at ascender 970?)

	* agrave (U+00E0): X=283.5,Y=1.5 (should be at baseline 0?)

	* aacute (U+00E1): X=283.5,Y=1.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=283.5,Y=1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=338.0,Y=709.0 (should be at cap-height 708?)

	* atilde (U+00E3): X=283.5,Y=1.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=283.5,Y=1.5 (should be at baseline 0?)

	* aring (U+00E5): X=283.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=162.5,Y=1.5 (should be at baseline 0?)

	* ntilde (U+00F1): X=359.0,Y=709.0 (should be at cap-height 708?)

	* otilde (U+00F5): X=349.0,Y=709.0 (should be at cap-height 708?)

	* amacron (U+0101): X=283.5,Y=1.5 (should be at baseline 0?)

	* abreve (U+0103): X=283.5,Y=1.5 (should be at baseline 0?)

	* aogonek (U+0105): X=283.5,Y=1.5 (should be at baseline 0?)

	* eogonek (U+0119): X=380.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=364.5,Y=-1.5 (should be at baseline 0?)

	* itilde (U+0129): X=181.0,Y=709.0 (should be at cap-height 708?)

	* Sacute (U+015A): X=247.5,Y=707.0 (should be at cap-height 708?)

	* Scircumflex (U+015C): X=247.5,Y=707.0 (should be at cap-height 708?)

	* Scedilla (U+015E): X=234.0,Y=706.5 (should be at cap-height 708?)

	* scedilla (U+015F): X=206.0,Y=-1.0 (should be at baseline 0?)

	* Scaron (U+0160): X=247.5,Y=707.0 (should be at cap-height 708?)

	* utilde (U+0169): X=343.0,Y=709.0 (should be at cap-height 708?)

	* Uring (U+016E): X=377.0,Y=969.0 (should be at ascender 970?)

	* Uring (U+016E): X=377.0,Y=969.0 (should be at ascender 970?)

	* Uogonek (U+0172): X=474.0,Y=1.5 (should be at baseline 0?)

	* Uogonek (U+0172): X=278.5,Y=2.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=239.5,Y=707.0 (should be at cap-height 708?)

	* uni0219 (U+0219): X=231.0,Y=-304.0 (should be at descender -305?)

	* uni021B (U+021B): X=175.0,Y=-304.0 (should be at descender -305?)

	* ogonek (U+02DB): X=286.0,Y=2.0 (should be at baseline 0?)

	* tilde (U+02DC): X=355.0,Y=709.0 (should be at cap-height 708?)

	* tildecomb (U+0303): X=-245.0,Y=709.0 (should be at cap-height 708?)

	* uni0328 (U+0328): X=-69.0,Y=2.0 (should be at baseline 0?)

	* uni0405 (U+0405): X=247.5,Y=707.0 (should be at cap-height 708?)

	* uni0417 (U+0417): X=431.0,Y=707.5 (should be at cap-height 708?)

	* uni041B (U+041B): X=30.0,Y=-1.0 (should be at baseline 0?)

	* uni041B (U+041B): X=1.0,Y=-1.0 (should be at baseline 0?)

	* uni0430 (U+0430): X=283.5,Y=1.5 (should be at baseline 0?)

	* uni0437 (U+0437): X=358.5,Y=-0.5 (should be at baseline 0?)

	* uni0437 (U+0437): X=189.0,Y=1.5 (should be at baseline 0?)

	* uni0455 (U+0455): X=352.0,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=398.0,Y=706.5 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=386.0,Y=0.5 (should be at baseline 0?) 

	* uni20B4 (U+20B4): X=212.5,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* paragraph (U+00B6) contains a short segment L<<221.0,315.0>--<207.0,315.0>>

	* Ccedilla (U+00C7) contains a short segment L<<416.0,-34.0>--<424.0,-34.0>>

	* Ccedilla (U+00C7) contains a short segment B<<319.5,-173.0>-<332.0,-174.0>-<343.0,-174.0>>

	* Ccedilla (U+00C7) contains a short segment B<<314.5,-106.0>-<301.0,-107.0>-<294.0,-109.0>>

	* ccedilla (U+00E7) contains a short segment L<<329.0,-35.0>--<337.0,-35.0>>

	* eogonek (U+0119) contains a short segment B<<380.0,1.0>-<373.0,0.0>-<364.5,-1.5>>

	* eogonek (U+0119) contains a short segment B<<364.5,-1.5>-<356.0,-3.0>-<348.0,-4.0>>

	* Scedilla (U+015E) contains a short segment L<<362.0,-36.0>--<370.0,-36.0>>

	* Scedilla (U+015E) contains a short segment B<<266.5,-176.0>-<279.0,-177.0>-<290.0,-177.0>>

	* Scedilla (U+015E) contains a short segment B<<264.0,-109.0>-<250.0,-110.0>-<240.0,-112.0>>

	* scedilla (U+015F) contains a short segment L<<297.0,-37.0>--<305.0,-37.0>>

	* uni0162 (U+0162) contains a short segment L<<342.0,-35.0>--<350.0,-35.0>>

	* uni0163 (U+0163) contains a short segment L<<259.0,-35.0>--<267.0,-35.0>>

	* uni0443 (U+0443) contains a short segment L<<81.0,-110.0>--<99.0,-110.0>>

	* uni045E (U+045E) contains a short segment L<<81.0,-110.0>--<99.0,-110.0>>

	* Euro (U+20AC) contains a short segment B<<296.0,378.0>-<295.0,366.0>-<295.5,354.0>>

	* Euro (U+20AC) contains a short segment B<<295.5,354.0>-<296.0,342.0>-<296.0,331.0>>

	* uni20B4 (U+20B4) contains a short segment B<<242.0,233.0>-<231.0,226.0>-<224.5,214.5>> 

	* uni20B4 (U+20B4) contains a short segment B<<224.5,214.5>-<218.0,203.0>-<218.0,193.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni041B (U+041B): L<<270.0,559.0>--<269.0,390.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] Onest-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '500'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 564 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 467:
less, greater

Width = 554:
equal, notequal

Width = 526:
multiply

Width = 516:
divide

Width = 540:
minus

Width = 627:
approxequal

Width = 531:
greaterequal, lessequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* S (U+0053): X=236.0,Y=705.5 (should be at cap-height 707?)

	* s (U+0073): X=184.5,Y=528.0 (should be at x-height 527?)

	* section (U+00A7): X=207.0,Y=706.5 (should be at cap-height 707?)

	* questiondown (U+00BF): X=164.0,Y=2.0 (should be at baseline 0?)

	* Oslash (U+00D8): X=299.0,Y=1.0 (should be at baseline 0?)

	* Oslash (U+00D8): X=471.0,Y=708.0 (should be at cap-height 707?)

	* Oslash (U+00D8): X=299.0,Y=1.0 (should be at baseline 0?)

	* ae (U+00E6): X=567.5,Y=1.5 (should be at baseline 0?)

	* eth (U+00F0): X=510.0,Y=705.0 (should be at cap-height 707?)

	* oslash (U+00F8): X=225.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=372.0,Y=1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=363.0,Y=-0.5 (should be at baseline 0?)

	* eogonek (U+0119): X=353.0,Y=-2.0 (should be at baseline 0?)

	* eogonek (U+0119): X=220.0,Y=1.0 (should be at baseline 0?)

	* uni0122 (U+0122): X=339.0,Y=-303.0 (should be at descender -305?)

	* uni0136 (U+0136): X=309.0,Y=-303.0 (should be at descender -305?)

	* uni0137 (U+0137): X=251.0,Y=-303.0 (should be at descender -305?)

	* uni013B (U+013B): X=288.0,Y=-303.0 (should be at descender -305?)

	* uni013C (U+013C): X=78.0,Y=-303.0 (should be at descender -305?)

	* uni0145 (U+0145): X=337.0,Y=-303.0 (should be at descender -305?)

	* uni0146 (U+0146): X=264.0,Y=-303.0 (should be at descender -305?)

	* uni0156 (U+0156): X=296.0,Y=-303.0 (should be at descender -305?)

	* uni0157 (U+0157): X=78.0,Y=-303.0 (should be at descender -305?)

	* Sacute (U+015A): X=236.0,Y=705.5 (should be at cap-height 707?)

	* Scircumflex (U+015C): X=236.0,Y=705.5 (should be at cap-height 707?)

	* Scedilla (U+015E): X=226.0,Y=705.5 (should be at cap-height 707?)

	* Scaron (U+0160): X=236.0,Y=705.5 (should be at cap-height 707?)

	* uogonek (U+0173): X=371.5,Y=1.5 (should be at baseline 0?)

	* uogonek (U+0173): X=355.0,Y=-2.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=226.0,Y=705.5 (should be at cap-height 707?)

	* uni0218 (U+0218): X=281.0,Y=-304.0 (should be at descender -305?)

	* uni021A (U+021A): X=248.0,Y=-304.0 (should be at descender -305?)

	* uni0326 (U+0326): X=-336.0,Y=-303.0 (should be at descender -305?)

	* uni0405 (U+0405): X=236.0,Y=705.5 (should be at cap-height 707?)

	* uni0417 (U+0417): X=248.5,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=412.5,Y=706.5 (should be at cap-height 707?)

	* uni0437 (U+0437): X=344.5,Y=0.5 (should be at baseline 0?)

	* uni0437 (U+0437): X=187.0,Y=1.0 (should be at baseline 0?)

	* uni0451 (U+0451): X=231.5,Y=707.5 (should be at cap-height 707?)

	* uni0451 (U+0451): X=128.0,Y=707.5 (should be at cap-height 707?)

	* uni0451 (U+0451): X=466.0,Y=707.5 (should be at cap-height 707?)

	* uni0451 (U+0451): X=362.5,Y=707.5 (should be at cap-height 707?)

	* quotesinglbase (U+201A): X=131.0,Y=-2.0 (should be at baseline 0?)

	* quotesinglbase (U+201A): X=131.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=131.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=131.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=336.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=336.0,Y=-2.0 (should be at baseline 0?)

	* uniE020 (U+E020): X=137.0,Y=-2.0 (should be at baseline 0?)

	* uniE020 (U+E020): X=137.0,Y=-2.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=91.0,Y=-2.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=91.0,Y=-2.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=296.0,Y=-2.0 (should be at baseline 0?) 

	* uniE021 (U+E021): X=296.0,Y=-2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<535.0,-74.5>-<552.0,-73.0>-<568.0,-70.5>>

	* at (U+0040) contains a short segment B<<568.0,-70.5>-<584.0,-68.0>-<605.0,-64.0>>

	* paragraph (U+00B6) contains a short segment L<<255.0,314.0>--<245.0,314.0>>

	* questiondown (U+00BF) contains a short segment B<<334.0,288.0>-<334.0,284.0>-<334.0,278.0>>

	* Ccedilla (U+00C7) contains a short segment B<<393.0,-50.0>-<403.0,-49.0>-<406.5,-49.0>>

	* Ccedilla (U+00C7) contains a short segment B<<406.5,-49.0>-<410.0,-49.0>-<413.0,-49.0>>

	* Ccedilla (U+00C7) contains a short segment B<<303.0,-187.0>-<311.0,-188.0>-<318.0,-188.0>>

	* Ccedilla (U+00C7) contains a short segment B<<318.0,-188.0>-<325.0,-188.0>-<332.0,-188.0>>

	* ccedilla (U+00E7) contains a short segment B<<312.0,-51.0>-<320.0,-50.0>-<325.5,-50.0>>

	* ccedilla (U+00E7) contains a short segment B<<325.5,-50.0>-<331.0,-50.0>-<333.0,-50.0>>

	* ccedilla (U+00E7) contains a short segment B<<220.0,-188.0>-<227.0,-189.0>-<236.0,-189.5>>

	* ccedilla (U+00E7) contains a short segment B<<236.0,-189.5>-<245.0,-190.0>-<251.0,-190.0>>

	* aogonek (U+0105) contains a short segment L<<506.0,0.0>--<496.0,0.0>>

	* Eogonek (U+0118) contains a short segment B<<385.0,0.0>-<378.0,-4.0>-<366.0,-12.0>>

	* eogonek (U+0119) contains a short segment B<<372.0,1.0>-<368.0,0.0>-<363.0,-0.5>>

	* eogonek (U+0119) contains a short segment B<<363.0,-0.5>-<358.0,-1.0>-<353.0,-2.0>>

	* eogonek (U+0119) contains a short segment B<<353.0,-2.0>-<349.0,-4.0>-<346.0,-7.0>>

	* eogonek (U+0119) contains a short segment B<<346.0,-7.0>-<343.0,-10.0>-<339.0,-12.0>>

	* Eng (U+014A) contains a short segment L<<560.0,0.0>--<550.0,0.0>>

	* Scedilla (U+015E) contains a short segment B<<340.0,-52.0>-<350.0,-51.0>-<354.0,-51.0>>

	* Scedilla (U+015E) contains a short segment B<<354.0,-51.0>-<358.0,-51.0>-<361.0,-51.0>>

	* Scedilla (U+015E) contains a short segment B<<250.0,-187.0>-<258.0,-188.0>-<266.0,-188.5>>

	* Scedilla (U+015E) contains a short segment B<<266.0,-188.5>-<274.0,-189.0>-<282.0,-189.0>>

	* Scedilla (U+015E) contains a short segment B<<273.5,-110.5>-<261.0,-112.0>-<251.0,-114.0>>

	* scedilla (U+015F) contains a short segment B<<280.0,-52.0>-<285.0,-51.0>-<290.0,-51.0>>

	* scedilla (U+015F) contains a short segment B<<290.0,-51.0>-<295.0,-51.0>-<300.0,-51.0>>

	* scedilla (U+015F) contains a short segment B<<190.0,-188.0>-<198.0,-189.0>-<206.0,-189.5>>

	* scedilla (U+015F) contains a short segment B<<206.0,-189.5>-<214.0,-190.0>-<222.0,-190.0>>

	* uni0162 (U+0162) contains a short segment B<<314.0,-50.0>-<322.0,-49.0>-<326.0,-49.0>>

	* uni0162 (U+0162) contains a short segment B<<326.0,-49.0>-<330.0,-49.0>-<334.0,-49.0>>

	* uni0162 (U+0162) contains a short segment B<<224.0,-186.0>-<233.0,-187.0>-<241.5,-187.5>>

	* uni0162 (U+0162) contains a short segment B<<241.5,-187.5>-<250.0,-188.0>-<258.0,-188.0>>

	* uni0163 (U+0163) contains a short segment B<<244.0,-51.0>-<253.0,-50.0>-<256.5,-50.0>>

	* uni0163 (U+0163) contains a short segment B<<256.5,-50.0>-<260.0,-50.0>-<265.0,-50.0>>

	* uni0163 (U+0163) contains a short segment B<<154.0,-188.0>-<163.0,-190.0>-<171.0,-190.5>>

	* uni0163 (U+0163) contains a short segment B<<171.0,-190.5>-<179.0,-191.0>-<187.0,-191.0>>

	* Uogonek (U+0172) contains a short segment B<<425.0,-4.0>-<423.0,-6.0>-<420.0,-8.0>>

	* Uogonek (U+0172) contains a short segment B<<420.0,-8.0>-<417.0,-10.0>-<415.0,-12.0>>

	* uogonek (U+0173) contains a short segment B<<387.0,5.0>-<380.0,3.0>-<371.5,1.5>>

	* uogonek (U+0173) contains a short segment B<<371.5,1.5>-<363.0,0.0>-<355.0,-2.0>>

	* uogonek (U+0173) contains a short segment B<<355.0,-2.0>-<351.0,-4.0>-<347.5,-6.5>>

	* uogonek (U+0173) contains a short segment B<<347.5,-6.5>-<344.0,-9.0>-<340.0,-12.0>>

	* uni040E (U+040E) contains a short segment B<<334.0,315.0>-<335.0,318.0>-<338.0,325.0>>

	* uni0414 (U+0414) contains a short segment L<<17.0,103.0>--<25.0,103.0>>

	* uni0443 (U+0443) contains a short segment L<<88.0,-149.0>--<96.0,-149.0>> 

	* uni045E (U+045E) contains a short segment L<<88.0,-149.0>--<96.0,-149.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[16] Onest-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '100'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 529 among a set of 4 math glyphs.
The following math glyphs have a different width, though:

Width = 508:
plus, minus

Width = 429:
less, greater

Width = 498:
plusminus

Width = 442:
multiply

Width = 459:
divide

Width = 602:
approxequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* comma (U+002C): X=91.0,Y=-2.0 (should be at baseline 0?)

	* semicolon (U+003B): X=92.0,Y=-2.0 (should be at baseline 0?)

	* b (U+0062): X=244.0,Y=1.0 (should be at baseline 0?)

	* m (U+006D): X=222.0,Y=526.5 (should be at x-height 527?)

	* p (U+0070): X=250.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=147.0,Y=706.0 (should be at cap-height 707?)

	* braceright (U+007D): X=224.0,Y=705.0 (should be at cap-height 707?)

	* section (U+00A7): X=193.5,Y=2.0 (should be at baseline 0?)

	* section (U+00A7): X=344.5,Y=705.0 (should be at cap-height 707?)

	* uni00B2 (U+00B2): X=137.0,Y=707.5 (should be at cap-height 707?)

	* uni00B3 (U+00B3): X=136.5,Y=707.5 (should be at cap-height 707?)

	* ordmasculine (U+00BA): X=186.0,Y=708.0 (should be at cap-height 707?)

	* atilde (U+00E3): X=218.0,Y=708.0 (should be at cap-height 707?)

	* atilde (U+00E3): X=156.0,Y=709.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=238.0,Y=708.0 (should be at cap-height 707?)

	* ntilde (U+00F1): X=176.0,Y=709.0 (should be at cap-height 707?)

	* otilde (U+00F5): X=237.0,Y=708.0 (should be at cap-height 707?)

	* otilde (U+00F5): X=175.0,Y=709.0 (should be at cap-height 707?)

	* itilde (U+0129): X=30.0,Y=708.0 (should be at cap-height 707?)

	* itilde (U+0129): X=-32.0,Y=709.0 (should be at cap-height 707?)

	* utilde (U+0169): X=220.0,Y=708.0 (should be at cap-height 707?)

	* utilde (U+0169): X=158.0,Y=709.0 (should be at cap-height 707?)

	* ogonek (U+02DB): X=271.0,Y=1.0 (should be at baseline 0?)

	* tilde (U+02DC): X=202.0,Y=708.0 (should be at cap-height 707?)

	* tilde (U+02DC): X=140.0,Y=709.0 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-335.0,Y=708.0 (should be at cap-height 707?)

	* tildecomb (U+0303): X=-397.0,Y=709.0 (should be at cap-height 707?)

	* uni0328 (U+0328): X=-239.0,Y=1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=237.0,Y=708.0 (should be at cap-height 707?)

	* uni0417 (U+0417): X=403.5,Y=2.0 (should be at baseline 0?)

	* uni0417 (U+0417): X=228.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=109.0,Y=-1.0 (should be at baseline 0?)

	* uni0431 (U+0431): X=349.0,Y=709.0 (should be at cap-height 707?)

	* uni0437 (U+0437): X=172.0,Y=2.0 (should be at baseline 0?)

	* uni0440 (U+0440): X=250.0,Y=1.0 (should be at baseline 0?)

	* quotesinglbase (U+201A): X=92.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=92.0,Y=-2.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=242.0,Y=-2.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=371.5,Y=2.0 (should be at baseline 0?)

	* uni2713 (U+2713): X=373.0,Y=2.0 (should be at baseline 0?)

	* uniE011 (U+E011): X=91.0,Y=-2.0 (should be at baseline 0?)

	* uniE013 (U+E013): X=92.0,Y=-2.0 (should be at baseline 0?)

	* uniE020 (U+E020): X=91.0,Y=-2.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=45.0,Y=-2.0 (should be at baseline 0?) 

	* uniE021 (U+E021): X=195.0,Y=-2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment L<<659.0,453.0>--<697.0,453.0>>

	* M (U+004D) contains a short segment L<<431.0,195.0>--<409.0,195.0>>

	* r (U+0072) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* paragraph (U+00B6) contains a short segment L<<193.0,419.0>--<177.0,419.0>>

	* Ccedilla (U+00C7) contains a short segment B<<355.0,-79.0>-<366.0,-77.0>-<373.0,-76.5>>

	* Ccedilla (U+00C7) contains a short segment B<<373.0,-76.5>-<380.0,-76.0>-<391.0,-76.0>>

	* ccedilla (U+00E7) contains a short segment B<<280.0,-79.0>-<291.0,-77.0>-<297.5,-76.5>>

	* ccedilla (U+00E7) contains a short segment B<<297.5,-76.5>-<304.0,-76.0>-<315.0,-76.0>>

	* Aogonek (U+0104) contains a short segment L<<622.0,0.0>--<614.0,0.0>>

	* aogonek (U+0105) contains a short segment B<<428.0,-11.0>-<432.0,-8.0>-<435.0,-5.0>>

	* aogonek (U+0105) contains a short segment B<<435.0,-5.0>-<438.0,-2.0>-<442.0,0.0>>

	* aogonek (U+0105) contains a short segment L<<482.0,0.0>--<478.0,0.0>>

	* Iogonek (U+012E) contains a short segment L<<135.0,0.0>--<131.0,0.0>>

	* iogonek (U+012F) contains a short segment B<<71.0,-11.0>-<75.0,-8.0>-<78.0,-5.0>>

	* iogonek (U+012F) contains a short segment B<<78.0,-5.0>-<81.0,-2.0>-<85.0,0.0>>

	* iogonek (U+012F) contains a short segment L<<125.0,0.0>--<121.0,0.0>>

	* Eng (U+014A) contains a short segment L<<467.0,-161.0>--<494.0,-161.0>>

	* racute (U+0155) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* uni0157 (U+0157) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* rcaron (U+0159) contains a short segment L<<334.0,494.0>--<327.0,494.0>>

	* Scedilla (U+015E) contains a short segment B<<320.0,-79.0>-<329.0,-77.0>-<337.0,-76.5>>

	* Scedilla (U+015E) contains a short segment B<<337.0,-76.5>-<345.0,-76.0>-<352.0,-76.0>>

	* Scedilla (U+015E) contains a short segment B<<339.0,-100.0>-<328.0,-100.0>-<312.0,-102.0>>

	* scedilla (U+015F) contains a short segment B<<242.0,-79.0>-<250.0,-77.0>-<259.0,-76.5>>

	* scedilla (U+015F) contains a short segment B<<259.0,-76.5>-<268.0,-76.0>-<275.0,-76.0>>

	* uni0162 (U+0162) contains a short segment B<<271.0,-79.0>-<282.0,-77.0>-<288.5,-76.5>>

	* uni0162 (U+0162) contains a short segment B<<288.5,-76.5>-<295.0,-76.0>-<306.0,-76.0>>

	* uni0162 (U+0162) contains a short segment L<<269.0,0.0>--<262.0,0.0>>

	* uni0162 (U+0162) contains a short segment L<<304.0,0.0>--<295.0,0.0>>

	* uni0163 (U+0163) contains a short segment B<<196.0,-79.0>-<207.0,-77.0>-<213.5,-76.5>>

	* uni0163 (U+0163) contains a short segment B<<213.5,-76.5>-<220.0,-76.0>-<231.0,-76.0>>

	* Uogonek (U+0172) contains a short segment B<<419.0,-168.0>-<428.0,-169.0>-<439.5,-166.5>>

	* Uogonek (U+0172) contains a short segment B<<439.5,-166.5>-<451.0,-164.0>-<459.0,-161.0>>

	* uni041C (U+041C) contains a short segment L<<431.0,195.0>--<409.0,195.0>> 

	* uni043C (U+043C) contains a short segment L<<353.0,139.0>--<339.0,139.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<104.0,177.0>--<102.0,707.0>>

	* exclam (U+0021): L<<143.0,707.0>--<141.0,177.0>>

	* exclamdown (U+00A1): L<<101.0,-181.0>--<103.0,349.0>> 

	* exclamdown (U+00A1): L<<140.0,349.0>--<142.0,-181.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] Onest-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '700'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 603 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 485:
less, greater

Width = 563:
equal, notequal

Width = 571:
multiply

Width = 554:
divide

Width = 573:
minus

Width = 646:
approxequal

Width = 552:
greaterequal, lessequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=265.0,Y=-1.0 (should be at baseline 0?)

	* ampersand (U+0026): X=390.0,Y=-0.5 (should be at baseline 0?)

	* two (U+0032): X=187.0,Y=707.5 (should be at cap-height 708?)

	* three (U+0033): X=382.5,Y=707.5 (should be at cap-height 708?)

	* question (U+003F): X=342.5,Y=710.0 (should be at cap-height 708?)

	* S (U+0053): X=239.5,Y=707.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=209.0,Y=709.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=311.0,Y=709.0 (should be at cap-height 708?)

	* a (U+0061): X=383.0,Y=526.0 (should be at x-height 527?)

	* section (U+00A7): X=217.0,Y=708.5 (should be at cap-height 708?)

	* ordfeminine (U+00AA): X=288.0,Y=708.5 (should be at cap-height 708?)

	* paragraph (U+00B6): X=709.0,Y=707.0 (should be at cap-height 708?)

	* paragraph (U+00B6): X=229.0,Y=707.0 (should be at cap-height 708?)

	* Aring (U+00C5): X=354.0,Y=968.0 (should be at ascender 970?)

	* Aring (U+00C5): X=354.0,Y=968.0 (should be at ascender 970?)

	* Oslash (U+00D8): X=320.0,Y=-2.0 (should be at baseline 0?)

	* Sacute (U+015A): X=237.5,Y=707.0 (should be at cap-height 708?)

	* Scircumflex (U+015C): X=240.0,Y=707.5 (should be at cap-height 708?)

	* Scedilla (U+015E): X=234.0,Y=707.5 (should be at cap-height 708?)

	* Scaron (U+0160): X=240.0,Y=709.0 (should be at cap-height 708?)

	* Uogonek (U+0172): X=280.0,Y=2.0 (should be at baseline 0?)

	* uogonek (U+0173): X=382.5,Y=0.5 (should be at baseline 0?)

	* uni0218 (U+0218): X=230.5,Y=707.0 (should be at cap-height 708?)

	* uni0218 (U+0218): X=275.0,Y=-303.0 (should be at descender -305?)

	* uni0219 (U+0219): X=226.0,Y=-304.0 (should be at descender -305?)

	* uni021B (U+021B): X=177.0,Y=-304.0 (should be at descender -305?)

	* uni0326 (U+0326): X=-335.0,Y=-303.0 (should be at descender -305?)

	* uni0405 (U+0405): X=240.0,Y=709.0 (should be at cap-height 708?)

	* uni0417 (U+0417): X=433.5,Y=707.0 (should be at cap-height 708?)

	* uni041B (U+041B): X=31.0,Y=-1.0 (should be at baseline 0?)

	* uni041B (U+041B): X=10.0,Y=-1.0 (should be at baseline 0?)

	* uni0431 (U+0431): X=236.0,Y=707.0 (should be at cap-height 708?)

	* uni0437 (U+0437): X=185.0,Y=1.0 (should be at baseline 0?)

	* quoteleft (U+2018): X=238.0,Y=710.0 (should be at cap-height 708?)

	* quoteright (U+2019): X=82.5,Y=709.5 (should be at cap-height 708?)

	* quotesinglbase (U+201A): X=132.0,Y=-1.0 (should be at baseline 0?)

	* quotesinglbase (U+201A): X=132.0,Y=-1.0 (should be at baseline 0?)

	* quotedblleft (U+201C): X=460.0,Y=710.0 (should be at cap-height 708?)

	* quotedblleft (U+201C): X=239.0,Y=710.0 (should be at cap-height 708?)

	* quotedblright (U+201D): X=82.5,Y=709.5 (should be at cap-height 708?)

	* quotedblright (U+201D): X=304.0,Y=709.5 (should be at cap-height 708?)

	* quotedblbase (U+201E): X=133.0,Y=-1.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=133.0,Y=-1.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=354.0,Y=-1.0 (should be at baseline 0?)

	* quotedblbase (U+201E): X=354.0,Y=-1.0 (should be at baseline 0?)

	* uniE002 (U+E002): X=251.0,Y=707.5 (should be at cap-height 708?)

	* uniE003 (U+E003): X=416.5,Y=707.5 (should be at cap-height 708?)

	* uniE016 (U+E016): X=95.5,Y=709.5 (should be at cap-height 708?)

	* uniE017 (U+E017): X=49.5,Y=709.5 (should be at cap-height 708?)

	* uniE017 (U+E017): X=271.0,Y=709.5 (should be at cap-height 708?)

	* uniE018 (U+E018): X=251.0,Y=710.0 (should be at cap-height 708?)

	* uniE019 (U+E019): X=426.0,Y=710.0 (should be at cap-height 708?)

	* uniE019 (U+E019): X=205.0,Y=710.0 (should be at cap-height 708?)

	* uniE020 (U+E020): X=145.0,Y=-1.0 (should be at baseline 0?)

	* uniE020 (U+E020): X=145.0,Y=-1.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=100.0,Y=-1.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=100.0,Y=-1.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=321.0,Y=-1.0 (should be at baseline 0?) 

	* uniE021 (U+E021): X=321.0,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* paragraph (U+00B6) contains a short segment L<<251.0,314.0>--<239.0,314.0>>

	* Aogonek (U+0104) contains a short segment B<<671.0,0.0>-<667.0,-2.0>-<662.5,-4.5>>

	* Aogonek (U+0104) contains a short segment B<<662.5,-4.5>-<658.0,-7.0>-<654.0,-10.0>>

	* aogonek (U+0105) contains a short segment B<<500.0,0.0>-<496.0,-2.0>-<491.5,-4.5>>

	* aogonek (U+0105) contains a short segment B<<491.5,-4.5>-<487.0,-7.0>-<483.0,-10.0>>

	* Eogonek (U+0118) contains a short segment B<<395.0,0.0>-<391.0,-2.0>-<386.5,-4.5>>

	* Eogonek (U+0118) contains a short segment B<<386.5,-4.5>-<382.0,-7.0>-<378.0,-10.0>>

	* Scedilla (U+015E) contains a short segment B<<288.0,-108.0>-<276.0,-108.0>-<268.5,-108.0>>

	* Scedilla (U+015E) contains a short segment B<<268.5,-108.0>-<261.0,-108.0>-<242.0,-109.0>>

	* tbar (U+0167) contains a short segment L<<238.0,206.0>--<238.0,191.0>>

	* uni041B (U+041B) contains a short segment L<<10.0,127.0>--<23.0,127.0>>

	* uni043B (U+043B) contains a short segment L<<12.0,124.0>--<26.0,124.0>>

	* uni0443 (U+0443) contains a short segment L<<314.0,138.0>--<315.0,138.0>> 

	* uni045E (U+045E) contains a short segment L<<314.0,138.0>--<315.0,138.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[14] Onest-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 521 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 446:
less, greater

Width = 542:
equal, notequal

Width = 477:
multiply

Width = 474:
divide

Width = 504:
minus

Width = 615:
approxequal

Width = 507:
greaterequal, lessequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* comma (U+002C): X=128.0,Y=-2.0 (should be at baseline 0?)

	* comma (U+002C): X=128.0,Y=-2.0 (should be at baseline 0?)

	* three (U+0033): X=206.5,Y=0.5 (should be at baseline 0?)

	* S (U+0053): X=240.5,Y=705.0 (should be at cap-height 707?)

	* a (U+0061): X=297.5,Y=-0.5 (should be at baseline 0?)

	* j (U+006A): X=95.0,Y=-1.0 (should be at baseline 0?)

	* s (U+0073): X=333.0,Y=1.0 (should be at baseline 0?)

	* s (U+0073): X=185.0,Y=526.5 (should be at x-height 527?)

	* cent (U+00A2): X=257.0,Y=-2.0 (should be at baseline 0?)

	* section (U+00A7): X=356.0,Y=-1.0 (should be at baseline 0?)

	* section (U+00A7): X=206.0,Y=0.5 (should be at baseline 0?)

	* agrave (U+00E0): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=297.5,Y=-0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aring (U+00E5): X=314.5,Y=708.5 (should be at cap-height 707?)

	* aring (U+00E5): X=251.5,Y=708.5 (should be at cap-height 707?)

	* aring (U+00E5): X=297.5,Y=-0.5 (should be at baseline 0?)

	* eth (U+00F0): X=496.0,Y=709.0 (should be at cap-height 707?)

	* amacron (U+0101): X=297.5,Y=-0.5 (should be at baseline 0?)

	* aogonek (U+0105): X=297.5,Y=-0.5 (should be at baseline 0?)

	* eogonek (U+0119): X=228.0,Y=1.0 (should be at baseline 0?)

	* uni0122 (U+0122): X=335.0,Y=-304.0 (should be at descender -305?)

	* ij (U+0133): X=301.0,Y=-1.0 (should be at baseline 0?)

	* jcircumflex (U+0135): X=95.0,Y=-1.0 (should be at baseline 0?)

	* uni0136 (U+0136): X=289.0,Y=-304.0 (should be at descender -305?)

	* uni0137 (U+0137): X=231.0,Y=-304.0 (should be at descender -305?)

	* uni013B (U+013B): X=286.0,Y=-304.0 (should be at descender -305?)

	* uni013C (U+013C): X=72.0,Y=-304.0 (should be at descender -305?)

	* uni0145 (U+0145): X=327.0,Y=-304.0 (should be at descender -305?)

	* uni0146 (U+0146): X=260.0,Y=-304.0 (should be at descender -305?)

	* eng (U+014B): X=442.0,Y=-1.0 (should be at baseline 0?)

	* uni0156 (U+0156): X=292.0,Y=-304.0 (should be at descender -305?)

	* uni0157 (U+0157): X=77.0,Y=-304.0 (should be at descender -305?)

	* Sacute (U+015A): X=240.5,Y=705.0 (should be at cap-height 707?)

	* sacute (U+015B): X=333.5,Y=1.0 (should be at baseline 0?)

	* Scircumflex (U+015C): X=240.5,Y=705.0 (should be at cap-height 707?)

	* scircumflex (U+015D): X=333.0,Y=1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=231.0,Y=705.0 (should be at cap-height 707?)

	* Scaron (U+0160): X=240.5,Y=705.0 (should be at cap-height 707?)

	* scaron (U+0161): X=333.5,Y=1.0 (should be at baseline 0?)

	* uni0163 (U+0163): X=250.0,Y=1.0 (should be at baseline 0?)

	* tcaron (U+0165): X=403.0,Y=708.0 (should be at cap-height 707?)

	* Uogonek (U+0172): X=429.0,Y=-2.0 (should be at baseline 0?)

	* uogonek (U+0173): X=348.0,Y=-1.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=231.5,Y=705.0 (should be at cap-height 707?)

	* uni0218 (U+0218): X=395.0,Y=709.0 (should be at cap-height 707?)

	* uni0219 (U+0219): X=337.5,Y=1.0 (should be at baseline 0?)

	* uni0237 (U+0237): X=95.0,Y=-1.0 (should be at baseline 0?)

	* uni0405 (U+0405): X=240.5,Y=705.0 (should be at cap-height 707?)

	* uni040E (U+040E): X=123.0,Y=-1.0 (should be at baseline 0?)

	* uni040E (U+040E): X=123.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0423 (U+0423): X=116.0,Y=-1.0 (should be at baseline 0?)

	* uni0430 (U+0430): X=297.5,Y=-0.5 (should be at baseline 0?)

	* uni0437 (U+0437): X=182.0,Y=1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=50.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=19.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=333.5,Y=1.0 (should be at baseline 0?)

	* uni0458 (U+0458): X=95.0,Y=-1.0 (should be at baseline 0?)

	* quotedblright (U+201D): X=179.5,Y=706.5 (should be at cap-height 707?)

	* quotedblright (U+201D): X=368.5,Y=706.5 (should be at cap-height 707?)

	* uni21BA (U+21BA): X=238.0,Y=1.0 (should be at baseline 0?)

	* uni21BB (U+21BB): X=701.5,Y=0.5 (should be at baseline 0?)

	* uni2713 (U+2713): X=373.0,Y=-1.0 (should be at baseline 0?)

	* uniE003 (U+E003): X=254.5,Y=0.5 (should be at baseline 0?)

	* uniE013 (U+E013): X=130.0,Y=-2.0 (should be at baseline 0?)

	* uniE013 (U+E013): X=130.0,Y=-2.0 (should be at baseline 0?)

	* uniE018 (U+E018): X=119.0,Y=709.0 (should be at cap-height 707?)

	* uniE021 (U+E021): X=83.0,Y=-2.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=83.0,Y=-2.0 (should be at baseline 0?)

	* uniE021 (U+E021): X=248.0,Y=-2.0 (should be at baseline 0?) 

	* uniE021 (U+E021): X=248.0,Y=-2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment B<<191.0,213.0>-<190.0,218.0>-<190.0,223.5>>

	* question (U+003F) contains a short segment B<<190.0,223.5>-<190.0,229.0>-<190.0,234.0>>

	* at (U+0040) contains a short segment B<<531.5,-98.0>-<547.0,-97.0>-<561.5,-95.0>>

	* at (U+0040) contains a short segment B<<561.5,-95.0>-<576.0,-93.0>-<597.0,-89.0>>

	* questiondown (U+00BF) contains a short segment B<<322.0,312.0>-<323.0,307.0>-<323.0,301.5>>

	* questiondown (U+00BF) contains a short segment B<<323.0,301.5>-<323.0,296.0>-<323.0,291.0>>

	* Ccedilla (U+00C7) contains a short segment B<<386.0,-61.0>-<392.0,-60.0>-<398.0,-59.5>>

	* Ccedilla (U+00C7) contains a short segment B<<398.0,-59.5>-<404.0,-59.0>-<409.0,-59.0>>

	* Ccedilla (U+00C7) contains a short segment B<<341.0,-255.0>-<333.0,-255.0>-<325.0,-254.5>>

	* Ccedilla (U+00C7) contains a short segment B<<325.0,-254.5>-<317.0,-254.0>-<308.0,-253.0>>

	* Ccedilla (U+00C7) contains a short segment B<<382.5,-113.0>-<369.0,-112.0>-<362.0,-112.0>>

	* Ccedilla (U+00C7) contains a short segment B<<362.0,-112.0>-<352.0,-112.0>-<337.5,-114.0>>

	* ae (U+00E6) contains a short segment B<<883.0,272.0>-<883.0,262.0>-<882.5,252.0>>

	* ae (U+00E6) contains a short segment B<<882.5,252.0>-<882.0,242.0>-<881.0,232.0>>

	* ccedilla (U+00E7) contains a short segment B<<305.0,-59.0>-<311.0,-58.0>-<317.0,-57.5>>

	* ccedilla (U+00E7) contains a short segment B<<317.0,-57.5>-<323.0,-57.0>-<328.0,-57.0>>

	* ccedilla (U+00E7) contains a short segment B<<260.0,-253.0>-<252.0,-253.0>-<243.5,-252.5>>

	* ccedilla (U+00E7) contains a short segment B<<243.5,-252.5>-<235.0,-252.0>-<227.0,-250.0>>

	* abreve (U+0103) contains a short segment L<<454.0,740.0>--<454.0,737.0>>

	* aogonek (U+0105) contains a short segment L<<490.0,0.0>--<480.0,0.0>>

	* eogonek (U+0119) contains a short segment B<<526.0,268.0>-<525.0,259.0>-<525.0,250.0>>

	* eogonek (U+0119) contains a short segment B<<525.0,250.0>-<525.0,241.0>-<524.0,232.0>>

	* Iogonek (U+012E) contains a short segment L<<174.0,0.0>--<167.0,0.0>>

	* iogonek (U+012F) contains a short segment L<<159.0,0.0>--<154.0,0.0>>

	* oe (U+0153) contains a short segment B<<938.0,268.0>-<937.0,259.0>-<937.0,250.0>>

	* oe (U+0153) contains a short segment B<<937.0,250.0>-<937.0,241.0>-<936.0,232.0>>

	* Scedilla (U+015E) contains a short segment B<<334.0,-59.0>-<340.0,-58.0>-<346.0,-57.5>>

	* Scedilla (U+015E) contains a short segment B<<346.0,-57.5>-<352.0,-57.0>-<357.0,-57.0>>

	* Scedilla (U+015E) contains a short segment B<<292.0,-253.0>-<284.0,-253.0>-<274.0,-252.5>>

	* Scedilla (U+015E) contains a short segment B<<274.0,-252.5>-<264.0,-252.0>-<256.0,-250.0>>

	* Scedilla (U+015E) contains a short segment B<<355.5,-119.5>-<344.0,-112.0>-<330.5,-111.0>>

	* Scedilla (U+015E) contains a short segment B<<330.5,-111.0>-<317.0,-110.0>-<310.0,-110.0>>

	* Scedilla (U+015E) contains a short segment B<<310.0,-110.0>-<300.0,-110.0>-<285.5,-112.0>>

	* scedilla (U+015F) contains a short segment B<<276.0,-59.0>-<282.0,-58.0>-<288.0,-57.5>>

	* scedilla (U+015F) contains a short segment B<<288.0,-57.5>-<294.0,-57.0>-<299.0,-57.0>>

	* scedilla (U+015F) contains a short segment B<<231.0,-253.0>-<223.0,-253.0>-<214.5,-252.0>>

	* scedilla (U+015F) contains a short segment B<<214.5,-252.0>-<206.0,-251.0>-<198.0,-250.0>>

	* scedilla (U+015F) contains a short segment B<<272.5,-111.0>-<259.0,-110.0>-<252.0,-110.0>>

	* uni0162 (U+0162) contains a short segment L<<328.0,0.0>--<313.0,0.0>>

	* uni0162 (U+0162) contains a short segment B<<300.0,-59.0>-<305.0,-58.0>-<310.5,-57.5>>

	* uni0162 (U+0162) contains a short segment B<<310.5,-57.5>-<316.0,-57.0>-<321.0,-57.0>>

	* uni0162 (U+0162) contains a short segment B<<255.0,-253.0>-<247.0,-253.0>-<238.5,-252.5>>

	* uni0162 (U+0162) contains a short segment B<<238.5,-252.5>-<230.0,-252.0>-<222.0,-250.0>>

	* uni0162 (U+0162) contains a short segment L<<252.0,0.0>--<241.0,0.0>>

	* uni0163 (U+0163) contains a short segment B<<267.0,0.0>-<264.0,0.0>-<261.0,0.0>>

	* uni0163 (U+0163) contains a short segment B<<261.0,0.0>-<258.0,0.0>-<250.0,1.0>>

	* uni0163 (U+0163) contains a short segment B<<231.0,-59.0>-<237.0,-58.0>-<243.0,-57.5>>

	* uni0163 (U+0163) contains a short segment B<<243.0,-57.5>-<249.0,-57.0>-<254.0,-57.0>>

	* Uogonek (U+0172) contains a short segment B<<312.0,-34.0>-<319.0,-26.0>-<326.0,-19.5>>

	* Uogonek (U+0172) contains a short segment B<<326.0,-19.5>-<333.0,-13.0>-<340.0,-7.0>>

	* Uogonek (U+0172) contains a short segment B<<429.0,-2.0>-<424.0,-5.0>-<419.5,-8.5>>

	* Uogonek (U+0172) contains a short segment B<<419.5,-8.5>-<415.0,-12.0>-<410.0,-16.0>>

	* uogonek (U+0173) contains a short segment B<<348.0,-1.0>-<343.0,-5.0>-<337.5,-8.5>>

	* uogonek (U+0173) contains a short segment B<<337.5,-8.5>-<332.0,-12.0>-<327.0,-16.0>>

	* uni0417 (U+0417) contains a short segment L<<63.0,529.0>--<63.0,537.0>>

	* Euro (U+20AC) contains a short segment B<<145.0,303.0>-<144.0,314.0>-<143.5,324.0>>

	* Euro (U+20AC) contains a short segment B<<143.5,324.0>-<143.0,334.0>-<143.0,344.0>>

	* Euro (U+20AC) contains a short segment B<<143.0,344.0>-<143.0,349.0>-<143.5,363.5>>

	* Euro (U+20AC) contains a short segment B<<225.5,366.0>-<225.0,350.0>-<225.0,347.0>>

	* Euro (U+20AC) contains a short segment B<<225.0,347.0>-<225.0,335.0>-<226.0,324.0>> 

	* Euro (U+20AC) contains a short segment B<<226.0,324.0>-<227.0,313.0>-<229.0,303.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[15] Onest-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '900'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/ttf/Onest-Light.ttf', 'fonts/ttf/Onest-ExtraBold.ttf', 'fonts/ttf/Onest-Medium.ttf', 'fonts/ttf/Onest-Thin.ttf', 'fonts/ttf/Onest-Bold.ttf', 'fonts/ttf/Onest-Regular.ttf', 'fonts/ttf/Onest-Black.ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 982, but got 970 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 334, but got 305 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌ і́

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ j̆ j̇ j̊ j̋ ǰ j̒ j̦̀ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 593 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 501:
less

Width = 577:
equal

Width = 500:
greater

Width = 635:
multiply

Width = 568:
divide

Width = 586:
minus

Width = 640:
approxequal

Width = 579:
notequal

Width = 532:
greaterequal, lessequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam (U+0021): X=212.0,Y=2.0 (should be at baseline 0?)

	* exclam (U+0021): X=114.5,Y=2.0 (should be at baseline 0?)

	* dollar (U+0024): X=258.0,Y=709.0 (should be at cap-height 708?)

	* dollar (U+0024): X=419.0,Y=707.0 (should be at cap-height 708?)

	* three (U+0033): X=401.0,Y=706.5 (should be at cap-height 708?)

	* eight (U+0038): X=223.0,Y=706.5 (should be at cap-height 708?)

	* eight (U+0038): X=405.5,Y=706.5 (should be at cap-height 708?)

	* question (U+003F): X=176.0,Y=706.0 (should be at cap-height 708?)

	* Q (U+0051): X=453.5,Y=-2.0 (should be at baseline 0?)

	* S (U+0053): X=245.5,Y=706.5 (should be at cap-height 708?)

	* asciicircum (U+005E): X=230.0,Y=709.0 (should be at cap-height 708?)

	* asciicircum (U+005E): X=347.0,Y=709.0 (should be at cap-height 708?)

	* d (U+0064): X=358.0,Y=525.5 (should be at x-height 527?)

	* q (U+0071): X=343.5,Y=2.0 (should be at baseline 0?)

	* s (U+0073): X=344.0,Y=1.0 (should be at baseline 0?)

	* s (U+0073): X=184.0,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=389.0,Y=1.0 (should be at baseline 0?)

	* cent (U+00A2): X=227.0,Y=1.0 (should be at baseline 0?)

	* section (U+00A7): X=388.5,Y=2.0 (should be at baseline 0?)

	* section (U+00A7): X=206.0,Y=1.0 (should be at baseline 0?)

	* dieresis (U+00A8): X=256.5,Y=708.5 (should be at cap-height 708?)

	* dieresis (U+00A8): X=511.5,Y=708.5 (should be at cap-height 708?)

	* uni00B3 (U+00B3): X=105.5,Y=708.5 (should be at cap-height 708?)

	* Aring (U+00C5): X=370.0,Y=968.0 (should be at ascender 970?)

	* Aring (U+00C5): X=370.0,Y=968.0 (should be at ascender 970?)

	* germandbls (U+00DF): X=468.5,Y=710.0 (should be at cap-height 708?)

	* atilde (U+00E3): X=364.0,Y=707.0 (should be at cap-height 708?)

	* atilde (U+00E3): X=364.0,Y=707.0 (should be at cap-height 708?)

	* aring (U+00E5): X=425.0,Y=710.0 (should be at cap-height 708?)

	* aring (U+00E5): X=159.0,Y=710.0 (should be at cap-height 708?)

	* ccedilla (U+00E7): X=226.0,Y=-2.0 (should be at baseline 0?)

	* ntilde (U+00F1): X=389.0,Y=707.0 (should be at cap-height 708?)

	* ntilde (U+00F1): X=389.0,Y=707.0 (should be at cap-height 708?)

	* otilde (U+00F5): X=370.0,Y=707.0 (should be at cap-height 708?)

	* otilde (U+00F5): X=370.0,Y=707.0 (should be at cap-height 708?)

	* eogonek (U+0119): X=381.0,Y=2.0 (should be at baseline 0?)

	* eogonek (U+0119): X=366.5,Y=-0.5 (should be at baseline 0?)

	* itilde (U+0129): X=210.0,Y=707.0 (should be at cap-height 708?)

	* itilde (U+0129): X=210.0,Y=707.0 (should be at cap-height 708?)

	* Sacute (U+015A): X=246.5,Y=706.5 (should be at cap-height 708?)

	* sacute (U+015B): X=344.0,Y=1.0 (should be at baseline 0?)

	* sacute (U+015B): X=184.0,Y=1.0 (should be at baseline 0?)

	* Scircumflex (U+015C): X=245.5,Y=706.5 (should be at cap-height 708?)

	* scircumflex (U+015D): X=344.0,Y=1.0 (should be at baseline 0?)

	* scircumflex (U+015D): X=184.0,Y=1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=237.5,Y=706.5 (should be at cap-height 708?)

	* scaron (U+0161): X=344.0,Y=1.0 (should be at baseline 0?)

	* scaron (U+0161): X=184.0,Y=1.0 (should be at baseline 0?)

	* uni0163 (U+0163): X=263.0,Y=1.0 (should be at baseline 0?)

	* utilde (U+0169): X=370.0,Y=707.0 (should be at cap-height 708?)

	* utilde (U+0169): X=370.0,Y=707.0 (should be at cap-height 708?)

	* uni0218 (U+0218): X=236.5,Y=706.5 (should be at cap-height 708?)

	* ring (U+02DA): X=449.0,Y=710.0 (should be at cap-height 708?)

	* ring (U+02DA): X=183.0,Y=710.0 (should be at cap-height 708?)

	* ogonek (U+02DB): X=308.0,Y=1.0 (should be at baseline 0?)

	* tilde (U+02DC): X=367.0,Y=707.0 (should be at cap-height 708?)

	* tilde (U+02DC): X=367.0,Y=707.0 (should be at cap-height 708?)

	* tildecomb (U+0303): X=-206.0,Y=707.0 (should be at cap-height 708?)

	* tildecomb (U+0303): X=-206.0,Y=707.0 (should be at cap-height 708?)

	* uni030A (U+030A): X=-157.0,Y=710.0 (should be at cap-height 708?)

	* uni030A (U+030A): X=-423.0,Y=710.0 (should be at cap-height 708?)

	* uni0312 (U+0312): X=-217.5,Y=707.5 (should be at cap-height 708?)

	* uni0328 (U+0328): X=-82.0,Y=1.0 (should be at baseline 0?)

	* uni0405 (U+0405): X=245.5,Y=706.5 (should be at cap-height 708?)

	* uni0417 (U+0417): X=447.0,Y=706.0 (should be at cap-height 708?)

	* uni0417 (U+0417): X=436.0,Y=-1.0 (should be at baseline 0?)

	* uni041B (U+041B): X=45.0,Y=-1.0 (should be at baseline 0?)

	* uni041B (U+041B): X=7.0,Y=-1.0 (should be at baseline 0?)

	* uni0437 (U+0437): X=365.0,Y=1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=45.0,Y=-1.0 (should be at baseline 0?)

	* uni043B (U+043B): X=7.0,Y=-1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=344.0,Y=1.0 (should be at baseline 0?)

	* uni0455 (U+0455): X=184.0,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=405.0,Y=710.0 (should be at cap-height 708?)

	* uni20B4 (U+20B4): X=223.0,Y=1.0 (should be at baseline 0?)

	* uni20B4 (U+20B4): X=237.0,Y=708.5 (should be at cap-height 708?)

	* uni21BA (U+21BA): X=680.0,Y=-0.5 (should be at baseline 0?)

	* uni21BA (U+21BA): X=234.5,Y=0.5 (should be at baseline 0?)

	* uni21BB (U+21BB): X=272.5,Y=-1.0 (should be at baseline 0?)

	* uniE003 (U+E003): X=431.0,Y=706.5 (should be at cap-height 708?)

	* uniE008 (U+E008): X=246.0,Y=706.5 (should be at cap-height 708?) 

	* uniE008 (U+E008): X=428.5,Y=706.5 (should be at cap-height 708?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<808.5,285.0>-<810.0,305.0>-<810.0,312.0>>

	* s (U+0073) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* asciitilde (U+007E) contains a short segment B<<625.5,460.0>-<626.0,452.0>-<626.0,452.0>>

	* paragraph (U+00B6) contains a short segment L<<217.0,315.0>--<201.0,315.0>>

	* germandbls (U+00DF) contains a short segment B<<457.0,400.0>-<457.0,387.0>-<465.5,378.5>>

	* germandbls (U+00DF) contains a short segment B<<494.0,175.0>-<494.0,184.0>-<489.0,192.5>>

	* Eogonek (U+0118) contains a short segment B<<397.0,-92.0>-<408.0,-92.0>-<417.0,-89.5>>

	* Eogonek (U+0118) contains a short segment B<<417.0,-89.5>-<426.0,-87.0>-<435.0,-83.0>>

	* eogonek (U+0119) contains a short segment B<<381.0,2.0>-<374.0,1.0>-<366.5,-0.5>>

	* eogonek (U+0119) contains a short segment B<<366.5,-0.5>-<359.0,-2.0>-<351.0,-4.0>>

	* sacute (U+015B) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* scircumflex (U+015D) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* Scedilla (U+015E) contains a short segment B<<257.5,-109.0>-<240.0,-112.0>-<232.0,-115.0>>

	* scedilla (U+015F) contains a short segment B<<207.0,368.0>-<207.0,361.0>-<213.0,353.5>>

	* scaron (U+0161) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* Uogonek (U+0172) contains a short segment B<<444.0,-92.0>-<455.0,-92.0>-<464.0,-89.5>>

	* Uogonek (U+0172) contains a short segment B<<464.0,-89.5>-<473.0,-87.0>-<482.0,-83.0>>

	* uni0219 (U+0219) contains a short segment B<<207.0,368.0>-<207.0,361.0>-<213.0,353.5>>

	* uni0443 (U+0443) contains a short segment L<<77.0,-67.0>--<92.0,-67.0>>

	* uni0455 (U+0455) contains a short segment B<<203.0,368.0>-<203.0,361.0>-<209.0,353.5>>

	* uni045E (U+045E) contains a short segment L<<80.0,-67.0>--<95.0,-67.0>>

	* uni20B4 (U+20B4) contains a short segment B<<429.0,347.0>-<419.0,341.0>-<412.0,337.0>>

	* uni20B4 (U+20B4) contains a short segment B<<255.0,229.0>-<246.0,223.0>-<242.0,214.5>>

	* uni20B4 (U+20B4) contains a short segment B<<242.0,214.5>-<238.0,206.0>-<238.0,198.0>>

	* uni20B4 (U+20B4) contains a short segment B<<169.0,337.0>-<176.0,341.0>-<186.5,348.5>>

	* uni20B4 (U+20B4) contains a short segment B<<186.5,348.5>-<197.0,356.0>-<206.5,362.5>>

	* uni20B4 (U+20B4) contains a short segment B<<206.5,362.5>-<216.0,369.0>-<218.0,370.0>> 

	* uni20B4 (U+20B4) contains a short segment B<<384.0,496.5>-<389.0,506.0>-<389.0,514.0>> [code: found-short-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 34 | 73 | 849 | 43 | 599 | 0 |
| 0% | 2% | 5% | 53% | 3% | 37% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
