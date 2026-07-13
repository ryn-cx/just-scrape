# TODO: Validate
"""Contains the CustomBuyBoxOffers class."""

from __future__ import annotations

from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.custom_buy_box_offers import query
from just_scrape.custom_buy_box_offers.models import CustomBuyBoxOffersResponse


class CustomBuyBoxOffers(BaseEndpoint[CustomBuyBoxOffersResponse]):
    """Manage the custom buy box offers file."""

    _response_model = CustomBuyBoxOffersResponse

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
        """Downloads the custom buy box offers file."""
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
            log_id=f"{self.__class__.__name__} {node_id}",
        )

    # PLR0913 - Each parameter maps to an API parameter.
    def get(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> CustomBuyBoxOffersResponse:
        """Downloads and parses the custom buy box offers file."""
        data = self.download(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )
        return self.parse(data)
