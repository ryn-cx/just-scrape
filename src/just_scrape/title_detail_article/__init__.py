# TODO: Validate
"""Contains the TitleDetailArticle class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.exceptions import (
    ArticleNotFoundError,
    InvalidFileError,
    JustScrapeError,
    ResourceNotFoundError,
)
from just_scrape.title_detail_article import query
from just_scrape.title_detail_article.models import (
    TitleDetailArticleModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_article(response: str) -> dict[str, Any]:
    """Extract the article from the TitleDetailArticle response."""
    if article := json.loads(response)["data"]["urlV2"]:
        return article

    msg = "The response has no article in it"
    raise JustScrapeError(msg)


# TODO: Validate
class TitleDetailArticle(BaseEndpoint):
    """Contains the title detail article.

    Source: https://www.justwatch.com{full_path}

    Example request:
        - POST /graphql HTTP/2
        - Host: apis.justwatch.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Content-Type: application/json
        - Referer: https://www.justwatch.com/
        - Origin: https://www.justwatch.com
        - Body:
            - operationName: GetTitleDetailArticle
            - query: the document in `query.py`
            - variables:
                - fullPath={full_path}
                - country=US
                - language=en
    """

    # TODO: Validate
    def __call__(
        self,
        full_path: str,
        *,
        language: str = "en",
        country: str = "US",
    ) -> TitleDetailArticleModel:
        """Download and parse the title's articles file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(full_path, language=language, country=country),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        full_path: str,
        *,
        language: str = "en",
        country: str = "US",
    ) -> str:
        """Download the title detail article file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                "GetTitleDetailArticle",
                query.QUERY,
                {
                    "fullPath": full_path,
                    "language": language,
                    "country": country,
                },
                log_id,
            )
        except ResourceNotFoundError as err:
            raise ArticleNotFoundError(full_path, err.errors, err.response) from err
        return self._validate_download(response)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str) -> str:
        # The response does not echo fullPath, so only the resolved node is
        # checked.
        node = json.loads(response).get("data", {}).get("urlV2", {}).get("node", {})
        if not node.get("id"):
            raise InvalidFileError(field="node id", response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TitleDetailArticleModel:
        """Load a title detail article file into its model."""
        return model_validate_json(
            extract_article(data),
            log_id or self.default_log_id,
        )
