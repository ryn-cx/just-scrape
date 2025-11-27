from typing import TYPE_CHECKING, Any, Protocol

from gapi import GapiCustomizations
from pydantic import BaseModel

if TYPE_CHECKING:
    from .__init__ import RESPONSE_MODELS


class JustWatchProtocol(Protocol):
    def _graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: BaseModel,
    ) -> dict[str, Any]: ...

    def parse_response[T: "RESPONSE_MODELS"](
        self,
        response_model: type[T],
        response: dict[str, Any],
        name: str,
        customizations: GapiCustomizations | None = None,
    ) -> T: ...
