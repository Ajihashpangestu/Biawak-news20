#!/usr/bin/env python3
"""Verify numbering, counts, and declared SVG text coordinates."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re


class Edition(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.briefs = []
        self.stats = []
        self.overflow = []
        self.brief_sources = 0
        self.text = None
        self.forbidden = []

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag in {"image", "img", "script", "link"} or "href" in attrs:
            self.forbidden.append(tag)
        if "data-number" in attrs:
            numbers = self.briefs if attrs.get("class") == "dispatch" else self.cards
            numbers.append(int(attrs["data-number"]))
        if "data-stat" in attrs:
            self.stats.append(int(attrs["data-stat"]))
        if tag == "text":
            self.text = [attrs, ""]

    def handle_data(self, value):
        if self.text is not None:
            self.text[1] += value

    def handle_endtag(self, tag):
        if tag != "text" or self.text is None:
            return
        attrs, copy = self.text
        self.text = None
        x = float(attrs.get("x", 0))
        y = float(attrs.get("y", 0))
        length = float(attrs.get("textlength", 0))
        if x < 0 or x + length > 1024 or y < 0 or y > 1016:
            self.overflow.append({"text": copy, "x": x, "y": y, "length": length})
        if attrs.get("class") == "brief" and re.search(r"\([^()]+, 20 Nov\)$", copy):
            self.brief_sources += 1


def main():
    parser = Edition()
    source = Path(__file__).resolve().parents[1].joinpath("cand.html").read_text(encoding="utf-8")
    parser.feed(source)
    parser.close()
    print(json.dumps({
        "cards": len(parser.cards),
        "briefs": len(parser.briefs),
        "brief_number_range": [min(parser.briefs), max(parser.briefs)] if parser.briefs else [],
        "band_stat_count": len(parser.stats),
        "text_overflow": parser.overflow,
        "dated_brief_sources": parser.brief_sources,
        "forbidden_elements": parser.forbidden,
    }))
    if (parser.cards != list(range(1, 14)) or parser.briefs != list(range(14, 58))
            or parser.stats != list(range(1, 9)) or parser.brief_sources != 44
            or parser.overflow or parser.forbidden or re.search(r"url\s*\(", source, re.I)):
        raise SystemExit(1)
    print(json.dumps({"passed": True}))


if __name__ == "__main__":
    main()
