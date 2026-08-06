from typing import Any
from pydantic import ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel

class Content(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    articles: list[None]
    field__typename: str = Field(..., alias='__typename')

class Node(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    content: Content
    field__typename: str = Field(..., alias='__typename')

class UrlV2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    node: Node
    field__typename: str = Field(..., alias='__typename')

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url_v2: UrlV2 = Field(..., alias='urlV2')

class TitleDetailArticleResponse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data
