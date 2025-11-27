from collections.abc import Sequence
from typing import Any

from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.get_buy_box_offers import query, request, response
from just_scrape.protocol import JustWatchProtocol


class BuyBoxOffersMixin(JustWatchProtocol):
    def _get_buy_box_offers_variables(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> request.Variables:
        return request.Variables(
            platform=platform,
            fallbackToForeignOffers=fallback_to_foreign_offers,
            excludePackages=list(exclude_packages),
            nodeId=node_id,
            country=country,
            language=language,
        )

    def _download_get_buy_box_offers(  # noqa: PLR0913
        self,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        node_id: str,
        country: str = "US",
        language: str = "en",
    ) -> dict[str, Any]:
        variables = self._get_buy_box_offers_variables(
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            node_id=node_id,
            country=country,
            language=language,
        )
        return self._graphql_request(
            operation_name="GetBuyBoxOffers",
            query=query.QUERY,
            variables=variables,
        )

    def parse_get_buy_box_offers(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> response.GetBuyBoxOffers:
        if update:
            return self.parse_response(
                response.GetBuyBoxOffers,
                data,
                "get_buy_box_offers",
            )

        return response.GetBuyBoxOffers.model_validate(data)

    def get_get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> response.GetBuyBoxOffers:
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
        resp = self._download_get_buy_box_offers(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )

        return self.parse_get_buy_box_offers(resp, update=True)
