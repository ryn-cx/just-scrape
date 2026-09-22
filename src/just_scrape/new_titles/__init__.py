# TODO: Validate
"""Contains the NewTitles class."""

from __future__ import annotations

import datetime
import json
from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.exceptions import InvalidFileError, JustScrapeError
from just_scrape.new_titles import query
from just_scrape.new_titles.models import NewTitlesModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_new_titles(response: str) -> dict[str, Any]:
    """Extract the new titles from the NewTitles response."""
    if new_titles := json.loads(response)["data"]["newTitles"]:
        return new_titles

    msg = "The response has no new titles in it"
    raise JustScrapeError(msg)


# TODO: Validate
class NewTitles(BaseEndpoint):
    """Contains the new titles.

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
            - operationName: GetNewTitles
            - query: the document in `query.py`
            - variables:
                - date={date}
                - first=10
                - pageType=NEW
                - country=US
                - language=en
                - platform=WEB
    """

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        *,
        first: int = 10,
        page_type: str = "NEW",
        date: datetime.date | None = None,
        language: str = "en",
        country: str = "US",
        price_drops: bool = False,
        platform: str = "WEB",
        after: str | None = None,
        show_date_badge: bool = False,
        available_to_packages: list[str] | None = None,
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
    ) -> NewTitlesModel:
        """Download and parse the new titles file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                first=first,
                page_type=page_type,
                date=date,
                language=language,
                country=country,
                price_drops=price_drops,
                platform=platform,
                after=after,
                show_date_badge=show_date_badge,
                available_to_packages=available_to_packages,
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
        first: int = 10,
        page_type: str = "NEW",
        date: datetime.date | None = None,
        language: str = "en",
        country: str = "US",
        price_drops: bool = False,
        platform: str = "WEB",
        after: str | None = None,
        show_date_badge: bool = False,
        available_to_packages: list[str] | None = None,
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
        """Download the new titles file, defaulting to what turned up today."""
        log_id = self.get_log_id(self.download, locals())
        response = self._client.download(
            "GetNewTitles",
            query.QUERY,
            {
                "after": after,
                "first": first,
                "pageType": page_type,
                "date": (
                    date or datetime.datetime.now(tz=datetime.UTC).date()
                ).isoformat(),
                "filter": {
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
                "language": language,
                "country": country,
                "priceDrops": price_drops,
                "platform": platform,
                "showDateBadge": show_date_badge,
                "availableToPackages": available_to_packages or [],
            },
            log_id,
        )
        return self._validate_download(response)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str) -> str:
        # The response carries no echo of the request, so only its shape is
        # checked. A date nothing turned up on is answered with an empty page.
        new_titles = json.loads(response).get("data", {}).get("newTitles", {})
        if new_titles.get("edges") is None:
            raise InvalidFileError(field="new titles", response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> NewTitlesModel:
        """Load a new titles file into its model."""
        return model_validate_json(
            extract_new_titles(data),
            log_id or self.default_log_id,
        )
