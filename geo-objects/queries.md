# Queries

### geoObjectTypes

Lists geo object types for an organization.

```graphql
geoObjectTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): GeoObjectTypeConnection!
```

**Arguments**

| Name             | Type                                                | Description                                                                                   |
| ---------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                               | The organization to retrieve geo object types for.                                            |
| `filter`         | [CatalogItemFilter](../catalogs/#catalogitemfilter) | Filtering options for the returned geo object types.                                          |
| `first`          | `Int`                                               | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                            | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                               | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                            | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../catalogs/#catalogitemorder)   | The ordering options for the returned geo object types.                                       |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

| Field           | Type                                                       | Description                                         |
| --------------- | ---------------------------------------------------------- | --------------------------------------------------- |
| `titleContains` | `String`                                                   | Partial match on title (case-insensitive contains). |
| `codes`         | \[[Code](../core-api-reference/common-resources.md#code)!] | Match any of these codes.                           |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

| Field       | Type                                                                        | Description             |
| ----------- | --------------------------------------------------------------------------- | ----------------------- |
| `field`     | [CatalogItemOrderField](../catalogs/#catalogitemorderfield)!                | The field to order by.  |
| `direction` | [OrderDirection](../core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>GeoObjectTypeConnection</code></summary>

| Field      | Type                                                                          | Description                                                |
| ---------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[GeoObjectTypeEdge](../catalogs/entity-types/types.md#geoobjecttypeedge)!]! | A list of edges.                                           |
| `nodes`    | \[[GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)!]!         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../core-api-reference/common-resources.md#pageinfo)!               | Information about the current page.                        |
| `total`    | [CountInfo](../core-api-reference/common-resources.md#countinfo)              | The total count of items matching the filter.              |

</details>

<details>

<summary><code>GeoObjectType (node)</code></summary>

| Field                    | Type                                                                    | Description                                                                          |
| ------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `id`                     | `ID!`                                                                   |                                                                                      |
| `version`                | `Int!`                                                                  |                                                                                      |
| `title`                  | `String!`                                                               |                                                                                      |
| `code`                   | [Code](../core-api-reference/common-resources.md#code)!                 |                                                                                      |
| `order`                  | `Int!`                                                                  |                                                                                      |
| `catalog`                | [Catalog](../core-api-reference/organizations/#catalog)!                |                                                                                      |
| `organization`           | [Organization](../core-api-reference/organizations/#organization)       |                                                                                      |
| `meta`                   | [CatalogItemMeta](../catalogs/#catalogitemmeta)!                        |                                                                                      |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

</details>

### geoObject

Retrieves a geo object by its ID.

```graphql
geoObject(id: ID!): GeoObject
```

**Arguments**

| Name | Type  | Description                           |
| ---- | ----- | ------------------------------------- |
| `id` | `ID!` | The ID of the geo object to retrieve. |

**Output types:**

<details>

<summary><code>GeoObject</code></summary>

| Field            | Type                                                               | Description                                 |
| ---------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| `id`             | `ID!`                                                              |                                             |
| `version`        | `Int!`                                                             |                                             |
| `title`          | `String!`                                                          |                                             |
| `organization`   | [Organization](../core-api-reference/organizations/#organization)! | The organization that owns this geo object. |
| `type`           | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)!  | The geo object type classification.         |
| `geometry`       | [GeoJSON](types.md#geojson)!                                       |                                             |
| `customFields`   | [JSON](../core-api-reference/common-resources.md#json)!            |                                             |
| `containsPoints` | \[[PointContainmentResult](types.md#pointcontainmentresult)!]!     |                                             |

</details>

### geoObjects

Lists geo objects for an organization.

```graphql
geoObjects(
  organizationId: ID!
  filter: GeoObjectFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: GeoObjectOrder = { field: TITLE, direction: ASC }
): GeoObjectConnection!
```

**Arguments**

| Name             | Type                                        | Description                                                                                   |
| ---------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                       | The organization to retrieve geo objects for.                                                 |
| `filter`         | [GeoObjectFilter](types.md#geoobjectfilter) | Filtering options for the returned geo objects.                                               |
| `first`          | `Int`                                       | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                    | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                       | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                    | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [GeoObjectOrder](types.md#geoobjectorder)   | The ordering options for the returned geo objects.                                            |

**Input types:**

<details>

<summary><code>GeoObjectFilter</code></summary>

| Field           | Type                                                           | Description                                         |
| --------------- | -------------------------------------------------------------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`                                                        | Filter by geo object types (OR within field).       |
| `titleContains` | `String`                                                       | Partial match on title (case-insensitive contains). |
| `customFields`  | \[[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values.                      |

</details>

<details>

<summary><code>CustomFieldFilter</code></summary>

| Field      | Type                                                    | Description                                                                   |
| ---------- | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `code`     | [Code](../core-api-reference/common-resources.md#code)! | The custom field code to filter by.                                           |
| `operator` | [FieldOperator](../custom-fields.md#fieldoperator)!     | The comparison operator.                                                      |
| `value`    | [JSON](../core-api-reference/common-resources.md#json)  | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary><code>GeoObjectOrder</code></summary>

| Field             | Type                                                                        | Description                                                                |
| ----------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `field`           | [GeoObjectOrderField](types.md#geoobjectorderfield)                         | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](../core-api-reference/common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](../core-api-reference/common-resources.md#orderdirection)! | The direction to order.                                                    |

</details>

**Output types:**

<details>

<summary><code>GeoObjectConnection</code></summary>

| Field      | Type                                                             | Description                                                |
| ---------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[GeoObjectEdge](types.md#geoobjectedge)!]!                     | A list of edges.                                           |
| `nodes`    | \[[GeoObject](types.md#geoobject)!]!                             | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>GeoObject (node)</code></summary>

| Field            | Type                                                               | Description                                 |
| ---------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| `id`             | `ID!`                                                              |                                             |
| `version`        | `Int!`                                                             |                                             |
| `title`          | `String!`                                                          |                                             |
| `organization`   | [Organization](../core-api-reference/organizations/#organization)! | The organization that owns this geo object. |
| `type`           | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)!  | The geo object type classification.         |
| `geometry`       | [GeoJSON](types.md#geojson)!                                       |                                             |
| `customFields`   | [JSON](../core-api-reference/common-resources.md#json)!            |                                             |
| `containsPoints` | \[[PointContainmentResult](types.md#pointcontainmentresult)!]!     |                                             |

</details>
