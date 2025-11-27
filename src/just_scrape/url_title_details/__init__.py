from collections.abc import Sequence
from typing import Any

from gapi import (
    CustomSerializer,
    GapiCustomizations,
    update_json_schema_and_pydantic_model,
)

from just_scrape.constants import (
    DATETIME_SERIALIZER,
    DEFAULT_EXCLUDE_PACKAGES,
    FILES_PATH,
    JUST_SCRAPE_PATH,
)
from just_scrape.protocol import JustWatchProtocol
from just_scrape.url_title_details import query, request, response


class UrlTitleDetailsMixin(JustWatchProtocol):
    URL_TITLE_DETAILS_CUSTOMIZATIONS = GapiCustomizations(
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
    ) -> request.Variables:
        if exclude_packages is None:
            exclude_packages = DEFAULT_EXCLUDE_PACKAGES

        return request.Variables(
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
            query=query.QUERY,
            variables=variables,
        )

    def parse_url_title_details(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> response.UrlTitleDetails:
        if update:
            return self.parse_response(
                response.UrlTitleDetails,
                data,
                "url_title_details",
                self.URL_TITLE_DETAILS_CUSTOMIZATIONS,
            )

        return response.UrlTitleDetails.model_validate(data)

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
    ) -> response.UrlTitleDetails:
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

    def rebuild_url_title_details_models(self) -> None:
        """Rebuild the url_title_details request and response models from JSON files.

        This function iterates through the url_title_details endpoint directory,
        processes JSON files for both request and response types, and regenerates
        the schema and Pydantic model files.
        """
        name = "url_title_details"
        endpoint_name = FILES_PATH / "url_title_details"
        if not endpoint_name.exists():
            msg = f"Endpoint path does not exist: {endpoint_name}"
            raise FileNotFoundError(msg)

        name = endpoint_name.name
        for endpoint_type in endpoint_name.iterdir():
            if not endpoint_type.is_dir():
                continue

            schema_path = JUST_SCRAPE_PATH / f"{name}/{endpoint_type.name}.schema.json"
            model_path = JUST_SCRAPE_PATH / f"{name}/{endpoint_type.name}.py"

            schema_path.unlink(missing_ok=True)
            model_path.unlink(missing_ok=True)

            json_files = list(endpoint_type.glob("*.json"))
            if json_files:
                update_json_schema_and_pydantic_model(
                    json_files,
                    schema_path,
                    model_path,
                    name,
                )
