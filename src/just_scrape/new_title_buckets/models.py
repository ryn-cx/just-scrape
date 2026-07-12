# TODO: Validate
# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from datetime import date as date_aliased

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    has_next_page: bool = Field(..., alias="hasNextPage")
    field__typename: str = Field(..., alias="__typename")


class Package(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    package_id: int = Field(..., alias="packageId")
    short_name: str = Field(..., alias="shortName")
    icon: str
    field__typename: str = Field(..., alias="__typename")


class Key(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field__typename: str = Field(..., alias="__typename")
    date: date_aliased
    package: Package


class PageInfo1(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    start_cursor: str = Field(..., alias="startCursor")
    end_cursor: str = Field(..., alias="endCursor")
    has_next_page: bool = Field(..., alias="hasNextPage")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    field__typename: str = Field(..., alias="__typename")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    total_count: int = Field(..., alias="totalCount")
    page_info: PageInfo1 = Field(..., alias="pageInfo")
    field__typename: str = Field(..., alias="__typename")


class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    key: Key
    node: Node
    field__typename: str = Field(..., alias="__typename")


class NewTitleBuckets(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: list[Edge]
    field__typename: str = Field(..., alias="__typename")


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    new_title_buckets: NewTitleBuckets = Field(..., alias="newTitleBuckets")


class NewTitlesFilter(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    age_certifications: list[None] = Field(..., alias="ageCertifications")
    exclude_genres: list[None] = Field(..., alias="excludeGenres")
    exclude_production_countries: list[None] = Field(
        ...,
        alias="excludeProductionCountries",
    )
    object_types: list[None] = Field(..., alias="objectTypes")
    production_countries: list[None] = Field(..., alias="productionCountries")
    subgenres: list[None]
    genres: list[None]
    packages: list[None]
    exclude_irrelevant_titles: bool = Field(..., alias="excludeIrrelevantTitles")
    presentation_types: list[None] = Field(..., alias="presentationTypes")
    monetization_types: list[None] = Field(..., alias="monetizationTypes")


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    first: int
    bucket_size: int = Field(..., alias="bucketSize")
    group_by: str = Field(..., alias="groupBy")
    page_type: str = Field(..., alias="pageType")
    country: str
    new_after_cursor: str = Field(..., alias="newAfterCursor")
    new_titles_filter: NewTitlesFilter = Field(..., alias="newTitlesFilter")
    price_drops: bool = Field(..., alias="priceDrops")


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


class NewTitleBucketsResponse(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
