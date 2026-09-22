from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from just_scrape import JustScrape
from just_scrape.episode_offers import extract_offers

MODEL_NAME = "EpisodeOffersModel"


# TODO: Validate
class EpisodeOffersId(RecordingId[JustScrape]):
    node_id: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.episode_offers.download(self.node_id)


NODE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, EpisodeOffersId)


# TODO: Validate
def generate_episode_offers(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, NODE_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, EpisodeOffersId, extract_offers)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_episode_offers(JustScrape(build_client_automatically()))
