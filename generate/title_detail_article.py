# TODO: Validate
"""Rebuilds TitleDetailArticleModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing
from just_scrape import JustScrape

FULL_PATHS = ["/us/movie/the-thursday-murder-club"]


# TODO: Validate
def generate_title_detail_article(client: JustScrape) -> None:
    """Rebuild TitleDetailArticleModel."""
    for full_path in FULL_PATHS:
        download_if_missing(
            FILES_PATH,
            "TitleDetailArticleModel",
            full_path,
            lambda full_path=full_path: client.title_detail_article.download(
                full_path,
            ),
        )
    generate_model(FILES_PATH, JUST_SCRAPE_PATH, "TitleDetailArticleModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_title_detail_article(JustScrape(build_client_automatically()))
