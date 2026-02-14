# ruff: noqa: COM812, TC003, D100, D101
from __future__ import annotations

from datetime import date as date_aliased

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Package(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    icon: str
    package_id: int = Field(..., alias="packageId")
    clear_name: str = Field(..., alias="clearName")
    short_name: str = Field(..., alias="shortName")
    technical_name: str = Field(..., alias="technicalName")
    icon_wide: str = Field(..., alias="iconWide")
    has_rectangular_icon: bool = Field(..., alias="hasRectangularIcon")
    field__typename: str = Field(..., alias="__typename")


class NewOffer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    stream_url: None = Field(..., alias="streamUrl")
    stream_url_external_player: None = Field(..., alias="streamUrlExternalPlayer")
    package: Package
    retail_price: None = Field(..., alias="retailPrice")
    retail_price_value: None = Field(..., alias="retailPriceValue")
    last_change_retail_price_value: None = Field(
        ..., alias="lastChangeRetailPriceValue"
    )
    currency: str
    presentation_type: str = Field(..., alias="presentationType")
    monetization_type: str = Field(..., alias="monetizationType")
    available_to: date_aliased | None = Field(..., alias="availableTo")
    date_created: date_aliased = Field(..., alias="dateCreated")
    new_element_count: int = Field(..., alias="newElementCount")
    last_change_retail_price: None = Field(..., alias="lastChangeRetailPrice")
    last_change_percent: int = Field(..., alias="lastChangePercent")


class Scoring(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_votes: int | float | None = Field(..., alias="imdbVotes")
    imdb_score: int | float | None = Field(..., alias="imdbScore")
    tmdb_popularity: float | None = Field(..., alias="tmdbPopularity")
    tmdb_score: int | float | None = Field(..., alias="tmdbScore")
    tomato_meter: int | None = Field(..., alias="tomatoMeter")
    certified_fresh: bool | None = Field(..., alias="certifiedFresh")
    field__typename: str = Field(..., alias="__typename")


class Genre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    translation: str
    field__typename: str = Field(..., alias="__typename")


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    short_description: str = Field(..., alias="shortDescription")
    full_path: str = Field(..., alias="fullPath")
    scoring: Scoring
    poster_url: str | None = Field(..., alias="posterUrl")
    runtime: int
    genres: list[Genre]
    is_released: bool = Field(..., alias="isReleased")
    field__typename: str = Field(..., alias="__typename")
    season_number: int | None = Field(None, alias="seasonNumber")


class Scoring1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_votes: int | None = Field(..., alias="imdbVotes")
    imdb_score: int | float | None = Field(..., alias="imdbScore")
    tmdb_popularity: float = Field(..., alias="tmdbPopularity")
    tmdb_score: int | float | None = Field(..., alias="tmdbScore")
    field__typename: str = Field(..., alias="__typename")


class Content1(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    short_description: str = Field(..., alias="shortDescription")
    full_path: str = Field(..., alias="fullPath")
    scoring: Scoring1
    poster_url: str | None = Field(..., alias="posterUrl")
    runtime: int
    genres: list[Genre]
    field__typename: str = Field(..., alias="__typename")


class SeenState(BaseModel):
    model_config = ConfigDict(extra="forbid")
    progress: int
    field__typename: str = Field(..., alias="__typename")


class Show(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    content: Content1
    likelist_entry: None = Field(..., alias="likelistEntry")
    dislikelist_entry: None = Field(..., alias="dislikelistEntry")
    watchlist_entry_v2: None = Field(..., alias="watchlistEntryV2")
    seen_state: SeenState = Field(..., alias="seenState")


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    content: Content
    likelist_entry: None = Field(..., alias="likelistEntry")
    dislikelist_entry: None = Field(..., alias="dislikelistEntry")
    seenlist_entry: None = Field(None, alias="seenlistEntry")
    watchlist_entry_v2: None = Field(None, alias="watchlistEntryV2")
    show: Show | None = None


class Edge(BaseModel):
    model_config = ConfigDict(extra="forbid")
    cursor: str
    new_offer: NewOffer = Field(..., alias="newOffer")
    node: Node
    field__typename: str = Field(..., alias="__typename")


class PageInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    end_cursor: str = Field(..., alias="endCursor")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    has_next_page: bool = Field(..., alias="hasNextPage")
    field__typename: str = Field(..., alias="__typename")


class NewTitles(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")
    field__typename: str = Field(..., alias="__typename")


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    new_titles: NewTitles = Field(..., alias="newTitles")


class Filter(BaseModel):
    model_config = ConfigDict(extra="forbid")
    age_certifications: list[None] = Field(..., alias="ageCertifications")
    exclude_genres: list[None] = Field(..., alias="excludeGenres")
    exclude_production_countries: list[None] = Field(
        ..., alias="excludeProductionCountries"
    )
    object_types: list[None] = Field(..., alias="objectTypes")
    production_countries: list[None] = Field(..., alias="productionCountries")
    subgenres: list[None]
    genres: list[None]
    packages: list[str]
    exclude_irrelevant_titles: bool = Field(..., alias="excludeIrrelevantTitles")
    presentation_types: list[None] = Field(..., alias="presentationTypes")
    monetization_types: list[None] = Field(..., alias="monetizationTypes")


class Variables(BaseModel):
    model_config = ConfigDict(extra="forbid")
    first: int
    page_type: str = Field(..., alias="pageType")
    date: date_aliased
    filter: Filter
    language: str
    country: str
    price_drops: bool = Field(..., alias="priceDrops")
    platform: str
    show_date_badge: bool = Field(..., alias="showDateBadge")
    available_to_packages: list[str] = Field(..., alias="availableToPackages")
    after: str | None


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    referer: str = Field(..., alias="Referer")
    origin: str = Field(..., alias="Origin")


class JustScrape(BaseModel):
    model_config = ConfigDict(extra="forbid")
    variables: Variables
    query: str
    operation_name: str = Field(..., alias="operationName")
    headers: Headers
    timestamp: AwareDatetime


class NewTitlesResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
