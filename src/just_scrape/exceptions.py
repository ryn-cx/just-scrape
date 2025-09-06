class JustScrapeError(Exception):
    """Base exception for just-scrape library."""


class HTTPError(JustScrapeError):
    """Raised when HTTP request fails with unexpected status code."""


class GraphQLError(JustScrapeError):
    """Raised when GraphQL API returns an error response."""
