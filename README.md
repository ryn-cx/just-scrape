<!-- TODO: Validate -->
# just-scrape

Unofficial [JustWatch](https://www.justwatch.com/) API.

`just-scrape` wraps JustWatch's internal GraphQL API and parses its raw JSON into
typed [Pydantic](https://docs.pydantic.dev/) models, giving you a small, structured
API for reading data about movies, shows, seasons, episodes, and streaming offers.

## Installation

```bash
uv add git+https://github.com/ryn-cx/just-scrape
```

## Usage

Create a client, then call `get(...)` on an endpoint to download from JustWatch and
get back a parsed, typed model. Every endpoint also exposes `download(...)`, which
returns the raw JSON dict, and `parse(...)`, which turns that dict into a model.

```python
from just_scrape import JustScrape

client = JustScrape()

# Search for titles, by query string.
results = client.search.get("Breaking")

# Title details, by full URL path (the part after the domain).
movie = client.url_title_details.get("/us/movie/the-thursday-murder-club")
show = client.url_title_details.get("/us/tv-show/strip-law")

# The episodes in a season, by season node ID.
episodes = client.season_episodes.get("tss337460")

# Streaming/buy/rent offers for a title, by node ID.
offers = client.buy_box_offers.get("tse9298997")

# Newly released titles. Defaults to today; accepts filters.
new_titles = client.new_titles.get(
    filter_packages=["net"],
    available_to_packages=["net"],
)

# New titles grouped into buckets by date and package.
buckets = client.new_title_buckets.get()

# A title's editorial article, by full URL path.
article = client.title_detail_article.get("/us/movie/the-thursday-murder-club")
```

### Pagination helpers

Endpoints that page through results offer `get_all*` methods that follow the
cursors for you, plus `extract_*` helpers that flatten the pages into a single list.

```python
from datetime import date, timedelta

# Every episode in a season, across all pages.
pages = client.season_episodes.get_all("tss23744")
episodes = client.season_episodes.extract_episodes(pages)

# Every new title on a given date.
pages = client.new_titles.get_all_for_date(date=date.today() - timedelta(days=1))
edges = client.new_titles.extract_edges(pages)

# Every new title from today back to a given end date.
pages = client.new_titles.get_all_since_date(end_date=date.today() - timedelta(days=7))
edges = client.new_titles.extract_edges(pages)

# Every new-title bucket back to a given date.
buckets = client.new_title_buckets.get_all_since_date(date.today() - timedelta(days=5))
edges = client.new_title_buckets.extract_edges(buckets)
```

### Endpoints

| Endpoint | Looked up by | Notes |
| --- | --- | --- |
| `client.search` | query string | Search for movies, shows, and people. |
| `client.url_title_details` | full URL path | Full details for a movie, show, or season. |
| `client.title_detail_article` | full URL path | Editorial article for a title. |
| `client.season_episodes` | season node ID | Episodes in a season. |
| `client.custom_season_episodes` | season node ID | Episodes with extra offer fields. |
| `client.buy_box_offers` | node ID | Streaming, buy, and rent offers. |
| `client.custom_buy_box_offers` | node ID | Offers with extra fields. |
| `client.new_titles` | date + filters | Newly released titles. |
| `client.new_title_buckets` | date + filters | New titles grouped into buckets. |

### Localization and filters

Most `get(...)` calls accept `country` (default `"US"`) and `language`
(default `"en"`) keyword arguments, and the new-titles endpoints accept a range of
`filter_*` arguments (genres, packages, monetization types, and so on). See each
endpoint's method signature for the full list of options.

