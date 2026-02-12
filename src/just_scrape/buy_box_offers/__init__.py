"""Buy Box Offers API endpoint."""

from __future__ import annotations

from functools import cached_property
from typing import Any, override

from gapi import CustomSerializer

from just_scrape.base_client import BaseEndpoint
from just_scrape.buy_box_offers import query
from just_scrape.buy_box_offers.request.models import Variables
from just_scrape.buy_box_offers.response.models import BuyBoxOffersResponse
from just_scrape.constants import DATETIME_SERIALIZER, DEFAULT_EXCLUDE_PACKAGES


class BuyBoxOffers(BaseEndpoint[BuyBoxOffersResponse]):
    """Provides methods to download, parse, and retrieve buy box offers data."""

    @cached_property
    @override
    def _response_model(self) -> type[BuyBoxOffersResponse]:
        return BuyBoxOffersResponse

    @cached_property
    @override
    def _response_model_folder_name(self) -> str:
        return "buy_box_offers/response"

    @cached_property
    @override
    def _custom_serializers(self) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Node",
                field_name="max_offer_updated_at",
                serializer_code=DATETIME_SERIALIZER,
                input_type="AwareDatetime",
                output_type="str",
            ),
        ]

    def download(
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> dict[str, Any]:
        """Downloads buy box offers data for a given node ID.

        Args:
            node_id: The ID of the episode.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        variables = Variables(
            platform=platform,
            fallbackToForeignOffers=fallback_to_foreign_offers,
            excludePackages=exclude_packages,
            nodeId=node_id,
            country=country,
            language=language,
        )
        return self._client.download_graphql_request(
            "GetBuyBoxOffers",
            query.QUERY,
            variables,
        )

    def get(
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: list[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> BuyBoxOffersResponse:
        """Downloads and parses buy box offers data for a given node ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            node_id: The ID of the episode.
        """
        data = self.download(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )
        return self.parse(data)
