#!/usr/bin/env python3
"""Composite a model-generated typography layer onto a text-free poster base.

The typography layer is drawn by the image model on a near-pure-black or
near-pure-white background; local code only crops, scales, positions and
blends. screen blending keeps a black background neutral, multiply keeps a
white background neutral, so the unprinted areas of the layer never shift
the base image.

python composite_text_layer.py --base base.png --layer type.png --out composite.png \
    --config-out composite-config.json --canvas 1920x1080 --box 0.06,0.05,0.88,0.30
"""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageChops

MODES = ("screen", "multiply", "normal")
NEUTRAL = {"screen": (0, 0, 0), "multiply": (255, 255, 255)}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_size(value):
    w, h = str(value).lower().split("x", 1)
    canvas = (int(w), int(h))
    if canvas[0] <= 0 or canvas[1] <= 0:
        raise ValueError("canvas must be positive WxH")
    return canvas


def parse_box(value, canvas):
    parts = [float(x.strip()) for x in str(value).split(",")]
    if len(parts) != 4:
        raise ValueError("box must be x,y,w,h")
    if all(0 <= x <= 1 for x in parts):
        x, y, w, h = parts
        box = [int(x * canvas[0]), int(y * canvas[1]), int(w * canvas[0]), int(h * canvas[1])]
    else:
        box = [int(x) for x in parts]
    if box[2] <= 0 or box[3] <= 0:
        raise ValueError("box width and height must be positive")
    if box[0] < 0 or box[1] < 0 or box[0] + box[2] > canvas[0] or box[1] + box[3] > canvas[1]:
        raise ValueError("box must stay inside the canvas")
    return box


def cover(im, size):
    w, h = size
    iw, ih = im.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return im.crop((left, top, left + w, top + h))


def fit(im, box):
    bw, bh = box[2], box[3]
    iw, ih = im.size
    scale = min(bw / iw, bh / ih)
    nw, nh = max(1, int(iw * scale + 0.5)), max(1, int(ih * scale + 0.5))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def detect_mode(layer):
    """Infer the blend mode from the layer's background luminance."""
    im = layer.convert("L")
    w, h = im.size
    corners = [im.getpixel((x, y)) for x, y in ((1, 1), (w - 2, 1), (1, h - 2), (w - 2, h - 2))]
    mean = sum(corners) / len(corners)
    if mean <= 48:
        return "screen"
    if mean >= 208:
        return "multiply"
    raise ValueError(
        "typography layer background must be near-pure black (screen) or near-pure white "
        f"(multiply); corner luminance {mean:.0f} is neither. Regenerate the layer, do not key it out locally."
    )


def blend(base, plane, mode, opacity):
    if not 0 < opacity <= 1:
        raise ValueError("opacity must be within (0, 1]")
    if mode == "normal":
        return Image.alpha_composite(base.convert("RGBA"), plane.convert("RGBA")).convert("RGB")
    effect = ImageChops.screen(base, plane) if mode == "screen" else ImageChops.multiply(base, plane)
    if opacity < 1:
        return Image.blend(base, effect, opacity)
    return effect


def composite(base_path, layer_path, out_path, config_path, canvas_size, box_value, mode, opacity):
    canvas = canvas_size
    base = cover(Image.open(base_path).convert("RGB"), canvas)
    layer = Image.open(layer_path).convert("RGB")
    if mode == "auto":
        mode = detect_mode(layer)
    if mode not in MODES:
        raise ValueError("mode must be one of " + ", ".join(("auto",) + MODES))
    box = parse_box(box_value, canvas)
    fitted = fit(layer, box)
    plane = Image.new("RGB", canvas, NEUTRAL.get(mode, (0, 0, 0)))
    plane.paste(fitted, (box[0] + (box[2] - fitted.width) // 2, box[1] + (box[3] - fitted.height) // 2))
    if mode == "normal":
        rgba = plane.convert("RGBA")
        rgba.putalpha(255)
        result = Image.alpha_composite(base.convert("RGBA"), rgba).convert("RGB")
    else:
        result = blend(base, plane, mode, opacity)
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    for guard in (base_path, layer_path):
        if out.resolve() == Path(guard).resolve():
            raise ValueError("output must not overwrite the base or the typography layer")
    result.save(out, quality=95)
    config = {
        "canvas": f"{canvas[0]}x{canvas[1]}",
        "base": {"path": str(Path(base_path).resolve()), "sha256": sha256(base_path)},
        "typography_layer": {
            "path": str(Path(layer_path).resolve()),
            "sha256": sha256(layer_path),
            "mode": mode,
            "box": box,
            "opacity": opacity,
        },
        "output": {"path": str(out.resolve()), "sha256": sha256(out)},
        "note": "Re-run with the same config to reproduce byte-identical output; swap the layer to revise text without regenerating the base.",
    }
    Path(config_path).write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    return config


def main():
    p = argparse.ArgumentParser(description="Blend a model-generated typography layer onto a text-free base.")
    p.add_argument("--base", required=True, help="text-free background image")
    p.add_argument("--layer", required=True, help="typography layer on pure black or pure white background")
    p.add_argument("--out", required=True, help="composite output path")
    p.add_argument("--config-out", required=True, help="JSON config recording the full composition")
    p.add_argument("--canvas", default=None, help="WxH; defaults to the base image size")
    p.add_argument("--box", default="0,0,1,1", help="layer box x,y,w,h in pixels or 0-1 ratios")
    p.add_argument("--mode", default="auto", help="auto, screen, multiply or normal")
    p.add_argument("--opacity", type=float, default=1.0)
    args = p.parse_args()
    base_image = Image.open(args.base)
    canvas = parse_size(args.canvas) if args.canvas else base_image.size
    config = composite(args.base, args.layer, args.out, args.config_out, canvas,
                       args.box, args.mode, max(0.0, min(1.0, args.opacity)))
    print(json.dumps(config, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
