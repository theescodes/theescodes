"""Convert a text run to a single SVG path.

GitHub renders README SVGs as image documents with no network access, so a
webfont never arrives. Outlining is the only way the banner looks the same
everywhere. Kerning is not applied: the display run is all-caps with positive
letter-spacing, where GPOS pairs contribute nothing visible.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform


def text_to_path(ttf, text, size, x, y, letter_spacing=0.0):
    font = TTFont(ttf)
    upem = font["head"].unitsPerEm
    scale = size / upem
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    cursor = x
    for ch in text:
        name = cmap.get(ord(ch))
        if name is None:
            cursor += size * 0.5 + letter_spacing
            continue
        # SVG y grows downward, font y grows upward: flip and sit on the baseline.
        tp = TransformPen(pen, Transform(scale, 0, 0, -scale, cursor, y))
        gs[name].draw(tp)
        cursor += hmtx[name][0] * scale + letter_spacing
    return pen.getCommands(), cursor - letter_spacing - x


if __name__ == "__main__":
    import json, sys
    ttf, text, size, x, y, ls = sys.argv[1:7]
    d, w = text_to_path(ttf, text, float(size), float(x), float(y), float(ls))
    print(json.dumps({"d": d, "width": round(w, 2)}))
