<div align="center">

# Just Scrape

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/ryn-cx/just-scrape/refs/heads/master/pyproject.toml)
![GitHub License](https://img.shields.io/github/license/ryn-cx/just-scrape)
![GitHub Issues](https://img.shields.io/github/issues/ryn-cx/just-scrape)

**An unofficial Python API client for JustWatch**

</div>

## Features

- **Type Safety** - Full Pydantic models for every endpoint with robust data validation
- **Self-Updating Models** - Models are automatically updated when the API response structure changes

## Installation

Requires Python 3.13+

```bash
uv add git+https://github.com/ryn-cx/just-scrape
```

## Quick Start

```python
from just_scrape import JustScrape

client = JustScrape()
```

### URL Title Details

```python
title_details = client.url_title_details.get(full_path="/us/movie/the-thursday-murder-club")
```

### Buy Box Offers

```python
offers = client.buy_box_offers.get(node_id="tse9298997")
```

### New Titles

```python
new_titles = client.new_titles.get(filter_packages=["net"], available_to_packages=["net"])
```

### New Title Buckets

```python
buckets = client.new_title_buckets.get()
```

### Season Episodes

```python
episodes = client.season_episodes.get(node_id="tss337460")
```

### Title Detail Article

```python
article = client.title_detail_article.get(full_path="/us/movie/the-thursday-murder-club")
```

## Two-Step API

Every endpoint supports a two-step `download()` / `parse()` workflow for cases where you want to inspect or cache the raw JSON before parsing:

```python
raw = client.url_title_details.download(full_path="/us/movie/the-thursday-murder-club")
parsed = client.url_title_details.parse(raw)

raw = client.buy_box_offers.download(node_id="tse9298997")
parsed = client.buy_box_offers.parse(raw)
```
