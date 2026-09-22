# TODO: Validate
"""Contains the NewTitleBuckets class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.exceptions import InvalidFileError, JustScrapeError
from just_scrape.new_title_buckets import query
from just_scrape.new_title_buckets.models import (
    NewTitleBucketsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_buckets(response: str) -> dict[str, Any]:
    """Extract the buckets from the NewTitleBuckets response."""
    if buckets := json.loads(response)["data"]["newTitleBuckets"]:
        return buckets

    msg = "The response has no new title buckets in it"
    raise JustScrapeError(msg)


# TODO: Validate
class NewTitleBuckets(BaseEndpoint):
    """Contains the new title buckets.

    As of 3/13/2026 the API pages wrongly when objectTypes is empty and answers
    with a truncated set of results. Set `filter_object_types` to
    `["SHOW_SEASON"]` or `["MOVIE"]` to fix pagination. It is a server side bug,
    because the website itself is broken:
    https://www.justwatch.com/us/tv-shows/new

    Source: https://www.justwatch.com/us/new

    Example request:
        - POST /graphql HTTP/2
        - Host: apis.justwatch.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Content-Type: application/json
        - Referer: https://www.justwatch.com/
        - Origin: https://www.justwatch.com
        - Body:
            - operationName: GetNewTitleBuckets
            - query: the document in `query.py`
            - variables:
                - first=8
                - bucketSize=0
                - groupBy=DATE_PACKAGE
                - pageType=NEW
                - country=US
                - priceDrops=false
    """

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        *,
        first: int = 8,
        bucket_size: int = 0,
        group_by: str = "DATE_PACKAGE",
        page_type: str = "NEW",
        country: str = "US",
        new_after_cursor: str = "",
        price_drops: bool = False,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> NewTitleBucketsModel:
        """Download and parse the new title buckets file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                first=first,
                bucket_size=bucket_size,
                group_by=group_by,
                page_type=page_type,
                country=country,
                new_after_cursor=new_after_cursor,
                price_drops=price_drops,
                filter_age_certifications=filter_age_certifications,
                filter_exclude_genres=filter_exclude_genres,
                filter_exclude_production_countries=(
                    filter_exclude_production_countries
                ),
                filter_object_types=filter_object_types,
                filter_production_countries=filter_production_countries,
                filter_subgenres=filter_subgenres,
                filter_genres=filter_genres,
                filter_packages=filter_packages,
                filter_exclude_irrelevant_titles=filter_exclude_irrelevant_titles,
                filter_presentation_types=filter_presentation_types,
                filter_monetization_types=filter_monetization_types,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        *,
        first: int = 8,
        bucket_size: int = 0,
        group_by: str = "DATE_PACKAGE",
        page_type: str = "NEW",
        country: str = "US",
        new_after_cursor: str = "",
        price_drops: bool = False,
        filter_age_certifications: list[Any] | None = None,
        filter_exclude_genres: list[Any] | None = None,
        filter_exclude_production_countries: list[Any] | None = None,
        filter_object_types: list[Any] | None = None,
        filter_production_countries: list[Any] | None = None,
        filter_subgenres: list[Any] | None = None,
        filter_genres: list[Any] | None = None,
        filter_packages: list[str] | None = None,
        filter_exclude_irrelevant_titles: bool = False,
        filter_presentation_types: list[Any] | None = None,
        filter_monetization_types: list[Any] | None = None,
    ) -> str:
        """Download the new title buckets file."""
        log_id = self.get_log_id(self.download, locals())
        response = self._client.download(
            "GetNewTitleBuckets",
            query.QUERY,
            {
                "first": first,
                "bucketSize": bucket_size,
                "groupBy": group_by,
                "pageType": page_type,
                "country": country,
                "newAfterCursor": new_after_cursor,
                "newTitlesFilter": {
                    "ageCertifications": filter_age_certifications or [],
                    "excludeGenres": filter_exclude_genres or [],
                    "excludeProductionCountries": (
                        filter_exclude_production_countries or []
                    ),
                    "objectTypes": filter_object_types or [],
                    "productionCountries": filter_production_countries or [],
                    "subgenres": filter_subgenres or [],
                    "genres": filter_genres or [],
                    "packages": filter_packages or [],
                    "excludeIrrelevantTitles": filter_exclude_irrelevant_titles,
                    "presentationTypes": filter_presentation_types or [],
                    "monetizationTypes": filter_monetization_types or [],
                },
                "priceDrops": price_drops,
            },
            log_id,
        )
        return self._validate_download(response)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str) -> str:
        # The response carries no echo of the request, so only its shape is
        # checked.
        buckets = json.loads(response).get("data", {}).get("newTitleBuckets", {})
        if buckets.get("edges") is None:
            raise InvalidFileError(field="new title buckets", response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> NewTitleBucketsModel:
        """Load a new title buckets file into its model."""
        return model_validate_json(
            extract_buckets(data),
            log_id or self.default_log_id,
        )
