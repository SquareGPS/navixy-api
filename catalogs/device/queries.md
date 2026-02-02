# Queries

### deviceTypes

Lists device types for an organization.

```graphql
deviceTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): DeviceTypeConnection!
```

**Arguments**

| Name             | Type                                       | Description                                                                                   |
| ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                      | The organization to retrieve device types for.                                                |
| `filter`         | [CatalogItemFilter](../#catalogitemfilter) | Filtering options for the returned device types.                                              |
| `first`          | `Int`                                      | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                   | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                      | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                   | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../#catalogitemorder)   | The ordering options for the returned device types.                                           |

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

<summary><code>DeviceTypeConnection</code></summary>

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceTypeEdge](types.md#devicetypeedge)!]!                      | A list of edges.                                           |
| `nodes`    | \[[DeviceType](types.md#devicetype)!]!                              | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>DeviceType (node)</code></summary>

| Field                    | Type                                                                       | Description                                                                      |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                      |                                                                                  |
| `version`                | `Int!`                                                                     |                                                                                  |
| `title`                  | `String!`                                                                  |                                                                                  |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                  |
| `order`                  | `Int!`                                                                     |                                                                                  |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                  |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                  |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                  |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

### deviceStatuses

Lists device statuses for an organization.

```graphql
deviceStatuses(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): DeviceStatusConnection!
```

**Arguments**

| Name             | Type                                       | Description                                                                                   |
| ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                      | The organization to retrieve device statuses for.                                             |
| `filter`         | [CatalogItemFilter](../#catalogitemfilter) | Filtering options for the returned device statuses.                                           |
| `first`          | `Int`                                      | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                   | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                      | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                   | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../#catalogitemorder)   | The ordering options for the returned device statuses.                                        |

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

<summary><code>DeviceStatusConnection</code></summary>

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceStatusEdge](types.md#devicestatusedge)!]!                  | A list of edges.                                           |
| `nodes`    | \[[DeviceStatus](types.md#devicestatus)!]!                          | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>DeviceStatus (node)</code></summary>

| Field          | Type                                                                 | Description |
| -------------- | -------------------------------------------------------------------- | ----------- |
| `id`           | `ID!`                                                                |             |
| `version`      | `Int!`                                                               |             |
| `title`        | `String!`                                                            |             |
| `code`         | [Code](../../core-api-reference/common-resources.md#code)!           |             |
| `order`        | `Int!`                                                               |             |
| `catalog`      | [Catalog](../../core-api-reference/organizations/#catalog)!          |             |
| `organization` | [Organization](../../core-api-reference/organizations/#organization) |             |
| `meta`         | [CatalogItemMeta](../#catalogitemmeta)!                              |             |

</details>

### deviceModels

Lists device models with optional vendor filter.

```graphql
deviceModels(
  organizationId: ID!
  filter: DeviceModelFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: TITLE, direction: ASC }
): DeviceModelConnection!
```

**Arguments**

| Name             | Type                                            | Description                                                                                   |
| ---------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                           | The organization to retrieve device models for.                                               |
| `filter`         | [DeviceModelFilter](types.md#devicemodelfilter) | Filtering options for the returned device models.                                             |
| `first`          | `Int`                                           | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                        | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                           | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                        | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../#catalogitemorder)        | The ordering options for the returned device models.                                          |

**Input types:**

<details>

<summary><code>DeviceModelFilter</code></summary>

| Field           | Type                                                      | Description                                         |
| --------------- | --------------------------------------------------------- | --------------------------------------------------- |
| `vendorIds`     | `[ID!]`                                                   | Filter by vendors (OR within field).                |
| `titleContains` | `String`                                                  | Partial match on title (case-insensitive contains). |
| `code`          | [Code](../../core-api-reference/common-resources.md#code) | Exact code match.                                   |

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

<summary><code>DeviceModelConnection</code></summary>

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceModelEdge](types.md#devicemodeledge)!]!                    | A list of edges.                                           |
| `nodes`    | \[[DeviceModel](types.md#devicemodel)!]!                            | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>DeviceModel (node)</code></summary>

| Field          | Type                                                                 | Description                              |
| -------------- | -------------------------------------------------------------------- | ---------------------------------------- |
| `id`           | `ID!`                                                                |                                          |
| `version`      | `Int!`                                                               |                                          |
| `title`        | `String!`                                                            |                                          |
| `code`         | [Code](../../core-api-reference/common-resources.md#code)!           |                                          |
| `order`        | `Int!`                                                               |                                          |
| `catalog`      | [Catalog](../../core-api-reference/organizations/#catalog)!          |                                          |
| `organization` | [Organization](../../core-api-reference/organizations/#organization) |                                          |
| `meta`         | [CatalogItemMeta](../#catalogitemmeta)!                              |                                          |
| `vendor`       | [DeviceVendor](types.md#devicevendor)!                               | The vendor that manufactures this model. |

</details>
