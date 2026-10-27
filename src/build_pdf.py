"""Builds pdf/Guillermo-Blanco-Brand-Guidelines.pdf from this repo (Playwright + Chromium)."""
import math, pathlib
from playwright.sync_api import sync_playwright
ROOT=pathlib.Path(__file__).resolve().parent.parent
PHI=(1+5**0.5)/2
ticks="".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{44 if i%8==0 else 16}" stroke="#10131a" stroke-opacity="{.75 if i%8==0 else .35}" stroke-width="2"/>' for i,x in enumerate(range(0,1665,32)))
def ruler(): return f'<svg class="ruler" width="1664" height="48">{ticks}</svg>'
rings="".join(f'<circle cx="0" cy="0" r="{150*PHI**n:.1f}" fill="none" stroke="#10131a" stroke-opacity=".22" stroke-width="2"/>' for n in range(1,5))
MARK='''<svg width="0" height="0" style="position:absolute"><defs><symbol id="gb" viewBox="0 0 96 60">
<path d="M60,30 A30,30 0 1 1 51.213,8.787 L45.556,14.444 A22,22 0 1 0 52,30 Z" fill="var(--m-ink)"/>
<rect x="30" y="30" width="30" height="8" fill="var(--m-acc)"/>
<rect x="67" y="0" width="8" height="60" fill="var(--m-ink)"/><rect x="67" y="0" width="12" height="8" fill="var(--m-ink)"/><rect x="67" y="26" width="12" height="8" fill="var(--m-ink)"/><rect x="67" y="52" width="12" height="8" fill="var(--m-ink)"/>
<path d="M79,0 A17,17 0 0 1 79,34 L79,26 A9,9 0 0 0 79,8 Z" fill="var(--m-ink)"/><path d="M79,26 A17,17 0 0 1 79,60 L79,52 A9,9 0 0 0 79,34 Z" fill="var(--m-ink)"/>
</symbol></defs></svg>'''
def mk(w,style=""): return f'<svg width="{w}" height="{w*60/96:.1f}" viewBox="0 0 96 60" style="{style}"><use href="#gb"/></svg>'
def lock(h,rev=False):
    ink="var(--paper)" if rev else "var(--ink)"; u=h/480
    return f'''<div class="lock" style="--m-ink:{ink};--m-acc:var(--verm);height:{h}px">{mk(h*1.6)}<i style="width:{max(3,5*u*1.0)}px;background:{ink};margin:0 {128*u}px"></i><div style="color:{ink}"><b style="font-size:{h*0.43:.0f}px;line-height:{h*0.375}px;display:block;height:{h*0.375}px">GUILLERMO</b><span style="color:var(--verm);font-size:{h*0.43:.0f}px;line-height:{h*0.375}px;display:block;margin-top:{h*0.25}px">BLANCO</span></div></div>'''
# 64x36 grid diagram (scaled 1/4: 16px per unit => 1024x576)
g="".join(f'<line x1="{i*16}" y1="0" x2="{i*16}" y2="576" stroke="#10131a" stroke-opacity="{.28 if i%8==0 else .1}" stroke-width="1"/>' for i in range(65))+"".join(f'<line x1="0" y1="{j*16}" x2="1024" y2="{j*16}" stroke="#10131a" stroke-opacity="{.28 if j%8==0 else .1}" stroke-width="1"/>' for j in range(37))
grid=f'''<svg width="1024" height="576" viewBox="0 0 1024 576" style="background:var(--paper);outline:2px solid #10131a22"><rect width="1024" height="576" fill="#f3efe6"/>{g}
<rect x="0" y="176" width="1024" height="224" fill="#e5412d" fill-opacity=".10"/><line x1="0" y1="176" x2="1024" y2="176" stroke="#e5412d" stroke-width="2" stroke-dasharray="6 5"/><line x1="0" y1="400" x2="1024" y2="400" stroke="#e5412d" stroke-width="2" stroke-dasharray="6 5"/>
<g style="--m-ink:#10131a;--m-acc:#e5412d"><svg x="384" y="176" width="256" height="160" viewBox="0 0 96 60"><use href="#gb"/></svg></g>
<rect x="384" y="368" width="256" height="16" fill="#10131a" fill-opacity=".85"/>
<text x="16" y="168" font-family="Carlito" font-size="14" fill="#e5412d" font-weight="700">row 11 — safe band — row 25</text></svg>'''
HTML=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"Carlito";src:url("../fonts/Carlito-Regular.ttf");font-weight:400}}
@font-face{{font-family:"Carlito";src:url("../fonts/Carlito-Bold.ttf");font-weight:700}}
@page{{size:1920px 1080px;margin:0}}
:root{{--paper:#f3efe6;--ink:#10131a;--verm:#e5412d;--stone:#5e5a50;--raised:#e9e4d8;--m-ink:#10131a;--m-acc:#e5412d}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Carlito,Calibri,sans-serif;color:var(--ink);background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:1920px;height:1080px;position:relative;overflow:hidden;background:var(--paper);padding:150px 128px 110px;page-break-after:always;break-after:page;display:flex;flex-direction:column;justify-content:center}}
.page>.label{{position:absolute;left:128px;top:96px;margin:0}}.label{{font-size:18px;font-weight:700;letter-spacing:.24em;color:var(--stone);margin-bottom:24px;text-transform:uppercase}}
h1{{font-size:76px;line-height:80px;font-weight:700;letter-spacing:-.01em;margin-bottom:32px}}
h3{{font-size:26px;font-weight:700;margin:0 0 10px}} p,li{{font-size:27px;line-height:38px}} li{{margin:0 0 8px 22px}}
.stone{{color:var(--stone)}} .cols{{display:grid;gap:64px}} .foot{{position:absolute;left:128px;right:128px;bottom:44px;display:flex;justify-content:space-between;font-size:16px;letter-spacing:.2em;color:var(--stone);font-weight:700}}
.ruler{{position:absolute;left:128px;top:40px}}.lock{{display:flex;align-items:center}}.lock i{{display:block;height:100%}}.lock b,.lock span{{font-weight:700;letter-spacing:.02em}}.lock span{{font-weight:400}}
.sw{{height:340px;padding:28px;display:flex;flex-direction:column;justify-content:flex-end;font-size:22px;line-height:30px}}.sw b{{font-size:34px;display:block}}
table{{border-collapse:collapse;font-size:22px}}td,th{{padding:10px 18px;text-align:left;border-bottom:2px solid #10131a22}}th{{font-size:16px;letter-spacing:.2em;color:var(--stone)}}
.tile{{height:250px;display:flex;align-items:center;justify-content:center;position:relative;background:#fff;border:2px solid #10131a1a}}.tile em{{position:absolute;left:16px;bottom:12px;font-style:normal;font-size:20px;color:var(--stone)}}.tile u{{position:absolute;right:14px;top:6px;color:var(--verm);font-size:34px;font-weight:700;text-decoration:none}}
img{{display:block}}
</style></head><body>{MARK}

<section class="page" style="background:var(--paper)">
 <svg style="position:absolute;left:0;top:0" width="1920" height="1080"><defs><linearGradient id="f" gradientUnits="userSpaceOnUse" x1="1440" x2="1530" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient><mask id="m"><rect width="1920" height="1080" fill="url(#f)"/></mask></defs><g mask="url(#m)"><g transform="translate(1560 540)">{rings}<circle r="30" fill="#e5412d"/></g></g></svg>
 {ruler()}<svg class="ruler" style="top:auto;bottom:40px;transform:scaleY(-1)" width="1664" height="48">{ticks}</svg>
 <div style="position:absolute;left:128px;top:330px">{lock(300)}</div>
 <div style="position:absolute;left:128px;bottom:120px"><div class="label" style="margin:0">Brand guidelines · Version 1.0 · October 2026</div></div>
</section>

<section class="page"><div class="label">01 — Brand idea</div><h1>One unit.<br>One proportion.<br>Nothing placed by eye.</h1>
<div class="cols" style="grid-template-columns:1fr 1fr;max-width:1500px"><div><p>Every size is a multiple of the grid unit (64px) or of the mark's own unit (1 u = 1/60 of its height). Every circle scales by φ = 1.618. Decoration never competes with the name because it is built from the same rules.</p></div>
<div><h3>Voice</h3><ul><li>Short, declarative, exact.</li><li>"Guillermo Blanco" in running text; capitals only in the wordmark and labels.</li><li>No exclamation marks, emoji or superlatives.</li></ul></div></div><div class="foot"><span>GUILLERMO BLANCO</span><span>01</span></div></section>

<section class="page"><div class="label">02 — The mark</div><div class="cols" style="grid-template-columns:1.25fr 1fr;align-items:start;gap:56px"><img src="../assets/diagrams/construction.png" width="1000"><div><h1 style="font-size:52px;line-height:56px">Drawn from circles and rectangles.</h1><ul><li>96 × 60 unit grid, one 8 u stroke.</li><li>G: ring Ø 60 u, 45° opening at the upper right, crossbar 8 u thick from centre to edge.</li><li>B: stem 8 u, three bars, two half-ring bowls r = 17 u that overlap into one bar.</li><li>Gap between G and B: 7 u.</li><li>Never redraw, retype or respace. Use the files.</li></ul></div></div><div class="foot"><span>GUILLERMO BLANCO</span><span>02</span></div></section>

<section class="page"><div class="label">03 — Variants and lockups</div>
<div class="cols" style="grid-template-columns:repeat(4,1fr);gap:32px;margin-bottom:40px">
<div style="background:#f3efe6;border:2px solid #10131a22;height:260px;display:flex;align-items:center;justify-content:center">{mk(220)}</div>
<div style="background:#10131a;height:260px;display:flex;align-items:center;justify-content:center;--m-ink:#f3efe6">{mk(220)}</div>
<div style="background:#f3efe6;border:2px solid #10131a22;height:260px;display:flex;align-items:center;justify-content:center;--m-acc:#10131a">{mk(220)}</div>
<div style="background:#10131a;height:260px;display:flex;align-items:center;justify-content:center;--m-ink:#f3efe6;--m-acc:#f3efe6">{mk(220)}</div></div>
<div class="cols" style="grid-template-columns:repeat(4,1fr);gap:32px;margin-bottom:56px"><p class="stone" style="font-size:20px;line-height:26px"><b style="color:#10131a">Primary</b> — ink + vermilion crossbar, on paper.</p><p class="stone" style="font-size:20px;line-height:26px"><b style="color:#10131a">Reversed</b> — paper + vermilion, on ink.</p><p class="stone" style="font-size:20px;line-height:26px"><b style="color:#10131a">Mono ink</b> — one colour print, stamps.</p><p class="stone" style="font-size:20px;line-height:26px"><b style="color:#10131a">Mono paper</b> — one colour on dark.</p></div>
<div class="cols" style="grid-template-columns:1fr 1fr;gap:32px"><div style="background:#f3efe6;border:2px solid #10131a22;height:190px;display:flex;align-items:center;padding-left:48px">{lock(100)}</div><div style="background:#10131a;height:190px;display:flex;align-items:center;padding-left:48px">{lock(100,True)}</div></div>
<div class="foot"><span>GUILLERMO BLANCO</span><span>03</span></div></section>

<section class="page"><div class="label">04 — Clear space, size and misuse</div><div class="cols" style="grid-template-columns:.8fr 1.2fr;gap:56px;align-items:start">
<div><img src="../assets/diagrams/clear-space-and-sizes.png" width="740"><ul style="margin-top:24px"><li>Keep x = 15 u clear on all sides.</li><li>Minimum mark height: 24px on screen, 8 mm in print.</li><li>Lockup: mark at least 32px high.</li></ul></div>
<div class="cols" style="grid-template-columns:repeat(3,1fr);gap:20px">
<div class="tile" style="--m-ink:#e5412d;--m-acc:#10131a"><u>✕</u>{mk(190)}<em>Do not recolour</em></div>
<div class="tile"><u>✕</u><div style="transform:scale(1.35,.75)">{mk(170)}</div><em>Do not stretch</em></div>
<div class="tile"><u>✕</u><div style="transform:rotate(-14deg)">{mk(190)}</div><em>Do not rotate</em></div>
<div class="tile"><u>✕</u><div style="filter:drop-shadow(8px 10px 6px #0008)">{mk(190)}</div><em>No shadows or effects</em></div>
<div class="tile" style="background:#e5412d"><u style="color:#10131a">✕</u>{mk(190)}<em style="color:#10131a">Not on vermilion</em></div>
<div class="tile" style="background:repeating-linear-gradient(45deg,#10131a 0 14px,#e5412d 14px 28px,#ffb02e 28px 42px)"><u style="color:#fff">✕</u>{mk(190)}<em style="color:#fff;background:#10131a;padding:2px 8px">Not on busy grounds</em></div></div></div>
<div class="foot"><span>GUILLERMO BLANCO</span><span>04</span></div></section>

<section class="page"><div class="label">05 — Colour</div><div class="cols" style="grid-template-columns:1.2fr 1.2fr 1fr .9fr;gap:0;margin-bottom:44px">
<div class="sw" style="background:#f3efe6;border:2px solid #10131a22"><b>Paper</b>#F3EFE6<br>RGB 243 239 230<br>Ground</div>
<div class="sw" style="background:#10131a;color:#f3efe6"><b>Ink</b>#10131A<br>RGB 16 19 26<br>Mark, text, dark ground</div>
<div class="sw" style="background:#e5412d;color:#10131a"><b>Vermilion</b>#E5412D<br>RGB 229 65 45<br>The single accent</div>
<div class="sw" style="background:#5e5a50;color:#f3efe6"><b>Stone</b>#5E5A50<br>RGB 94 90 80<br>Secondary text</div></div>
<div class="cols" style="grid-template-columns:1fr 1fr;gap:80px"><div><h3>Proportion</h3><div style="display:flex;height:48px;margin:12px 0 24px"><div style="flex:75;background:#f3efe6;border:2px solid #10131a22"></div><div style="flex:20;background:#10131a"></div><div style="flex:5;background:#e5412d"></div></div><p>Ground 70–80%, content 15–25%, vermilion at most 10%. One accent per view: a crossbar, or an arc, or a dot — not all three.</p></div>
<div><h3>Contrast</h3><table><tr><th>PAIR</th><th>RATIO</th><th>USE</th></tr><tr><td>Ink on paper</td><td>16.2 : 1</td><td>All text</td></tr><tr><td>Stone on paper</td><td>6.0 : 1</td><td>Captions</td></tr><tr><td>Vermilion on ink</td><td>4.6 : 1</td><td>Type ≥ 24px</td></tr><tr><td>Vermilion on paper</td><td>3.6 : 1</td><td>Marks, large type only</td></tr></table></div></div>
<div class="foot"><span>GUILLERMO BLANCO</span><span>05</span></div></section>

<section class="page"><div class="label">06 — Typography</div><div class="cols" style="grid-template-columns:1fr 1fr;gap:96px">
<div><div style="font-size:300px;line-height:260px;font-weight:700;letter-spacing:-.02em">Aa</div><p style="margin-top:34px;font-size:34px;line-height:42px"><b>Carlito</b> — one family, two weights.<br><span class="stone">Calibri-compatible, open licence (SIL OFL). Files in /fonts.</span></p>
<p style="margin-top:28px;font-size:30px;letter-spacing:.02em"><b>GUILLERMO</b> <span style="color:var(--verm)">BLANCO</span></p></div>
<div><table style="width:100%"><tr><th>STYLE</th><th>SPEC</th></tr>
<tr><td style="font-size:44px;font-weight:700">Display</td><td>Bold 80/76 · sentence case</td></tr>
<tr><td style="font-size:34px;font-weight:700">Heading</td><td>Bold 32/38</td></tr>
<tr><td style="font-size:26px;font-weight:700">Subheading</td><td>Bold 20/26</td></tr>
<tr><td style="font-size:22px">Body text</td><td>Regular 16/24</td></tr>
<tr><td style="font-size:18px;color:var(--stone)">Caption</td><td>Regular 13/18 · stone</td></tr>
<tr><td style="font-size:16px;font-weight:700;letter-spacing:.2em">LABEL</td><td>Bold 12/16 · tracking .2em</td></tr></table>
<ul style="margin-top:28px"><li>Lines under 70 characters; align left.</li><li>Justify only the wordmark, by tracking.</li><li>No second family.</li></ul></div></div><div class="foot"><span>GUILLERMO BLANCO</span><span>06</span></div></section>

<section class="page"><div class="label">07 — Grid and layout</div><div class="cols" style="grid-template-columns:1024px 1fr;gap:64px;align-items:start"><div>{grid}</div>
<div><h3>64 × 36 units</h3><ul><li>Unit = 64px. A 4096 × 2304 canvas is 64 × 36 units; any 16:9 canvas keeps the division.</li><li>Margins: 2 units. Gaps: 2 units between related objects, 4 between groups.</li><li>Asymmetric splits at 1/φ, not at half.</li><li>Square corners. Round only dots and the ring disc.</li><li>Lockup sits half a unit above centre.</li></ul></div></div><div class="foot"><span>GUILLERMO BLANCO</span><span>07</span></div></section>

<section class="page"><div class="label">08 — Pattern</div><div class="cols" style="grid-template-columns:1fr 1fr;gap:64px;align-items:center">
<div style="background:#f3efe6;border:2px solid #10131a22;height:640px;position:relative;overflow:hidden"><svg width="880" height="640" viewBox="0 0 880 640"><g transform="translate(560 320)">{"".join(f'<circle r="{110*PHI**n:.1f}" fill="none" stroke="#10131a" stroke-opacity=".3" stroke-width="2"/>' for n in range(1,5))}<path d="M{110*PHI**2*math.cos(math.radians(235)):.1f},{110*PHI**2*math.sin(math.radians(235)):.1f} A{110*PHI**2:.1f},{110*PHI**2:.1f} 0 0 1 {110*PHI**2*math.cos(math.radians(290)):.1f},{110*PHI**2*math.sin(math.radians(290)):.1f}" fill="none" stroke="#e5412d" stroke-width="6"/><circle r="22" fill="#e5412d"/></g></svg></div>
<div><h3>Rings and a ruler</h3><ul><li>Concentric rings, radius n = 320px × φⁿ, n = 1…4, 2px hairline.</li><li>At most one vermilion arc (35–55°) and one vermilion dot of 2 units.</li><li>Ruler on the top and bottom margins: tick every unit, long tick every 8.</li><li>Fade rings out before text; never cross the mark or wordmark.</li><li>No photography, gradients, shadows or other patterns with it.</li></ul></div></div><div class="foot"><span>GUILLERMO BLANCO</span><span>08</span></div></section>

<section class="page"><div class="label">09 — Google Play developer page</div><div class="cols" style="grid-template-columns:420px 1fr;gap:64px;align-items:start">
<div><div style="display:flex;gap:24px;align-items:center"><img src="../assets/google-play/developer-icon-512.png" width="200" style="border-radius:50%"><img src="../assets/google-play/developer-icon-512.png" width="160"></div><p class="stone" style="font-size:20px;line-height:28px;margin-top:20px">Icon 512 × 512 · PNG, 24-bit, no transparency, ≤ 1 MB. The mark lies inside the central 80% circle, so a circular mask never touches it.</p></div>
<div><img src="../assets/google-play/developer-header-4096x2304.jpg" width="1050" style="border:2px solid #10131a22"><p class="stone" style="font-size:20px;line-height:28px;margin-top:20px">Header 4096 × 2304 · JPEG, ≤ 1 MB. Lockup at x = 8, y = 14 units; rings fade before the text; all key content in the central band (rows 11–25).</p></div></div><div class="foot"><span>GUILLERMO BLANCO</span><span>09</span></div></section>

<section class="page" style="background:#10131a;color:#f3efe6"><div class="label" style="color:#a9a599">10 — Files</div><h1 style="color:#f3efe6">Everything is in the repository.</h1>
<div class="cols" style="grid-template-columns:1fr 1fr;max-width:1500px;color:#f3efe6"><ul style="color:#f3efe6"><li><b>assets/logos</b> — 4 mark SVGs, 2 lockup PNGs</li><li><b>assets/diagrams</b> — construction, clear space</li><li><b>assets/google-play</b> — icon 512, header 4096×2304</li></ul><ul style="color:#f3efe6"><li><b>tokens</b> — tokens.json, tokens.css</li><li><b>fonts</b> — Carlito Regular, Bold</li><li><b>brand-book.md</b> — the guidelines as text</li></ul></div>
<div style="position:absolute;left:128px;bottom:96px;--m-ink:#f3efe6;--m-acc:#e5412d">{lock(120,True)}</div></section>
</body></html>'''
out=ROOT/"src"/"brand-book.html"; out.write_text(HTML)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080}); pg.goto(out.as_uri()); pg.wait_for_timeout(600)
    pg.pdf(path=str(ROOT/"pdf"/"Guillermo-Blanco-Brand-Guidelines.pdf"),width="1920px",height="1080px",print_background=True,prefer_css_page_size=True)
    pg.screenshot(path="/home/claude/prev_page.png"); b.close()
