from pydantic import ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from typing import Any

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    short_name: str = Field(..., alias='shortName')
    field__typename: str = Field(..., alias='__typename')

class Scoring(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    imdb_score: float = Field(..., alias='imdbScore')
    imdb_votes: int | float = Field(..., alias='imdbVotes')
    tmdb_score: float | None = Field(..., alias='tmdbScore')
    tmdb_popularity: float = Field(..., alias='tmdbPopularity')
    tomato_meter: int | None = Field(..., alias='tomatoMeter')
    certified_fresh: bool | None = Field(..., alias='certifiedFresh')
    field__typename: str = Field(..., alias='__typename')

class Backdrop(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    backdrop_url: str = Field(..., alias='backdropUrl')
    field__typename: str = Field(..., alias='__typename')

class Content(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    full_path: str = Field(..., alias='fullPath')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    genres: list[Genre]
    scoring: Scoring
    poster_url: str | None = Field(..., alias='posterUrl')
    backdrops: list[Backdrop]
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    field__typename: str = Field(..., alias='__typename')

class WatchNowOffer(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    field__typename: str = Field(..., alias='__typename')

class Package(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    package_id: int = Field(..., alias='packageId')
    short_name: str = Field(..., alias='shortName')
    field__typename: str = Field(..., alias='__typename')

class Offer(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    monetization_type: str = Field(..., alias='monetizationType')
    presentation_type: str = Field(..., alias='presentationType')
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    package: Package
    id: str
    field__typename: str = Field(..., alias='__typename')

class Node(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field__typename: str = Field(..., alias='__typename')
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    content: Content
    watch_now_offer: WatchNowOffer | None = Field(..., alias='watchNowOffer')
    offers: list[Offer]

class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    cursor: str
    node: Node
    field__typename: str = Field(..., alias='__typename')

class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    start_cursor: str = Field(..., alias='startCursor')
    end_cursor: str = Field(..., alias='endCursor')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    has_next_page: bool = Field(..., alias='hasNextPage')
    field__typename: str = Field(..., alias='__typename')

class SearchTitles(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')
    total_count: int = Field(..., alias='totalCount')
    field__typename: str = Field(..., alias='__typename')

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    search_titles: SearchTitles = Field(..., alias='searchTitles')

class SearchResponse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data
