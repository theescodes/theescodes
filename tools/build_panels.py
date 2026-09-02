"""Render the README's structured sections as SVG panels.

GitHub applies its own markdown styles to a README and offers no way to
override them, so anything meant to look designed has to arrive as an image.
These panels share the boot panel's language — dark ground, monospace grid,
one orange accent — so the page reads as one piece rather than a banner
followed by default markdown.

Prose and links deliberately stay as real markdown: an image cannot be
selected, searched, translated or followed.
"""
from outline import text_to_path

FONT, MONO_MED = "IBMPlexMono-Regular.ttf", "IBMPlexMono-Medium.ttf"
SIZE, ADV, LH = 20, 12.0, 32          # Plex Mono advance is 0.6 em
LABEL_SIZE = 13
X0, W = 40, 1200

DIM, HEAD, KEY, TEXT, ACC = "#5b6c80", "#4c5d70", "#8fa3b8", "#dce4ee", "#ffb384"
GREEN, GHOST = "#3fb950", "#46566a"

SCAN = ('  <defs><pattern id="s{n}" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<rect width="4" height="1.4" fill="#9fe8ff" opacity=".04"/></pattern></defs>')


def seg(text, col, x, y, size=SIZE, font=FONT, precision=1):
    d, _ = text_to_path(font, text, size, x, y, 0, precision=precision)
    return f'    <path d="{d}" fill="{col}"/>'


def chip(label, col, x, y):
    """A bordered status pill, vertically centred on the text baseline."""
    w = len(label) * 9 + 22
    out = [f'    <rect x="{x}" y="{y - 20:.0f}" width="{w}" height="27" rx="4" '
           f'fill="none" stroke="{col}" stroke-opacity=".55" stroke-width="1.2"/>']
    out.append(seg(label, col, x + 11, y - 1, 15, MONO_MED))
    return out, w


def panel(name, blocks):
    """blocks: list of ('label', text) | ('rule',) | ('row', [...]) | ('gap', n)"""
    body, y = [], 62
    for b in blocks:
        kind = b[0]
        if kind == "gap":
            y += b[1]
        elif kind == "label":
            body.append(seg(b[1], DIM, X0, y, LABEL_SIZE, MONO_MED))
            rx = X0 + len(b[1]) * LABEL_SIZE * 0.6 + 14
            body.append(f'    <line x1="{rx:.0f}" y1="{y - 4}" x2="{W - X0}" y2="{y - 4}" '
                        f'stroke="#1d2836" stroke-width="1.2"/>')
            y += 34
        elif kind == "rule":
            body.append(f'    <line x1="{X0}" y1="{y - 12}" x2="{W - X0}" y2="{y - 12}" '
                        f'stroke="#1d2836" stroke-width="1.2"/>')
            y += 8
        elif kind == "row":
            for item in b[1]:
                if item[0] == "dot":
                    _, off, filled = item
                    cx = X0 + off * ADV + 5
                    body.append(f'    <circle cx="{cx:.1f}" cy="{y - 6:.0f}" r="5.5" '
                                + (f'fill="{ACC}"/>' if filled else f'fill="none" stroke="{GHOST}" stroke-width="1.6"/>'))
                elif item[0] == "chip":
                    _, off, label, col = item
                    lines, _w = chip(label, col, X0 + off * ADV, y)
                    body += lines
                else:
                    off, text, col = item
                    size = LABEL_SIZE if col == HEAD else SIZE
                    body.append(seg(text, col, X0 + off * ADV, y, size,
                                    MONO_MED if col == HEAD else FONT))
            y += LH
    H = int(y + 20)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{name}">
  <title id="{name}">{ALT[name]}</title>
{SCAN.format(n=name)}
  <rect width="{W}" height="{H}" rx="8" fill="#0b0f16"/>
  <rect x=".6" y=".6" width="{W - 1.2}" height="{H - 1.2}" rx="7.4" fill="none" stroke="#1d2836" stroke-width="1.2"/>
{chr(10).join(body)}
  <rect width="{W}" height="{H}" rx="8" fill="url(#s{name})"/>
</svg>
'''
    open(f"../assets/{name}.svg", "w").write(svg)
    print(f"{name}.svg  {W}×{H}")


ALT = {
 "running": "Currently running: 01 B2B ticketing at CTS Eventim, Angular, Nx, NgRx — live. "
            "02 thees.codes, SvelteKit and Paraglide — live. 03 and 04 private.",
 "system":  "System configuration. Daytime: Angular, TypeScript, Nx, Module Federation, RxJS, NgRx, Signals. "
            "Evenings: Svelte 5, SvelteKit, Node, Docker, CI/CD. Always: WCAG 2.2 AA, Core Web Vitals, Storybook, "
            "code reviews. Never: cookie banners. Log: 2025 senior software engineer at CTS Eventim; 2024 private; "
            "2022 frontend developer at CTS Eventim; 2020 full-stack at Nordfrost, yard management system and site "
            "relaunch; 2018 IT specialist apprenticeship finished in two years instead of three; 1996 init.",
}

panel("running", [
    ("label", "// CURRENTLY RUNNING"),
    ("row", [(2, "SIGNAL", HEAD), (9, "CHANNEL", HEAD), (46, "STACK", HEAD), (70, "STATUS", HEAD)]),
    ("rule",),
    ("row", [("dot", 2, True),  (4, "01", TEXT), (9, "B2B ticketing @ CTS Eventim", TEXT), (46, "Angular · Nx · NgRx", ACC),   ("chip", 70, "LIVE", GREEN)]),
    ("row", [("dot", 2, True),  (4, "02", TEXT), (9, "thees.codes", TEXT),                 (46, "SvelteKit · Paraglide", ACC), ("chip", 70, "LIVE", GREEN)]),
    ("row", [("dot", 2, False), (4, "03", DIM),  (9, "— private —", DIM),                  (46, "—", DIM),                     ("chip", 70, "PRIVATE", DIM)]),
    ("row", [("dot", 2, False), (4, "04", DIM),  (9, "— private —", DIM),                  (46, "—", DIM),                     ("chip", 70, "PRIVATE", DIM)]),
])

panel("system", [
    ("label", "// SYSTEM CONFIGURATION"),
    ("row", [(2, "daytime", KEY),  (13, "Angular · TypeScript · Nx · Module Federation · RxJS · NgRx · Signals", TEXT)]),
    ("row", [(2, "evenings", KEY), (13, "Svelte 5 · SvelteKit · Node · Docker · CI/CD", TEXT)]),
    ("row", [(2, "always", KEY),   (13, "WCAG 2.2 AA · Core Web Vitals · Storybook · code reviews", TEXT)]),
    ("row", [(2, "never", KEY),    (13, "cookie banners", ACC)]),
    ("gap", 26),
    ("label", "// LOG"),
    ("row", [(2, "2025", KEY), (9, "senior software engineer @ cts eventim", TEXT)]),
    ("row", [(2, "2024", DIM), (9, "— private —", DIM)]),
    ("row", [(2, "2022", KEY), (9, "frontend developer @ cts eventim", TEXT)]),
    ("row", [(2, "2020", KEY), (9, "full-stack @ nordfrost — yard management system, site relaunch", TEXT)]),
    ("row", [(2, "2018", KEY), (9, "IT specialist apprenticeship — finished in two years instead of three", TEXT)]),
    ("row", [(2, "1996", KEY), (9, "init", ACC)]),
])
