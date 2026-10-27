## Brand idea

Build the identity from one unit and one proportion. Every size is a multiple of `grid-unit` (64px) or of the mark's own unit (1 u = 1/60 of mark height); every circle is scaled by `phi`. Nothing is placed by eye, so decoration never competes with the name.

The voice follows the geometry: short, declarative, exact. Write the name as "Guillermo Blanco" in running text and as `GUILLERMO BLANCO` in capitals only in the wordmark and labels. Do not use exclamation marks, emoji or superlatives.

## The mark

The mark is the monogram GB, drawn from circles and rectangles on a 96 × 60 unit grid (`assets/Diagrams/construction.png`).

- Draw G as a ring of outer diameter 60 u and stroke 8 u, open over 45° at the upper right, with a horizontal crossbar 8 u thick from the centre to the right edge.
- Draw B with a stem 8 u wide, three horizontal bars and two half-ring bowls of outer radius 17 u; the bowls overlap so the middle bar is a single 8 u stroke.
- Set the gap between G and B to 7 u. Never redraw, retype or respace the mark: place the files in `assets/Logos/`.
- Colour: ink `ink` for G and B, `vermilion` for the crossbar only. On dark grounds use `gb-mark-reversed.svg`, with `paper` for G and B.
- Use `gb-mark-mono-ink.svg` or `gb-mark-mono-paper.svg` when only one colour is available.

### Lockups

- Use `gb-lockup-horizontal.png` on paper and `gb-lockup-reversed.png` on ink. The divider is 2 grid-units from the mark and the name is 2 grid-units from the divider; the name is two lines, GUILLERMO in Bold ink and BLANCO in Regular `vermilion`.
- Stack the mark alone above the justified wordmark (centred lockup) only where the format is centred, as in a square or a centred header. Justify the wordmark to the exact width of the mark.

### Clear space and size

- Keep x = 15 u clear on all four sides, where x is a quarter of the mark height (`assets/Diagrams/clear-space-and-sizes.png`). Nothing enters it: no text, edge or ring line.
- Never show the mark below 24px high on screen or 8 mm in print. Below 24px use the app icon at its native size.
- Show the lockup no smaller than a 32px-high mark.

### Misuse

- Do not recolour G or B, move the accent to the B, or use `vermilion` for the whole mark.
- Do not outline, shadow, rotate, skew, stretch or add effects.
- Do not place the mark on a busy photograph or on `vermilion`; use an `ink` or `paper` panel behind it.
- Do not set the name in another typeface or in all capitals Bold on both lines.
- Do not round the corners of the icon file; the store applies its own mask.

## Colour

Compose each layout from `paper` and `ink` with `vermilion` as the single accent.

| Role | Token | Share of a layout |
| --- | --- | --- |
| Ground | `surface` (`paper` in light, `ink` in dark) | 70–80% |
| Content | `on-surface` | 15–25% |
| Accent | `vermilion` | at most 10% |

- Set text in `on-surface`; secondary text and captions in `stone`.
- Use `vermilion` for marks, one rule, one arc, or type of 24px and larger. It is 3.6:1 on `paper`, so never use it for body copy there; on `ink` it is 4.6:1.
- Put text on a vermilion fill in `on-vermilion`.
- Use `surface-raised` for panels; draw rules with `hairline` at 2px.
- Use one accent per view: a crossbar, or a ring arc, or a single dot, not all three together.

## Typography

One family: Carlito (Calibri-compatible, open licence), files in `fonts/`.

- Set the name in `display` (Bold, sentence case) and the typographic wordmark in `wordmark-first` over `wordmark-second`.
- Set headings in `heading` and `subheading`, running text in `body`, captions in `caption`, small tracked capitals in `label`.
- Keep line lengths under 70 characters. Align text left; never justify running text.
- Justify only the wordmark, to the mark's width, by tracking (not by stretching letters).
- Do not mix in a second family. Where Carlito is unavailable the stack falls back to Calibri, then Segoe UI, then the system sans.

## Grid and layout

- Lay out on `grid-unit` (64px). A 4096 × 2304 canvas is 64 × 36 units; a 16:9 canvas of any size keeps the same 64 × 36 division.
- Margins are `grid-2` (128px at 4096 wide, 2 units); gaps between related objects are 2 units, between groups 4 units (`tile`).
- Split asymmetric layouts at 1/`phi` (about 62/38), not at half.
- Keep corners square (`radius-none`). Use `radius-round` only for dots and the ring disc.
- Centre the lockup on the horizontal axis and half a unit above the vertical centre; optical centre sits higher than the geometric one.

## Pattern

The pattern is rings and a ruler: precise, measured, and drawn from the same unit as the mark.

- Draw concentric rings centred on one point, with radius n = 320px × `phi`ⁿ, n = 1…4, stroke 2px in `hairline` strength. Let them bleed off the canvas edges.
- Add at most one `vermilion` arc of 35–55° on one ring, and at most one solid `vermilion` dot of 2 grid-units diameter at the ring centre.
- Draw a ruler along the top and bottom margins: a tick every grid-unit (16px long, 2px) and a long tick every 8 units (44px).
- Fade rings out before they reach text; do not let a ring line cross the wordmark or the mark.
- Do not combine rings with photography, gradients, shadows or other patterns.

## Google Play developer page

- Icon: place the mark in the central 80% circle of a 512 × 512 canvas on `paper` (`assets/Google Play/developer-icon-512.png`); PNG or JPEG, 24-bit, no transparency, under 1 MB.
- Header: 4096 × 2304, JPEG or PNG, no transparency, under 1 MB; use `assets/Google Play/developer-header-4096x2304.jpg`.
- Keep header content in the central band (rows 11–25 of 36); the page crops top and bottom on some screens.
- Developer name: "Guillermo Blanco", exactly as in running text.
- Short description: one sentence in the brand voice, without scope words that limit what is built.

## Apps and product icons

- Give each app its own icon on `paper` or `ink` with a single accent; do not reuse the GB monogram as an app icon, so the developer mark stays the developer's.
- Credit the developer with the horizontal lockup in an app's about screen and store listing footer.
