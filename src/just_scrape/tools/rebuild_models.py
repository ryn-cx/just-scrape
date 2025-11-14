from gapi import update_json_schema_and_pydantic_model

from just_scrape.constants import FILES_PATH, JUST_SCRAPE_PATH

if __name__ == "__main__":
    for endpoint_name in FILES_PATH.iterdir():
        if endpoint_name.name == ".git":
            continue

        name = endpoint_name.name
        for endpoint_type in endpoint_name.iterdir():
            schema_path = JUST_SCRAPE_PATH / f"{name}/{endpoint_type.name}.schema.json"
            model_path = JUST_SCRAPE_PATH / f"{name}/{endpoint_type.name}.py"

            schema_path.unlink(missing_ok=True)
            model_path.unlink(missing_ok=True)

            json_files = list(endpoint_type.glob("*.json"))
            update_json_schema_and_pydantic_model(
                json_files,
                schema_path,
                model_path,
                name,
            )
