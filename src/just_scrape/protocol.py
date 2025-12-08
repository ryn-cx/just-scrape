from typing import Any, Protocol

from gapi import GapiCustomizations
from pydantic import BaseModel


class JustWatchProtocol(Protocol):
    def _download_graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: BaseModel,
    ) -> dict[str, Any]: ...

    def parse_response[T: BaseModel](
        self,
        response_model: type[T],
        data: dict[str, Any],
        name: str,
        customizations: GapiCustomizations | None = None,
    ) -> T: ...
