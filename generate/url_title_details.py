# TODO: Validate
"""Rebuilds UrlTitleDetailsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from just_scrape import JustScrape

FULL_PATHS = load_ids("UrlTitleDetailsModel")


# TODO: Validate
def generate_url_title_details(client: JustScrape) -> None:
    """Rebuild UrlTitleDetailsModel."""
    for full_path in FULL_PATHS:
        download_if_missing(
            FILES_PATH,
            "UrlTitleDetailsModel",
            full_path,
            lambda full_path=full_path: client.url_title_details.download(full_path),
        )
    rebuild_model(FILES_PATH, JUST_SCRAPE_PATH, "UrlTitleDetailsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_url_title_details(JustScrape(build_client_automatically()))
