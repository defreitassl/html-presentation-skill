#!/usr/bin/env python3
"""Basic quality checks for standalone HTML presentations."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


LARGE_DATA_IMAGE_CHARS = 20_000
PLACEHOLDER_PATTERNS = (
    re.compile(r"lorem ipsum", re.IGNORECASE),
    re.compile(r"\{\{[^}]+\}\}"),
    re.compile(r"\bTODO\b"),
    re.compile(r"\[TODO\b"),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
)


class PresentationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.viewport = False
        self.sections: list[str] = []
        self.section_details: list[dict[str, object]] = []
        self._section_stack: list[int] = []
        self.ids: list[str] = []
        self.links: list[str] = []
        self.empty_hash_links = 0
        self.buttons: list[str] = []
        self.images_missing_alt = 0
        self.image_sources: list[str] = []
        self.nav_count = 0
        self.h1_count = 0
        self.h2_count = 0
        self.interactive_buttons = 0
        self.aria_controls: list[str] = []
        self._button_depth = 0
        self._button_text: list[str] = []
        self.styles = 0
        self.scripts = 0
        self.accordion_contents: list[str] = []
        self._accordion_capture_depth = 0
        self._accordion_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key: value or "" for key, value in attrs}
        tag = tag.lower()

        if tag == "title":
            self._in_title = True
        if tag == "meta" and attrs_dict.get("name") == "viewport":
            self.viewport = True
        if attrs_dict.get("id"):
            self.ids.append(attrs_dict["id"])
        if attrs_dict.get("aria-controls"):
            self.aria_controls.append(attrs_dict["aria-controls"])

        if tag == "section":
            section_id = attrs_dict.get("id", "")
            if section_id:
                self.sections.append(section_id)
            self.section_details.append({"id": section_id, "has_heading": False})
            self._section_stack.append(len(self.section_details) - 1)

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self._section_stack:
            self.section_details[self._section_stack[-1]]["has_heading"] = True

        if tag == "a" and attrs_dict.get("href", "").startswith("#"):
            href = attrs_dict.get("href", "")
            if href == "#":
                self.empty_hash_links += 1
            else:
                self.links.append(href[1:])

        if tag == "button":
            self._button_depth += 1
            self._button_text = []
            if any(key in attrs_dict for key in ("aria-expanded", "aria-selected", "aria-pressed", "aria-controls")):
                self.interactive_buttons += 1

        if tag == "img":
            self.image_sources.append(attrs_dict.get("src", ""))
            if "alt" not in attrs_dict:
                self.images_missing_alt += 1

        if tag == "nav":
            self.nav_count += 1
        if tag == "h1":
            self.h1_count += 1
        if tag == "h2":
            self.h2_count += 1
        if tag == "style":
            self.styles += 1
        if tag == "script":
            self.scripts += 1

        class_names = attrs_dict.get("class", "").split()
        if "accordion-content" in class_names:
            self._accordion_capture_depth = 1
            self._accordion_text = []
        elif self._accordion_capture_depth:
            self._accordion_capture_depth += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        if tag == "section" and self._section_stack:
            self._section_stack.pop()
        if tag == "button" and self._button_depth:
            self.buttons.append("".join(self._button_text).strip())
            self._button_depth -= 1
            self._button_text = []
        if self._accordion_capture_depth:
            self._accordion_capture_depth -= 1
            if self._accordion_capture_depth == 0:
                self.accordion_contents.append("".join(self._accordion_text).strip())
                self._accordion_text = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data.strip()
        if self._button_depth:
            self._button_text.append(data)
        if self._accordion_capture_depth:
            self._accordion_text.append(data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a standalone HTML presentation.")
    parser.add_argument("path", help="Path to the presentation HTML file.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors for release-ready presentations and CI.",
    )
    parser.add_argument(
        "--allow-template",
        action="store_true",
        help="Allow intentional template placeholders such as {{TITLE}}.",
    )
    return parser.parse_args()


def local_image_path(src: str, html_path: Path) -> Path | None:
    if not src:
        return html_path.parent

    parsed = urlparse(src)
    if parsed.scheme in {"http", "https"} or src.startswith("#"):
        return None
    if parsed.scheme == "data":
        return None
    if parsed.scheme and parsed.scheme != "file":
        return None

    raw_path = unquote(parsed.path)
    if not raw_path:
        return html_path.parent

    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = html_path.parent / candidate
    return candidate


def main() -> int:
    args = parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 2

    html = path.read_text(encoding="utf-8", errors="replace")
    lower_html = html.lower()
    parser = PresentationParser()
    parser.feed(html)

    errors: list[str] = []
    warnings: list[str] = []

    if not parser.title:
        errors.append("Missing <title>.")
    if not parser.viewport:
        errors.append("Missing responsive viewport meta tag.")
    if len(parser.sections) < 3:
        warnings.append("Presentation has fewer than 3 navigable sections.")
    if parser.styles == 0:
        warnings.append("No embedded <style> block found.")
    if parser.h1_count == 0:
        errors.append("Missing <h1>.")
    if parser.h1_count > 1:
        warnings.append("Multiple <h1> elements found; use one primary presentation title.")
    if parser.h2_count < 2:
        warnings.append("Few section headings found; presentation may lack structure.")

    document_ids = set(parser.ids)
    broken = sorted({href for href in parser.links if href not in document_ids})
    if broken:
        errors.append("Broken internal anchors: " + ", ".join(f"#{item}" for item in broken))

    broken_controls = sorted({control for control in parser.aria_controls if control not in document_ids})
    if broken_controls:
        errors.append("Broken aria-controls references: " + ", ".join(f"#{item}" for item in broken_controls))

    if parser.empty_hash_links:
        errors.append(f"{parser.empty_hash_links} link(s) use href=\"#\" without a real target.")

    empty_buttons = sum(1 for text in parser.buttons if not text)
    if empty_buttons:
        errors.append(f"{empty_buttons} button(s) have no text.")
    if parser.images_missing_alt:
        errors.append(f"{parser.images_missing_alt} image(s) missing alt text.")

    empty_accordions = sum(1 for text in parser.accordion_contents if not text)
    if empty_accordions:
        errors.append(f"{empty_accordions} accordion content panel(s) are empty.")

    missing_section_headings = [
        str(detail.get("id") or index + 1)
        for index, detail in enumerate(parser.section_details)
        if not detail.get("has_heading")
    ]
    if missing_section_headings:
        warnings.append("Section(s) without heading: " + ", ".join(missing_section_headings))

    missing_local_images: list[str] = []
    large_data_images = 0
    for src in parser.image_sources:
        if src.startswith("data:image") and len(src) > LARGE_DATA_IMAGE_CHARS:
            large_data_images += 1
            continue
        local_path = local_image_path(src, path)
        if local_path is None:
            continue
        try:
            exists = local_path.exists()
        except OSError:
            exists = False
        if not exists:
            missing_local_images.append(src or "<empty src>")

    if missing_local_images:
        errors.append("Missing local image source(s): " + ", ".join(missing_local_images))
    if large_data_images:
        warnings.append(f"{large_data_images} large base64 image(s) found; prefer relative asset files.")

    found_placeholders = [pattern.pattern for pattern in PLACEHOLDER_PATTERNS if pattern.search(html)]
    if found_placeholders and not args.allow_template:
        errors.append("Unresolved placeholder markers found: " + ", ".join(found_placeholders))

    font_size_values = re.findall(r"font-size\s*:\s*([^;]+);", html, flags=re.IGNORECASE)
    if any(("vw" in value or "vh" in value) and "clamp(" not in value.lower() for value in font_size_values):
        warnings.append("Viewport-based font sizing found; prefer clamp/rem for stable text.")
    if ":root" not in html:
        warnings.append("No :root theme tokens found; define CSS variables for a coherent visual system.")
    if "focus-visible" not in html and "<button" in lower_html:
        warnings.append("Buttons found without obvious focus-visible styles.")
    if "prefers-reduced-motion" not in html and ("animation:" in html or "transition:" in html):
        warnings.append("Motion styles found without prefers-reduced-motion handling.")
    if "overflow-x: auto" not in html and "<table" in lower_html:
        warnings.append("Tables found without obvious horizontal overflow handling.")
    if len(html) > 50_000 and len(parser.links) < 5:
        warnings.append("Long presentation has few internal navigation links.")
    if len(parser.sections) >= 5 and parser.nav_count == 0:
        warnings.append("Long presentation has no <nav> element.")
    if parser.buttons and parser.interactive_buttons == 0:
        warnings.append("Buttons found without ARIA state/control attributes.")

    if args.strict and warnings:
        errors.extend(f"Strict mode: {warning}" for warning in warnings)
        warnings = []

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    if not errors and not warnings:
        print("OK: presentation passed all checks.")
    elif not errors:
        print("OK: no blocking errors found.")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
