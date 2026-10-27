# Guillermo Blanco — brand

Source of truth for the Guillermo Blanco identity (direction **v4 Paper**): logo files, colour and type tokens, the Google Play developer assets and the guidelines.

**PDF:** [`pdf/Guillermo-Blanco-Brand-Guidelines.pdf`](pdf/Guillermo-Blanco-Brand-Guidelines.pdf) — 11 pages, 16:9, shareable.
**Text version:** [`brand-book.md`](brand-book.md)

## Contents

| Path | What |
| --- | --- |
| `assets/logos/` | Mark as SVG (primary, reversed, mono ink, mono paper) and horizontal lockups as PNG |
| `assets/diagrams/` | Construction grid, clear space and minimum sizes |
| `assets/google-play/` | Developer icon 512×512 and header 4096×2304, ready to upload |
| `tokens/` | `tokens.json` (source) and `tokens.css` (generated) |
| `fonts/` | Carlito Regular and Bold (SIL Open Font License) |
| `pdf/` | Shareable guidelines PDF |
| `src/` | Scripts that build the PDF and the assets |

## Quick rules

- Mark: GB monogram on a 96 × 60 unit grid, 8 u stroke. Use the files; never redraw.
- Colour: paper `#F3EFE6`, ink `#10131A`, one accent vermilion `#E5412D` (marks and type ≥ 24px only).
- Type: Carlito. Grid unit 64px (4096 × 2304 = 64 × 36 units). Rings scale by φ.

## Rebuild the PDF

```bash
pip install playwright && playwright install chromium
python src/build_pdf.py    # writes pdf/Guillermo-Blanco-Brand-Guidelines.pdf
```

`src/build_pdf.py` reads the assets and fonts in this repo. `src/build_brand_assets.py` and `src/build_identity_variants.py` generate the logos, diagrams and the Google Play images; they were written for the original working directory, so adjust the paths at the top before running them.

## Keeping it live

Edit `tokens/tokens.json` and `brand-book.md`, regenerate `tokens/tokens.css` and the PDF, then commit. The repo is the source; any other copy (such as a Claude design-system page) should be updated from it.

## Licence

Logos and brand assets © Guillermo Blanco, all rights reserved. Carlito is licensed under the SIL Open Font License 1.1.
