"""Buy Box Offers API endpoint."""

from __future__ import annotations

from typing import Any, override

from good_ass_pydantic_integrator import CustomSerializer

from just_scrape.base_client import BaseEndpoint
from just_scrape.buy_box_offers import query
from just_scrape.buy_box_offers.response_models import BuyBoxOffersResponse
from just_scrape.constants import DEFAULT_EXCLUDE_PACKAGES


class BuyBoxOffers(BaseEndpoint[BuyBoxOffersResponse]):
    """Provides methods to download, parse, and retrieve buy box offers data."""

    _response_model = BuyBoxOffersResponse

    @classmethod
    @override
    def _custom_serializers(cls) -> list[CustomSerializer]:
        return [
            CustomSerializer(
                class_name="Node",
                field_name="max_offer_updated_at",
                serializer_code=(
                    "if value is None:\n"
                    "    return None\n"
                    'return value.strftime("%Y-%m-%dT%H:%M:%S.%f")'
                    '.rstrip("0").rstrip(".") + "Z"'
                ),
                output_type="str | None",
            ),
        ]

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
        """Downloads buy box offers data for a given node ID.

        Args:
            node_id: The ID of the episode.
            platform: ???
            fallback_to_foreign_offers: ???
            exclude_packages: ???
            country: ???
            language: ???

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
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
    ) -> BuyBoxOffersResponse:
        """Downloads and parses buy box offers data for a given node ID.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            node_id: The ID of the episode.
            platform: ???
            fallback_to_foreign_offers: ???
            exclude_packages: ???
            country: ???
            language: ???
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
