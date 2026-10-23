#!/usr/bin/env python3
"""Validate local sitemap and optionally the deployed GitHub Pages response."""
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = "https://roofmere.com/"
SITEMAP = BASE + "sitemap.xml"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
EXPECTED = {
    BASE,
    BASE + "guides/",
    BASE + "guides/track-net-worth-without-bank-connections/",
}

def check_xml(payload):
    root = ET.fromstring(payload)
    assert root.tag == NS + "urlset", f"Unexpected root tag: {root.tag}"
    urls = [node.text for node in root.findall(f"{NS}url/{NS}loc")]
    assert len(urls) == len(set(urls)), "Duplicate sitemap URLs"
    assert set(urls) == EXPECTED, f"Unexpected sitemap URLs: {urls}"
    print(f"PASS: valid sitemap XML with {len(urls)} expected URLs")

def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Roofmere-Sitemap-Smoke-Test/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        status = response.status
        mime = response.headers.get_content_type()
        body = response.read()
        assert status == 200, f"{url}: HTTP {status}"
        print(f"HTTP {status} {url} Content-Type={mime}")
        return body, mime

def main():
    check_xml(Path("sitemap.xml").read_bytes())
    if "--live" not in sys.argv:
        return
    body, mime = fetch(SITEMAP)
    assert mime in ("application/xml", "text/xml"), f"Unexpected sitemap Content-Type: {mime}"
    check_xml(body)
    robots, _ = fetch(BASE + "robots.txt")
    assert SITEMAP.encode() in robots, "robots.txt does not point to the sitemap"
    for url in sorted(EXPECTED):
        _, mime = fetch(url)
        assert mime == "text/html", f"Expected HTML at {url}, got {mime}"
    print("PASS: live sitemap, robots.txt and all listed pages are reachable")

if __name__ == "__main__":
    main()
