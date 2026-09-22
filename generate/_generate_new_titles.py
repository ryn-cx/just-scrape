from __future__ import annotations

import logging
from datetime import date

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from just_scrape import JustScrape
from just_scrape.new_titles import extract_new_titles

MODEL_NAME = "NewTitlesModel"


# TODO: Validate
FIRST = 3


# TODO: Validate
class NewTitlesId(RecordingId[JustScrape]):
    release_date: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.new_titles.download(
            date=date.fromisoformat(self.release_date),
            first=FIRST,
        )


RELEASE_DATES = load_ids(GENERATOR_PATHS, MODEL_NAME, NewTitlesId)


# TODO: Validate
def generate_new_titles(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, RELEASE_DATES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, NewTitlesId, extract_new_titles)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_new_titles(JustScrape(build_client_automatically()))
