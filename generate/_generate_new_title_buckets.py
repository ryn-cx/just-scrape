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
from just_scrape.new_title_buckets import extract_buckets

MODEL_NAME = "NewTitleBucketsModel"


# TODO: Validate
FIRST = 3


# TODO: Validate
class NewTitleBucketsId(RecordingId[JustScrape]):
    object_type: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.new_title_buckets.download(
            filter_object_types=[self.object_type],
            first=FIRST,
        )


OBJECT_TYPES = load_ids(GENERATOR_PATHS, MODEL_NAME, NewTitleBucketsId)


# TODO: Validate
def generate_new_title_buckets(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, OBJECT_TYPES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, NewTitleBucketsId, extract_buckets)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_new_title_buckets(JustScrape(build_client_automatically()))
