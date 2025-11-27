"""BuyBoxOffers with the addition of the dateCreated field."""

from collections.abc import Sequence
from typing import Any

from gapi import (
    CustomSerializer,
    GapiCustomizations,
)

from just_scrape.constants import DATETIME_SERIALIZER, DEFAULT_EXCLUDE_PACKAGES
from just_scrape.custom_get_buy_box_offers import query, request, response
from just_scrape.protocol import JustWatchProtocol


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
    ) -> request.Variables:
        return request.Variables(
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
            query=query.QUERY,
            variables=variables,
        )

    def parse_custom_get_buy_box_offers(
        self,
        data: dict[str, Any],
        *,
        update: bool = False,
    ) -> response.CustomGetBuyBoxOffers:
        if update:
            return self.parse_response(
                response.CustomGetBuyBoxOffers,
                data,
                "custom_get_buy_box_offers",
                self.CUSTOM_GET_BUY_BOX_OFFERS_CUSTOMIZATIONS,
            )

        return response.CustomGetBuyBoxOffers.model_validate(data)

    def get_custom_get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> response.CustomGetBuyBoxOffers:
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
        resp = self._download_custom_get_buy_box_offers(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )

        return self.parse_custom_get_buy_box_offers(resp, update=True)
