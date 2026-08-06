from pydantic import ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from datetime import date as date_aliased

class PageInfo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    start_cursor: str = Field(..., alias='startCursor')
    end_cursor: str = Field(..., alias='endCursor')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    has_next_page: bool = Field(..., alias='hasNextPage')
    field__typename: str = Field(..., alias='__typename')

class Package(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    package_id: int = Field(..., alias='packageId')
    short_name: str = Field(..., alias='shortName')
    icon: str
    field__typename: str = Field(..., alias='__typename')

class Key(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field__typename: str = Field(..., alias='__typename')
    date: date_aliased
    package: Package

class PageInfo1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    start_cursor: str = Field(..., alias='startCursor')
    end_cursor: str = Field(..., alias='endCursor')
    has_next_page: bool = Field(..., alias='hasNextPage')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    field__typename: str = Field(..., alias='__typename')

class Node(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total_count: int = Field(..., alias='totalCount')
    page_info: PageInfo1 = Field(..., alias='pageInfo')
    field__typename: str = Field(..., alias='__typename')

class Edge(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    key: Key
    node: Node
    field__typename: str = Field(..., alias='__typename')

class NewTitleBuckets(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    page_info: PageInfo = Field(..., alias='pageInfo')
    edges: list[Edge]
    field__typename: str = Field(..., alias='__typename')

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    new_title_buckets: NewTitleBuckets = Field(..., alias='newTitleBuckets')

class NewTitleBucketsResponse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data
