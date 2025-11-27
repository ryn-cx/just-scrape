"""BuyBoxOffers with the addition of the dateCreated field."""

from collections.abc import Sequence
from typing import Any

from gapi import (
    CustomSerializer,
    GapiCustomizations,
)

from just_scrape.constants import DATETIME_SERIALIZER, DEFAULT_EXCLUDE_PACKAGES
from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import CustomGetBuyBoxOffers


class CustomGetBuyBoxOffersMixin(JustWatchProtocol):
    CUSTOM_GET_BUY_BOX_OFFERS_CUSTOMIZATIONS = GapiCustomizations(
        custom_serializers=[
            CustomSerializer(
                class_name="Node",
                field_name="max_offer_updated_at",
                serializer_code=DATETIME_SERIALIZER,
            ),
        ],
    )

    def _custom_get_buy_box_offers_variables(  # noqa: PLR0913
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

    def _download_custom_get_buy_box_offers(  # noqa: PLR0913
        self,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        node_id: str,
        country: str = "US",
        language: str = "en",
    ) -> dict[str, Any]:
        variables = self._custom_get_buy_box_offers_variables(
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
            variables=variables,
        )

    def parse_custom_get_buy_box_offers(
        self,
        response: dict[str, Any],
        *,
        update: bool = False,
    ) -> CustomGetBuyBoxOffers:
        if update:
            return self.parse_response(
                CustomGetBuyBoxOffers,
                response,
                "custom_get_buy_box_offers",
                self.CUSTOM_GET_BUY_BOX_OFFERS_CUSTOMIZATIONS,
            )

        return CustomGetBuyBoxOffers.model_validate(response)

    def get_custom_get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> CustomGetBuyBoxOffers:
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
        response = self._download_custom_get_buy_box_offers(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )

        return self.parse_custom_get_buy_box_offers(response, update=True)
