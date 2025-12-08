from typing import Any

from just_scrape.protocol import JustWatchProtocol
from just_scrape.title_detail_article import query
from just_scrape.title_detail_article.request import models as request_models
from just_scrape.title_detail_article.response import models as response_models


class TitleDetailArticleMixin(JustWatchProtocol):
    def download_get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> dict[str, Any]:
        variables = request_models.Variables(
            fullPath=full_path,
            language=language,
            country=country,
        )
        return self._download_graphql_request(
            "GetTitleDetailArticle",
            query.QUERY,
            variables,
        )

    def parse_get_title_detail_article(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> response_models.TitleDetailArticleResponse:
        if update:
            return self.parse_response(
                response_models.TitleDetailArticleResponse,
                data,
                "title_detail_article",
            )

        return response_models.TitleDetailArticleResponse.model_validate(data)

    def get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> response_models.TitleDetailArticleResponse:
        """This may be deprecated and no longer used."""
        response = self.download_get_title_detail_article(
            full_path=full_path,
            language=language,
            country=country,
        )

        return self.parse_get_title_detail_article(response)
