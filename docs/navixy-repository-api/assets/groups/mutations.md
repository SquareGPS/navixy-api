# Asset groups — Mutations

{% include "../../.gitbook/includes/navixy-repository-api-is-a-....md" %}

### assetGroupCreate

Creates a new asset group.

```graphql
assetGroupCreate(
    input: AssetGroupCreateInput!
  ): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupCreateInput!` | The input fields for creating the asset group. |

**Input types:**

<details>

<summary>AssetGroupCreateInput</summary>

Input for creating a new asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the group. |
| `typeId` | `ID` | The group type ID. Immutable after creation. |
| `title` | `String!` | The group display name. |
| `color` | `HexColorCode` | The color for UI display. |
| `assetIds` | `[ID!]` | Initial list of asset IDs to add to the group. |

</details>

**Output types:**

<details>

<summary>AssetGroupPayload</summary>

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](types.md#type-assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary>AssetGroup (entity)</summary>

A group of assets.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#type-organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#type-assetgrouptype) | The group type with membership constraints. Immutable after creation. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#type-assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](types.md#type-assetgroupitemconnection)! | The full membership history for this group. |

</details>

---

### assetGroupUpdate

Updates an existing asset group.

```graphql
assetGroupUpdate(
    input: AssetGroupUpdateInput!
  ): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupUpdateInput!` | The input fields for updating the asset group. |

**Input types:**

<details>

<summary>AssetGroupUpdateInput</summary>

Input for updating an existing asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `color` | `HexColorCode` | The new color. |
| `assetIds` | `[ID!]` | Full replacement list of asset IDs in the group. If provided, replaces all current memberships. |

</details>

**Output types:**

<details>

<summary>AssetGroupPayload</summary>

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](types.md#type-assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary>AssetGroup (entity)</summary>

A group of assets.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#type-organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#type-assetgrouptype) | The group type with membership constraints. Immutable after creation. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#type-assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](types.md#type-assetgroupitemconnection)! | The full membership history for this group. |

</details>

---

### assetGroupDelete

Deletes an asset group.

```graphql
assetGroupDelete(
    input: AssetGroupDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupDeleteInput!` | The input fields for deleting the asset group. |

**Input types:**

<details>

<summary>AssetGroupDeleteInput</summary>

Input for deleting an asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

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

### assetGroupItemsAdd

Adds assets to a group.

```graphql
assetGroupItemsAdd(
    input: AssetGroupItemsAddInput!
  ): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupItemsAddInput!` | The input fields for adding assets to the group. |

**Input types:**

<details>

<summary>AssetGroupItemsAddInput</summary>

Input for adding assets to a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetIds` | `[ID!]!` | The asset IDs to add. |

</details>

**Output types:**

<details>

<summary>AssetGroupPayload</summary>

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](types.md#type-assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary>AssetGroup (entity)</summary>

A group of assets.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#type-organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#type-assetgrouptype) | The group type with membership constraints. Immutable after creation. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#type-assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](types.md#type-assetgroupitemconnection)! | The full membership history for this group. |

</details>

---

### assetGroupItemsRemove

Removes assets from a group.

```graphql
assetGroupItemsRemove(
    input: AssetGroupItemsRemoveInput!
  ): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupItemsRemoveInput!` | The input fields for removing assets from the group. |

**Input types:**

<details>

<summary>AssetGroupItemsRemoveInput</summary>

Input for removing assets from a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetIds` | `[ID!]!` | The asset IDs to remove. |

</details>

**Output types:**

<details>

<summary>AssetGroupPayload</summary>

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](types.md#type-assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary>AssetGroup (entity)</summary>

A group of assets.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#type-organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#type-assetgrouptype) | The group type with membership constraints. Immutable after creation. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#type-assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](types.md#type-assetgroupitemconnection)! | The full membership history for this group. |

</details>

---

### assetGroupTypeCreate

Creates a new asset group type.

```graphql
assetGroupTypeCreate(
    input: AssetGroupTypeCreateInput!
  ): AssetGroupTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupTypeCreateInput!` | The input fields for creating the asset group type. |

**Input types:**

<details>

<summary>AssetGroupTypeCreateInput</summary>

Input for creating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](types.md#type-assetgrouptypeconstraintinput)!] | The allowed asset types with optional limits. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>AssetGroupTypeConstraintInput</summary>

Input for a constraint defining allowed asset types in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetTypeId` | `ID!` | The asset type ID. |
| `maxItems` | `Int` | The maximum assets of this type. Null means unlimited. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

**Output types:**

<details>

<summary>AssetGroupTypePayload</summary>

The result of an asset group type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupType` | [AssetGroupType](types.md#type-assetgrouptype)! | The created or updated asset group type. |

</details>

<details>

<summary>AssetGroupType (entity)</summary>

A type for asset groups with membership constraints.

**Implements:** [CatalogItem](../../catalogs/catalog-items.md#type-catalogitem), [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](types.md#type-assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

---

### assetGroupTypeUpdate

Updates an asset group type.

```graphql
assetGroupTypeUpdate(
    input: AssetGroupTypeUpdateInput!
  ): AssetGroupTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupTypeUpdateInput!` | The input fields for updating the asset group type. |

**Input types:**

<details>

<summary>AssetGroupTypeUpdateInput</summary>

Input for updating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](types.md#type-assetgrouptypeconstraintinput)!] | Replace allowed asset types. Null means no change. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>AssetGroupTypeConstraintInput</summary>

Input for a constraint defining allowed asset types in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetTypeId` | `ID!` | The asset type ID. |
| `maxItems` | `Int` | The maximum assets of this type. Null means unlimited. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

**Output types:**

<details>

<summary>AssetGroupTypePayload</summary>

The result of an asset group type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupType` | [AssetGroupType](types.md#type-assetgrouptype)! | The created or updated asset group type. |

</details>

<details>

<summary>AssetGroupType (entity)</summary>

A type for asset groups with membership constraints.

**Implements:** [CatalogItem](../../catalogs/catalog-items.md#type-catalogitem), [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](types.md#type-assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

---

### assetGroupTypeDelete

Deletes an asset group type.

```graphql
assetGroupTypeDelete(
    input: CatalogItemDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the asset group type. |

**Input types:**

<details>

<summary>CatalogItemDeleteInput</summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

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
