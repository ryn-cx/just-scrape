# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class JustScrapeError(Exception):
    """Base exception for JustScrape."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(JustScrapeError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class GraphQLError(JustScrapeError):
    """Raised when the API answers with errors instead of the data asked for."""

    # TODO: Validate
    def __init__(
        self,
        errors: list[dict[str, Any]],
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the errors and the whole response body.

        The whole body is kept because GraphQL answers with `errors` and `data`
        together, so a response that failed on one field can still carry usable
        data for every other field.
        """
        self.errors = errors
        self.response = response
        super().__init__(f"GraphQL errors occurred: {errors}")


# TODO: Validate
class ResourceNotFoundError(GraphQLError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class EpisodeNotFoundError(ResourceNotFoundError):
    """Raised when the requested episode does not exist."""

    # TODO: Validate
    def __init__(
        self,
        node_id: str,
        errors: list[dict[str, Any]],
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the episode node id and the originating response."""
        self.node_id = node_id
        super().__init__(errors, response)


# TODO: Validate
class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season does not exist."""

    # TODO: Validate
    def __init__(
        self,
        node_id: str,
        errors: list[dict[str, Any]],
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the season node id and the originating response."""
        self.node_id = node_id
        super().__init__(errors, response)


# TODO: Validate
class TitleNotFoundError(ResourceNotFoundError):
    """Raised when no title sits at the requested path."""

    # TODO: Validate
    def __init__(
        self,
        full_path: str,
        errors: list[dict[str, Any]],
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the requested path and the originating response."""
        self.full_path = full_path
        super().__init__(errors, response)


# TODO: Validate
class ArticleNotFoundError(ResourceNotFoundError):
    """Raised when no title to write about sits at the requested path."""

    # TODO: Validate
    def __init__(
        self,
        full_path: str,
        errors: list[dict[str, Any]],
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the requested path and the originating response."""
        self.full_path = full_path
        super().__init__(errors, response)


# TODO: Validate
class InvalidFileError(JustScrapeError):
    """Raised when a downloaded file does not match what was requested."""

    # TODO: Validate
    def __init__(
        self,
        field: str,
        expected: object = None,
        *,
        response: str | dict[str, Any] | None = None,
    ) -> None:
        """Initialize with the field, its expected value and the response.

        `expected` is left out when the check is only that the field has a value.
        """
        self.field = field
        self.expected = expected
        self.response = response
        if expected is None:
            super().__init__(f"Downloaded file has no {field}")
        else:
            super().__init__(f"Downloaded file is not for {field} {expected!r}")
