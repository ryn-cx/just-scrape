from typing import Any

from just_scrape.api.just_watch_protocol import JustWatchProtocol
from just_scrape.models.request.get_title_detail_article import Variables
from just_scrape.models.response.get_title_detail_article import Model, UrlV2
from just_scrape.queries.get_title_detail_article import QUERY


class GetTitleDetailArticle(JustWatchProtocol):
    """Mixin for GraphQL clients that implement JustWatchProtocol."""

    def _variables_get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> Variables:
        return Variables(
            fullPath=full_path,
            language=language,
            country=country,
        )

    def download_get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> dict[str, Any]:
        variables = self._variables_get_title_detail_article(
            full_path=full_path,
            language=language,
            country=country,
        )
        return self.graphql_request(
            operation_name="GetTitleDetailArticle",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_get_title_detail_article(self, data: dict[str, Any]) -> UrlV2:
        return self.parse_response(
            Model,
            data,
            "get_title_detail_article",
        ).data.url_v2

    def get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> UrlV2:
        data = self.download_get_title_detail_article(
            full_path=full_path,
            language=language,
            country=country,
        )

        return self.parse_get_title_detail_article(data)
