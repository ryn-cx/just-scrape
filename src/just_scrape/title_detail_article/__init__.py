"""Title Detail Article API endpoint."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.title_detail_article import query
from just_scrape.title_detail_article.response_models import TitleDetailArticleResponse


class TitleDetailArticle(BaseEndpoint[TitleDetailArticleResponse]):
    """Provides methods to download, parse, and retrieve title detail article data."""

    _response_model = TitleDetailArticleResponse

    def download(
        self,
        full_path: str,
        *,
        language: str = "en",
        country: str = "US",
    ) -> dict[str, Any]:
        """Downloads title detail article data for a given path.

        Args:
            full_path: The full URL path of the title.
            language: ???
            country: ???

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        return self._client.download(
            "GetTitleDetailArticle",
            query.QUERY,
            {
                "fullPath": full_path,
                "language": language,
                "country": country,
            },
        )

    def get(
        self,
        full_path: str,
        *,
        language: str = "en",
        country: str = "US",
    ) -> TitleDetailArticleResponse:
        """Downloads and parses title detail article data for a given path.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            full_path: The full URL path of the title.
            language: ???
            country: ???
        """
        data = self.download(
            full_path=full_path,
            language=language,
            country=country,
        )
        return self.parse(data)
