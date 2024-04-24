from fontTools.svgLib.path import SVGPath
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
import svgwrite

def prepareGlyphs(rawGlyphs, dotSize = 100):
    advanceWidths = {}
    charMap = {}
    glyphs = {}

    halfSize = dotSize / 2

    for character, data in rawGlyphs.items():
        dwg = svgwrite.Drawing()
        shapes = dwg.add(dwg.g(id='shapes', fill='#000000'))

        if data['code'] is not None:
            charMap[data['code']] = character

        lsb, heightOffset = (data['baseline-offset'] if 'baseline-offset' in data else (0, 0))
        height = len(data['data']) * dotSize - heightOffset * dotSize
        width = len(data['data'][0]) * dotSize - lsb * dotSize
        advanceWidths[character] = width

        for y, lineData in enumerate(data['data']):
            for x, dot in enumerate(lineData):
                if dot != ' ':
                    shapes.add(dwg.circle(center=(x * dotSize + halfSize - lsb * dotSize, height - (y * dotSize + halfSize)), r = halfSize))
        
        glyphPen = TTGlyphPen(None)
        cu2quPen = Cu2QuPen(glyphPen, 1.0, True)
        SVGPath.fromstring(dwg.tostring()).draw(cu2quPen)
        glyphs[character] = glyphPen.glyph()

    return (advanceWidths, charMap, glyphs)
