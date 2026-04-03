"""GraphQL query."""

# ruff: noqa: E501
QUERY = """query GetSearchTitles($country: Country!, $first: Int! = 5, $language: Language!, $searchAfterCursor: String, $searchTitlesFilter: TitleFilter, $searchTitlesSortBy: PopularTitlesSorting! = POPULAR, $sortRandomSeed: Int! = 0, $location: String!) {
  searchTitles(
    after: $searchAfterCursor
    country: $country
    filter: $searchTitlesFilter
    first: $first
    sortBy: $searchTitlesSortBy
    sortRandomSeed: $sortRandomSeed
    source: $location
  ) {
    edges {
      ...SearchTitleGraphql
      __typename
    }
    pageInfo {
      startCursor
      endCursor
      hasPreviousPage
      hasNextPage
      __typename
    }
    totalCount
    __typename
  }
}

fragment SearchTitleGraphql on TitleSearchResultEdge {
  cursor
  node {
    __typename
    id
    objectId
    objectType
    content(country: $country, language: $language) {
      title
      fullPath
      originalReleaseYear
      genres {
        shortName
        __typename
      }
      scoring {
        imdbScore
        imdbVotes
        tmdbScore
        tmdbPopularity
        tomatoMeter
        certifiedFresh
        __typename
      }
      posterUrl
      backdrops {
        backdropUrl
        __typename
      }
      upcomingReleases(releaseTypes: [DIGITAL]) {
        releaseDate
        __typename
      }
      __typename
    }
    watchNowOffer(country: $country, platform: WEB) {
      id
      standardWebURL
      preAffiliatedStandardWebURL
      __typename
    }
    offers(country: $country, platform: WEB, filter: {preAffiliate: true}) {
      monetizationType
      presentationType
      standardWebURL
      preAffiliatedStandardWebURL
      package {
        id
        packageId
        shortName
        __typename
      }
      id
      __typename
    }
  }
  __typename
}
"""
