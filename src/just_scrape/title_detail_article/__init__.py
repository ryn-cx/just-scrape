# TODO: Validate
"""Contains the TitleDetailArticle class."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.title_detail_article import query
from just_scrape.title_detail_article.models import TitleDetailArticleResponse


class TitleDetailArticle(BaseEndpoint[TitleDetailArticleResponse]):
    """Manage the title detail article file."""

    _response_model = TitleDetailArticleResponse

    def download(
        self,
        full_path: str,
        *,
        language: str = "en",
        country: str = "US",
    ) -> dict[str, Any]:
        """Downloads the title detail article file."""
        return self._client.download(
            "GetTitleDetailArticle",
            query.QUERY,
            {
                "fullPath": full_path,
                "language": language,
                "country": country,
            },
            log_id=f"{self.__class__.__name__} {full_path}",
        )

    def get(
        self,
        full_path: str,
        *,
        language: str = "en",
        country: str = "US",
    ) -> TitleDetailArticleResponse:
        """Downloads and parses the title detail article file."""
        data = self.download(
            full_path=full_path,
            language=language,
            country=country,
        )
        return self.parse(data)
