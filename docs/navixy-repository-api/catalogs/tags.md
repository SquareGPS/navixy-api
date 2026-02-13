# Tags

Tag management for flexible entity classification.

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
| `filter` | `TagFilter` | Filtering options for the returned tags. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned tags. |

**Input types:**

<details>

<summary>TagFilter</summary>

Filtering options for tags.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary>CatalogItemOrder</summary>

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>TagConnection</summary>

A paginated list of Tag items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[TagEdge](#tagedge)!]! | A list of edges. |
| `nodes` | [[Tag](#tag)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary>PageInfo (entity)</summary>

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

</details>

---

## Mutations

### tagCreate

Creates a new tag.

```graphql
tagCreate(
    input: TagCreateInput!
  ): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `TagCreateInput!` | The input fields for creating the tag. |

**Input types:**

<details>

<summary>TagCreateInput</summary>

Input for creating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>TagPayload</summary>

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](#tag)! | The created or updated tag. |

</details>

<details>

<summary>Tag (entity)</summary>

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `entityTypes` | [[EntityType](system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

---

### tagUpdate

Updates a tag.

```graphql
tagUpdate(
    input: TagUpdateInput!
  ): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `TagUpdateInput!` | The input fields for updating the tag. |

**Input types:**

<details>

<summary>TagUpdateInput</summary>

Input for updating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | [CatalogItemMetaInput](catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>TagPayload</summary>

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](#tag)! | The created or updated tag. |

</details>

<details>

<summary>Tag (entity)</summary>

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `entityTypes` | [[EntityType](system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

---

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
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the tag. |

**Input types:**

<details>

<summary>CatalogItemDeleteInput</summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary>DeletePayload</summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

## Objects

### Tag

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `entityTypes` | [[EntityType](system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

---

### TagPayload

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](#tag)! | The created or updated tag. |

---

## Inputs

### TagFilter

Filtering options for tags.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

### TagCreateInput

Input for creating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](catalog-items.md#catalogitemmetainput) | The display properties. |

---

### TagUpdateInput

Input for updating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | [CatalogItemMetaInput](catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Pagination types

### TagConnection

A paginated list of Tag items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[TagEdge](#tagedge)!]! | A list of edges. |
| `nodes` | [[Tag](#tag)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### TagEdge

An edge in the Tag connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Tag](#tag)! | The tag at the end of the edge. |

---
