# Access control — Mutations

### roleAssign

Assigns a role to an actor.

```graphql
roleAssign(input: RoleAssignInput!): ActorRolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleAssignInput!` | The input fields for assigning the role. |

**Input types:**

<details>

<summary>RoleAssignInput</summary>

Input for assigning a role to an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID (user or integration). |
| `roleId` | `ID!` | The role ID to assign. |
| `expireDate` | `DateTime` | The expiration date. Null means the role is permanent. |

</details>

**Output types:**

<details>

<summary>ActorRolePayload</summary>

The result of a role assignment mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRole` | [ActorRole](types.md#actorrole)! | The created role assignment. |

</details>

<details>

<summary>ActorRole (entity)</summary>

An assignment of a role to an actor.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `actor` | [Actor](../actors/README.md#actor)! | The actor receiving the role. |
| `role` | [Role](types.md#role)! | The role being assigned. |
| `assignedAt` | `DateTime!` | The date and time when the role was assigned. |
| `assignedBy` | [Actor](../actors/README.md#actor) | The actor who assigned the role. |
| `expireDate` | `DateTime` | The date and time when the role expires. Null means the role is permanent. |

</details>

---

### roleRevoke

Revokes a role from an actor.

```graphql
roleRevoke(input: RoleRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleRevokeInput!` | The input fields for revoking the role. |

**Input types:**

<details>

<summary>RoleRevokeInput</summary>

Input for revoking a role from an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

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

### permissionGrant

Grants a permission to a role.

```graphql
permissionGrant(input: PermissionGrantInput!): RolePermissionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `PermissionGrantInput!` | The input fields for granting the permission. |

**Input types:**

<details>

<summary>PermissionGrantInput</summary>

Input for granting a permission to a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleId` | `ID!` | The role ID. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID` | The specific entity ID. Null means all entities of the type. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions to allow. |

</details>

**Output types:**

<details>

<summary>RolePermissionPayload</summary>

The result of a permission grant mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `rolePermission` | [RolePermission](types.md#rolepermission)! | The created permission. |

</details>

<details>

<summary>RolePermission (entity)</summary>

A permission granted to a role.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `role` | [Role](types.md#role)! | The role receiving the permission. |
| `permissionScope` | [PermissionScope](types.md#permissionscope)! | The permission scope being granted. |
| `targetEntityId` | `ID` | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions allowed by this permission. |
| `grantedAt` | `DateTime!` | The date and time when the permission was granted. |
| `grantedBy` | [Actor](../actors/README.md#actor)! | The actor who granted the permission. |

</details>

---

### permissionRevoke

Revokes a permission from a role.

```graphql
permissionRevoke(input: PermissionRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `PermissionRevokeInput!` | The input fields for revoking the permission. |

**Input types:**

<details>

<summary>PermissionRevokeInput</summary>

Input for revoking a permission from a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

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

### userScopeSet

Sets a user scope restriction.

```graphql
userScopeSet(input: UserScopeSetInput!): UserScopePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserScopeSetInput!` | The input fields for setting the user scope. |

**Input types:**

<details>

<summary>UserScopeSetInput</summary>

Input for setting a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID to restrict. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID!` | The specific entity ID to allow access to. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions to allow. |

</details>

**Output types:**

<details>

<summary>UserScopePayload</summary>

The result of a user scope mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScope` | [UserScope](types.md#userscope)! | The created user scope restriction. |

</details>

<details>

<summary>UserScope (entity)</summary>

A whitelist filter that restricts an actor's access to specific entities.
When present, effective permissions = role permissions ∩ user scope.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `actor` | [Actor](../actors/README.md#actor)! | The actor being restricted. |
| `permissionScope` | [PermissionScope](types.md#permissionscope)! | The permission scope being filtered. |
| `targetEntityId` | `ID!` | The specific entity the actor can access. |
| `actions` | [[ActionPermission](types.md#actionpermission)!]! | The actions allowed on this specific entity. |

</details>

---

### userScopeRemove

Removes a user scope restriction.

```graphql
userScopeRemove(input: UserScopeRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserScopeRemoveInput!` | The input fields for removing the user scope. |

**Input types:**

<details>

<summary>UserScopeRemoveInput</summary>

Input for removing a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

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

### roleCreate

Creates a new role.

```graphql
roleCreate(input: RoleCreateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleCreateInput!` | The input fields for creating the role. |

**Input types:**

<details>

<summary>RoleCreateInput</summary>

Input for creating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

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

<summary>RolePayload</summary>

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](types.md#role)! | The created or updated role. |

</details>

<details>

<summary>Role (entity)</summary>

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
| `permissions` | [RolePermissionConnection](types.md#rolepermissionconnection)! | The permissions assigned to this role. |

</details>

---

### roleUpdate

Updates a role.

```graphql
roleUpdate(input: RoleUpdateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleUpdateInput!` | The input fields for updating the role. |

**Input types:**

<details>

<summary>RoleUpdateInput</summary>

Input for updating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

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

<summary>RolePayload</summary>

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](types.md#role)! | The created or updated role. |

</details>

<details>

<summary>Role (entity)</summary>

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
| `permissions` | [RolePermissionConnection](types.md#rolepermissionconnection)! | The permissions assigned to this role. |

</details>

---

### roleDelete

Deletes a role.

```graphql
roleDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the role. |

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
