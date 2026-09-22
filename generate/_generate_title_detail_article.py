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
from just_scrape.title_detail_article import extract_article

MODEL_NAME = "TitleDetailArticleModel"


# TODO: Validate
class TitleDetailArticleId(RecordingId[JustScrape]):
    full_path: str

    # TODO: Validate
    def download(self, client: JustScrape) -> str:
        return client.title_detail_article.download(self.full_path)


FULL_PATHS = load_ids(GENERATOR_PATHS, MODEL_NAME, TitleDetailArticleId)


# TODO: Validate
def generate_title_detail_article(client: JustScrape) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, FULL_PATHS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TitleDetailArticleId, extract_article)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_title_detail_article(JustScrape(build_client_automatically()))
