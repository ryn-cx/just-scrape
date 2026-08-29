from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from typing import Any

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    short_name: str = Field(..., alias='shortName')
    field__typename: str = Field(..., alias='__typename')

class Scoring(BaseModel):
    model_config = ConfigDict(defer_build=True)
    imdb_score: float | None = Field(..., alias='imdbScore')
    imdb_votes: int | None = Field(..., alias='imdbVotes')
    tmdb_score: int | float | None = Field(..., alias='tmdbScore')
    tmdb_popularity: float | None = Field(..., alias='tmdbPopularity')
    tomato_meter: int | None = Field(..., alias='tomatoMeter')
    certified_fresh: None = Field(..., alias='certifiedFresh')
    field__typename: str = Field(..., alias='__typename')

class Backdrop(BaseModel):
    model_config = ConfigDict(defer_build=True)
    backdrop_url: str = Field(..., alias='backdropUrl')
    field__typename: str = Field(..., alias='__typename')

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    full_path: str = Field(..., alias='fullPath')
    original_release_year: int = Field(..., alias='originalReleaseYear')
    genres: list[Genre]
    scoring: Scoring
    poster_url: str | None = Field(..., alias='posterUrl')
    backdrops: list[Backdrop]
    upcoming_releases: list[None] = Field(..., alias='upcomingReleases')
    field__typename: str = Field(..., alias='__typename')

class WatchNowOffer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    field__typename: str = Field(..., alias='__typename')

class Package(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    package_id: int = Field(..., alias='packageId')
    short_name: str = Field(..., alias='shortName')
    field__typename: str = Field(..., alias='__typename')

class Offer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    monetization_type: str = Field(..., alias='monetizationType')
    presentation_type: str = Field(..., alias='presentationType')
    standard_web_url: str = Field(..., alias='standardWebURL')
    pre_affiliated_standard_web_url: None = Field(..., alias='preAffiliatedStandardWebURL')
    package: Package
    id: str
    field__typename: str = Field(..., alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__typename: str = Field(..., alias='__typename')
    id: str
    object_id: int = Field(..., alias='objectId')
    object_type: str = Field(..., alias='objectType')
    content: Content
    watch_now_offer: WatchNowOffer | None = Field(..., alias='watchNowOffer')
    offers: list[Offer]

class Edge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cursor: str
    node: Node
    field__typename: str = Field(..., alias='__typename')

class PageInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_cursor: str = Field(..., alias='startCursor')
    end_cursor: str = Field(..., alias='endCursor')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    has_next_page: bool = Field(..., alias='hasNextPage')
    field__typename: str = Field(..., alias='__typename')

class SearchTitles(BaseModel):
    model_config = ConfigDict(defer_build=True)
    edges: list[Edge]
    page_info: PageInfo = Field(..., alias='pageInfo')
    total_count: int = Field(..., alias='totalCount')
    field__typename: str = Field(..., alias='__typename')

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    search_titles: SearchTitles = Field(..., alias='searchTitles')

class SearchModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: Data
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
