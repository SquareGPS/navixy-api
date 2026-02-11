# Access control — Mutations

### roleAssign

Assigns a role to an actor.

```graphql
roleAssign("The input fields for assigning the role." input: RoleAssignInput!): ActorRolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleAssignInput](types.md#roleassigninput)! | The input fields for assigning the role. |

**Input types:**

<details>

<summary><code>RoleAssignInput</code></summary>

Input for assigning a role to an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID (user or integration). |
| `roleId` | `ID!` | The role ID to assign. |
| `expireDate` | `DateTime` | The expiration date. Null means the role is permanent. |

</details>

**Output types:**

<details>

<summary><code>ActorRolePayload</code></summary>

The result of a role assignment mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRole` | [ActorRole](types.md#actorrole)! | The created role assignment. |

</details>

<details>

<summary><code>ActorRole (entity)</code></summary>

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

</details>

---

### roleRevoke

Revokes a role from an actor.

```graphql
roleRevoke("The input fields for revoking the role." input: RoleRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleRevokeInput](types.md#rolerevokeinput)! | The input fields for revoking the role. |

**Input types:**

<details>

<summary><code>RoleRevokeInput</code></summary>

Input for revoking a role from an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

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

### permissionGrant

Grants a permission to a role.

```graphql
permissionGrant("The input fields for granting the permission." input: PermissionGrantInput!): RolePermissionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [PermissionGrantInput](types.md#permissiongrantinput)! | The input fields for granting the permission. |

**Input types:**

<details>

<summary><code>PermissionGrantInput</code></summary>

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

<summary><code>RolePermissionPayload</code></summary>

The result of a permission grant mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `rolePermission` | [RolePermission](types.md#rolepermission)! | The created permission. |

</details>

<details>

<summary><code>RolePermission (entity)</code></summary>

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

</details>

---

### permissionRevoke

Revokes a permission from a role.

```graphql
permissionRevoke("The input fields for revoking the permission." input: PermissionRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [PermissionRevokeInput](types.md#permissionrevokeinput)! | The input fields for revoking the permission. |

**Input types:**

<details>

<summary><code>PermissionRevokeInput</code></summary>

Input for revoking a permission from a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

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

### userScopeSet

Sets a user scope restriction.

```graphql
userScopeSet("The input fields for setting the user scope." input: UserScopeSetInput!): UserScopePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserScopeSetInput](types.md#userscopesetinput)! | The input fields for setting the user scope. |

**Input types:**

<details>

<summary><code>UserScopeSetInput</code></summary>

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

<summary><code>UserScopePayload</code></summary>

The result of a user scope mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScope` | [UserScope](types.md#userscope)! | The created user scope restriction. |

</details>

<details>

<summary><code>UserScope (entity)</code></summary>

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

</details>

---

### userScopeRemove

Removes a user scope restriction.

```graphql
userScopeRemove("The input fields for removing the user scope." input: UserScopeRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserScopeRemoveInput](types.md#userscoperemoveinput)! | The input fields for removing the user scope. |

**Input types:**

<details>

<summary><code>UserScopeRemoveInput</code></summary>

Input for removing a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

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

### roleCreate

Creates a new role.

```graphql
roleCreate("The input fields for creating the role." input: RoleCreateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleCreateInput](types.md#rolecreateinput)! | The input fields for creating the role. |

**Input types:**

<details>

<summary><code>RoleCreateInput</code></summary>

Input for creating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

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

<summary><code>RolePayload</code></summary>

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](types.md#role)! | The created or updated role. |

</details>

<details>

<summary><code>Role (entity)</code></summary>

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

</details>

---

### roleUpdate

Updates a role.

```graphql
roleUpdate("The input fields for updating the role." input: RoleUpdateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleUpdateInput](types.md#roleupdateinput)! | The input fields for updating the role. |

**Input types:**

<details>

<summary><code>RoleUpdateInput</code></summary>

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

<summary><code>RolePayload</code></summary>

The result of a role mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `role` | [Role](types.md#role)! | The created or updated role. |

</details>

<details>

<summary><code>Role (entity)</code></summary>

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

</details>

---

### roleDelete

Deletes a role.

```graphql
roleDelete("The input fields for deleting the role." input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../catalogs/catalog-items.md#catalogitemdeleteinput)! | The input fields for deleting the role. |

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
