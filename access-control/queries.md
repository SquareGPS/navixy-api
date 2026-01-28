# Access Control — Queries

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
| `organizationId` | `ID!` | The organization to retrieve actor roles for. |
| `filter` | [ActorRoleFilter](./types.md#actorrolefilter) | Filtering options for the returned actor roles. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [ActorRoleOrder](./types.md#actorroleorder) | The ordering options for the returned actor roles. |

**Input types:**

<details>

<summary><code>ActorRoleFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean` | Include expired role assignments. |

</details>

<details>

<summary><code>ActorRoleOrder</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField](./types.md#actorroleorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>ActorRoleConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ActorRoleEdge](./types.md#actorroleedge)!]! | A list of edges. |
| `nodes` | [[ActorRole](./types.md#actorrole)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>ActorRole (node)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `actor` | [Actor](./types.md#actor)! | The actor receiving the role. |
| `role` | [Role](../catalogs/roles.md#role)! | The role being assigned. |
| `assignedAt` | [DateTime](../common.md#datetime)! | The date and time when the role was assigned. |
| `assignedBy` | [Actor](./types.md#actor) | The actor who assigned the role. |
| `expireDate` | [DateTime](../common.md#datetime) | The date and time when the role expires. Null means the role is permanent. |

</details>

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
| `organizationId` | `ID!` | The organization to retrieve role permissions for. |
| `filter` | [RolePermissionFilter](./types.md#rolepermissionfilter) | Filtering options for the returned role permissions. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [RolePermissionOrder](./types.md#rolepermissionorder) | The ordering options for the returned role permissions. |

**Input types:**

<details>

<summary><code>RolePermissionFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

</details>

<details>

<summary><code>RolePermissionOrder</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [RolePermissionOrderField](./types.md#rolepermissionorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>RolePermissionConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RolePermissionEdge](./types.md#rolepermissionedge)!]! | A list of edges. |
| `nodes` | [[RolePermission](./types.md#rolepermission)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>RolePermission (node)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `role` | [Role](../catalogs/roles.md#role)! | The role receiving the permission. |
| `permissionScope` | [PermissionScope](../catalogs/roles.md#permissionscope)! | The permission scope being granted. |
| `targetEntityId` | `ID` | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions` | [[ActionPermission](./types.md#actionpermission)!]! | The actions allowed by this permission. |
| `grantedAt` | [DateTime](../common.md#datetime)! | The date and time when the permission was granted. |
| `grantedBy` | [Actor](./types.md#actor)! | The actor who granted the permission. |

</details>

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
| `organizationId` | `ID!` | The organization to retrieve user scopes for. |
| `filter` | [UserScopeFilter](./types.md#userscopefilter) | Filtering options for the returned user scopes. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [UserScopeOrder](./types.md#userscopeorder) | The ordering options for the returned user scopes. |

**Input types:**

<details>

<summary><code>UserScopeFilter</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

</details>

<details>

<summary><code>UserScopeOrder</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [UserScopeOrderField](./types.md#userscopeorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>UserScopeConnection</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserScopeEdge](./types.md#userscopeedge)!]! | A list of edges. |
| `nodes` | [[UserScope](./types.md#userscope)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>UserScope (node)</code></summary>

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `actor` | [Actor](./types.md#actor)! | The actor being restricted. |
| `permissionScope` | [PermissionScope](../catalogs/roles.md#permissionscope)! | The permission scope being filtered. |
| `targetEntityId` | `ID!` | The specific entity the actor can access. |
| `actions` | [[ActionPermission](./types.md#actionpermission)!]! | The actions allowed on this specific entity. |

</details>
