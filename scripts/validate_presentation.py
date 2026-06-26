#!/usr/bin/env python3
"""Basic quality checks for standalone HTML presentations."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


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
        self.ids: list[str] = []
        self.links: list[str] = []
        self.buttons: list[str] = []
        self.images_missing_alt = 0
        self.nav_count = 0
        self.h1_count = 0
        self.h2_count = 0
        self.interactive_buttons = 0
        self._button_depth = 0
        self._button_text: list[str] = []
        self.styles = 0
        self.scripts = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key: value or "" for key, value in attrs}
        if tag == "title":
            self._in_title = True
        if tag == "meta" and attrs_dict.get("name") == "viewport":
            self.viewport = True
        if attrs_dict.get("id"):
            self.ids.append(attrs_dict["id"])
        if tag == "section" and attrs_dict.get("id"):
            self.sections.append(attrs_dict["id"])
        if tag == "a" and attrs_dict.get("href", "").startswith("#"):
            self.links.append(attrs_dict["href"][1:])
        if tag == "button":
            self._button_depth += 1
            self._button_text = []
            if any(key in attrs_dict for key in ("aria-expanded", "aria-selected", "aria-pressed", "aria-controls")):
                self.interactive_buttons += 1
        if tag == "img" and "alt" not in attrs_dict:
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

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "button" and self._button_depth:
            self.buttons.append("".join(self._button_text).strip())
            self._button_depth -= 1
            self._button_text = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data.strip()
        if self._button_depth:
            self._button_text.append(data)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_presentation.py path/to/presentation.html")
        return 2

    path = Path(sys.argv[1])
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

    empty_buttons = sum(1 for text in parser.buttons if not text)
    if empty_buttons:
        errors.append(f"{empty_buttons} button(s) have no text.")
    if parser.images_missing_alt:
        errors.append(f"{parser.images_missing_alt} image(s) missing alt text.")

    found_placeholders = [pattern.pattern for pattern in PLACEHOLDER_PATTERNS if pattern.search(html)]
    if found_placeholders:
        errors.append("Unresolved placeholder markers found: " + ", ".join(found_placeholders))

    if re.search(r"font-size\s*:\s*[^;]*(vw|vh)", html):
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
