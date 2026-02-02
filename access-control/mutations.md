# Mutations

### roleAssign

Assigns a role to an actor.

```graphql
roleAssign(input: RoleAssignInput!): ActorRolePayload
```

**Arguments**

| Name    | Type                                         | Description                              |
| ------- | -------------------------------------------- | ---------------------------------------- |
| `input` | [RoleAssignInput](types.md#roleassigninput)! | The input fields for assigning the role. |

**Input types:**

<details>

<summary><code>RoleAssignInput</code></summary>

| Field        | Type                                                           | Description                                            |
| ------------ | -------------------------------------------------------------- | ------------------------------------------------------ |
| `actorId`    | `ID!`                                                          | The actor ID (user or integration).                    |
| `roleId`     | `ID!`                                                          | The role ID to assign.                                 |
| `expireDate` | [DateTime](../core-api-reference/common-resources.md#datetime) | The expiration date. Null means the role is permanent. |

</details>

**Output types:**

<details>

<summary><code>ActorRolePayload</code></summary>

| Field       | Type                             | Description                  |
| ----------- | -------------------------------- | ---------------------------- |
| `actorRole` | [ActorRole](types.md#actorrole)! | The created role assignment. |

</details>

<details>

<summary><code>ActorRole (entity)</code></summary>

| Field        | Type                                                            | Description                                                                |
| ------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`         | `ID!`                                                           |                                                                            |
| `actor`      | [Actor](types.md#actor)!                                        | The actor receiving the role.                                              |
| `role`       | [Role](../catalogs/roles.md#role)!                              | The role being assigned.                                                   |
| `assignedAt` | [DateTime](../core-api-reference/common-resources.md#datetime)! | The date and time when the role was assigned.                              |
| `assignedBy` | [Actor](types.md#actor)                                         | The actor who assigned the role.                                           |
| `expireDate` | [DateTime](../core-api-reference/common-resources.md#datetime)  | The date and time when the role expires. Null means the role is permanent. |

</details>

### roleRevoke

Revokes a role from an actor.

```graphql
roleRevoke(input: RoleRevokeInput!): DeletePayload
```

**Arguments**

| Name    | Type                                         | Description                             |
| ------- | -------------------------------------------- | --------------------------------------- |
| `input` | [RoleRevokeInput](types.md#rolerevokeinput)! | The input fields for revoking the role. |

**Input types:**

<details>

<summary><code>RoleRevokeInput</code></summary>

| Field         | Type  | Description                             |
| ------------- | ----- | --------------------------------------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### permissionGrant

Grants a permission to a role.

```graphql
permissionGrant(
  input: PermissionGrantInput!
): RolePermissionPayload
```

**Arguments**

| Name    | Type                                                   | Description                                   |
| ------- | ------------------------------------------------------ | --------------------------------------------- |
| `input` | [PermissionGrantInput](types.md#permissiongrantinput)! | The input fields for granting the permission. |

**Input types:**

<details>

<summary><code>PermissionGrantInput</code></summary>

| Field               | Type                                               | Description                                                  |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| `roleId`            | `ID!`                                              | The role ID.                                                 |
| `permissionScopeId` | `ID!`                                              | The permission scope ID.                                     |
| `targetEntityId`    | `ID`                                               | The specific entity ID. Null means all entities of the type. |
| `actions`           | \[[ActionPermission](types.md#actionpermission)!]! | The actions to allow.                                        |

</details>

**Output types:**

<details>

<summary><code>RolePermissionPayload</code></summary>

| Field            | Type                                       | Description             |
| ---------------- | ------------------------------------------ | ----------------------- |
| `rolePermission` | [RolePermission](types.md#rolepermission)! | The created permission. |

</details>

<details>

<summary><code>RolePermission (entity)</code></summary>

| Field             | Type                                                            | Description                                                                             |
| ----------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`              | `ID!`                                                           |                                                                                         |
| `role`            | [Role](../catalogs/roles.md#role)!                              | The role receiving the permission.                                                      |
| `permissionScope` | [PermissionScope](../catalogs/roles.md#permissionscope)!        | The permission scope being granted.                                                     |
| `targetEntityId`  | `ID`                                                            | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions`         | \[[ActionPermission](types.md#actionpermission)!]!              | The actions allowed by this permission.                                                 |
| `grantedAt`       | [DateTime](../core-api-reference/common-resources.md#datetime)! | The date and time when the permission was granted.                                      |
| `grantedBy`       | [Actor](types.md#actor)!                                        | The actor who granted the permission.                                                   |

</details>

### permissionRevoke

Revokes a permission from a role.

```graphql
permissionRevoke(
  input: PermissionRevokeInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                     | Description                                   |
| ------- | -------------------------------------------------------- | --------------------------------------------- |
| `input` | [PermissionRevokeInput](types.md#permissionrevokeinput)! | The input fields for revoking the permission. |

**Input types:**

<details>

<summary><code>PermissionRevokeInput</code></summary>

| Field          | Type  | Description                       |
| -------------- | ----- | --------------------------------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### userScopeSet

Sets a user scope restriction.

```graphql
userScopeSet(input: UserScopeSetInput!): UserScopePayload
```

**Arguments**

| Name    | Type                                             | Description                                  |
| ------- | ------------------------------------------------ | -------------------------------------------- |
| `input` | [UserScopeSetInput](types.md#userscopesetinput)! | The input fields for setting the user scope. |

**Input types:**

<details>

<summary><code>UserScopeSetInput</code></summary>

| Field               | Type                                               | Description                                |
| ------------------- | -------------------------------------------------- | ------------------------------------------ |
| `actorId`           | `ID!`                                              | The actor ID to restrict.                  |
| `permissionScopeId` | `ID!`                                              | The permission scope ID.                   |
| `targetEntityId`    | `ID!`                                              | The specific entity ID to allow access to. |
| `actions`           | \[[ActionPermission](types.md#actionpermission)!]! | The actions to allow.                      |

</details>

**Output types:**

<details>

<summary><code>UserScopePayload</code></summary>

| Field       | Type                             | Description                         |
| ----------- | -------------------------------- | ----------------------------------- |
| `userScope` | [UserScope](types.md#userscope)! | The created user scope restriction. |

</details>

<details>

<summary><code>UserScope (entity)</code></summary>

| Field             | Type                                                     | Description                                  |
| ----------------- | -------------------------------------------------------- | -------------------------------------------- |
| `id`              | `ID!`                                                    |                                              |
| `actor`           | [Actor](types.md#actor)!                                 | The actor being restricted.                  |
| `permissionScope` | [PermissionScope](../catalogs/roles.md#permissionscope)! | The permission scope being filtered.         |
| `targetEntityId`  | `ID!`                                                    | The specific entity the actor can access.    |
| `actions`         | \[[ActionPermission](types.md#actionpermission)!]!       | The actions allowed on this specific entity. |

</details>

### userScopeRemove

Removes a user scope restriction.

```graphql
userScopeRemove(
  input: UserScopeRemoveInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                   | Description                                   |
| ------- | ------------------------------------------------------ | --------------------------------------------- |
| `input` | [UserScopeRemoveInput](types.md#userscoperemoveinput)! | The input fields for removing the user scope. |

**Input types:**

<details>

<summary><code>UserScopeRemoveInput</code></summary>

| Field         | Type  | Description                  |
| ------------- | ----- | ---------------------------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>
