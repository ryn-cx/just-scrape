# TODO: Validate
"""Rebuilds EpisodeOffersModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, JUST_SCRAPE_PATH
from generate.utils import download_if_missing
from just_scrape import JustScrape

NODE_IDS = ["tse0000000", "tse1126259", "tse1610421"]


# TODO: Validate
def generate_episode_offers(client: JustScrape) -> None:
    """Rebuild EpisodeOffersModel."""
    for node_id in NODE_IDS:
        download_if_missing(
            FILES_PATH,
            "EpisodeOffersModel",
            node_id,
            lambda node_id=node_id: client.episode_offers.download(node_id),
        )
    generate_model(FILES_PATH, JUST_SCRAPE_PATH, "EpisodeOffersModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episode_offers(JustScrape(build_client_automatically()))
