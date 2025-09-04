# ruff: noqa: E501
QUERY = """query GetTitleDetailArticle($fullPath: String!, $country: Country!, $language: Language!) {
  urlV2(fullPath: $fullPath) {
    id
    node {
      id
      ... on MovieOrShowOrSeason {
        content(country: $country, language: $language) {
          articles(articleTypes: TITLE_DETAIL_ARTICLE) {
            ...TitleDetailArticle
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment TitleDetailArticle on Article {
  id
  content {
    __typename
    synopsis
    whatToKnow
    productionNews
  }
  __typename
}
"""
