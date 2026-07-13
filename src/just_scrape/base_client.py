# TODO: Validate
"""Base GAPIClient for just-scrape."""

from __future__ import annotations

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from just_scrape.constants import FILES_PATH

if TYPE_CHECKING:
    from just_scrape import JustScrape


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    JSON_FILES_ROOT = FILES_PATH

    def __init__(self, client: JustScrape) -> None:
        """Initialize the endpoint with the JustScrape client."""
        self._client = client
