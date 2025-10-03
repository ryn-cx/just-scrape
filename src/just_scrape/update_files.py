import json
import logging
import subprocess
import uuid
from pathlib import Path
from typing import Any, Literal

from gapi import generate_from_folder

from just_scrape.constants import JUST_SCRAPE_DIR, TEST_FILE_DIR

logger = logging.getLogger(__name__)


def update_all_models() -> None:
    for endpoint in TEST_FILE_DIR.glob("*/*"):
        update_model(endpoint.parent.name, endpoint.name)


def update_model(endpoint: str, endpoint_type: Literal["request", "response"]) -> None:
    input_folder = TEST_FILE_DIR / endpoint / endpoint_type
    output_folder = JUST_SCRAPE_DIR / f"{endpoint}/{endpoint_type}.py"
    class_name = endpoint.replace("_", " ").title().replace(" ", "")
    logger.info("Updating schema for %s %s", endpoint, endpoint_type)
    generate_from_folder(
        input_folder,
        output_folder,
        class_name,
        remove_redundant_files=True,
    )


def add_test_file(
    endpoint: str,
    endpoint_type: Literal["request", "response"],
    data: dict[str, Any],
) -> None:
    """Add a new test file for a given endpoint."""
    # Assume this function will only ever be used for responses.
    input_folder = TEST_FILE_DIR / endpoint / endpoint_type
    new_json_path = input_folder / f"{uuid.uuid4()}.json"
    new_json_path.parent.mkdir(parents=True, exist_ok=True)
    new_json_path.write_text(json.dumps(data, indent=2))


def update_query(endpoint: Path) -> None:
    first_file = next(endpoint.glob("*.json"))
    file_content = json.loads(first_file.read_text())
    output_file = JUST_SCRAPE_DIR / f"{endpoint.parent.name}/query.py"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(f'# ruff: noqa: E501\nQUERY="""{file_content["query"]}"""')

    subprocess.run(
        ["uv", "run", "ruff", "check", "--fix", str(output_file)],  # noqa: S607
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    subprocess.run(
        ["uv", "run", "ruff", "format", str(output_file)],  # noqa: S607
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    update_all_models()
