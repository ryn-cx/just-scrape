from collections.abc import Sequence
from typing import Any

from just_scrape.api.just_watch_protocol import JustWatchProtocol
from just_scrape.models.request.get_url_title_details import Variables
from just_scrape.models.response.get_url_title_details import Model, UrlV2
from just_scrape.queries.get_url_title_details import QUERY

DEFAULT_EXCLUDE_PACKAGES = [
    "3ca",
    "als",
    "amo",
    "bfi",
    "cgv",
    "chi",
    "cnv",
    "cut",
    "daf",
    "kod",
    "koc",
    "mrp",
    "mte",
    "mvt",
    "nxp",
    "org",
    "ply",
    "rvl",
    "tak",
    "tbv",
    "tf1",
    "uat",
    "vld",
    "wa4",
    "wdt",
    "yot",
    "yrk",
    "jpc",
    "thl",
]


class GetUrlTitleDetails(JustWatchProtocol):
    """Mixin for GraphQL clients that implement JustWatchProtocol."""

    def _variables_get_url_title_details(  # noqa: PLR0913
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

    def download_get_url_title_details(  # noqa: PLR0913
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
        variables = self._variables_get_url_title_details(
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
        return self.graphql_request(
            operation_name="GetUrlTitleDetails",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_get_url_title_details(self, data: dict[str, Any]) -> UrlV2:
        return self.parse_response(Model, data, "get_url_title_details").data.url_v2

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
    ) -> UrlV2:
        data = self.download_get_url_title_details(
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

        return self.parse_get_url_title_details(data)
