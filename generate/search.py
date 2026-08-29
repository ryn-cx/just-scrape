# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from just_scrape import JustScrape

QUERIES = load_ids("SearchModel")


# TODO: Validate
def generate_search(client: JustScrape) -> None:
    """Rebuild SearchModel."""
    for search_query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            search_query,
            lambda search_query=search_query: client.search.download(search_query),
        )
    rebuild_model(FILES_PATH, JUST_SCRAPE_PATH, "SearchModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(JustScrape(build_client_automatically()))
