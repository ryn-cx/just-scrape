# TODO: Validate
"""Rebuilds NewTitlesModel."""

from __future__ import annotations

import logging
from datetime import date

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing
from just_scrape import JustScrape

RELEASE_DATES = ["2026-08-01", "2050-01-01"]
"""The days the recorded pages of new titles are for."""

FIRST = 3
"""A short page, so what a page holds stays small enough to read."""


# TODO: Validate
def generate_new_titles(client: JustScrape) -> None:
    """Rebuild NewTitlesModel."""
    for release_date in RELEASE_DATES:
        download_if_missing(
            FILES_PATH,
            "NewTitlesModel",
            release_date,
            lambda release_date=release_date: client.new_titles.download(
                date=date.fromisoformat(release_date),
                first=FIRST,
            ),
        )
    generate_model(FILES_PATH, JUST_SCRAPE_PATH, "NewTitlesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_new_titles(JustScrape(build_client_automatically()))
