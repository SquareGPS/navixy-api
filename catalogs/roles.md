# Roles Catalog

Role definitions and permission templates.

## Queries

### roles

Lists roles for an organization.

```graphql
roles(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): RoleConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve roles for. |
| `filter` | [CatalogItemFilter](./README.md#catalogitemfilter) | Filtering options for the returned roles. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [CatalogItemOrder](./README.md#catalogitemorder) | The ordering options for the returned roles. |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | [[Code](../common.md#code)!] | Match any of these codes. |

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

<summary><code>RoleConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RoleEdge](./roles.md#roleedge)!]! | A list of edges. |
| `nodes` | [[Role](./roles.md#role)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>Role (node)</code></summary>

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
| `permissions` | [RolePermissionConnection](../access-control/types.md#rolepermissionconnection)! | The permissions assigned to this role. |

</details>

## Mutations

### roleCreate

Creates a new role.

```graphql
roleCreate(input: RoleCreateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleCreateInput](./roles.md#rolecreateinput)! | The input fields for creating the role. |

**Input types:**

<details>

<summary><code>RoleCreateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
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

<summary><code>RolePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](./roles.md#role)! | The created or updated role. |

</details>

<details>

<summary><code>Role (entity)</code></summary>

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
| `permissions` | [RolePermissionConnection](../access-control/types.md#rolepermissionconnection)! | The permissions assigned to this role. |

</details>

### roleUpdate

Updates a role.

```graphql
roleUpdate(input: RoleUpdateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleUpdateInput](./roles.md#roleupdateinput)! | The input fields for updating the role. |

**Input types:**

<details>

<summary><code>RoleUpdateInput</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
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

<summary><code>RolePayload</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](./roles.md#role)! | The created or updated role. |

</details>

<details>

<summary><code>Role (entity)</code></summary>

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
| `permissions` | [RolePermissionConnection](../access-control/types.md#rolepermissionconnection)! | The permissions assigned to this role. |

</details>

### roleDelete

Deletes a role.

```graphql
roleDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](./README.md#catalogitemdeleteinput)! | The input fields for deleting the role. |

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

### RoleConnection

A paginated list of Role items.

**Implements:** [`Connection`](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RoleEdge](./roles.md#roleedge)!]! | A list of edges. |
| `nodes` | [[Role](./roles.md#role)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

### RoleEdge

An edge in the Role connection.

**Implements:** [`Edge`](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Role](./roles.md#role)! | The role at the end of the edge. |

### Role

A role that can be assigned to actors to grant permissions.

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
| `permissions` | [RolePermissionConnection](../access-control/types.md#rolepermissionconnection)! | The permissions assigned to this role. |

### PermissionScope

A definition of a permission scope that can be granted to roles.

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
| `module` | [Module](./system.md#module)! | The module this permission scope belongs to. |
| `entityType` | [EntityType](./system.md#entitytype)! | The entity type this permission applies to. |

### RolePayload

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](./roles.md#role)! | The created or updated role. |

## Inputs

### RoleCreateInput

Input for creating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code](../common.md#code)! | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |

### RoleUpdateInput

Input for updating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](./README.md#catalogitemmetainput) | The display properties. |
