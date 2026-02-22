"""URL Title Details API endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, override

from just_scrape.base_client import BaseEndpoint
from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.url_title_details import query
from just_scrape.url_title_details.response_models import UrlTitleDetailsResponse

if TYPE_CHECKING:
    from good_ass_pydantic_integrator import CustomSerializer


class UrlTitleDetails(BaseEndpoint[UrlTitleDetailsResponse]):
    """Provides methods to download, parse, and retrieve URL title details data."""

    _response_model = UrlTitleDetailsResponse

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            # There is a date field called updated_at too so the class name needs to be
            # specified.
            cls._datetime_serializer("updated_at", class_name="RankInfo"),
            cls._datetime_serializer("updated_at", class_name="StreamingChartInfo"),
            cls._datetime_serializer("available_from_time"),
            cls._datetime_serializer("available_to_time"),
            cls._datetime_serializer("max_offer_updated_at", class_name="Node"),
        ]

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
        """Downloads URL title details data for a given path.

        Args:
            full_path: The full URL path excluding the domain.
            platform: ???
            exclude_text_recommendation_title: ???
            first: ???
            fallback_to_foreign_offers: ???
            exclude_packages: ???
            language: ???
            country: ???
            episode_max_limit: ???

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
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
        """Downloads and parses URL title details data for a given path.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            full_path: The full URL path excluding the domain.
            platform: ???
            exclude_text_recommendation_title: ???
            first: ???
            fallback_to_foreign_offers: ???
            exclude_packages: ???
            language: ???
            country: ???
            episode_max_limit: ???
        """
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
