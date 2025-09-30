import json
import logging
import subprocess
from pathlib import Path
from typing import Literal

from gapix import GAPIX

from just_scrape.constants import JUST_SCRAPE_DIR, TEST_FILE_DIR

logger = logging.getLogger(__name__)


class Updater(GAPIX):
    def __init__(
        self,
        endpoint: str,
        endpoint_type: Literal["request", "response"],
    ) -> None:
        self.endpoint = endpoint
        self.endpoint_type = endpoint_type

    def endpoint_name(self) -> str:
        return f"{self.endpoint}/{self.endpoint_type}"

    def output_file(self) -> Path:
        return JUST_SCRAPE_DIR / f"{self.endpoint_name()}.py"

    def input_folder(self) -> Path:
        return TEST_FILE_DIR / self.endpoint_name()


def update_all_schemas() -> None:
    for endpoint in TEST_FILE_DIR.glob("*/*"):
        if endpoint.is_dir():
            logger.info("Updating schema for %s", endpoint.name)
            updater = Updater(endpoint.parent.name, endpoint.name)
            updater.generate_schema()
            updater.remove_redundant_files()
            if updater.endpoint_type == "request":
                update_query(endpoint)


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
    update_all_schemas()
