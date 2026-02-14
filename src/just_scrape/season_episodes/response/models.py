# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Package(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    clear_name: str = Field(..., alias="clearName")
    package_id: int = Field(..., alias="packageId")
    field__typename: str = Field(..., alias="__typename")


class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class FreeItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    title: str
    short_description: str = Field(..., alias="shortDescription")
    episode_number: int = Field(..., alias="episodeNumber")
    season_number: int = Field(..., alias="seasonNumber")
    is_released: bool = Field(..., alias="isReleased")
    runtime: int
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")


class Episode(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    object_id: int = Field(..., alias="objectId")
    object_type: str = Field(..., alias="objectType")
    seenlist_entry: None = Field(..., alias="seenlistEntry")
    unique_offer_count: int = Field(..., alias="uniqueOfferCount")
    flatrate: list[FlatrateItem]
    buy: list[None]
    rent: list[None]
    free: list[FreeItem]
    fast: list[None]
    content: Content
    field__typename: str = Field(..., alias="__typename")


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    field__typename: str = Field(..., alias="__typename")
    episodes: list[Episode]


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    node: Node


class Variables(BaseModel):
    model_config = ConfigDict(extra="forbid")
    platform: str
    country: str
    language: str
    limit: int
    node_id: str = Field(..., alias="nodeId")
    offset: int


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


class SeasonEpisodesResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
