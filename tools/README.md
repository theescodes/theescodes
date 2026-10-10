# Regenerating the banner

The banner is the share card of [thees.codes](https://www.thees.codes) made
wide, in the site's "Gezeiten" design. It comes in two files, one per colour
scheme, and the README picks one through `<picture>`, which GitHub matches to
the viewer's theme. `gezeiten-dark.svg` is also the plain `<img>` fallback,
because a dark banner keeps its edge on either ground.

The type ships converted to outlines, because GitHub renders SVG as an image
document and never fetches a webfont — any `font-family` in there would
silently fall back.

```bash
python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz
.venv/bin/python build_banner.py     # writes ../assets/gezeiten-{light,dark}.svg
```

Nothing in the banner is designed here. The copy, the colours, the career
years and the mug are copied from the site repo, and the top of
`build_banner.py` names the file each one comes from. When one of them
changes there, change it here and rebuild. Rebuild once a year as well: the
map has one ring per year since 2018, frozen at the year the banner is built.

The script prints the width of each run and where the type ends and the
outermost ring begins, so you can check the two never meet.

The motion is the site's own, from its `app.css`: the rings draw themselves
once, the map breathes, a beacon pulses over today and the sea drifts behind.
Under `prefers-reduced-motion` all of it stops on the last frame, lines drawn
and beacon out.

Text runs are shaped with HarfBuzz, so kerning applies as it does in a
browser. The name is mixed case at -0.052em tracking, where an unkerned "Th"
opens a visible gap.

Fonts bundled here are Schibsted Grotesk and IBM Plex Mono, both SIL Open
Font License 1.1. Schibsted Grotesk is the site's self-hosted Fontsource file
(variable, Latin subset) converted to TTF. Licence texts are in
`OFL-SchibstedGrotesk.txt` and `OFL-IBMPlexMono.txt`.
