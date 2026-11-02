#!/usr/bin/env python3
"""Validate sitemap URLs against local pages; optionally smoke-test the live site."""
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

BASE = "https://roofmere.com/"
SITEMAP = BASE + "sitemap.xml"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
REQUIRED = {
    BASE,
    BASE + "guides/",
    BASE + "guides/track-net-worth-without-bank-connections/",
}


def check_xml(payload, check_local_files=True):
    root = ET.fromstring(payload)
    assert root.tag == NS + "urlset", f"Unexpected root tag: {root.tag}"
    urls = [node.text for node in root.findall(f"{NS}url/{NS}loc")]
    assert urls, "Sitemap contains no URLs"
    assert len(urls) == len(set(urls)), "Duplicate sitemap URLs"
    assert REQUIRED.issubset(urls), f"Missing required URLs: {REQUIRED - set(urls)}"
    for url in urls:
        parsed = urlsplit(url)
        assert parsed.scheme == "https" and parsed.netloc == "roofmere.com", f"Non-canonical URL: {url}"
        assert not parsed.query and not parsed.fragment, f"Unexpected query/fragment: {url}"
        if check_local_files:
            path = unquote(parsed.path).lstrip("/")
            local = Path(path) / "index.html" if not path or path.endswith("/") else Path(path)
            assert local.is_file(), f"Sitemap URL has no matching local page: {url} -> {local}"
    print(f"PASS: valid sitemap XML with {len(urls)} canonical URLs")
    return urls


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
    urls = check_xml(Path("sitemap.xml").read_bytes())
    if "--live" not in sys.argv:
        return
    body, mime = fetch(SITEMAP)
    assert mime in ("application/xml", "text/xml"), f"Unexpected sitemap Content-Type: {mime}"
    live_urls = check_xml(body, check_local_files=False)
    assert set(live_urls) == set(urls), "Deployed sitemap differs from repository"
    robots, _ = fetch(BASE + "robots.txt")
    assert SITEMAP.encode() in robots, "robots.txt does not point to the sitemap"
    for url in sorted(urls):
        _, mime = fetch(url)
        assert mime == "text/html", f"Expected HTML at {url}, got {mime}"
    print("PASS: live sitemap, robots.txt and all listed pages are reachable")


if __name__ == "__main__":
    main()
