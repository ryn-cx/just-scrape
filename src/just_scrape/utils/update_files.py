import json
import logging
from pathlib import Path
from typing import Literal

from gapi import Override
from gapix import GAPIX

from just_scrape.constants import JUST_SCRAPE_DIR, TEST_FILE_DIR

logger = logging.getLogger(__name__)


class Updater(GAPIX):
    def __init__(
        self,
        endpoint_type: Literal["request", "response"],
        endpoint: str,
    ) -> None:
        self.endpoint = endpoint
        self.endpoint_type = endpoint_type

    def endpoint_name(self) -> str:
        return f"{self.endpoint_type}/{self.endpoint}"

    def output_file(self) -> Path:
        return JUST_SCRAPE_DIR / f"models/{self.endpoint_name()}.py"

    def input_folder(self) -> Path:
        return TEST_FILE_DIR / self.endpoint_name()


def update_all_schemas() -> None:
    for endpoint in TEST_FILE_DIR.glob("*/*"):
        if endpoint.is_dir():
            logger.info("Updating schema for %s", endpoint.name)
            updater = Updater(endpoint.parent.name, endpoint.name)
            overrides: list[Override] = []
            if updater.endpoint_type == "request" and endpoint.name == "get_new_titles":
                overrides.append(
                    Override(
                        class_name="Variables",
                        variable_name="date",
                        replacement="str",
                    ),
                )

            updater.generate_schema(overrides)
            updater.remove_redundant_files()
            if updater.endpoint_type == "request":
                update_query(endpoint)


def update_query(endpoint: Path) -> None:
    first_file = next(endpoint.glob("*.json"))
    file_content = json.loads(first_file.read_text())
    output_file = JUST_SCRAPE_DIR / f"queries/{endpoint.name}.py"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(f'# ruff: noqa: E501\nQUERY="""{file_content["query"]}"""')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    update_all_schemas()
