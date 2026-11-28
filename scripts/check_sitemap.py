#!/usr/bin/env python3
"""Validate sitemap URLs against local pages; optionally smoke-test the live site.

Every public HTML page must be listed in the sitemap, carry a self-referencing
canonical and have no noindex. With --live the deployed responses are checked
too (status, Content-Type, X-Robots-Tag, robots meta and canonical).
"""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

BASE = "https://roofmere.com/"
SITEMAP = BASE + "sitemap.xml"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
# Files that are served but are not pages for Google to index.
NOT_PAGES = {"googlee08d1711f6de4095.html"}
CANONICAL_RE = re.compile(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', re.I)
NOINDEX_RE = re.compile(r'<meta[^>]*name=["\'](?:robots|googlebot)["\'][^>]*noindex', re.I)
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


def page_url(path):
    """Public URL for a local HTML file (index.html is served as its directory)."""
    rel = path.as_posix()
    if rel == "index.html":
        return BASE
    if rel.endswith("/index.html"):
        return BASE + rel[: -len("index.html")]
    return BASE + rel


def check_html(url, html, where):
    canonicals = CANONICAL_RE.findall(html)
    assert canonicals == [url], f"{where}: canonical {canonicals} should be exactly [{url}]"
    assert not NOINDEX_RE.search(html), f"{where}: has a noindex robots meta tag"


def check_pages(urls):
    pages = {}
    for path in sorted(Path(".").rglob("*.html")):
        if path.parts[0].startswith(".") or path.parts[0] == "docs" or path.name in NOT_PAGES:
            continue
        pages[page_url(path)] = path
    missing = set(pages) - set(urls)
    assert not missing, f"Public pages missing from sitemap: {sorted(missing)}"
    for url, path in pages.items():
        check_html(url, path.read_text(encoding="utf-8"), str(path))
    print(f"PASS: {len(pages)} pages listed, self-canonical and indexable")


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Roofmere-Sitemap-Smoke-Test/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        status = response.status
        mime = response.headers.get_content_type()
        body = response.read()
        assert status == 200, f"{url}: HTTP {status}"
        robots_header = response.headers.get("X-Robots-Tag", "")
        assert "noindex" not in robots_header.lower(), f"{url}: X-Robots-Tag {robots_header}"
        print(f"HTTP {status} {url} Content-Type={mime}")
        return body, mime


def main():
    urls = check_xml(Path("sitemap.xml").read_bytes())
    check_pages(urls)
    if "--live" not in sys.argv:
        return
    body, mime = fetch(SITEMAP)
    assert mime in ("application/xml", "text/xml"), f"Unexpected sitemap Content-Type: {mime}"
    live_urls = check_xml(body, check_local_files=False)
    assert set(live_urls) == set(urls), "Deployed sitemap differs from repository"
    robots, _ = fetch(BASE + "robots.txt")
    assert SITEMAP.encode() in robots, "robots.txt does not point to the sitemap"
    for url in sorted(urls):
        body, mime = fetch(url)
        assert mime == "text/html", f"Expected HTML at {url}, got {mime}"
        check_html(url, body.decode("utf-8"), url)
    print("PASS: live sitemap, robots.txt and all listed pages are reachable")


if __name__ == "__main__":
    main()
