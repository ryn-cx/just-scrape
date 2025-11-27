from typing import Any

from just_scrape.protocol import JustWatchProtocol
from just_scrape.title_detail_article import query, request, response


class TitleDetailArticleMixin(JustWatchProtocol):
    def _variables_get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> request.Variables:
        return request.Variables(
            fullPath=full_path,
            language=language,
            country=country,
        )

    def _download_get_title_detail_article(
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
        return self._graphql_request(
            operation_name="GetTitleDetailArticle",
            query=query.QUERY,
            variables=variables,
        )

    def parse_get_title_detail_article(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> response.TitleDetailArticle:
        if update:
            return self.parse_response(
                response.TitleDetailArticle,
                data,
                "title_detail_article",
            )

        return response.TitleDetailArticle.model_validate(data)

    def get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> response.TitleDetailArticle:
        """This may be deprecated and no longer used."""
        resp = self._download_get_title_detail_article(
            full_path=full_path,
            language=language,
            country=country,
        )

        return self.parse_get_title_detail_article(resp, update=True)
