#!/usr/bin/env python3
"""
Recursive web crawler that discovers internal links.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(start_url, max_depth=2):
    """
    Recursively crawl a website and return visited URLs.

    Args:
        start_url (str): Starting URL.
        max_depth (int): Maximum recursion depth.

    Returns:
        set: Set of successfully visited URLs.
    """
    visited = set()

    try:
        domain = urlparse(start_url).netloc
    except Exception:
        return set()

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except (
            requests.exceptions.RequestException,
            ValueError,
        ):
            return

        print(f"Crawling: {url}")
        visited.add(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(url, link["href"])

            parsed = urlparse(absolute_url)

            # Crawl only HTTP/HTTPS pages from the same domain
            if parsed.scheme not in ("http", "https"):
                continue

            if parsed.netloc != domain:
                continue

            # Remove fragments (#section)
            clean_url = parsed._replace(fragment="").geturl()

            crawl(clean_url, depth + 1)

    crawl(start_url, 0)
    return visited
