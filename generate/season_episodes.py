# TODO: Validate
"""Rebuilds SeasonEpisodesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing
from just_scrape import JustScrape

NODE_IDS = ["tss0000000", "tss486285"]


# TODO: Validate
def generate_season_episodes(client: JustScrape) -> None:
    """Rebuild SeasonEpisodesModel."""
    for node_id in NODE_IDS:
        download_if_missing(
            FILES_PATH,
            "SeasonEpisodesModel",
            node_id,
            lambda node_id=node_id: client.season_episodes.download(node_id),
        )
    generate_model(FILES_PATH, JUST_SCRAPE_PATH, "SeasonEpisodesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season_episodes(JustScrape(build_client_automatically()))
