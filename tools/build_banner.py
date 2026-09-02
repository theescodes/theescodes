from outline import text_to_path

NAME = "THEES HENGSTERMANN"
ROLE = "SENIOR SOFTWARE ENGINEER"
GEO  = "53.3985° N, 8.1362° E — VAREL, FRIESLAND, GERMANY"

d_name, w_name = text_to_path("ChakraPetch-Bold.ttf",     NAME, 62,   72, 140, 2)
d_role, w_role = text_to_path("IBMPlexMono-Medium.ttf",   ROLE, 16,   74, 177, 6)
d_geo,  w_geo  = text_to_path("IBMPlexMono-Regular.ttf",  GEO,  13,   74, 204, 2.6)
for label, w, x in (("name", w_name, 72), ("role", w_role, 74), ("geo", w_geo, 74)):
    print(f"{label:5} {w:7.1f}px  ends at x={x + w:.0f}")

SVG = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-labelledby="t">
  <title id="t">Thees Hengstermann — Senior Software Engineer, Varel, Friesland, Germany</title>
  <style>
    /* All type is outlined: GitHub serves SVG as an image document and never
       fetches a webfont, so nothing here may depend on one. */
    .sweep{{transform-origin:1047px 86px;animation:rot 7s linear infinite}}
    @keyframes rot{{to{{transform:rotate(360deg)}}}}
    .grid-run{{animation:run 3.4s linear infinite}}
    @keyframes run{{to{{transform:translateY(34px)}}}}
    .lamp{{animation:lamp 5s steps(1) infinite}}
    @keyframes lamp{{0%,92%,96%,100%{{opacity:1}}94%{{opacity:.3}}98%{{opacity:.65}}}}
    .twinkle{{animation:tw 3.1s ease-in-out infinite alternate}}
    @keyframes tw{{to{{opacity:.15}}}}
    .shimmer{{animation:sh 4.6s ease-in-out infinite alternate}}
    @keyframes sh{{from{{opacity:.2}}to{{opacity:.45}}}}
    /* Chromatic aberration: the ghosts slip out of register now and then,
       rather than the whole wordmark blinking. */
    .ga{{transform:translate(-3px,2px);animation:ga 6.5s steps(1) infinite}}
    @keyframes ga{{0%,87%{{transform:translate(-3px,2px)}}88%{{transform:translate(-10px,3px)}}
      89%,93%{{transform:translate(-3px,2px)}}94%{{transform:translate(-6px,-1px)}}95%,100%{{transform:translate(-3px,2px)}}}}
    .gb{{transform:translate(3px,-2px);animation:gb 6.5s steps(1) infinite}}
    @keyframes gb{{0%,87%{{transform:translate(3px,-2px)}}88%{{transform:translate(11px,-3px)}}
      89%,93%{{transform:translate(3px,-2px)}}94%{{transform:translate(7px,1px)}}95%,100%{{transform:translate(3px,-2px)}}}}
    @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#04060b"/><stop offset=".62" stop-color="#0a0913"/>
      <stop offset=".72" stop-color="#2a1004"/><stop offset=".78" stop-color="#08060c"/>
    </linearGradient>
    <radialGradient id="glow" cx=".5" cy="1" r=".72">
      <stop offset="0" stop-color="#f54900" stop-opacity=".5"/>
      <stop offset=".55" stop-color="#f54900" stop-opacity=".16"/>
      <stop offset="1" stop-color="#f54900" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="halo" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#ffb384" stop-opacity=".5"/><stop offset="1" stop-color="#ffb384" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffe6d2" stop-opacity=".7"/>
      <stop offset=".35" stop-color="#ff8a4d" stop-opacity=".26"/>
      <stop offset="1" stop-color="#f54900" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="refl" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffb384" stop-opacity=".6"/><stop offset="1" stop-color="#f54900" stop-opacity="0"/>
    </linearGradient>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1.4" fill="#9fe8ff" opacity=".05"/>
    </pattern>
    <clipPath id="frame"><rect width="1200" height="320"/></clipPath>
    <clipPath id="tower"><path d="M1032,228 L1039,98 L1055,98 L1062,228 Z"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="1200" height="320" fill="url(#sky)"/>
    <ellipse cx="600" cy="240" rx="880" ry="176" fill="url(#glow)"/>

    <g fill="#cfe9ff">
      <circle cx="140" cy="46" r="1.2" class="twinkle"/>
      <circle cx="318" cy="82" r="1" opacity=".7"/>
      <circle cx="742" cy="38" r="1.3" class="twinkle" style="animation-delay:.8s"/>
      <circle cx="906" cy="70" r="1" opacity=".6"/>
      <circle cx="1120" cy="52" r="1.2" class="twinkle" style="animation-delay:1.6s"/>
      <circle cx="486" cy="30" r="1" opacity=".55"/>
      <circle cx="222" cy="112" r=".9" opacity=".4"/>
      <circle cx="1006" cy="26" r="1" class="twinkle" style="animation-delay:2.3s"/>
    </g>

    <rect x="0" y="226" width="1200" height="1.6" fill="#ff8a4d"/>
    <rect x="0" y="226" width="1200" height="6" fill="#f54900" opacity=".3"/>

    <g stroke="#f54900" stroke-width="1" opacity=".5">
      <g class="grid-run">
        <line x1="0" y1="240" x2="1200" y2="240"/><line x1="0" y1="256" x2="1200" y2="256"/>
        <line x1="0" y1="276" x2="1200" y2="276"/><line x1="0" y1="302" x2="1200" y2="302"/>
        <line x1="0" y1="336" x2="1200" y2="336"/>
      </g>
    </g>
    <g stroke="#f54900" stroke-width="1" opacity=".28">
      <line x1="600" y1="226" x2="-460" y2="340"/><line x1="600" y1="226" x2="-120" y2="340"/>
      <line x1="600" y1="226" x2="160" y2="340"/><line x1="600" y1="226" x2="380" y2="340"/>
      <line x1="600" y1="226" x2="530" y2="340"/><line x1="600" y1="226" x2="670" y2="340"/>
      <line x1="600" y1="226" x2="820" y2="340"/><line x1="600" y1="226" x2="1040" y2="340"/>
      <line x1="600" y1="226" x2="1320" y2="340"/><line x1="600" y1="226" x2="1660" y2="340"/>
    </g>

    <!-- the lamp laid down on the water -->
    <polygon points="1032,228 1062,228 1086,320 1008,320" fill="url(#refl)" class="shimmer"/>

    <!-- sweeping beams, drawn behind the tower -->
    <g class="sweep"><polygon points="1047,86 1460,4 1460,168" fill="url(#beam)"/></g>
    <g class="sweep" style="animation-delay:-3.5s"><polygon points="1047,86 640,14 640,158" fill="url(#beam)" opacity=".45"/></g>

    <!-- lighthouse: tapered tower with two bands, gallery, lamp room, roof -->
    <ellipse cx="1047" cy="86" rx="54" ry="46" fill="url(#halo)" class="lamp"/>
    <path d="M1032,228 L1039,98 L1055,98 L1062,228 Z" fill="#0c0f16" stroke="#f54900" stroke-width="1.3"/>
    <g clip-path="url(#tower)" fill="#f54900" opacity=".85">
      <rect x="1028" y="132" width="40" height="20"/>
      <rect x="1028" y="184" width="40" height="22"/>
    </g>
    <rect x="1028" y="92" width="38" height="6" fill="#0c0f16" stroke="#f54900" stroke-width="1.1"/>
    <rect x="1037" y="70" width="20" height="22" fill="#ffd7bd" class="lamp"/>
    <rect x="1037" y="70" width="20" height="22" fill="none" stroke="#f54900" stroke-width="1.1"/>
    <polygon points="1031,70 1047,52 1063,70" fill="#0c0f16" stroke="#f54900" stroke-width="1.2"/>
    <circle cx="1047" cy="48" r="2.4" fill="#ff8a4d"/>

    <g>
      <path class="ga" d="{d_name}" fill="#5fd0e6" opacity=".55"/>
      <path class="gb" d="{d_name}" fill="#f54900" opacity=".6"/>
      <path d="{d_name}" fill="#fff2e8"/>
    </g>
    <path d="{d_role}" fill="#ff8a4d"/>
    <path d="{d_geo}" fill="#8fa3b8"/>

    <g stroke="#f54900" stroke-width="2" fill="none">
      <path d="M20 20 L20 46 M20 20 L46 20"/><path d="M1180 20 L1180 46 M1180 20 L1154 20"/>
    </g>
    <rect width="1200" height="320" fill="url(#scan)"/>
  </g>
</svg>
'''
open("../assets/neonhafen.svg", "w").write(SVG)
