# TODO: Validate
"""Rebuilds NewTitleBucketsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing
from just_scrape import JustScrape

OBJECT_TYPES = ["MOVIE"]
"""The object type each recorded page of buckets is filtered to, because the API
pages wrongly when it is not filtered."""

FIRST = 3
"""A short page, so what a page holds stays small enough to read."""


# TODO: Validate
def generate_new_title_buckets(client: JustScrape) -> None:
    """Rebuild NewTitleBucketsModel."""
    for object_type in OBJECT_TYPES:
        download_if_missing(
            FILES_PATH,
            "NewTitleBucketsModel",
            object_type,
            lambda object_type=object_type: client.new_title_buckets.download(
                filter_object_types=[object_type],
                first=FIRST,
            ),
        )
    generate_model(FILES_PATH, JUST_SCRAPE_PATH, "NewTitleBucketsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_new_title_buckets(JustScrape(build_client_automatically()))
