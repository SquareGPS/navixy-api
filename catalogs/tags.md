# Tags Catalog

Tag definitions for categorizing entities.

## Queries

### tags

Lists tags for an organization.

```graphql
tags(
  organizationId: ID!
  filter: TagFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: TITLE, direction: ASC }
): TagConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve tags for. |
| `filter` | [TagFilter](./tags.md#tagfilter) | Filtering options for the returned tags. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [CatalogItemOrder](./README.md#catalogitemorder) | The ordering options for the returned tags. |

**Input types:**

<details>

<summary><code>TagFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](./README.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>TagConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[TagEdge](./tags.md#tagedge)!]! | A list of edges. |
| `nodes` | [[Tag](./tags.md#tag)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>Tag (node)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](./system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

## Mutations

### tagCreate

Creates a new tag.

```graphql
tagCreate(input: TagCreateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [TagCreateInput](./tags.md#tagcreateinput)! | The input fields for creating the tag. |

**Input types:**

<details>

<summary><code>TagCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>TagPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](./tags.md#tag)! | The created or updated tag. |

</details>

<details>

<summary><code>Tag (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](./system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

### tagUpdate

Updates a tag.

```graphql
tagUpdate(input: TagUpdateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [TagUpdateInput](./tags.md#tagupdateinput)! | The input fields for updating the tag. |

**Input types:**

<details>

<summary><code>TagUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary><code>TagPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](./tags.md#tag)! | The created or updated tag. |

</details>

<details>

<summary><code>Tag (entity)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](./system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

### tagDelete

Deletes a tag.

```graphql
tagDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](./README.md#catalogitemdeleteinput)! | The input fields for deleting the tag. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

## Types

### TagConnection

A paginated list of Tag items.

**Implements:** [`Connection`](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[TagEdge](./tags.md#tagedge)!]! | A list of edges. |
| `nodes` | [[Tag](./tags.md#tag)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

### TagEdge

An edge in the Tag connection.

**Implements:** [`Edge`](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Tag](./tags.md#tag)! | The tag at the end of the edge. |

### Tag

A tag for labeling and categorizing entities.

**Implements:** [`CatalogItem`](./README.md#catalogitem), [`Node`](../common.md#node), [`Versioned`](../common.md#versioned), [`Titled`](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](./system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

### TagPayload

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](./tags.md#tag)! | The created or updated tag. |

## Inputs

### TagFilter

Filtering options for tags.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

### TagCreateInput

Input for creating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |

### TagUpdateInput

Input for updating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |
