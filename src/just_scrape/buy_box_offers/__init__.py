# TODO: Validate
"""Contains the BuyBoxOffers class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.buy_box_offers import query
from just_scrape.buy_box_offers.models import BuyBoxOffersResponse
from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class BuyBoxOffers(BaseEndpoint[BuyBoxOffersResponse]):
    """Manage the buy box offers file."""

    _response_model = BuyBoxOffersResponse

    # PLR0913 - Each parameter maps to an API parameter.
    def get_log_id(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {node_id=}",
            platform=(platform, "WEB"),
            fallback_to_foreign_offers=(fallback_to_foreign_offers, False),
            exclude_packages=(exclude_packages, DEFAULT_EXCLUDE_PACKAGES),
            country=(country, "US"),
            language=(language, "en"),
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def download(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> dict[str, Any]:
        """Downloads the buy box offers file."""
        return self._client.download(
            "GetBuyBoxOffers",
            query.QUERY,
            {
                "platform": platform,
                "fallbackToForeignOffers": fallback_to_foreign_offers,
                "excludePackages": exclude_packages,
                "nodeId": node_id,
                "country": country,
                "language": language,
            },
            log_id=self.get_log_id(
                node_id,
                platform=platform,
                fallback_to_foreign_offers=fallback_to_foreign_offers,
                exclude_packages=exclude_packages,
                country=country,
                language=language,
            ),
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def download_and_parse(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> BuyBoxOffersResponse:
        """Downloads and parses the buy box offers file."""
        data = self.download(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )
        return self.parse(data)
