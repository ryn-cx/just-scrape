from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Scoring(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    imdb_score: float | Any = Field(None, alias='imdbScore', union_mode='left_to_right')
    imdb_votes: int | Any = Field(None, alias='imdbVotes', union_mode='left_to_right')
    tmdb_score: int | float | Any = Field(None, alias='tmdbScore', union_mode='left_to_right')
    tmdb_popularity: float | Any = Field(None, alias='tmdbPopularity', union_mode='left_to_right')
    tomato_meter: int | Any = Field(None, alias='tomatoMeter', union_mode='left_to_right')
    certified_fresh: Any | None = Field(None, alias='certifiedFresh')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Backdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrop_url: str | Any = Field(None, alias='backdropUrl', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    full_path: str | Any = Field(None, alias='fullPath', union_mode='left_to_right')
    original_release_year: int | Any = Field(None, alias='originalReleaseYear', union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    scoring: Scoring | Any = Field(default=None, union_mode='left_to_right')
    poster_url: str | Any = Field(None, alias='posterUrl', union_mode='left_to_right')
    backdrops: list[Backdrop] | Any = Field(default=None, union_mode='left_to_right')
    upcoming_releases: list[Any] | Any = Field(None, alias='upcomingReleases', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class WatchNowOffer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Package(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    package_id: int | Any = Field(None, alias='packageId', union_mode='left_to_right')
    short_name: str | Any = Field(None, alias='shortName', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Offer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    monetization_type: str | Any = Field(None, alias='monetizationType', union_mode='left_to_right')
    presentation_type: str | Any = Field(None, alias='presentationType', union_mode='left_to_right')
    standard_web_url: str | Any = Field(None, alias='standardWebURL', union_mode='left_to_right')
    pre_affiliated_standard_web_url: Any | None = Field(None, alias='preAffiliatedStandardWebURL')
    package: Package | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    object_id: int | Any = Field(None, alias='objectId', union_mode='left_to_right')
    object_type: str | Any = Field(None, alias='objectType', union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    watch_now_offer: WatchNowOffer | Any = Field(None, alias='watchNowOffer', union_mode='left_to_right')
    offers: list[Offer] | Any = Field(default=None, union_mode='left_to_right')

class Edge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cursor: str | Any = Field(default=None, union_mode='left_to_right')
    node: Node | Any = Field(default=None, union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class PageInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_cursor: str | Any = Field(None, alias='startCursor', union_mode='left_to_right')
    end_cursor: str | Any = Field(None, alias='endCursor', union_mode='left_to_right')
    has_previous_page: bool | Any = Field(None, alias='hasPreviousPage', union_mode='left_to_right')
    has_next_page: bool | Any = Field(None, alias='hasNextPage', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    edges: list[Edge] | Any = Field(default=None, union_mode='left_to_right')
    page_info: PageInfo | Any = Field(None, alias='pageInfo', union_mode='left_to_right')
    total_count: int | Any = Field(None, alias='totalCount', union_mode='left_to_right')
    field__typename: str | Any = Field(None, alias='__typename', union_mode='left_to_right')
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
