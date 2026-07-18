import pytest
from get_around import build_client_automatically

from just_scrape import JustScrape


@pytest.fixture(scope="session")
def client() -> JustScrape:
    return JustScrape(get_around_client=build_client_automatically())
