# ruff: noqa: D100, D101
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Content(BaseModel):
    model_config = ConfigDict(extra="forbid")
    articles: list[None]
    field__typename: str = Field(..., alias="__typename")


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    content: Content
    field__typename: str = Field(..., alias="__typename")


class UrlV2(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    node: Node
    field__typename: str = Field(..., alias="__typename")


class Data(BaseModel):
    model_config = ConfigDict(extra="forbid")
    url_v2: UrlV2 = Field(..., alias="urlV2")


class Variables(BaseModel):
    model_config = ConfigDict(extra="forbid")
    full_path: str = Field(..., alias="fullPath")
    language: str
    country: str


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


class TitleDetailArticleResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: Data
    just_scrape: JustScrape
