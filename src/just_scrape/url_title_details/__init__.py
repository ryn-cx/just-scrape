"""URL Title Details API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import Any, override

from gapi import CustomSerializer, ReplacementField

from just_scrape.base_client import BaseEndpoint
from just_scrape.constants import DATETIME_SERIALIZER, DEFAULT_EXCLUDE_PACKAGES
from just_scrape.url_title_details import query
from just_scrape.url_title_details.request.models import Variables
from just_scrape.url_title_details.response.models import UrlTitleDetailsResponse


class UrlTitleDetails(BaseEndpoint[UrlTitleDetailsResponse]):
    """Provides methods to download, parse, and retrieve URL title details data."""

    @cached_property
    @override
    def _response_model(self) -> type[UrlTitleDetailsResponse]:
        return UrlTitleDetailsResponse

    @cached_property
    @override
    def _response_model_folder_name(self) -> str:
        return "url_title_details/response"

    @cached_property
    @override
    def _custom_serializers(self) -> list[CustomSerializer]:
        return [
            # There is a date field called updated_at so the class name needs to be
            # specified.
            CustomSerializer(
                class_name="RankInfo",
                field_name="updated_at",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
            CustomSerializer(
                class_name="StreamingChartInfo",
                field_name="updated_at",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
            CustomSerializer(
                field_name="available_from_time",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
            CustomSerializer(
                field_name="available_to_time",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
            CustomSerializer(
                class_name="Node",
                field_name="max_offer_updated_at",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
        ]

    def download(
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

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        variables = Variables(
            platform=platform,
            excludeTextRecommendationTitle=exclude_text_recommendation_title,
            first=first,
            fallbackToForeignOffers=fallback_to_foreign_offers,
            excludePackages=exclude_packages,
            fullPath=full_path,
            language=language,
            country=country,
            episodeMaxLimit=episode_max_limit,
        )
        return self._client.download_graphql_request(
            "GetUrlTitleDetails",
            query.QUERY,
            variables,
        )

    def get(
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
