"""Base GAPIClient for just-scrape."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from good_ass_pydantic_integrator import CustomSerializer, GAPIClient
from pydantic import BaseModel

from just_scrape.constants import FILES_PATH

if TYPE_CHECKING:
    from pathlib import Path

    from just_scrape import JustScrape


class BaseEndpoint[T: BaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    def __init__(self, client: JustScrape) -> None:
        """Initialize the endpoint with the JustScrape client."""
        self._client = client

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        folder_name = cls._to_folder_name(cls._get_model_name())
        name = folder_name.removesuffix("_response")
        return FILES_PATH / name

    @staticmethod
    def _datetime_serializer(
        field_name: str,
        class_name: str | None = None,
    ) -> CustomSerializer:
        """Create a CustomSerializer for an AwareDatetime field."""
        return CustomSerializer(
            class_name=class_name,
            field_name=field_name,
            serializer_code=(
                "if not value:\n"
                "    return None\n"
                'return value.strftime("%Y-%m-%dT%H:%M:%S.%f")'
                '.rstrip("0").rstrip(".") + "Z"'
            ),
            input_type="AwareDatetime",
            output_type="str",
        )
