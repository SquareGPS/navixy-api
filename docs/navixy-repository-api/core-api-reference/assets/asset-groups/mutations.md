# Mutations

### assetGroupCreate

Creates a new asset group.

```graphql
assetGroupCreate(
  input: AssetGroupCreateInput!
): AssetGroupPayload
```

**Arguments**

| Name    | Type                                                     | Description                                    |
| ------- | -------------------------------------------------------- | ---------------------------------------------- |
| `input` | [AssetGroupCreateInput](types.md#assetgroupcreateinput)! | The input fields for creating the asset group. |

**Input types:**

<details>

<summary><code>AssetGroupCreateInput</code></summary>

| Field            | Type                                                   | Description                               |
| ---------------- | ------------------------------------------------------ | ----------------------------------------- |
| `organizationId` | `ID!`                                                  | The organization that will own the group. |
| `typeId`         | `ID!`                                                  | The group type ID.                        |
| `title`          | `String!`                                              | The group display name.                   |
| `color`          | [HexColorCode](../../common-resources.md#hexcolorcode) | The color for UI display.                 |

</details>

**Output types:**

<details>

<summary><code>AssetGroupPayload</code></summary>

| Field        | Type                               | Description                         |
| ------------ | ---------------------------------- | ----------------------------------- |
| `assetGroup` | [AssetGroup](types.md#assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary><code>AssetGroup (entity)</code></summary>

| Field           | Type                                                                      | Description                                     |
| --------------- | ------------------------------------------------------------------------- | ----------------------------------------------- |
| `id`            | `ID!`                                                                     |                                                 |
| `version`       | `Int!`                                                                    |                                                 |
| `title`         | `String!`                                                                 |                                                 |
| `organization`  | [Organization](../../organizations/#organization)!                        | The organization that owns this group.          |
| `type`          | [AssetGroupType](../../../catalogs/entity-types/types.md#assetgrouptype)! | The group type with membership constraints.     |
| `color`         | [HexColorCode](../../common-resources.md#hexcolorcode)                    | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../#assetconnection)!                                   | The assets currently in this group.             |
| `history`       | [AssetGroupItemConnection](types.md#assetgroupitemconnection)!            | The full membership history for this group.     |

</details>

### assetGroupUpdate

Updates an existing asset group.

```graphql
assetGroupUpdate(
  input: AssetGroupUpdateInput!
): AssetGroupPayload
```

**Arguments**

| Name    | Type                                                     | Description                                    |
| ------- | -------------------------------------------------------- | ---------------------------------------------- |
| `input` | [AssetGroupUpdateInput](types.md#assetgroupupdateinput)! | The input fields for updating the asset group. |

**Input types:**

<details>

<summary><code>AssetGroupUpdateInput</code></summary>

| Field     | Type                                                   | Description                                 |
| --------- | ------------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                                  | The asset group ID to update.               |
| `version` | `Int!`                                                 | The current version for optimistic locking. |
| `title`   | `String`                                               | The new display name.                       |
| `color`   | [HexColorCode](../../common-resources.md#hexcolorcode) | The new color.                              |

</details>

**Output types:**

<details>

<summary><code>AssetGroupPayload</code></summary>

| Field        | Type                               | Description                         |
| ------------ | ---------------------------------- | ----------------------------------- |
| `assetGroup` | [AssetGroup](types.md#assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary><code>AssetGroup (entity)</code></summary>

| Field           | Type                                                                      | Description                                     |
| --------------- | ------------------------------------------------------------------------- | ----------------------------------------------- |
| `id`            | `ID!`                                                                     |                                                 |
| `version`       | `Int!`                                                                    |                                                 |
| `title`         | `String!`                                                                 |                                                 |
| `organization`  | [Organization](../../organizations/#organization)!                        | The organization that owns this group.          |
| `type`          | [AssetGroupType](../../../catalogs/entity-types/types.md#assetgrouptype)! | The group type with membership constraints.     |
| `color`         | [HexColorCode](../../common-resources.md#hexcolorcode)                    | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../#assetconnection)!                                   | The assets currently in this group.             |
| `history`       | [AssetGroupItemConnection](types.md#assetgroupitemconnection)!            | The full membership history for this group.     |

</details>

### assetGroupDelete

Deletes an asset group.

```graphql
assetGroupDelete(
  input: AssetGroupDeleteInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                     | Description                                    |
| ------- | -------------------------------------------------------- | ---------------------------------------------- |
| `input` | [AssetGroupDeleteInput](types.md#assetgroupdeleteinput)! | The input fields for deleting the asset group. |

**Input types:**

<details>

<summary><code>AssetGroupDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The asset group ID to delete.               |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### assetGroupItemAdd

Adds an asset to a group.

```graphql
assetGroupItemAdd(
  input: AssetGroupItemAddInput!
): AssetGroupItemPayload
```

**Arguments**

| Name    | Type                                                       | Description                                         |
| ------- | ---------------------------------------------------------- | --------------------------------------------------- |
| `input` | [AssetGroupItemAddInput](types.md#assetgroupitemaddinput)! | The input fields for adding the asset to the group. |

**Input types:**

<details>

<summary><code>AssetGroupItemAddInput</code></summary>

| Field     | Type  | Description          |
| --------- | ----- | -------------------- |
| `groupId` | `ID!` | The group ID.        |
| `assetId` | `ID!` | The asset ID to add. |

</details>

**Output types:**

<details>

<summary><code>AssetGroupItemPayload</code></summary>

| Field            | Type                                       | Description                          |
| ---------------- | ------------------------------------------ | ------------------------------------ |
| `assetGroupItem` | [AssetGroupItem](types.md#assetgroupitem)! | The created group membership record. |

</details>

<details>

<summary><code>AssetGroupItem (entity)</code></summary>

| Field        | Type                                            | Description                                                                                              |
| ------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `id`         | `ID!`                                           |                                                                                                          |
| `group`      | [AssetGroup](types.md#assetgroup)!              | The group containing the asset.                                                                          |
| `asset`      | [Asset](../#asset)!                             | The asset in the group.                                                                                  |
| `attachedAt` | [DateTime](../../common-resources.md#datetime)! | The date and time when the asset was added to the group.                                                 |
| `detachedAt` | [DateTime](../../common-resources.md#datetime)  | The date and time when the asset was removed from the group. Null means the asset is currently attached. |

</details>

### assetGroupItemRemove

Removes an asset from a group.

```graphql
assetGroupItemRemove(
  input: AssetGroupItemRemoveInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                             | Description                                             |
| ------- | ---------------------------------------------------------------- | ------------------------------------------------------- |
| `input` | [AssetGroupItemRemoveInput](types.md#assetgroupitemremoveinput)! | The input fields for removing the asset from the group. |

**Input types:**

<details>

<summary><code>AssetGroupItemRemoveInput</code></summary>

| Field     | Type  | Description             |
| --------- | ----- | ----------------------- |
| `groupId` | `ID!` | The group ID.           |
| `assetId` | `ID!` | The asset ID to remove. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### assetGroupTypeCreate

Creates a new asset group type.

```graphql
assetGroupTypeCreate(
  input: AssetGroupTypeCreateInput!
): AssetGroupTypePayload
```

**Arguments**

| Name    | Type                                                                                            | Description                                         |
| ------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `input` | [AssetGroupTypeCreateInput](../../../catalogs/entity-types/types.md#assetgrouptypecreateinput)! | The input fields for creating the asset group type. |

**Input types:**

<details>

<summary><code>AssetGroupTypeCreateInput</code></summary>

| Field               | Type                                                                                                       | Description                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `organizationId`    | `ID!`                                                                                                      | The organization that will own the item.      |
| `code`              | [Code](../../common-resources.md#code)!                                                                    | The machine-readable code.                    |
| `title`             | `String!`                                                                                                  | The display name.                             |
| `order`             | `Int`                                                                                                      | The display order.                            |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraintInput](../../../catalogs/entity-types/types.md#assetgrouptypeconstraintinput)!] | The allowed asset types with optional limits. |
| `meta`              | [CatalogItemMetaInput](../../../catalogs/#catalogitemmetainput)                                            | The display properties.                       |

</details>

<details>

<summary><code>AssetGroupTypeConstraintInput</code></summary>

| Field         | Type  | Description                                            |
| ------------- | ----- | ------------------------------------------------------ |
| `assetTypeId` | `ID!` | The asset type ID.                                     |
| `maxItems`    | `Int` | The maximum assets of this type. Null means unlimited. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field             | Type                                                   | Description                                       |
| ----------------- | ------------------------------------------------------ | ------------------------------------------------- |
| `description`     | `String`                                               | The description.                                  |
| `hidden`          | `Boolean`                                              | Whether the item is hidden from regular UI lists. |
| `textColor`       | [HexColorCode](../../common-resources.md#hexcolorcode) | The text color for UI display.                    |
| `backgroundColor` | [HexColorCode](../../common-resources.md#hexcolorcode) | The background color for UI display.              |
| `icon`            | `String`                                               | A relative URL to the icon.                       |

</details>

**Output types:**

<details>

<summary><code>AssetGroupTypePayload</code></summary>

| Field            | Type                                                                      | Description                              |
| ---------------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| `assetGroupType` | [AssetGroupType](../../../catalogs/entity-types/types.md#assetgrouptype)! | The created or updated asset group type. |

</details>

<details>

<summary><code>AssetGroupType (entity)</code></summary>

| Field               | Type                                                                                              | Description                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `id`                | `ID!`                                                                                             |                                                                                |
| `version`           | `Int!`                                                                                            |                                                                                |
| `title`             | `String!`                                                                                         |                                                                                |
| `code`              | [Code](../../common-resources.md#code)!                                                           |                                                                                |
| `order`             | `Int!`                                                                                            |                                                                                |
| `catalog`           | [Catalog](../../organizations/#catalog)!                                                          |                                                                                |
| `organization`      | [Organization](../../organizations/#organization)                                                 |                                                                                |
| `meta`              | [CatalogItemMeta](../../../catalogs/#catalogitemmeta)!                                            |                                                                                |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraint](../../../catalogs/entity-types/types.md#assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

### assetGroupTypeUpdate

Updates an asset group type.

```graphql
assetGroupTypeUpdate(
  input: AssetGroupTypeUpdateInput!
): AssetGroupTypePayload
```

**Arguments**

| Name    | Type                                                                                            | Description                                         |
| ------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `input` | [AssetGroupTypeUpdateInput](../../../catalogs/entity-types/types.md#assetgrouptypeupdateinput)! | The input fields for updating the asset group type. |

**Input types:**

<details>

<summary><code>AssetGroupTypeUpdateInput</code></summary>

| Field               | Type                                                                                                       | Description                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `id`                | `ID!`                                                                                                      | The item ID to update.                             |
| `version`           | `Int!`                                                                                                     | The current version for optimistic locking.        |
| `title`             | `String`                                                                                                   | The new display name.                              |
| `order`             | `Int`                                                                                                      | The new display order.                             |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraintInput](../../../catalogs/entity-types/types.md#assetgrouptypeconstraintinput)!] | Replace allowed asset types. Null means no change. |
| `meta`              | [CatalogItemMetaInput](../../../catalogs/#catalogitemmetainput)                                            | The display properties.                            |

</details>

<details>

<summary><code>AssetGroupTypeConstraintInput</code></summary>

| Field         | Type  | Description                                            |
| ------------- | ----- | ------------------------------------------------------ |
| `assetTypeId` | `ID!` | The asset type ID.                                     |
| `maxItems`    | `Int` | The maximum assets of this type. Null means unlimited. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

| Field             | Type                                                   | Description                                       |
| ----------------- | ------------------------------------------------------ | ------------------------------------------------- |
| `description`     | `String`                                               | The description.                                  |
| `hidden`          | `Boolean`                                              | Whether the item is hidden from regular UI lists. |
| `textColor`       | [HexColorCode](../../common-resources.md#hexcolorcode) | The text color for UI display.                    |
| `backgroundColor` | [HexColorCode](../../common-resources.md#hexcolorcode) | The background color for UI display.              |
| `icon`            | `String`                                               | A relative URL to the icon.                       |

</details>

**Output types:**

<details>

<summary><code>AssetGroupTypePayload</code></summary>

| Field            | Type                                                                      | Description                              |
| ---------------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| `assetGroupType` | [AssetGroupType](../../../catalogs/entity-types/types.md#assetgrouptype)! | The created or updated asset group type. |

</details>

<details>

<summary><code>AssetGroupType (entity)</code></summary>

| Field               | Type                                                                                              | Description                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `id`                | `ID!`                                                                                             |                                                                                |
| `version`           | `Int!`                                                                                            |                                                                                |
| `title`             | `String!`                                                                                         |                                                                                |
| `code`              | [Code](../../common-resources.md#code)!                                                           |                                                                                |
| `order`             | `Int!`                                                                                            |                                                                                |
| `catalog`           | [Catalog](../../organizations/#catalog)!                                                          |                                                                                |
| `organization`      | [Organization](../../organizations/#organization)                                                 |                                                                                |
| `meta`              | [CatalogItemMeta](../../../catalogs/#catalogitemmeta)!                                            |                                                                                |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraint](../../../catalogs/entity-types/types.md#assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

### assetGroupTypeDelete

Deletes an asset group type.

```graphql
assetGroupTypeDelete(
  input: CatalogItemDeleteInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                                 | Description                                         |
| ------- | -------------------------------------------------------------------- | --------------------------------------------------- |
| `input` | [CatalogItemDeleteInput](../../../catalogs/#catalogitemdeleteinput)! | The input fields for deleting the asset group type. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The catalog item ID to delete.              |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>
