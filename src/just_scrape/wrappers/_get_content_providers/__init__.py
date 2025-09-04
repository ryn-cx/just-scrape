from typing import Any

import requests

from just_scrape.lib import HEADERS, parse_response

from .response import ModelItem


def download(locale: str = "en_US") -> dict[str, Any]:
    response = requests.get(
        f"https://apis.justwatch.com/content/providers/locale/{locale}",
        timeout=60,
        headers=HEADERS,
    )
    response.raise_for_status()
    return response.json()


def parse(data: dict[str, Any]) -> ModelItem:
    return parse_response(ModelItem, data, "get_content_providers")


def get_content_providers(locale: str = "en_US") -> ModelItem:
    data = download(locale=locale)
    return parse(data)
