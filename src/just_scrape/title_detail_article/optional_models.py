from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    articles: list[Any] | None = None
    field__typename: str | None = Field(None, alias='__typename')

class Node(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    content: Content | None = None
    field__typename: str | None = Field(None, alias='__typename')

class TitleDetailArticleModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    node: Node | None = None
    field__typename: str | None = Field(None, alias='__typename')
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
