from typing import Any

from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES
from just_scrape.get_buy_box_offers import query
from just_scrape.get_buy_box_offers.request import models as request_models
from just_scrape.get_buy_box_offers.response import models as response_models
from just_scrape.protocol import JustWatchProtocol


class BuyBoxOffersMixin(JustWatchProtocol):
    def download_get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> dict[str, Any]:
        variables = request_models.Variables(
            platform=platform,
            fallbackToForeignOffers=fallback_to_foreign_offers,
            excludePackages=exclude_packages,
            nodeId=node_id,
            country=country,
            language=language,
        )
        return self._download_graphql_request("GetBuyBoxOffers", query.QUERY, variables)

    def parse_get_buy_box_offers(
        self,
        data: dict[str, Any],
        *,
        update: bool = True,
    ) -> response_models.GetBuyBoxOffersResponse:
        if update:
            return self.parse_response(
                response_models.GetBuyBoxOffersResponse,
                data,
                "get_buy_box_offers",
            )

        return response_models.GetBuyBoxOffersResponse.model_validate(data)

    def get_get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> response_models.GetBuyBoxOffersResponse:
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
        response = self.download_get_buy_box_offers(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )

        return self.parse_get_buy_box_offers(response)
