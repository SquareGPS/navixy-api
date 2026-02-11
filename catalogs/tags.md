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
| `organizationId` | `ID!` |  |
| `filter` | [TagFilter](../tags.md#tagfilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [CatalogItemOrder](../catalog-items.md#catalogitemorder) |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary><code>TagFilter</code></summary>

Filtering options for tags.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>TagConnection</code></summary>

A paginated list of Tag items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[TagEdge](../tags.md#tagedge)!]! | A list of edges. |
| `nodes` | [[Tag](../tags.md#tag)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>PageInfo (entity)</code></summary>

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
tagCreate("The input fields for creating the tag." input: TagCreateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [TagCreateInput](../tags.md#tagcreateinput)! | The input fields for creating the tag. |

**Input types:**

<details>

<summary><code>TagCreateInput</code></summary>

Input for creating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](../catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>TagPayload</code></summary>

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](../tags.md#tag)! | The created or updated tag. |

</details>

<details>

<summary><code>Tag (entity)</code></summary>

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](../system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

---

### tagUpdate

Updates a tag.

```graphql
tagUpdate("The input fields for updating the tag." input: TagUpdateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [TagUpdateInput](../tags.md#tagupdateinput)! | The input fields for updating the tag. |

**Input types:**

<details>

<summary><code>TagUpdateInput</code></summary>

Input for updating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | [CatalogItemMetaInput](../catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>TagPayload</code></summary>

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](../tags.md#tag)! | The created or updated tag. |

</details>

<details>

<summary><code>Tag (entity)</code></summary>

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](../system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

</details>

---

### tagDelete

Deletes a tag.

```graphql
tagDelete("The input fields for deleting the tag." input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../catalog-items.md#catalogitemdeleteinput)! | The input fields for deleting the tag. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

## Objects

### Tag

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `entityTypes` | [[EntityType](../system.md#entitytype)!]! | The entity types this tag can be applied to. Empty means the tag is universal. |

---

### TagPayload

The result of a tag mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tag` | [Tag](../tags.md#tag)! | The created or updated tag. |

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
| `order` | `Int = 0` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](../catalog-items.md#catalogitemmetainput) | The display properties. |

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
| `meta` | [CatalogItemMetaInput](../catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Pagination types

### TagConnection

A paginated list of Tag items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[TagEdge](../tags.md#tagedge)!]! | A list of edges. |
| `nodes` | [[Tag](../tags.md#tag)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### TagEdge

An edge in the Tag connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Tag](../tags.md#tag)! | The tag at the end of the edge. |

---
