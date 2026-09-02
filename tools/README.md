# Regenerating the banner

The banner ships with its type already converted to outlines, because GitHub
renders SVG as an image document and never fetches a webfont — any
`font-family` in there would silently fall back.

To change the wording:

```bash
python3 -m venv .venv && .venv/bin/pip install fonttools
.venv/bin/python build_banner.py     # writes ../assets/neonhafen.svg
```

Edit `NAME`, `ROLE` and `GEO` at the top of `build_banner.py`. The script prints
the pixel width of each run so you can check nothing collides with the
lighthouse, which starts at x = 1032.

Fonts bundled here are Chakra Petch and IBM Plex Mono, both SIL Open Font
License 1.1.

Kerning is not applied. The display run is all-caps with positive
letter-spacing, where GPOS pairs contribute nothing visible.

## The boot panel

`build_boot.py` writes `../assets/boot.svg`. It exists as an image rather than a
fenced code block because GitHub gives a README no control over code-block
colours, and its markdown pipeline ignores ANSI escapes — a fenced block renders
monochrome in both themes. Inside an SVG the colours are ours, and the panel
brings its own dark ground, so it reads the same on light and dark GitHub.

Edit the `LINES` table at the top; each entry is a list of `(text, colour)`
segments laid out on the monospace grid. `REDACT` draws a bar instead of glyphs.

## The section panels

`build_panels.py` writes `../assets/running.svg` and `../assets/system.svg`.
Same reason as the boot panel: GitHub applies its own markdown styles to a
README and offers no way to override them, so anything meant to look designed
has to arrive as an image.

What deliberately stays markdown: the two prose paragraphs and the contact
links. An image cannot be selected, searched, translated or followed, so the
words that matter and every link live in real text.

The tradeoff to know about: these panels are 1200 units wide, so on a phone
they scale to roughly a third and the type gets small. The prose carries the
message there; the panels are detail for a wider screen. Each one also has a
full `<title>`, which is what a screen reader announces.
