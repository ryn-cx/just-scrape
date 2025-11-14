import json
import logging
import uuid
from pathlib import Path
from typing import Any, Literal

from gapi import (
    GapiCustomizations,
    apply_customizations,
    update_json_schema_and_pydantic_model,
)

from just_scrape.constants import FILES_PATH, JUST_SCRAPE_PATH

logger = logging.getLogger(__name__)


def update_model(
    endpoint_name: str,
    endpoint_type: Literal["request", "response"],
    data: dict[str, Any],
    customizations: GapiCustomizations | None = None,
) -> None:
    schema_path = JUST_SCRAPE_PATH / f"{endpoint_name}/{endpoint_type}.schema.json"
    model_path = JUST_SCRAPE_PATH / f"{endpoint_name}/{endpoint_type}.py"
    update_json_schema_and_pydantic_model(data, schema_path, model_path, endpoint_name)
    apply_customizations(model_path, customizations)


def save_file(
    endpoint_name: str,
    endpoint_type: Literal["request", "response"],
    data: dict[str, Any],
) -> None:
    """Add a new test file for a given endpoint."""
    input_folder = FILES_PATH / endpoint_name / endpoint_type
    new_json_path = input_folder / f"{uuid.uuid4()}.json"
    new_json_path.parent.mkdir(parents=True, exist_ok=True)
    new_json_path.write_text(json.dumps(data, indent=2))


def update_query(endpoint: Path) -> None:
    first_file = next(endpoint.glob("*.json"))
    file_content = json.loads(first_file.read_text())
    output_file = JUST_SCRAPE_PATH / f"{endpoint.parent.name}/query.py"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        f'# ruff: noqa: E501\nQUERY = """{file_content["query"]}"""\n',
    )
