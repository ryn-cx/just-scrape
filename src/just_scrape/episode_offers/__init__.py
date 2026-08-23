# TODO: Validate
"""Contains the EpisodeOffers class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from just_scrape.base_api_endpoint import BaseEndpoint
from just_scrape.episode_offers import query
from just_scrape.episode_offers.models import EpisodeOffersModel, model_validate_json
from just_scrape.exceptions import (
    EpisodeNotFoundError,
    InvalidFileError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class EpisodeOffers(BaseEndpoint):
    """Manage the episode offers file.

    Source: https://www.justwatch.com/us/tv-show/{slug}/season-{n}/episode-{n}

    Example request:
        - POST /graphql HTTP/2
        - Host: apis.justwatch.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Content-Type: application/json
        - Referer: https://www.justwatch.com/
        - Origin: https://www.justwatch.com
        - Body:
            - operationName: GetBuyBoxOffers
            - query: the document in `query.py`
            - variables:
                - nodeId={node_id}
                - country=US
                - language=en
                - platform=WEB
                - fallbackToForeignOffers=true
                - excludePackages=[]
                - isLinearTvExperiment=false
    """

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        node_id: str,
        *,
        is_linear_tv_experiment: bool = False,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = True,
        exclude_packages: Sequence[str] = (),
        country: str = "US",
        language: str = "en",
    ) -> EpisodeOffersModel:
        """Look the episode offers up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                node_id,
                is_linear_tv_experiment=is_linear_tv_experiment,
                platform=platform,
                fallback_to_foreign_offers=fallback_to_foreign_offers,
                exclude_packages=exclude_packages,
                country=country,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        node_id: str,
        *,
        is_linear_tv_experiment: bool = False,
        platform: str = "WEB",
        fallback_to_foreign_offers: bool = True,
        exclude_packages: Sequence[str] = (),
        country: str = "US",
        language: str = "en",
    ) -> str:
        """Download the episode offers file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                "GetBuyBoxOffers",
                query.QUERY,
                {
                    "isLinearTvExperiment": is_linear_tv_experiment,
                    "platform": platform,
                    "fallbackToForeignOffers": fallback_to_foreign_offers,
                    "excludePackages": list(exclude_packages),
                    "nodeId": node_id,
                    "country": country,
                    "language": language,
                },
                log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeNotFoundError(node_id, err.errors, err.response) from err
        return self._validate_download(response, node_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, node_id: str) -> str:
        # An unknown node id is not an error to the API: it echoes the id back in
        # a node carrying no offers, which is the same answer a real episode with
        # nowhere to watch it gives.
        node = json.loads(response).get("data", {}).get("node", {})
        if node.get("id") != node_id:
            raise InvalidFileError(field="node id", expected=node_id, response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> EpisodeOffersModel:
        """Read a downloaded episode offers file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
