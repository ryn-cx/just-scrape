# TODO: Validate
import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> JustScrape:
    return JustScrape(build_client_automatically())
