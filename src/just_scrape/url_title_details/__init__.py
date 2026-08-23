# TODO: Validate
"""Contains the UrlTitleDetails class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    TitleNotFoundError,
)
from just_scrape.url_title_details import query
from just_scrape.url_title_details.models import (
    UrlTitleDetailsModel,
    model_validate_json,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class UrlTitleDetails(BaseEndpoint):
    """Manage the url title details file.

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
            - operationName: GetUrlTitleDetails
            - query: the document in `query.py`
            - variables:
                - fullPath={full_path}
                - country=US
                - language=en
                - platform=WEB
                - first=10
                - episodeMaxLimit=20
    """

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = (),
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> UrlTitleDetailsModel:
        """Look the title details up and return the model they are read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                full_path,
                platform=platform,
                exclude_text_recommendation_title=exclude_text_recommendation_title,
                first=first,
                fallback_to_foreign_offers=fallback_to_foreign_offers,
                exclude_packages=exclude_packages,
                language=language,
                country=country,
                episode_max_limit=episode_max_limit,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = (),
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> str:
        """Download the url title details file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                "GetUrlTitleDetails",
                query.QUERY,
                {
                    "platform": platform,
                    "excludeTextRecommendationTitle": (
                        exclude_text_recommendation_title
                    ),
                    "first": first,
                    "fallbackToForeignOffers": fallback_to_foreign_offers,
                    "excludePackages": list(exclude_packages),
                    "fullPath": full_path,
                    "language": language,
                    "country": country,
                    "episodeMaxLimit": episode_max_limit,
                },
                log_id,
            )
        except ResourceNotFoundError as err:
            raise TitleNotFoundError(full_path, err.errors, err.response) from err
        return self._validate_download(response, full_path)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, full_path: str) -> str:
        node = json.loads(response).get("data", {}).get("urlV2", {}).get("node", {})
        if node.get("content", {}).get("fullPath") != full_path:
            raise InvalidFileError(
                field="full path",
                expected=full_path,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> UrlTitleDetailsModel:
        """Read a downloaded url title details file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
