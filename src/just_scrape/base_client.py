"""Base GAPIClient for just-scrape."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, override

from gapi import GAPIClient
from pydantic import BaseModel

from just_scrape.constants import FILES_PATH

if TYPE_CHECKING:
    from pathlib import Path

    from just_scrape import JustScrape


class BaseExtractor[T: BaseModel](GAPIClient[T]):
    """Base class to extract data from API responses."""

    @cached_property
    @override
    def _root_files_path(self) -> Path:
        return FILES_PATH

    @cached_property
    def json_files_folder(self) -> Path:
        """Model-specific subdirectory under ``_root_files_path``."""
        return self._json_files_folder


class BaseEndpoint[T: BaseModel](BaseExtractor[T]):
    """Base class for API endpoints."""

    def __init__(self, client: JustScrape) -> None:
        """Initialize the endpoint with the JustScrape client."""
        self._client = client
