from typing import Any

from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import TitleDetailArticle


class TitleDetailArticleMixin(JustWatchProtocol):
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
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_get_title_detail_article(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> TitleDetailArticle:
        if update:
            return self._parse_response(
                TitleDetailArticle,
                response,
                "title_detail_article",
            )

        return TitleDetailArticle.model_validate(response)

    def get_title_detail_article(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> TitleDetailArticle:
        """This may be deprecated and no longer used."""
        response = self._download_get_title_detail_article(
            full_path=full_path,
            language=language,
            country=country,
        )

        return self.parse_get_title_detail_article(response, update=True)
