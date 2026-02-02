# Queries

### assetTypes

Lists asset types for an organization.

```graphql
assetTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): AssetTypeConnection!
```

**Arguments**

| Name             | Type                                       | Description                                                                                   |
| ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                      | The organization to retrieve asset types for.                                                 |
| `filter`         | [CatalogItemFilter](../#catalogitemfilter) | Filtering options for the returned asset types.                                               |
| `first`          | `Int`                                      | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                   | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                      | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                   | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../#catalogitemorder)   | The ordering options for the returned asset types.                                            |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

| Field           | Type                                                          | Description                                         |
| --------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| `titleContains` | `String`                                                      | Partial match on title (case-insensitive contains). |
| `codes`         | \[[Code](../../core-api-reference/common-resources.md#code)!] | Match any of these codes.                           |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

| Field       | Type                                                                           | Description             |
| ----------- | ------------------------------------------------------------------------------ | ----------------------- |
| `field`     | [CatalogItemOrderField](../#catalogitemorderfield)!                            | The field to order by.  |
| `direction` | [OrderDirection](../../core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>AssetTypeConnection</code></summary>

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AssetTypeEdge](types.md#assettypeedge)!]!                        | A list of edges.                                           |
| `nodes`    | \[[AssetType](types.md#assettype)!]!                                | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>AssetType (node)</code></summary>

| Field                    | Type                                                                       | Description                                                                     |
| ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                      |                                                                                 |
| `version`                | `Int!`                                                                     |                                                                                 |
| `title`                  | `String!`                                                                  |                                                                                 |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                 |
| `order`                  | `Int!`                                                                     |                                                                                 |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                 |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                 |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                 |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this asset type, ordered by display order. |

</details>

### scheduleTypes

Lists schedule types for an organization.

```graphql
scheduleTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): ScheduleTypeConnection!
```

**Arguments**

| Name             | Type                                       | Description                                                                                   |
| ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                      | The organization to retrieve schedule types for.                                              |
| `filter`         | [CatalogItemFilter](../#catalogitemfilter) | Filtering options for the returned schedule types.                                            |
| `first`          | `Int`                                      | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                   | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                      | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                   | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../#catalogitemorder)   | The ordering options for the returned schedule types.                                         |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

| Field           | Type                                                          | Description                                         |
| --------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| `titleContains` | `String`                                                      | Partial match on title (case-insensitive contains). |
| `codes`         | \[[Code](../../core-api-reference/common-resources.md#code)!] | Match any of these codes.                           |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

| Field       | Type                                                                           | Description             |
| ----------- | ------------------------------------------------------------------------------ | ----------------------- |
| `field`     | [CatalogItemOrderField](../#catalogitemorderfield)!                            | The field to order by.  |
| `direction` | [OrderDirection](../../core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>ScheduleTypeConnection</code></summary>

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[ScheduleTypeEdge](types.md#scheduletypeedge)!]!                  | A list of edges.                                           |
| `nodes`    | \[[ScheduleType](types.md#scheduletype)!]!                          | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>ScheduleType (node)</code></summary>

| Field                    | Type                                                                       | Description                                                                        |
| ------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                      |                                                                                    |
| `version`                | `Int!`                                                                     |                                                                                    |
| `title`                  | `String!`                                                                  |                                                                                    |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                    |
| `order`                  | `Int!`                                                                     |                                                                                    |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                    |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                    |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                    |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

</details>
