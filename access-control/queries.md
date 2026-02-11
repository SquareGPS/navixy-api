# Access control — Queries

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
| `organizationId` | `ID!` |  |
| `filter` | [CatalogItemFilter](../catalogs/catalog-items.md#catalogitemfilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [CatalogItemOrder](../catalogs/catalog-items.md#catalogitemorder) |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | `[Code!]` | Match any of these codes. |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../catalogs/catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>RoleConnection</code></summary>

A paginated list of Role items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RoleEdge](types.md#roleedge)!]! | A list of edges. |
| `nodes` | [[Role](types.md#role)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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

### actorRoles

Lists actor role assignments for an organization.

```graphql
actorRoles(
    organizationId: ID!
    filter: ActorRoleFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: ActorRoleOrder = { field: ASSIGNED_AT, direction: DESC }
  ): ActorRoleConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | [ActorRoleFilter](types.md#actorrolefilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [ActorRoleOrder](types.md#actorroleorder) |  |
| `direction` | `DESC }` |  |

**Input types:**

<details>

<summary><code>ActorRoleFilter</code></summary>

Filtering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean = true` | Include expired role assignments. |

</details>

<details>

<summary><code>ActorRoleOrder</code></summary>

Ordering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField](types.md#actorroleorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>ActorRoleConnection</code></summary>

A paginated list of ActorRole items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ActorRoleEdge](types.md#actorroleedge)!]! | A list of edges. |
| `nodes` | [[ActorRole](types.md#actorrole)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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

### rolePermissions

Lists role permissions for an organization.

```graphql
rolePermissions(
    organizationId: ID!
    filter: RolePermissionFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: RolePermissionOrder = { field: GRANTED_AT, direction: DESC }
  ): RolePermissionConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | [RolePermissionFilter](types.md#rolepermissionfilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [RolePermissionOrder](types.md#rolepermissionorder) |  |
| `direction` | `DESC }` |  |

**Input types:**

<details>

<summary><code>RolePermissionFilter</code></summary>

Filtering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

</details>

<details>

<summary><code>RolePermissionOrder</code></summary>

Ordering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [RolePermissionOrderField](types.md#rolepermissionorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>RolePermissionConnection</code></summary>

A paginated list of RolePermission items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RolePermissionEdge](types.md#rolepermissionedge)!]! | A list of edges. |
| `nodes` | [[RolePermission](types.md#rolepermission)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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

### userScopes

Lists user scope restrictions for an organization.

```graphql
userScopes(
    organizationId: ID!
    filter: UserScopeFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: UserScopeOrder = { field: ID, direction: ASC }
  ): UserScopeConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | [UserScopeFilter](types.md#userscopefilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [UserScopeOrder](types.md#userscopeorder) |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary><code>UserScopeFilter</code></summary>

Filtering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

</details>

<details>

<summary><code>UserScopeOrder</code></summary>

Ordering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [UserScopeOrderField](types.md#userscopeorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>UserScopeConnection</code></summary>

A paginated list of UserScope items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserScopeEdge](types.md#userscopeedge)!]! | A list of edges. |
| `nodes` | [[UserScope](types.md#userscope)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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
