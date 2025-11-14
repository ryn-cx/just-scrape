from collections.abc import Sequence
from typing import Any

from gapi import CustomSerializer, GapiCustomizations

from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import UrlTitleDetails

DATETIME_SERIALIZER = 'return value.strftime("%Y-%m-%dT%H:%M:%S.%f").rstrip("0") + "Z"'
GAPI_CUSTOMIZATIONS = GapiCustomizations(
    custom_serializers=[
        # There is a date field called updated_at so the class name needs to be
        # specified.
        CustomSerializer(
            class_name="RankInfo",
            field_name="updated_at",
            serializer_code=DATETIME_SERIALIZER,
        ),
        CustomSerializer(
            class_name="StreamingChartInfo",
            field_name="updated_at",
            serializer_code=DATETIME_SERIALIZER,
        ),
        CustomSerializer(
            field_name="available_from_time",
            serializer_code=DATETIME_SERIALIZER,
        ),
        CustomSerializer(
            field_name="available_to_time",
            serializer_code=DATETIME_SERIALIZER,
        ),
        CustomSerializer(
            class_name="Node",
            field_name="max_offer_updated_at",
            serializer_code=DATETIME_SERIALIZER,
        ),
    ],
)


class UrlTitleDetailsMixin(JustWatchProtocol):
    def _url_title_details_variables(  # noqa: PLR0913
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] | None = None,
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> Variables:
        if exclude_packages is None:
            exclude_packages = DEFAULT_EXCLUDE_PACKAGES

        return Variables(
            platform=platform,
            excludeTextRecommendationTitle=exclude_text_recommendation_title,
            first=first,
            fallbackToForeignOffers=fallback_to_foreign_offers,
            excludePackages=list(exclude_packages),
            fullPath=full_path,
            language=language,
            country=country,
            episodeMaxLimit=episode_max_limit,
        )

    def _download_url_title_details(  # noqa: PLR0913
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] | None = None,
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> dict[str, Any]:
        variables = self._url_title_details_variables(
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
        return self._graphql_request(
            operation_name="GetUrlTitleDetails",
            query=QUERY,
            variables=variables,
        )

    def parse_url_title_details(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> UrlTitleDetails:
        if update:
            return self._parse_response(
                UrlTitleDetails,
                response,
                "url_title_details",
                GAPI_CUSTOMIZATIONS,
            )

        return UrlTitleDetails.model_validate(response)

    def get_url_title_details(  # noqa: PLR0913
        self,
        full_path: str,
        *,
        platform: str = "WEB",
        exclude_text_recommendation_title: bool = True,
        first: int = 10,
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] | None = None,
        language: str = "en",
        country: str = "US",
        episode_max_limit: int = 20,
    ) -> UrlTitleDetails:
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
        response = self._download_url_title_details(
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

        return self.parse_url_title_details(response, update=True)
