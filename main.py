
from fontTools.fontBuilder import FontBuilder

import projectInfo
from db import GLYPHS
from utils import prepareGlyphs

metrics = {}
advanceWidths, charMap, glyphs = prepareGlyphs(GLYPHS)

fb = FontBuilder(1024, isTTF=True)
fb.setupGlyphOrder(list(GLYPHS.keys()))
fb.setupCharacterMap(charMap)
fb.setupGlyf(glyphs)

glyphTable = fb.font["glyf"]
for gn, advanceWidth in advanceWidths.items():
    metrics[gn] = (advanceWidth, glyphTable[gn].xMin)

fb.setupHorizontalMetrics(metrics)
fb.setupHorizontalHeader(ascent=824, descent=-200)
fb.setupNameTable(projectInfo.nameStrings)
fb.setupOS2(sTypoAscender=824, sTypoDescender=-200, usWinAscent=824, usWinDescent=200)
fb.setupPost()

fb.save("OpenDotMatrix.ttf")
