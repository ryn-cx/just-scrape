"""Title Detail Article API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import Any, override

from just_scrape.base_client import BaseEndpoint
from just_scrape.title_detail_article import query
from just_scrape.title_detail_article.request.models import Variables
from just_scrape.title_detail_article.response.models import TitleDetailArticleResponse


class TitleDetailArticle(BaseEndpoint[TitleDetailArticleResponse]):
    """Provides methods to download, parse, and retrieve title detail article data."""

    @cached_property
    @override
    def _response_model(self) -> type[TitleDetailArticleResponse]:
        return TitleDetailArticleResponse

    @cached_property
    @override
    def _response_model_folder_name(self) -> str:
        return "title_detail_article/response"

    def download(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> dict[str, Any]:
        """Downloads title detail article data for a given path.

        Args:
            full_path: The full URL path of the title.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        variables = Variables(
            fullPath=full_path,
            language=language,
            country=country,
        )
        return self._client.download_graphql_request(
            "GetTitleDetailArticle",
            query.QUERY,
            variables,
        )

    def get(
        self,
        *,
        full_path: str,
        language: str = "en",
        country: str = "US",
    ) -> TitleDetailArticleResponse:
        """Downloads and parses title detail article data for a given path.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            full_path: The full URL path of the title.
        """
        data = self.download(
            full_path=full_path,
            language=language,
            country=country,
        )
        return self.parse(data)
