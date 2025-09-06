import json
import subprocess
from pathlib import Path
from typing import Any

JUST_SCRAPE_DIR = Path(__file__).parent.parent
ROOT_DIR = JUST_SCRAPE_DIR.parent.parent
SCHEMA_DIR = JUST_SCRAPE_DIR / "schema"


def update_response(endpoint: Path) -> None:
    name = endpoint.name

    response_folder = endpoint / "response"
    if not response_folder.exists():
        return

    file_content: list[Any] = [
        json.loads(file.read_text()) for file in response_folder.glob("*.json")
    ]

    combined_schema_path = SCHEMA_DIR / "temp.json"
    combined_schema_path.write_text(json.dumps(file_content))

    # Generate Python schema using datamodel-codegen
    output_schema = JUST_SCRAPE_DIR / f"wrappers/{name}_/response.py"
    output_schema.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "uv",
        "run",
        "datamodel-codegen",
        "--input-file-type",
        "json",
        "--input",
        str(combined_schema_path),
        "--output",
        str(output_schema),
        "--snake-case-field",
        "--formatters",
        "ruff-check",
        "--disable-timestamp",
        "--extra-fields=forbid",
    ]

    subprocess.run(command, check=True, capture_output=True, text=True)

    # Remove the last 3 lines which will contain the extra wrapper class used to combine
    # files into a single json file.
    lines = output_schema.read_text().splitlines()
    lines = "\n".join(lines[:-4])
    content = "# ruff: noqa: ERA001, E742, E501\n" + lines
    content = content.replace("extra = Extra.forbid", "extra='forbid'")
    output_schema.write_text(content)

    combined_schema_path.unlink()


def update_request(endpoint: Path) -> None:
    name = endpoint.name

    request_folder = endpoint / "request"
    if not request_folder.exists():
        return

    file_content: list[Any] = [
        json.loads(file.read_text()) for file in request_folder.glob("*.json")
    ]

    combined_schema_path = SCHEMA_DIR / "temp.json"
    combined_schema_path.write_text(json.dumps(file_content))

    # Generate Python schema using datamodel-codegen
    output_schema = JUST_SCRAPE_DIR / f"wrappers/{name}_/request.py"
    output_schema.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "uv",
        "run",
        "datamodel-codegen",
        "--input-file-type",
        "json",
        "--input",
        str(combined_schema_path),
        "--output",
        str(output_schema),
        "--snake-case-field",
        "--formatters",
        "ruff-check",
        "--disable-timestamp",
        "--extra-fields=forbid",
    ]

    subprocess.run(command, check=True, capture_output=True, text=True)

    # Remove the last 3 lines which will contain the extra wrapper class used to combine
    # files into a single json file.
    lines = output_schema.read_text().splitlines()
    lines = "\n".join(lines[:-4])
    content = "# ruff: noqa: ERA001\n" + lines
    content = content.replace("extra = Extra.forbid", "extra='forbid'")
    output_schema.write_text(content)

    combined_schema_path.unlink()


def update_query(endpoint: Path) -> None:
    name = endpoint.name
    request_folder = endpoint / "request"
    file = next(request_folder.glob("*.json"), None)

    # The provider API lookup doesn't have a regular request because it uses a different
    # API.
    if not file:
        return

    file_content = json.loads(file.read_text())
    output_file = JUST_SCRAPE_DIR / f"wrappers/{name}_/query.py"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(f'# ruff: noqa: E501\nQUERY="""{file_content["query"]}"""')


def update_all_schemas() -> None:
    for endpoint in SCHEMA_DIR.glob("*"):
        if endpoint.is_dir():
            update_response(endpoint)
            update_request(endpoint)
            update_query(endpoint)


if __name__ == "__main__":
    update_all_schemas()
