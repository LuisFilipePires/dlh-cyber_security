#!/usr/bin/env python3
"HTTP headers module."

import requests


def get_http_headers(url):
    "Retrieve HTTP status code and headers."

    try:
        response = requests.get(url)

        return {
            "status_code": response.status_code,
            "headers": dict(response.headers)
        }

    except requests.exceptions.RequestException:
        return None
