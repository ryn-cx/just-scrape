from collections.abc import Sequence
from typing import Any

from just_scrape.protocol import JustWatchProtocol

from .query import QUERY
from .request import Variables
from .response import Model

DEFAULT_EXCLUDE_PACKAGES = (
    "3ca",
    "als",
    "amo",
    "bfi",
    "cgv",
    "chi",
    "cnv",
    "daf",
    "kod",
    "koc",
    "mrp",
    "mte",
    "mvt",
    "nxp",
    "org",
    "ply",
    "rvl",
    "tak",
    "tbv",
    "tf1",
    "uat",
    "vld",
    "yot",
    "yrk",
    "jpc",
    "thl",
)


class GetBuyBoxOffers(JustWatchProtocol):
    def _variables_get_buy_box_offers(  # noqa: PLR0913
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
        variables = self._variables_get_buy_box_offers(
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            node_id=node_id,
            country=country,
            language=language,
        )
        return self.graphql_request(
            operation_name="GetBuyBoxOffers",
            query=QUERY,
            variables=variables.model_dump(by_alias=True),
        )

    def parse_get_buy_box_offers(self, response: dict[str, Any]) -> Model:
        return self.parse_response(Model, response, "get_buy_box_offers")

    def get_buy_box_offers(  # noqa: PLR0913
        self,
        node_id: str,
        *,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = False,
        exclude_packages: Sequence[str] = DEFAULT_EXCLUDE_PACKAGES,
        country: str = "US",
        language: str = "en",
    ) -> Model:
        response = self._download_get_buy_box_offers(
            node_id=node_id,
            platform=platform,
            fallback_to_foreign_offers=fallback_to_foreign_offers,
            exclude_packages=exclude_packages,
            country=country,
            language=language,
        )

        return self.parse_get_buy_box_offers(response)
