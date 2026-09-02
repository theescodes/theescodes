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

License texts for the bundled faces are in `OFL-ChakraPetch.txt` and
`OFL-IBMPlexMono.txt`.
