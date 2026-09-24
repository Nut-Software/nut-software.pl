"""Extend the existing walnut SVG family with hand-drawn technology motifs."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / 'assets/brand'
# This traced variant has five shell/kernel paths followed by three database paths.
# Keep only the shared walnut geometry, leaving its centre transparent.
base = (BRAND / 'nut-database.svg').read_text()
paths = re.findall(r'<path\b[^>]+/>', base)
assert len(paths) == 8, 'Review base geometry before regenerating the variants'
walnut = ''.join(paths[:5])
MOTIFS = {
    'fastapi': ('FastAPI', '<path d="M43 4 15 44h23l-5 31 32-44H43z"/>'),
    'terraform': ('Terraform', '<path d="m9 8 24 14v27L9 35zm29 17 24 14v27L38 52zm29-3 12-7v27l-12 7zM38 57l24 14v14L38 71z" transform="translate(0 -5) scale(.92)"/>'),
    'docker': ('Docker', '<g><path d="M5 44h55c2-8 7-13 14-13-1 6-3 11-8 15h11c-5 8-12 10-20 10-8 14-20 20-35 16C11 69 6 59 5 44z"/><path d="M14 31h11v10H14zm14 0h11v10H28zm14 0h11v10H42zM28 18h11v10H28zm14 0h11v10H42zM42 5h11v10H42z"/></g>'),
    'ai-search': ('AI and search', '<g fill="none" stroke="#101b22" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><circle cx="34" cy="32" r="25"/><path d="m53 51 21 22M23 22l23 4-14 19-9-23"/></g><circle cx="23" cy="22" r="6"/><circle cx="46" cy="26" r="6"/><circle cx="32" cy="45" r="6"/>'),
}
for slug, (label, geometry) in MOTIFS.items():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
           'fill="#101b22" role="img" aria-labelledby="title">'
           f'<title id="title">Nut Software — {escape(label)}</title>' + walnut
           + '<g transform="translate(217 219) scale(.94)">' + geometry + '</g></svg>\n')
    (BRAND / f'nut-{slug}.svg').write_text(svg)
    print(f'nut-{slug}.svg')
