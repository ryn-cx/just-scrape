from typing import Any, Protocol

from pydantic import BaseModel


class JustWatchProtocol(Protocol):
    def graphql_request(
        self,
        operation_name: str,
        query: str,
        variables: dict[str, Any],
    ) -> dict[str, Any]: ...

    def parse_response[T: BaseModel](
        self,
        response_model: type[T],
        data: dict[str, Any],
        name: str,
    ) -> T: ...
