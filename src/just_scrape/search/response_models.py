# ruff: noqa: COM812, D100, D101
from __future__ import annotations

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Genre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    short_name: str = Field(..., alias="shortName")
    field__typename: str = Field(..., alias="__typename")


class Scoring(BaseModel):
    model_config = ConfigDict(extra="forbid")
    imdb_score: float | None = Field(..., alias="imdbScore")
    imdb_votes: int | None = Field(..., alias="imdbVotes")
    tmdb_score: int | float | None = Field(..., alias="tmdbScore")
    tmdb_popularity: float = Field(..., alias="tmdbPopularity")
    tomato_meter: int | None = Field(..., alias="tomatoMeter")
    certified_fresh: bool | None = Field(..., alias="certifiedFresh")
    field__typename: str = Field(..., alias="__typename")


class Backdrop(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backdrop_url: str = Field(..., alias="backdropUrl")
    field__typename: str = Field(..., alias="__typename")


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    full_path: str = Field(..., alias="fullPath")
    original_release_year: int = Field(..., alias="originalReleaseYear")
    genres: list[Genre]
    scoring: Scoring
    poster_url: str = Field(..., alias="posterUrl")
    backdrops: list[Backdrop]
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")
    field__typename: str = Field(..., alias="__typename")


class WatchNowOffer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    field__typename: str = Field(..., alias="__typename")


class Package(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    short_name: str = Field(..., alias="shortName")
    field__typename: str = Field(..., alias="__typename")


class Offer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    monetization_type: str = Field(..., alias="monetizationType")
    presentation_type: str = Field(..., alias="presentationType")
    standard_web_url: str = Field(..., alias="standardWebURL")
    pre_affiliated_standard_web_url: None = Field(
        ..., alias="preAffiliatedStandardWebURL"
    )
    package: Package
    id: str
    field__typename: str = Field(..., alias="__typename")


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    content: Content
    watch_now_offer: WatchNowOffer | None = Field(..., alias="watchNowOffer")
    offers: list[Offer]


class Edge(BaseModel):
    model_config = ConfigDict(extra="forbid")
    cursor: str
    node: Node
    field__typename: str = Field(..., alias="__typename")


class PageInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    has_next_page: bool = Field(..., alias="hasNextPage")
    field__typename: str = Field(..., alias="__typename")


class SearchTitles(BaseModel):
    model_config = ConfigDict(extra="forbid")
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias="pageInfo")
    total_count: int = Field(..., alias="totalCount")
    field__typename: str = Field(..., alias="__typename")


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    search_titles: SearchTitles = Field(..., alias="searchTitles")


class SearchTitlesFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")
    search_query: str = Field(..., alias="searchQuery")
    person_id: None = Field(..., alias="personId")
    include_titles_without_url: bool = Field(..., alias="includeTitlesWithoutUrl")


class Variables(BaseModel):
    model_config = ConfigDict(extra="forbid")
    first: int
    search_titles_sort_by: str = Field(..., alias="searchTitlesSortBy")
    sort_random_seed: int = Field(..., alias="sortRandomSeed")
    search_after_cursor: str = Field(..., alias="searchAfterCursor")
    search_titles_filter: SearchTitlesFilter = Field(..., alias="searchTitlesFilter")
    language: str
    country: str
    location: str


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    referer: str = Field(..., alias="Referer")
    origin: str = Field(..., alias="Origin")


class JustScrape(BaseModel):
    model_config = ConfigDict(extra="forbid")
    variables: Variables
    operation_name: str = Field(..., alias="operationName")
    headers: Headers
    timestamp: AwareDatetime


class SearchResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
