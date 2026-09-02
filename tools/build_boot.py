"""Render the boot sequence as an SVG panel.

GitHub gives a README no control over code-block colours, and its markdown
pipeline ignores ANSI escapes, so a fenced block renders monochrome in both
themes. Inside an SVG every colour is ours, and the panel carries its own dark
ground — so it reads the same whether the viewer is on light or dark GitHub.
"""
from outline import text_to_path

FONT = "IBMPlexMono-Regular.ttf"
SIZE = 22
ADV = SIZE * 0.6          # IBM Plex Mono is monospace at 600/1000 em
X0, Y0, LH = 40, 70, 34

OK, WARN, DIM, LABEL, KEY, TEXT = "#3fb950", "#ff8a4d", "#5b6c80", "#8fa3b8", "#ffb384", "#dce4ee"
REDACT = object()         # drawn as a bar, not glyphs

LINES = [
    [("// BOOT SEQUENCE", DIM)],
    [("[  OK  ]", OK),   ("  mounting  ", LABEL), ("/dev/angular", KEY),      (" ........... ", DIM), ("v21 · shipping since v7", TEXT)],
    [("[  OK  ]", OK),   ("  mounting  ", LABEL), ("/dev/svelte", KEY),       (" ............ ", DIM), ("v5 · SvelteKit", TEXT)],
    [("[  OK  ]", OK),   ("  loading   ", LABEL), ("module-federation", KEY), (" ...... ", DIM), ("1 host, n remotes", TEXT)],
    [("[  OK  ]", OK),   ("  policy    ", LABEL), ("wcag-2.2-aa", KEY),       (" ............ ", DIM), ("enforced", TEXT)],
    [("[  OK  ]", OK),   ("  policy    ", LABEL), ("cookie-banner", KEY),     (" .......... ", DIM), ("never", TEXT)],
    [("[ ---- ]", DIM),  ("  service   ", LABEL), ("x" * 12, REDACT),         (" ........... ", DIM), ("classified", DIM)],
    [("[ WARN ]", WARN), ("  resource  ", LABEL), ("spare-time", KEY),        (" ............. ", DIM), ("low", WARN)],
]

body, widest = [], 0
for i, line in enumerate(LINES):
    y = Y0 + i * LH
    x = X0
    for text, fill in line:
        w = len(text) * ADV
        if fill is REDACT:
            body.append(f'    <rect x="{x:.1f}" y="{y - SIZE * 0.74:.1f}" width="{w:.1f}" height="{SIZE * 0.74:.1f}" rx="1.5" fill="#2c3746"/>')
        else:
            d, _ = text_to_path(FONT, text, SIZE, x, y, 0, precision=1)
            body.append(f'    <path d="{d}" fill="{fill}"/>')
        x += w
    widest = max(widest, x)

# the header rule runs from after the label to the right margin
rule_x = X0 + len(LINES[0][0][0]) * ADV + ADV
cursor_y = Y0 + (len(LINES) - 1) * LH
H = int(cursor_y + 44)
print(f"panel {1200}×{H}, widest line ends at x={widest:.0f}")

SVG = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-labelledby="b">
  <title id="b">Boot sequence: Angular 21, Svelte 5, module federation, WCAG 2.2 AA enforced, no cookie banners, one classified service, spare time low</title>
  <style>
    .cur{{animation:blink 1.06s steps(1) infinite}}
    @keyframes blink{{0%,50%{{opacity:1}}50.01%,100%{{opacity:0}}}}
    @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
  <defs>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1.4" fill="#9fe8ff" opacity=".04"/>
    </pattern>
  </defs>
  <rect width="1200" height="{H}" rx="8" fill="#0b0f16"/>
  <rect x=".6" y=".6" width="1198.8" height="{H - 1.2}" rx="7.4" fill="none" stroke="#1d2836" stroke-width="1.2"/>
  <line x1="{rule_x:.0f}" y1="{Y0 - 7}" x2="1160" y2="{Y0 - 7}" stroke="#1d2836" stroke-width="1.2"/>
{chr(10).join(body)}
  <rect class="cur" x="{X0:.0f}" y="{cursor_y + LH - SIZE * 0.74:.1f}" width="{ADV:.1f}" height="{SIZE * 0.74:.1f}" fill="#f54900"/>
  <rect width="1200" height="{H}" rx="8" fill="url(#scan)"/>
</svg>
'''
open("../assets/boot.svg", "w").write(SVG)
