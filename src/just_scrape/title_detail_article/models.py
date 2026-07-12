# TODO: Validate
# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class Content(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    articles: list[None]
    field__typename: str = Field(..., alias="__typename")


class Node(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    content: Content
    field__typename: str = Field(..., alias="__typename")


class UrlV2(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    node: Node
    field__typename: str = Field(..., alias="__typename")


class Data(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    url_v2: UrlV2 = Field(..., alias="urlV2")


class Variables(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    full_path: str = Field(..., alias="fullPath")
    language: str
    country: str


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


class TitleDetailArticleResponse(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
