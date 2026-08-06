# TODO: Validate
"""Contains the BuyBoxOffers class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from just_scrape.base_client import BaseEndpoint
from just_scrape.buy_box_offers import query
from just_scrape.buy_box_offers.models import BuyBoxOffersResponse
from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.exceptions import InvalidFileError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class BuyBoxOffers(BaseEndpoint[BuyBoxOffersResponse]):
    """Manage the buy box offers file."""

    _response_model = BuyBoxOffersResponse

    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
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
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
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
            log_id=log_id,
        )
        if data.get("data", {}).get("node", {}).get("id") != node_id:
            raise InvalidFileError(field="node id", expected=node_id)
        return data

    def download_and_parse(  # noqa: PLR0913 - Each parameter maps to an API parameter.
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
