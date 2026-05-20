# Access control — Types

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

## Objects

<a id="type-role"></a>

### Role

A role that can be assigned to actors to grant permissions.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `permissions` | [RolePermissionConnection](#type-rolepermissionconnection)! | The permissions assigned to this role. |

---

<a id="type-permissionscope"></a>

### PermissionScope

A definition of a permission scope that can be granted to roles.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](../catalogs/system.md#type-module)! | The module this permission scope belongs to. |
| `entityType` | [EntityType](../catalogs/system.md#type-entitytype)! | The entity type this permission applies to. |

---

<a id="type-actorrole"></a>

### ActorRole

An assignment of a role to an actor.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `actor` | [Actor](../actors/README.md#type-actor)! | The actor receiving the role. |
| `role` | [Role](#type-role)! | The role being assigned. |
| `assignedAt` | `DateTime!` | The date and time when the role was assigned. |
| `assignedBy` | [Actor](../actors/README.md#type-actor) | The actor who assigned the role. |
| `expireDate` | `DateTime` | The date and time when the role expires. Null means the role is permanent. |

---

<a id="type-rolepermission"></a>

### RolePermission

A permission granted to a role.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `role` | [Role](#type-role)! | The role receiving the permission. |
| `permissionScope` | [PermissionScope](#type-permissionscope)! | The permission scope being granted. |
| `targetEntityId` | `ID` | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions` | [[ActionPermission](#type-actionpermission)!]! | The actions allowed by this permission. |
| `grantedAt` | `DateTime!` | The date and time when the permission was granted. |
| `grantedBy` | [Actor](../actors/README.md#type-actor)! | The actor who granted the permission. |

---

<a id="type-userscope"></a>

### UserScope

A whitelist filter that restricts an actor's access to specific entities.
When present, effective permissions = role permissions ∩ user scope.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `actor` | [Actor](../actors/README.md#type-actor)! | The actor being restricted. |
| `permissionScope` | [PermissionScope](#type-permissionscope)! | The permission scope being filtered. |
| `targetEntityId` | `ID!` | The specific entity the actor can access. |
| `actions` | [[ActionPermission](#type-actionpermission)!]! | The actions allowed on this specific entity. |

---

<a id="type-actorrolepayload"></a>

### ActorRolePayload

The result of a role assignment mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRole` | [ActorRole](#type-actorrole)! | The created role assignment. |

---

<a id="type-rolepermissionpayload"></a>

### RolePermissionPayload

The result of a permission grant mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `rolePermission` | [RolePermission](#type-rolepermission)! | The created permission. |

---

<a id="type-userscopepayload"></a>

### UserScopePayload

The result of a user scope mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScope` | [UserScope](#type-userscope)! | The created user scope restriction. |

---

<a id="type-rolepayload"></a>

### RolePayload

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](#type-role)! | The created or updated role. |

---

## Inputs

<a id="type-actorrolefilter"></a>

### ActorRoleFilter

Filtering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean` | Include expired role assignments. |

---

<a id="type-actorroleorder"></a>

### ActorRoleOrder

Ordering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField](#type-actorroleorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-rolepermissionfilter"></a>

### RolePermissionFilter

Filtering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

---

<a id="type-rolepermissionorder"></a>

### RolePermissionOrder

Ordering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [RolePermissionOrderField](#type-rolepermissionorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-userscopefilter"></a>

### UserScopeFilter

Filtering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

---

<a id="type-userscopeorder"></a>

### UserScopeOrder

Ordering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [UserScopeOrderField](#type-userscopeorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-roleassigninput"></a>

### RoleAssignInput

Input for assigning a role to an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID (user or integration). |
| `roleId` | `ID!` | The role ID to assign. |
| `expireDate` | `DateTime` | The expiration date. Null means the role is permanent. |

---

<a id="type-rolerevokeinput"></a>

### RoleRevokeInput

Input for revoking a role from an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

---

<a id="type-permissiongrantinput"></a>

### PermissionGrantInput

Input for granting a permission to a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleId` | `ID!` | The role ID. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID` | The specific entity ID. Null means all entities of the type. |
| `actions` | [[ActionPermission](#type-actionpermission)!]! | The actions to allow. |

---

<a id="type-permissionrevokeinput"></a>

### PermissionRevokeInput

Input for revoking a permission from a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

---

<a id="type-userscopesetinput"></a>

### UserScopeSetInput

Input for setting a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID to restrict. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID!` | The specific entity ID to allow access to. |
| `actions` | [[ActionPermission](#type-actionpermission)!]! | The actions to allow. |

---

<a id="type-userscoperemoveinput"></a>

### UserScopeRemoveInput

Input for removing a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

---

<a id="type-rolecreateinput"></a>

### RoleCreateInput

Input for creating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-roleupdateinput"></a>

### RoleUpdateInput

Input for updating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

## Enums

<a id="type-actionpermission"></a>

### ActionPermission

Permission actions that can be granted to actors for entity operations.

| Value | Description |
| ----- | ----------- |
| `READ` | Permission to view entities and their data. |
| `CREATE` | Permission to create new entities. |
| `UPDATE` | Permission to modify existing entities. |
| `DELETE` | Permission to delete entities. |

---

<a id="type-actorroleorderfield"></a>

### ActorRoleOrderField

Fields available for ordering actor roles.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

---

<a id="type-rolepermissionorderfield"></a>

### RolePermissionOrderField

Fields available for ordering role permissions.

| Value | Description |
| ----- | ----------- |
| `GRANTED_AT` | Order by grant date. |

---

<a id="type-userscopeorderfield"></a>

### UserScopeOrderField

Fields available for ordering user scopes.

| Value | Description |
| ----- | ----------- |
| `ID` | Order by ID. |

---

## Pagination types

<a id="type-roleconnection"></a>

### RoleConnection

A paginated list of Role items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RoleEdge](#type-roleedge)!]! | A list of edges. |
| `nodes` | [[Role](#type-role)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-roleedge"></a>

### RoleEdge

An edge in the Role connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Role](#type-role)! | The role at the end of the edge. |

---

<a id="type-actorroleconnection"></a>

### ActorRoleConnection

A paginated list of ActorRole items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ActorRoleEdge](#type-actorroleedge)!]! | A list of edges. |
| `nodes` | [[ActorRole](#type-actorrole)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-actorroleedge"></a>

### ActorRoleEdge

An edge in the ActorRole connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [ActorRole](#type-actorrole)! | The actor role at the end of the edge. |

---

<a id="type-rolepermissionconnection"></a>

### RolePermissionConnection

A paginated list of RolePermission items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[RolePermissionEdge](#type-rolepermissionedge)!]! | A list of edges. |
| `nodes` | [[RolePermission](#type-rolepermission)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-rolepermissionedge"></a>

### RolePermissionEdge

An edge in the RolePermission connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [RolePermission](#type-rolepermission)! | The role permission at the end of the edge. |

---

<a id="type-userscopeconnection"></a>

### UserScopeConnection

A paginated list of UserScope items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserScopeEdge](#type-userscopeedge)!]! | A list of edges. |
| `nodes` | [[UserScope](#type-userscope)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-userscopeedge"></a>

### UserScopeEdge

An edge in the UserScope connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [UserScope](#type-userscope)! | The user scope at the end of the edge. |

---
