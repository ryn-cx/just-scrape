from typing import Any

from gapi import (
    CustomSerializer,
    GapiCustomizations,
)

from just_scrape.constants import DATETIME_SERIALIZER, DEFAULT_EXCLUDE_PACKAGES
from just_scrape.protocol import JustWatchProtocol
from just_scrape.url_title_details import query
from just_scrape.url_title_details.request import models as request_models
from just_scrape.url_title_details.response import models as response_models

URL_TITLE_DETAILS_CUSTOMIZATIONS = GapiCustomizations(
    custom_serializers=[
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
    ],
)


class UrlTitleDetailsMixin(JustWatchProtocol):
    def download_url_title_details(  # noqa: PLR0913
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
        variables = request_models.Variables(
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
        return self._download_graphql_request(
            "GetUrlTitleDetails",
            query.QUERY,
            variables,
        )

    def parse_url_title_details(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> response_models.UrlTitleDetailsResponse:
        if update:
            return self.parse_response(
                response_models.UrlTitleDetailsResponse,
                data,
                "url_title_details",
                URL_TITLE_DETAILS_CUSTOMIZATIONS,
            )

        return response_models.UrlTitleDetailsResponse.model_validate(data)

    def get_url_title_details(  # noqa: PLR0913
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
    ) -> response_models.UrlTitleDetailsResponse:
        """Get information about a specific TV show.

        This API request normally occurs when visiting a the page for a specific season
        of a TV show, on the TV show's main page, the information is embedded in the
        HTML.

        Args:
            full_path: The full URL of the TV show excluding the domain.
            platform: ???
            exclude_text_recommendation_title: ???
            first: ???
            fallback_to_foreign_offers: ???
            exclude_packages: ???
            language: ???
            country: ???
            episode_max_limit: ???
        """
        response = self.download_url_title_details(
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

        return self.parse_url_title_details(response)
