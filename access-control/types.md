# Access control — Types

## Objects

### Role

A role that can be assigned to actors to grant permissions.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `filter` | [RolePermissionFilter](types.md#rolepermissionfilter) | Filtering options for the returned permissions. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `RolePermissionOrder = { field: GRANTED_AT, direction: DESC }` | The ordering options for the returned permissions. |

---

### PermissionScope

A definition of a permission scope that can be granted to roles.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `module` | [Module](../catalogs/system.md#module)! | The module this permission scope belongs to. |
| `entityType` | [EntityType](../catalogs/system.md#entitytype)! | The entity type this permission applies to. |

---

### ActorRole

An assignment of a role to an actor.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `actor` | [Actor](../actors.md#actor)! | The actor receiving the role. |
| `role` | [Role](types.md#role)! | The role being assigned. |
| `assignedAt` | `DateTime!` | The date and time when the role was assigned. |
| `assignedBy` | [Actor](../actors.md#actor) | The actor who assigned the role. |
| `expireDate` | `DateTime` | The date and time when the role expires. Null means the role is permanent. |

---

### RolePermission

A permission granted to a role.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `role` | [Role](types.md#role)! | The role receiving the permission. |
| `permissionScope` | [PermissionScope](types.md#permissionscope)! | The permission scope being granted. |
| `targetEntityId` | `ID` | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions allowed by this permission. |
| `grantedAt` | `DateTime!` | The date and time when the permission was granted. |
| `grantedBy` | [Actor](../actors.md#actor)! | The actor who granted the permission. |

---

### UserScope

A whitelist filter that restricts an actor's access to specific entities.
When present, effective permissions = role permissions ∩ user scope.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `actor` | [Actor](../actors.md#actor)! | The actor being restricted. |
| `permissionScope` | [PermissionScope](types.md#permissionscope)! | The permission scope being filtered. |
| `targetEntityId` | `ID!` | The specific entity the actor can access. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions allowed on this specific entity. |

---

### ActorRolePayload

The result of a role assignment mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRole` | [ActorRole](types.md#actorrole)! | The created role assignment. |

---

### RolePermissionPayload

The result of a permission grant mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `rolePermission` | [RolePermission](types.md#rolepermission)! | The created permission. |

---

### UserScopePayload

The result of a user scope mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScope` | [UserScope](types.md#userscope)! | The created user scope restriction. |

---

### RolePayload

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](types.md#role)! | The created or updated role. |

---

## Inputs

### ActorRoleFilter

Filtering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean = true` | Include expired role assignments. |

---

### ActorRoleOrder

Ordering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField](types.md#actorroleorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### RolePermissionFilter

Filtering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

---

### RolePermissionOrder

Ordering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [RolePermissionOrderField](types.md#rolepermissionorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### UserScopeFilter

Filtering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

---

### UserScopeOrder

Ordering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [UserScopeOrderField](types.md#userscopeorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### RoleAssignInput

Input for assigning a role to an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID (user or integration). |
| `roleId` | `ID!` | The role ID to assign. |
| `expireDate` | `DateTime` | The expiration date. Null means the role is permanent. |

---

### RoleRevokeInput

Input for revoking a role from an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

---

### PermissionGrantInput

Input for granting a permission to a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleId` | `ID!` | The role ID. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID` | The specific entity ID. Null means all entities of the type. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions to allow. |

---

### PermissionRevokeInput

Input for revoking a permission from a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

---

### UserScopeSetInput

Input for setting a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID to restrict. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID!` | The specific entity ID to allow access to. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions to allow. |

---

### UserScopeRemoveInput

Input for removing a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

---

### RoleCreateInput

Input for creating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### RoleUpdateInput

Input for updating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Enums

### ActionPermission

Permission actions that can be granted to actors for entity operations.

| Value | Description |
| ----- | ----------- |
| `READ` | Permission to view entities and their data. |
| `CREATE` | Permission to create new entities. |
| `UPDATE` | Permission to modify existing entities. |
| `DELETE` | Permission to delete entities. |

---

### ActorRoleOrderField

Fields available for ordering actor roles.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

---

### RolePermissionOrderField

Fields available for ordering role permissions.

| Value | Description |
| ----- | ----------- |
| `GRANTED_AT` | Order by grant date. |

---

### UserScopeOrderField

Fields available for ordering user scopes.

| Value | Description |
| ----- | ----------- |
| `ID` | Order by ID. |

---

## Pagination types

### RoleConnection

A paginated list of Role items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RoleEdge](types.md#roleedge)!]! | A list of edges. |
| `nodes` | [[Role](types.md#role)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### RoleEdge

An edge in the Role connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Role](types.md#role)! | The role at the end of the edge. |

---

### ActorRoleConnection

A paginated list of ActorRole items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ActorRoleEdge](types.md#actorroleedge)!]! | A list of edges. |
| `nodes` | [[ActorRole](types.md#actorrole)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### ActorRoleEdge

An edge in the ActorRole connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [ActorRole](types.md#actorrole)! | The actor role at the end of the edge. |

---

### RolePermissionConnection

A paginated list of RolePermission items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RolePermissionEdge](types.md#rolepermissionedge)!]! | A list of edges. |
| `nodes` | [[RolePermission](types.md#rolepermission)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### RolePermissionEdge

An edge in the RolePermission connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [RolePermission](types.md#rolepermission)! | The role permission at the end of the edge. |

---

### UserScopeConnection

A paginated list of UserScope items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserScopeEdge](types.md#userscopeedge)!]! | A list of edges. |
| `nodes` | [[UserScope](types.md#userscope)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### UserScopeEdge

An edge in the UserScope connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserScope](types.md#userscope)! | The user scope at the end of the edge. |

---
