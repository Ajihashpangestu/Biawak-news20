#!/usr/bin/env python3
"""Capture the edition and normalize its square image for delivery."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 fit.py OUTPUT.png")

    browser = next(
        (path for name in ("chromium", "chromium-browser", "google-chrome")
         if (path := shutil.which(name))),
        Path("/root/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome"),
    )

    from PIL import Image, ImageChops

    page = Path(__file__).resolve().with_name("cand.html")
    raw = Path("/tmp/news20_raw.png")
    subprocess.run([
        browser, "--headless", "--disable-gpu", "--hide-scrollbars",
        "--no-sandbox", "--disable-background-networking", "--no-first-run",
        "--window-size=1024,1400", f"--screenshot={raw}", page.as_uri(),
    ], check=True)

    with Image.open(raw) as screenshot:
        frame = screenshot.convert("RGB")
    difference = ImageChops.difference(frame, Image.new("RGB", frame.size, "#f7f5ef"))
    content = difference.point(lambda channel: 255 if channel > 8 else 0).getbbox()
    if content is None:
        raise SystemExit("Screenshot contains no visible edition")
    left, top, right, bottom = content
    width, height = frame.size
    crop = (max(0, left - 8), max(0, top - 8),
            min(width, right + 8), min(height, bottom + 8))
    final = frame.crop(crop).resize((1024, 1024), Image.Resampling.LANCZOS)
    output = Path(sys.argv[1])
    final.save(output, format="PNG")
    data = output.read_bytes()
    print(json.dumps({
        "output": str(output),
        "screenshot_size": frame.size,
        "content_bbox": content,
        "crop_bbox": crop,
        "final_size": final.size,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }))


if __name__ == "__main__":
    main()
