from collections.abc import Sequence
from typing import Any

from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import BuyBoxOffers


class BuyBoxOffersMixin(JustWatchProtocol):
    def _buy_box_offers_variables(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> Variables:
        return Variables(
            platform=platform,
            fallbackToForeignOffers=fallback_to_foreign_offers,
            excludePackages=list(exclude_packages),
            nodeId=node_id,
            country=country,
            language=language,
        )

    def _download_buy_box_offers(  # noqa: PLR0913
        self,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        node_id: str,
        country: str = "US",
        language: str = "en",
    ) -> dict[str, Any]:
        variables = self._buy_box_offers_variables(
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            node_id=node_id,
            country=country,
            language=language,
        )
        return self._graphql_request(
            operation_name="GetBuyBoxOffers",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_buy_box_offers(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> BuyBoxOffers:
        if update:
            return self._parse_response(BuyBoxOffers, response, "buy_box_offers")

        return BuyBoxOffers.model_validate(response)

    def get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> BuyBoxOffers:
        """Get all of the different websites that a specific episode can be watched.

        This API request normally occurs when clicking on an episode.

        Args:
            node_id: The ID of the episode.
            platform: ???
            fallback_to_foreign_offers: ???
            exclude_packages: ???
            country: ???
            language: ???
        """
        response = self._download_buy_box_offers(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )

        return self.parse_buy_box_offers(response, update=True)
