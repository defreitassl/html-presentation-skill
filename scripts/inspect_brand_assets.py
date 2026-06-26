#!/usr/bin/env python3
"""Inspect a workspace or brand asset folder and suggest usable colors/assets."""

from __future__ import annotations

import json
import re
import sys
import argparse
from collections import Counter
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
VECTOR_EXTENSIONS = {".svg"}
FONT_EXTENSIONS = {".woff", ".woff2", ".ttf", ".otf"}
TEXT_EXTENSIONS = {".svg", ".css", ".json", ".md", ".txt", ".html"}
ASSET_EXTENSIONS = IMAGE_EXTENSIONS | VECTOR_EXTENSIONS | FONT_EXTENSIONS | TEXT_EXTENSIONS
IGNORED_DIRS = {
    ".git",
    ".codex",
    ".claude",
    ".github",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".nuxt",
    "coverage",
    "vendor",
}
BRAND_HINT_RE = re.compile(r"(brand|logo|mark|icon|asset|media|image|photo|screenshot|font|style|theme|identity)", re.IGNORECASE)
HEX_COLOR_RE = re.compile(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b")
RGB_COLOR_RE = re.compile(r"rgba?\(([^)]+)\)", re.IGNORECASE)


def normalize_hex(color: str) -> str:
    color = color.strip()
    if len(color) == 4:
        return "#" + "".join(ch * 2 for ch in color[1:]).lower()
    return color.lower()


def rgb_to_hex(match: str) -> str | None:
    parts = [part.strip() for part in match.split(",")[:3]]
    try:
        values = [max(0, min(255, int(float(part.rstrip("%"))))) for part in parts]
    except ValueError:
        return None
    return "#{:02x}{:02x}{:02x}".format(*values)


def extract_text_colors(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    colors = [normalize_hex(match.group(0)) for match in HEX_COLOR_RE.finditer(text)]
    for match in RGB_COLOR_RE.finditer(text):
        color = rgb_to_hex(match.group(1))
        if color:
            colors.append(color)
    return colors


def extract_raster_colors(path: Path) -> list[str]:
    try:
        from PIL import Image
    except ImportError:
        return []

    try:
        with Image.open(path) as image:
            image = image.convert("RGBA")
            image.thumbnail((160, 160))
            pixels = []
            for red, green, blue, alpha in image.getdata():
                if alpha < 180:
                    continue
                if red > 245 and green > 245 and blue > 245:
                    continue
                if red < 10 and green < 10 and blue < 10:
                    continue
                bucket = (red // 16 * 16, green // 16 * 16, blue // 16 * 16)
                pixels.append(bucket)
    except OSError:
        return []

    return ["#{:02x}{:02x}{:02x}".format(*rgb) for rgb, _count in Counter(pixels).most_common(8)]


def iter_candidate_files(folder: Path, scan_workspace: bool, max_files: int) -> list[Path]:
    files: list[Path] = []
    for path in folder.rglob("*"):
        if len(files) >= max_files:
            break
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if not path.is_file() or path.name in {".gitkeep", ".gitignore"}:
            continue
        if path.suffix.lower() not in ASSET_EXTENSIONS:
            continue
        if scan_workspace and not BRAND_HINT_RE.search(str(path.relative_to(folder))):
            continue
        files.append(path)
    return files


def inspect(folder: Path, scan_workspace: bool = False, max_files: int = 300) -> dict[str, object]:
    files = iter_candidate_files(folder, scan_workspace=scan_workspace, max_files=max_files)
    colors: Counter[str] = Counter()
    assets: dict[str, list[str]] = {
        "logos_or_vectors": [],
        "images": [],
        "fonts": [],
        "text_brand_files": [],
    }

    for path in files:
        rel = str(path.relative_to(folder))
        suffix = path.suffix.lower()
        if suffix in VECTOR_EXTENSIONS:
            assets["logos_or_vectors"].append(rel)
        if suffix in IMAGE_EXTENSIONS:
            assets["images"].append(rel)
        if suffix in FONT_EXTENSIONS:
            assets["fonts"].append(rel)
        if suffix in TEXT_EXTENSIONS:
            assets["text_brand_files"].append(rel)
            colors.update(extract_text_colors(path))
        if suffix in IMAGE_EXTENSIONS:
            colors.update(extract_raster_colors(path))

    return {
        "folder": str(folder),
        "mode": "workspace-scan" if scan_workspace else "asset-folder",
        "candidate_files_scanned": len(files),
        "asset_counts": {key: len(value) for key, value in assets.items()},
        "assets": assets,
        "suggested_palette": [color for color, _count in colors.most_common(10)],
        "notes": [
            "Raster color extraction requires Pillow. If no raster colors appear, inspect images visually or install Pillow.",
            "Treat suggested colors as candidates; verify contrast before using them as backgrounds.",
        ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect brand assets or scan a workspace for likely brand files.")
    parser.add_argument("path", help="Folder to inspect.")
    parser.add_argument(
        "--scan-workspace",
        action="store_true",
        help="Scan likely brand/image/style/font assets across a workspace instead of assuming the folder only contains brand assets.",
    )
    parser.add_argument("--max-files", type=int, default=300, help="Maximum candidate files to inspect.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    folder = Path(args.path)
    if not folder.exists() or not folder.is_dir():
        print(f"ERROR: folder not found: {folder}")
        return 2

    print(json.dumps(inspect(folder, scan_workspace=args.scan_workspace, max_files=args.max_files), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
