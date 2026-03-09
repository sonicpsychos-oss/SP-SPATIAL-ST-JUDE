#!/usr/bin/env python3
"""Build visual prototype mockups for Project St. Jude / SP Spatial.

Outputs SVG frames in ./dist:
- frame1_donor_reveal.svg
- frame2_trauma_informed_pivot.svg
- frame3_feasibility_triptych.svg
"""
from pathlib import Path

DIST = Path(__file__).resolve().parents[1] / "dist"
DIST.mkdir(exist_ok=True)


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def frame1() -> str:
    return """
<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f7dfb5"/>
      <stop offset="60%" stop-color="#f2d29d"/>
      <stop offset="100%" stop-color="#e5c58b"/>
    </linearGradient>
    <linearGradient id="ground" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ddd3c1"/>
      <stop offset="100%" stop-color="#c5b8a2"/>
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#a9c0c8"/>
      <stop offset="100%" stop-color="#7c969f"/>
    </linearGradient>
    <linearGradient id="interiorGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f8c980"/>
      <stop offset="100%" stop-color="#e5a55c"/>
    </linearGradient>
    <filter id="softShadow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
    <filter id="tiltShift" x="0" y="0" width="100%" height="100%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="0 0" result="sharp"/>
    </filter>
  </defs>

  <rect width="1920" height="1080" fill="url(#sky)"/>
  <rect y="420" width="1920" height="660" fill="url(#ground)"/>

  <!-- Low-poly Memphis context -->
  <g opacity="0.6">
    <rect x="120" y="490" width="120" height="120" fill="#b9b9b9"/>
    <rect x="255" y="515" width="150" height="95" fill="#a8a8a8"/>
    <rect x="430" y="495" width="110" height="120" fill="#b0b0b0"/>
    <rect x="1420" y="520" width="170" height="120" fill="#adadad"/>
    <rect x="1610" y="500" width="130" height="145" fill="#b7b7b7"/>
  </g>

  <!-- Family Commons -->
  <g>
    <ellipse cx="520" cy="760" rx="210" ry="90" fill="#8a9e73" opacity="0.65"/>
    <circle cx="430" cy="730" r="35" fill="#6b8753"/>
    <circle cx="505" cy="700" r="28" fill="#5e7a48"/>
    <circle cx="570" cy="740" r="30" fill="#688450"/>
    <circle cx="620" cy="710" r="24" fill="#5e7645"/>
  </g>

  <!-- Long warm shadows -->
  <polygon points="770,360 990,360 1400,900 1180,900" fill="#9f8a68" opacity="0.25" filter="url(#softShadow)"/>

  <!-- Hero building with subtle chamfer look -->
  <g>
    <polygon points="760,250 1030,250 1030,760 760,760" fill="#c5b39b"/>
    <polygon points="1030,250 1140,310 1140,820 1030,760" fill="#b49e83"/>
    <polygon points="760,250 870,310 1140,310 1030,250" fill="#d7c7b3"/>

    <!-- Repeated wall modules + window modules -->
    <g>
      <rect x="790" y="300" width="210" height="420" fill="#b9a487"/>
      <g fill="url(#glass)">
        <rect x="805" y="320" width="40" height="55" rx="2"/>
        <rect x="855" y="320" width="40" height="55" rx="2"/>
        <rect x="905" y="320" width="40" height="55" rx="2"/>
        <rect x="955" y="320" width="30" height="55" rx="2"/>

        <rect x="805" y="390" width="40" height="55" rx="2"/>
        <rect x="855" y="390" width="40" height="55" rx="2"/>
        <rect x="905" y="390" width="40" height="55" rx="2"/>
        <rect x="955" y="390" width="30" height="55" rx="2"/>

        <rect x="805" y="460" width="40" height="55" rx="2"/>
        <rect x="855" y="460" width="40" height="55" rx="2"/>
        <rect x="905" y="460" width="40" height="55" rx="2"/>
        <rect x="955" y="460" width="30" height="55" rx="2"/>

        <rect x="805" y="530" width="40" height="55" rx="2"/>
        <rect x="855" y="530" width="40" height="55" rx="2"/>
        <rect x="905" y="530" width="40" height="55" rx="2"/>
        <rect x="955" y="530" width="30" height="55" rx="2"/>

        <rect x="805" y="600" width="40" height="55" rx="2"/>
        <rect x="855" y="600" width="40" height="55" rx="2"/>
        <rect x="905" y="600" width="40" height="55" rx="2"/>
        <rect x="955" y="600" width="30" height="55" rx="2"/>
      </g>

      <!-- Interior mapping suggestion (warm cubemap illusion) -->
      <g fill="url(#interiorGlow)" opacity="0.45">
        <rect x="805" y="322" width="40" height="20"/>
        <rect x="905" y="392" width="40" height="20"/>
        <rect x="855" y="462" width="40" height="20"/>
        <rect x="955" y="532" width="30" height="20"/>
        <rect x="805" y="602" width="40" height="20"/>
      </g>
    </g>
  </g>

  <!-- Sky-bridge segment -->
  <g>
    <rect x="1140" y="500" width="260" height="42" rx="8" fill="#cdbda8"/>
    <rect x="1148" y="508" width="244" height="24" fill="#90a8af" opacity="0.9"/>
  </g>

  <!-- St. Jude logo mark (red only for logo) -->
  <circle cx="780" cy="736" r="10" fill="#c8102e"/>

  <text x="80" y="96" font-family="Arial, sans-serif" font-size="44" fill="#3e3528" font-weight="700">Frame 1 · Donor Reveal</text>
  <text x="80" y="142" font-family="Arial, sans-serif" font-size="28" fill="#5d513e">Soft Realism · Tilt-Shift Macro · Warm Interior Mapping</text>
</svg>
"""


def frame2() -> str:
    return """
<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">
  <defs>
    <linearGradient id="leftBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0d2a1"/>
      <stop offset="100%" stop-color="#d2b388"/>
    </linearGradient>
    <linearGradient id="rightBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f8f4eb"/>
      <stop offset="100%" stop-color="#ece6d9"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="540" height="1920" fill="url(#leftBg)"/>
  <rect x="540" width="540" height="1920" fill="url(#rightBg)"/>
  <line x1="540" y1="0" x2="540" y2="1920" stroke="#bfb39f" stroke-width="6"/>

  <!-- Left: exploration mode (cropped from donor style) -->
  <g>
    <rect x="90" y="250" width="300" height="860" fill="#bea98d"/>
    <rect x="390" y="300" width="70" height="760" fill="#ae987a"/>
    <rect x="112" y="280" width="255" height="780" fill="#8ca3ab" opacity="0.85"/>
    <ellipse cx="250" cy="1220" rx="200" ry="70" fill="#779061" opacity="0.7"/>
    <text x="70" y="1600" font-family="Arial, sans-serif" font-size="40" fill="#4b3f2f" font-weight="700">Exploration Mode</text>
  </g>

  <!-- Right: focus mode (flattened paper model) -->
  <g>
    <rect x="640" y="320" width="250" height="760" fill="#f1eadb" stroke="#d9cfbb" stroke-width="3"/>
    <rect x="890" y="360" width="60" height="760" fill="#e8decb" stroke="#d9cfbb" stroke-width="3"/>
    <rect x="670" y="350" width="185" height="700" fill="#f7f2e8"/>

    <!-- Yellow path Pantone 108C approximation -->
    <path d="M 730 1680 C 740 1540, 750 1450, 780 1330 C 810 1200, 820 1120, 825 1035" 
          fill="none" stroke="#F4D000" stroke-width="22" stroke-linecap="round" filter="url(#glow)"/>
    <circle cx="730" cy="1680" r="20" fill="#F4D000"/>
    <circle cx="825" cy="1035" r="20" fill="#F4D000"/>

    <text x="610" y="1600" font-family="Arial, sans-serif" font-size="40" fill="#6a604f" font-weight="700">Focus Mode</text>
    <text x="610" y="1660" font-family="Arial, sans-serif" font-size="26" fill="#847a67">Reduced detail · high-contrast wayfinding</text>
    <text x="642" y="1728" font-family="Arial, sans-serif" font-size="24" fill="#736851">Parking</text>
    <text x="842" y="1000" font-family="Arial, sans-serif" font-size="24" fill="#736851">Main Entry</text>
  </g>

  <text x="58" y="86" font-family="Arial, sans-serif" font-size="44" fill="#3e3528" font-weight="700">Frame 2 · Trauma-Informed Pivot</text>
</svg>
"""


def frame3() -> str:
    return """
<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0dcc0"/>
      <stop offset="100%" stop-color="#dcc4a3"/>
    </linearGradient>
  </defs>
  <rect width="1920" height="1080" fill="url(#bg)"/>

  <!-- Triptych panels -->
  <rect x="70" y="150" width="560" height="820" rx="20" fill="#efe3d0"/>
  <rect x="680" y="150" width="560" height="820" rx="20" fill="#f3ecde"/>
  <rect x="1290" y="150" width="560" height="820" rx="20" fill="#ece5d8"/>

  <!-- Beauty pass -->
  <g>
    <rect x="250" y="320" width="190" height="460" fill="#bfa78b"/>
    <rect x="440" y="350" width="60" height="460" fill="#ac9476"/>
    <rect x="270" y="340" width="145" height="400" fill="#85a0a9"/>
    <ellipse cx="285" cy="820" rx="160" ry="55" fill="#7f9568" opacity="0.7"/>
  </g>

  <!-- Topology pass (clean quad wireframe) -->
  <g stroke="#5f5f5f" stroke-width="2" fill="none">
    <rect x="860" y="320" width="190" height="460"/>
    <rect x="1050" y="350" width="60" height="460"/>
    <line x1="860" y1="380" x2="1050" y2="380"/>
    <line x1="860" y1="440" x2="1050" y2="440"/>
    <line x1="860" y1="500" x2="1050" y2="500"/>
    <line x1="860" y1="560" x2="1050" y2="560"/>
    <line x1="860" y1="620" x2="1050" y2="620"/>
    <line x1="860" y1="680" x2="1050" y2="680"/>
    <line x1="920" y1="320" x2="920" y2="780"/>
    <line x1="980" y1="320" x2="980" y2="780"/>
    <line x1="1040" y1="320" x2="1040" y2="780"/>
  </g>

  <!-- Fabrication pass -->
  <g>
    <rect x="1470" y="320" width="190" height="460" fill="#d4d0ca"/>
    <rect x="1660" y="350" width="60" height="460" fill="#c8c4be"/>
    <ellipse cx="1570" cy="840" rx="180" ry="40" fill="#c0bbb3"/>

    <!-- Nozzle overlay -->
    <polygon points="1680,230 1725,300 1635,300" fill="#8c8a86"/>
    <line x1="1680" y1="300" x2="1600" y2="420" stroke="#8c8a86" stroke-width="8"/>
    <circle cx="1600" cy="420" r="8" fill="#8c8a86"/>
  </g>

  <text x="70" y="96" font-family="Arial, sans-serif" font-size="44" fill="#3e3528" font-weight="700">Frame 3 · Feasibility Mic-Drop (Technical Triptych)</text>
  <text x="230" y="920" font-family="Arial, sans-serif" font-size="28" fill="#5d513e" font-weight="700">Beauty Pass</text>
  <text x="820" y="920" font-family="Arial, sans-serif" font-size="28" fill="#5d513e" font-weight="700">Topology Pass</text>
  <text x="1440" y="920" font-family="Arial, sans-serif" font-size="28" fill="#5d513e" font-weight="700">Fabrication Pass</text>
</svg>
"""


def main() -> None:
    write(DIST / "frame1_donor_reveal.svg", frame1())
    write(DIST / "frame2_trauma_informed_pivot.svg", frame2())
    write(DIST / "frame3_feasibility_triptych.svg", frame3())
    print("Built 3 mockup frames in dist/")


if __name__ == "__main__":
    main()
