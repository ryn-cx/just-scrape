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
from just_scrape.url_title_details import extract_title

MODEL_NAME = "UrlTitleDetailsModel"


# TODO: Validate
class UrlTitleDetailsId(RecordingId[JustScrape]):
    full_path: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.url_title_details.download(self.full_path)


FULL_PATHS = load_ids(GENERATOR_PATHS, MODEL_NAME, UrlTitleDetailsId)


# TODO: Validate
def generate_url_title_details(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, FULL_PATHS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, UrlTitleDetailsId, extract_title)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_url_title_details(JustScrape(build_client_automatically()))
