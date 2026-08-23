<!-- TODO: Validate -->
# just-scrape

Unofficial [JustWatch](https://www.justwatch.com/) API wrapper built using [Good Ass
Pydantic Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and
[Get Around](https://github.com/ryn-cx/get-around).

## Installation

```bash
uv add git+https://github.com/ryn-cx/just-scrape
```

## Usage

Every endpoint is called to get the parsed model, and splits into `download()` (the
response as text) and `load()` (that text read into the model).

```python
from datetime import date

from just_scrape import JustScrape

client = JustScrape()

search = client.search("Frieren")
title = client.url_title_details("/us/movie/the-thursday-murder-club")
article = client.title_detail_article("/us/movie/the-thursday-murder-club")
episodes = client.season_episodes("tss486285")
offers = client.episode_offers("tse1126259")
new_titles = client.new_titles(date=date(2026, 8, 1))
buckets = client.new_title_buckets(filter_object_types=["MOVIE"])

downloaded = client.search.download("Frieren")
search = client.search.load(downloaded)
```

Every call takes the API's own parameters as keyword arguments with the site's own
defaults, including `country` (default `"US"`) and `language` (default `"en"`).

### Endpoints

| Endpoint | Looked up by | Gives back |
| --- | --- | --- |
| `client.search` | query string | Titles matching a search. |
| `client.url_title_details` | full URL path | One title, its offers and its seasons. |
| `client.title_detail_article` | full URL path | What has been written about a title. |
| `client.season_episodes` | season node ID | The episodes in one season. |
| `client.episode_offers` | node ID | Everywhere one episode can be watched. |
| `client.new_titles` | date + filters | What turned up on a date. |
| `client.new_title_buckets` | date + filters | What turned up, counted by date and service. |
