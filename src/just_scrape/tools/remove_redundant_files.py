from logging import getLogger

from gapi import remove_redundant_files

from just_scrape.constants import FILES_PATH

logger = getLogger(__name__)
if __name__ == "__main__":
    for endpoint_name in FILES_PATH.iterdir():
        if endpoint_name.name == ".git":
            continue

        for endpoint_type in endpoint_name.iterdir():
            json_files = list(endpoint_type.glob("*.json"))
            remove_redundant_files(json_files, logger=logger)
