# TODO: Validate
# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class Package(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    clear_name: str = Field(..., alias="clearName")
    package_id: int = Field(..., alias="packageId")
    field__typename: str = Field(..., alias="__typename")


class FlatrateItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class FreeItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package: Package
    field__typename: str = Field(..., alias="__typename")


class Content(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    title: str
    short_description: str = Field(..., alias="shortDescription")
    episode_number: int = Field(..., alias="episodeNumber")
    season_number: int = Field(..., alias="seasonNumber")
    is_released: bool = Field(..., alias="isReleased")
    runtime: int
    upcoming_releases: list[None] = Field(..., alias="upcomingReleases")


class Episode(GAPIBaseModel):
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


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    field__typename: str = Field(..., alias="__typename")
    episodes: list[Episode]


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    node: Node


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    platform: str
    country: str
    language: str
    limit: int
    node_id: str = Field(..., alias="nodeId")
    offset: int


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    user_agent: str = Field(..., alias="User-Agent")
    referer: str = Field(..., alias="Referer")
    origin: str = Field(..., alias="Origin")


class JustScrape(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    variables: Variables
    operation_name: str = Field(..., alias="operationName")
    headers: Headers
    timestamp: AwareDatetime


class SeasonEpisodesResponse(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
