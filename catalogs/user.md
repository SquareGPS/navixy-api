# User Catalog

User-related catalog items including statuses.

## Mutations

### userCatalogItemCreate

Creates a new user catalog item.

```graphql
userCatalogItemCreate(
  input: UserCatalogItemCreateInput!
): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserCatalogItemCreateInput](./user.md#usercatalogitemcreateinput)! | The input fields for creating the item. |

**Input types:**

<details>

<summary><code>UserCatalogItemCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | [Code](../common.md#code)! | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
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

<summary><code>UserCatalogItemPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](./user.md#usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary><code>UserCatalogItem (entity)</code></summary>

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
| `parent` | [UserCatalogItem](./user.md#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](./user.md#usercatalogitemconnection)! | The child items in the hierarchy. |

</details>

### userCatalogItemUpdate

Updates a user catalog item.

```graphql
userCatalogItemUpdate(
  input: UserCatalogItemUpdateInput!
): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserCatalogItemUpdateInput](./user.md#usercatalogitemupdateinput)! | The input fields for updating the item. |

**Input types:**

<details>

<summary><code>UserCatalogItemUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
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

<summary><code>UserCatalogItemPayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](./user.md#usercatalogitem)! | The created or updated user catalog item. |

</details>

<details>

<summary><code>UserCatalogItem (entity)</code></summary>

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
| `parent` | [UserCatalogItem](./user.md#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](./user.md#usercatalogitemconnection)! | The child items in the hierarchy. |

</details>

### userCatalogItemDelete

Deletes a user catalog item.

```graphql
userCatalogItemDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](./README.md#catalogitemdeleteinput)! | The input fields for deleting the item. |

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

### UserCatalogItemConnection

A paginated list of UserCatalogItem items.

**Implements:** [`Connection`](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserCatalogItemEdge](./user.md#usercatalogitemedge)!]! | A list of edges. |
| `nodes` | [[UserCatalogItem](./user.md#usercatalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

### UserCatalogItemEdge

An edge in the UserCatalogItem connection.

**Implements:** [`Edge`](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserCatalogItem](./user.md#usercatalogitem)! | The user catalog item at the end of the edge. |

### UserCatalogItem

A user-defined catalog item that supports hierarchical organization.

**Implements:** [`CatalogItem`](./README.md#catalogitem), [`HierarchicalCatalogItem`](./README.md#hierarchicalcatalogitem), [`Node`](../common.md#node), [`Versioned`](../common.md#versioned), [`Titled`](../common.md#titled)

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
| `parent` | [UserCatalogItem](./user.md#usercatalogitem) | The parent item in the hierarchy. Null for root items. |
| `children` | [UserCatalogItemConnection](./user.md#usercatalogitemconnection)! | The child items in the hierarchy. |

### UserCatalogItemPayload

The result of a user catalog item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `item` | [UserCatalogItem](./user.md#usercatalogitem)! | The created or updated user catalog item. |

## Inputs

### UserCatalogItemCreateInput

Input for creating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | [Code](../common.md#code)! | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |

### UserCatalogItemUpdateInput

Input for updating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |
