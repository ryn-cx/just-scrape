# ruff: noqa: E501
QUERY = """query GetNewTitleBuckets($country: Country!, $newTitlesFilter: TitleFilter, $newAfterCursor: String, $first: Int! = 2, $priceDrops: Boolean!, $bucketSize: Int! = 8, $groupBy: NewTitleAggregation! = DATE_PACKAGE, $pageType: NewPageType! = NEW) {
  newTitleBuckets(
    country: $country
    filter: $newTitlesFilter
    after: $newAfterCursor
    first: $first
    bucketSize: $bucketSize
    priceDrops: $priceDrops
    pageType: $pageType
    groupBy: $groupBy
  ) {
    pageInfo {
      startCursor
      endCursor
      hasPreviousPage
      hasNextPage
      __typename
    }
    edges {
      key {
        __typename
        ...NewBucketByDate
        ...NewBucketByPackage
      }
      node {
        totalCount
        pageInfo {
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment NewBucketByDate on DatePackageAggregationKey {
  __typename
  date
  package {
    id
    packageId
    shortName
    icon
    __typename
  }
}

fragment NewBucketByPackage on BucketPackageAggregationKey {
  __typename
  bucketType
  package {
    id
    packageId
    shortName
    icon
    __typename
  }
}
"""
