<div align="center">

# 🎬 Just Scrape

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/ryn-cx/just-scrape/refs/heads/master/pyproject.toml)
![GitHub License](https://img.shields.io/github/license/ryn-cx/just-scrape)
![GitHub Issues](https://img.shields.io/github/issues/ryn-cx/just-scrape)

**An unofficial Python API client for JustWatch**

</div>

## ✨ Features

- 🛡️ **Type Safety**: Full Pydantic models for every endpoint
- 🔄 **Dynamically Updating Models**: Models are dynamically updated based on the response from the API

## 📦 Installation

### Requirements

- 🐍 Python 3.13 or higher

### Install from source

```bash
uv add git+https://github.com/ryn-cx/just-scrape
```

## 🚀 Quick Start

### Create Client

```python
from just_scrape import JustScrape

# 🌐 Create client
client = JustScrape()
```

### Access API

```python
# 🆕 Get new titles
new_titles = client.get_new_titles()

# 📺 Get title details by URL
title_details = client.get_url_title_details(full_path="/us/movie/the-thursday-murder-club")

# 📋 Get season episodes
episodes = client.get_season_episodes(node_id="tss337460")

# 🎬 Get buy box offers
offers = client.get_buy_box_offers(node_id="tse9298997")

# 🗂️ Get new title buckets
buckets = client.get_new_title_buckets()
```
