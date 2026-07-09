#!/usr/bin/env python3
"Download a web page and format its HTML."

import requests
from bs4 import BeautifulSoup


def download_page(url):
    "Download a web page and return formatted HTML."

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.prettify()

    except requests.exceptions.RequestException as e:
        return str(e)
