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
from just_scrape.search import extract_titles

MODEL_NAME = "SearchModel"


# TODO: Validate
class SearchId(RecordingId[JustScrape]):
    search_query: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.search.download(self.search_query)


QUERIES = load_ids(GENERATOR_PATHS, MODEL_NAME, SearchId)


# TODO: Validate
def generate_search(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, QUERIES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SearchId, extract_titles)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(JustScrape(build_client_automatically()))
