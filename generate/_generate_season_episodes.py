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
from just_scrape.season_episodes import extract_season

MODEL_NAME = "SeasonEpisodesModel"


# TODO: Validate
class SeasonEpisodesId(RecordingId[JustScrape]):
    node_id: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.season_episodes.download(self.node_id)


NODE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, SeasonEpisodesId)


# TODO: Validate
def generate_season_episodes(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, NODE_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SeasonEpisodesId, extract_season)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season_episodes(JustScrape(build_client_automatically()))
