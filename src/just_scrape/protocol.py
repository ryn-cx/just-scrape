from typing import Any, Protocol

from pydantic import BaseModel


class JustWatchProtocol(Protocol):
    def _graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: BaseModel,
    ) -> dict[str, Any]: ...

    def _parse_response[T: BaseModel](
        self,
        response_model: type[T],
        response: dict[str, Any],
        name: str,
    ) -> T: ...
