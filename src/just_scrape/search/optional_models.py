from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short_name: str | None = Field(None, alias='shortName')
    field__typename: str | None = Field(None, alias='__typename')

class Scoring(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_score: float | None = Field(None, alias='imdbScore')
    imdb_votes: int | None = Field(None, alias='imdbVotes')
    tmdb_score: int | float | None = Field(None, alias='tmdbScore')
    tmdb_popularity: float | None = Field(None, alias='tmdbPopularity')
    tomato_meter: int | None = Field(None, alias='tomatoMeter')
    certified_fresh: Any | None = Field(None, alias='certifiedFresh')
    field__typename: str | None = Field(None, alias='__typename')

class Backdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrop_url: str | None = Field(None, alias='backdropUrl')
    field__typename: str | None = Field(None, alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    full_path: str | None = Field(None, alias='fullPath')
    original_release_year: int | None = Field(None, alias='originalReleaseYear')
    genres: list[Genre] | None = None
    scoring: Scoring | None = None
    poster_url: str | None = Field(None, alias='posterUrl')
    backdrops: list[Backdrop] | None = None
    upcoming_releases: list[Any] | None = Field(None, alias='upcomingReleases')
    field__typename: str | None = Field(None, alias='__typename')

class WatchNowOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    field__typename: str | None = Field(None, alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    package_id: int | None = Field(None, alias='packageId')
    short_name: str | None = Field(None, alias='shortName')
    field__typename: str | None = Field(None, alias='__typename')

class Offer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    monetization_type: str | None = Field(None, alias='monetizationType')
    presentation_type: str | None = Field(None, alias='presentationType')
    standard_web_url: str | None = Field(None, alias='standardWebURL')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    package: Package | None = None
    id: str | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | None = Field(None, alias='__typename')
    id: str | None = None
    object_id: int | None = Field(None, alias='objectId')
    object_type: str | None = Field(None, alias='objectType')
    content: Content | None = None
    watch_now_offer: Any | WatchNowOffer | None = Field(None, alias='watchNowOffer')
    offers: list[Offer] | None = None

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cursor: str | None = None
    node: Node | None = None
    field__typename: str | None = Field(None, alias='__typename')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_cursor: str | None = Field(None, alias='startCursor')
    end_cursor: str | None = Field(None, alias='endCursor')
    has_previous_page: bool | None = Field(None, alias='hasPreviousPage')
    has_next_page: bool | None = Field(None, alias='hasNextPage')
    field__typename: str | None = Field(None, alias='__typename')

class SearchTitles(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    edges: list[Edge] | None = None
    page_info: PageInfo | None = Field(None, alias='pageInfo')
    total_count: int | None = Field(None, alias='totalCount')
    field__typename: str | None = Field(None, alias='__typename')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    search_titles: SearchTitles | None = Field(None, alias='searchTitles')

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: Data | None = None
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
