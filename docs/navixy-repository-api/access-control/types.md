# Access control — Types

## Objects

### Role

A role that can be assigned to actors to grant permissions.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `permissions` | [RolePermissionConnection](#rolepermissionconnection)! | The permissions assigned to this role. |

---

### PermissionScope

A definition of a permission scope that can be granted to roles.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](../catalogs/system.md#module)! | The module this permission scope belongs to. |
| `entityType` | [EntityType](../catalogs/system.md#entitytype)! | The entity type this permission applies to. |

---

### ActorRole

An assignment of a role to an actor.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `actor` | [Actor](../actors/README.md#actor)! | The actor receiving the role. |
| `role` | [Role](#role)! | The role being assigned. |
| `assignedAt` | `DateTime!` | The date and time when the role was assigned. |
| `assignedBy` | [Actor](../actors/README.md#actor) | The actor who assigned the role. |
| `expireDate` | `DateTime` | The date and time when the role expires. Null means the role is permanent. |

---

### RolePermission

A permission granted to a role.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `role` | [Role](#role)! | The role receiving the permission. |
| `permissionScope` | [PermissionScope](#permissionscope)! | The permission scope being granted. |
| `targetEntityId` | `ID` | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions` | [[ActionPermission](#actionpermission)!]! | The actions allowed by this permission. |
| `grantedAt` | `DateTime!` | The date and time when the permission was granted. |
| `grantedBy` | [Actor](../actors/README.md#actor)! | The actor who granted the permission. |

---

### UserScope

A whitelist filter that restricts an actor's access to specific entities.
When present, effective permissions = role permissions ∩ user scope.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `actor` | [Actor](../actors/README.md#actor)! | The actor being restricted. |
| `permissionScope` | [PermissionScope](#permissionscope)! | The permission scope being filtered. |
| `targetEntityId` | `ID!` | The specific entity the actor can access. |
| `actions` | [[ActionPermission](#actionpermission)!]! | The actions allowed on this specific entity. |

---

### ActorRolePayload

The result of a role assignment mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRole` | [ActorRole](#actorrole)! | The created role assignment. |

---

### RolePermissionPayload

The result of a permission grant mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `rolePermission` | [RolePermission](#rolepermission)! | The created permission. |

---

### UserScopePayload

The result of a user scope mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScope` | [UserScope](#userscope)! | The created user scope restriction. |

---

### RolePayload

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](#role)! | The created or updated role. |

---

## Inputs

### ActorRoleFilter

Filtering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean` | Include expired role assignments. |

---

### ActorRoleOrder

Ordering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField](#actorroleorderfield)! | The field to order by. |
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
| `field` | [RolePermissionOrderField](#rolepermissionorderfield)! | The field to order by. |
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
| `field` | [UserScopeOrderField](#userscopeorderfield)! | The field to order by. |
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
| `actions` | [[ActionPermission](#actionpermission)!]! | The actions to allow. |

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
| `actions` | [[ActionPermission](#actionpermission)!]! | The actions to allow. |

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
| `order` | `Int` | The display order. |
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
| `edges` | [[RoleEdge](#roleedge)!]! | A list of edges. |
| `nodes` | [[Role](#role)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### RoleEdge

An edge in the Role connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Role](#role)! | The role at the end of the edge. |

---

### ActorRoleConnection

A paginated list of ActorRole items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ActorRoleEdge](#actorroleedge)!]! | A list of edges. |
| `nodes` | [[ActorRole](#actorrole)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### ActorRoleEdge

An edge in the ActorRole connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [ActorRole](#actorrole)! | The actor role at the end of the edge. |

---

### RolePermissionConnection

A paginated list of RolePermission items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RolePermissionEdge](#rolepermissionedge)!]! | A list of edges. |
| `nodes` | [[RolePermission](#rolepermission)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### RolePermissionEdge

An edge in the RolePermission connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [RolePermission](#rolepermission)! | The role permission at the end of the edge. |

---

### UserScopeConnection

A paginated list of UserScope items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserScopeEdge](#userscopeedge)!]! | A list of edges. |
| `nodes` | [[UserScope](#userscope)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### UserScopeEdge

An edge in the UserScope connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserScope](#userscope)! | The user scope at the end of the edge. |

---
