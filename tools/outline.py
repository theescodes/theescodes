"""Convert a text run to a single SVG path.

GitHub renders README SVGs as image documents with no network access, so a
webfont never arrives. Outlining is the only way the banner looks the same
everywhere.

The run is shaped by HarfBuzz, so kerning and ligatures apply as they do in a
browser. That matters here: the name is mixed case at -0.052em tracking, where
an unkerned "Th" or "Te" opens a visible gap. A variable font is drawn at the
requested weight, the way the site asks for `font-weight: 820`.
"""
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform


def text_to_path(ttf, text, size, x, y, tracking=0.0, weight=None, precision=2):
    """Path data for `text` set at `size` px with its baseline starting at (x, y).

    `tracking` is CSS letter-spacing in px. Returns the path data and the
    advance width of the run, trailing tracking excluded.
    """
    location = {"wght": weight} if weight is not None else None

    face = hb.Face(hb.Blob.from_file_path(ttf))
    font = hb.Font(face)
    if location:
        font.set_variations(location)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)

    tt = TTFont(ttf)
    scale = size / tt["head"].unitsPerEm
    order = tt.getGlyphOrder()
    glyphs = tt.getGlyphSet(location=location)
    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.{precision}f}".rstrip("0").rstrip("."))

    cursor = x
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        # SVG y grows downward, font y grows upward: flip and sit on the baseline.
        origin = Transform(scale, 0, 0, -scale, cursor + pos.x_offset * scale, y - pos.y_offset * scale)
        glyphs[order[info.codepoint]].draw(TransformPen(pen, origin))
        cursor += pos.x_advance * scale + tracking
    return pen.getCommands(), cursor - tracking - x
