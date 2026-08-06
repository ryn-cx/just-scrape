# TODO: Validate
"""Exceptions."""


class JustScrapeError(Exception):
    """Base exception for just-scrape library."""


class HTTPError(JustScrapeError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(self, status_code: int, body: str) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.body = body
        super().__init__(f"Unexpected response status code: {status_code}\n{body}")


class GraphQLError(JustScrapeError):
    """Raised when GraphQL API returns an error response."""
