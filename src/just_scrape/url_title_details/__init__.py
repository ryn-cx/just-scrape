# TODO: Validate
"""Contains the UrlTitleDetails class."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.url_title_details import query
from just_scrape.url_title_details.models import UrlTitleDetailsResponse


class UrlTitleDetails(BaseEndpoint[UrlTitleDetailsResponse]):
    """Manage the url title details file."""

    _response_model = UrlTitleDetailsResponse

    # PLR0913 - Each parameter maps to an API parameter.
    def download(  # noqa: PLR0913
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> dict[str, Any]:
        """Downloads the url title details file."""
        return self._client.download(
            "GetUrlTitleDetails",
            query.QUERY,
            {
                "platform": platform,
                "excludeTextRecommendationTitle": exclude_text_recommendation_title,
                "first": first,
                "fallbackToForeignOffers": fallback_to_foreign_offers,
                "excludePackages": exclude_packages,
                "fullPath": full_path,
                "language": language,
                "country": country,
                "episodeMaxLimit": episode_max_limit,
            },
            log_id=f"{self.__class__.__name__} {full_path}",
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def get(  # noqa: PLR0913
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> UrlTitleDetailsResponse:
        """Downloads and parses the url title details file."""
        data = self.download(
            platform=platform,
            exclude_text_recommendation_title=exclude_text_recommendation_title,
            first=first,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            full_path=full_path,
            language=language,
            country=country,
            episode_max_limit=episode_max_limit,
        )
        return self.parse(data)
