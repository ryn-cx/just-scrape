# ruff: noqa: E501
QUERY = """query GetNewTitles($country: Country!, $date: Date!, $language: Language!, $filter: TitleFilter, $after: String, $first: Int! = 10, $profile: PosterProfile, $format: ImageFormat, $priceDrops: Boolean!, $platform: Platform!, $bucketType: NewDateRangeBucket, $pageType: NewPageType! = NEW, $showDateBadge: Boolean!, $availableToPackages: [String!]) {
  newTitles(
    country: $country
    date: $date
    filter: $filter
    after: $after
    first: $first
    priceDrops: $priceDrops
    bucketType: $bucketType
    pageType: $pageType
  ) {
    totalCount
    edges {
      ...NewTitleGraphql
      __typename
    }
    pageInfo {
      endCursor
      hasPreviousPage
      hasNextPage
      __typename
    }
    __typename
  }
}

fragment NewTitleGraphql on NewTitlesEdge {
  cursor
  newOffer(platform: $platform) {
    ...NewWatchNowOffer
    __typename
  }
  node {
    __typename
    ... on MovieOrSeason {
      id
      objectId
      objectType
      content(country: $country, language: $language) {
        title
        shortDescription
        fullPath
        scoring {
          imdbVotes
          imdbScore
          tmdbPopularity
          tmdbScore
          tomatoMeter
          certifiedFresh
          __typename
        }
        posterUrl(profile: $profile, format: $format)
        runtime
        genres {
          translation(language: $language)
          __typename
        }
        ... on SeasonContent {
          seasonNumber
          __typename
        }
        upcomingReleases @include(if: $showDateBadge) {
          releaseDate
          package {
            id
            shortName
            __typename
          }
          releaseCountDown(country: $country)
          __typename
        }
        isReleased
        __typename
      }
      availableTo(
        country: $country
        platform: $platform
        packages: $availableToPackages
      ) @include(if: $showDateBadge) {
        availableCountDown(country: $country)
        package {
          id
          shortName
          __typename
        }
        availableToDate
        __typename
      }
      ... on Movie {
        likelistEntry {
          createdAt
          __typename
        }
        dislikelistEntry {
          createdAt
          __typename
        }
        seenlistEntry {
          createdAt
          __typename
        }
        watchlistEntryV2 {
          createdAt
          __typename
        }
        __typename
      }
      ... on Season {
        likelistEntry {
          createdAt
          __typename
        }
        dislikelistEntry {
          createdAt
          __typename
        }
        show {
          __typename
          id
          objectId
          objectType
          content(country: $country, language: $language) {
            title
            shortDescription
            fullPath
            scoring {
              imdbVotes
              imdbScore
              tmdbPopularity
              tmdbScore
              __typename
            }
            posterUrl(profile: $profile, format: $format)
            runtime
            genres {
              translation(language: $language)
              __typename
            }
            __typename
          }
          likelistEntry {
            createdAt
            __typename
          }
          dislikelistEntry {
            createdAt
            __typename
          }
          watchlistEntryV2 {
            createdAt
            __typename
          }
          seenState(country: $country) {
            progress
            __typename
          }
        }
        __typename
      }
      __typename
    }
  }
  __typename
}

fragment NewWatchNowOffer on Offer {
  ...WatchNowOffer
  lastChangeRetailPrice(language: $language)
  lastChangePercent
  __typename
}

fragment WatchNowOffer on Offer {
  __typename
  id
  standardWebURL
  preAffiliatedStandardWebURL
  streamUrl
  streamUrlExternalPlayer
  package {
    id
    icon
    packageId
    clearName
    shortName
    technicalName
    iconWide(profile: S160)
    hasRectangularIcon(country: $country, platform: WEB)
    __typename
  }
  retailPrice(language: $language)
  retailPriceValue
  lastChangeRetailPriceValue
  currency
  presentationType
  monetizationType
  availableTo
  dateCreated
  newElementCount
}
"""
