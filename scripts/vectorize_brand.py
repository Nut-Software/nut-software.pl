"""Rebuild monochrome SVG paths: pip install Pillow vtracer==0.6.15."""

from pathlib import Path
from tempfile import TemporaryDirectory
import re
import xml.etree.ElementTree as ET

from PIL import Image, ImageOps, ImageFilter
import vtracer

ROOT = Path(__file__).resolve().parents[1] / "assets" / "brand"
NS = "http://www.w3.org/2000/svg"


def trace(source, target, title, board=False):
    image = Image.open(source).convert("RGBA")
    if board:
        # The upper three quarters of each archived board contain the large mark.
        image = image.crop((0, 0, image.width, int(image.height * .75)))
        mask = image.convert("L").point(lambda value: 255 if value < 100 else 0)
    else:
        mask = image.getchannel("A").point(lambda value: 255 if value > 127 else 0)
    mask = mask.crop(mask.getbbox())
    mask.thumbnail((450, 450), Image.Resampling.LANCZOS)
    canvas = Image.new("L", (512, 512), 0)
    canvas.paste(mask, ((512 - mask.width) // 2, (512 - mask.height) // 2))
    canvas = canvas.filter(ImageFilter.MedianFilter(3))
    with TemporaryDirectory() as temp:
        input_path, output_path = Path(temp) / "mask.png", Path(temp) / "trace.svg"
        ImageOps.invert(canvas).save(input_path)
        vtracer.convert_image_to_svg_py(
            str(input_path), str(output_path), colormode="binary", mode="spline",
            filter_speckle=4, corner_threshold=60, length_threshold=4,
            splice_threshold=45, path_precision=2,
        )
        tree = ET.parse(output_path)
    paths = []
    for path in tree.getroot().findall(f"{{{NS}}}path"):
        geometry = re.sub(r"\s*([A-Za-z])\s*", r"\1", path.attrib["d"].strip())
        paths.append(f'<path d="{geometry}" transform="{path.attrib["transform"]}"/>')
    svg = (f'<svg xmlns="{NS}" viewBox="0 0 512 512" fill="#101b22" '
           f'role="img" aria-labelledby="title"><title id="title">{title}</title>'
           + "".join(paths) + "</svg>\n")
    target.write_text(svg)
    print(target.name, len(svg.encode()), "bytes")


if __name__ == "__main__":
    for name, title in {
        "aws": "AWS", "python": "Python", "django": "Django", "react": "React",
        "database": "Database", "linux": "Linux", "plain": "Walnut kernel",
    }.items():
        trace(ROOT / f"nut-{name}.png", ROOT / f"nut-{name}.svg", f"Nut Software — {title}")
    for source, target, title in [
        ("03-shell-subtle-code.png", "nut-subtle.svg", "Nut Software — subtle code"),
        ("04-shell-neutral-code.png", "nut-logo.svg", "Nut Software"),
        ("04-shell-neutral-code.png", "nut-code.svg", "Nut Software — code"),
    ]:
        trace(ROOT / "concepts" / source, ROOT / target, title, board=True)
    primary = (ROOT / "nut-logo.svg").read_text()
    (ROOT / "nut-logo-lime.svg").write_text(primary.replace('#101b22', '#d6f36b'))
