import json
from pathlib import Path

import datamodel_code_generator
from datamodel_code_generator.format import Formatter

from just_scrape.constants import JUST_SCRAPE_DIR, TEST_FILE_DIR


def combine_json_files(input_folder: Path) -> str:
    input_files = input_folder.glob("*.json")
    input_contents = [file.read_text() for file in input_files]
    input_parsed = [json.loads(content) for content in input_contents]
    return json.dumps(input_parsed)


def generate_schema(input_data: str, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    datamodel_code_generator.generate(
        input_=input_data,
        output=output_file,
        input_file_type=datamodel_code_generator.InputFileType.Json,
        output_model_type=datamodel_code_generator.DataModelType.PydanticV2BaseModel,
        snake_case_field=True,
        disable_timestamp=True,
        extra_fields="forbid",
        formatters=[Formatter.RUFF_CHECK, Formatter.RUFF_FORMAT],
        target_python_version=datamodel_code_generator.PythonVersion.PY_313,
    )

    # Remove the last 3 lines which will contain the extra wrapper class used to combine
    # files into a single json file which is not actually used by the API
    lines = output_file.read_text().splitlines()
    lines = "\n".join(lines[:-3])

    output_file.write_text(lines)


def update_response(endpoint: Path) -> None:
    response_input_dumped = combine_json_files(endpoint / "response")
    output_schema = JUST_SCRAPE_DIR / f"models/response/{endpoint.name}.py"
    generate_schema(response_input_dumped, output_schema)


def update_request(endpoint: Path) -> None:
    request_input_dumped = combine_json_files(endpoint / "request")
    output_schema = JUST_SCRAPE_DIR / f"models/request/{endpoint.name}.py"
    generate_schema(request_input_dumped, output_schema)


def update_query(endpoint: Path) -> None:
    name = endpoint.name
    request_folder = endpoint / "request"
    first_file = next(request_folder.glob("*.json"))
    file_content = json.loads(first_file.read_text())
    output_file = JUST_SCRAPE_DIR / f"queries/{name}.py"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(f'# ruff: noqa: E501\nQUERY="""{file_content["query"]}"""')


def update_all_schemas() -> None:
    for endpoint in TEST_FILE_DIR.glob("*"):
        if endpoint.is_dir():
            update_response(endpoint)
            update_request(endpoint)
            update_query(endpoint)


if __name__ == "__main__":
    update_all_schemas()
