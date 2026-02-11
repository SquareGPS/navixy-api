# Asset groups — Mutations

### assetGroupCreate

Creates a new asset group.

```graphql
assetGroupCreate(input: AssetGroupCreateInput!): AssetGroupPayload
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
| `typeId` | `ID!` | The group type ID. |
| `title` | `String!` | The group display name. |
| `color` | `HexColorCode` | The color for UI display. |

</details>

**Output types:**

<details>

<summary>AssetGroupPayload</summary>

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](types.md#assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary>AssetGroup (entity)</summary>

A group of assets.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#assetgrouptype)! | The group type with membership constraints. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `filter` | [AssetFilter](../types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [AssetGroupItemFilter](types.md#assetgroupitemfilter) | Filtering options for the returned history. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetGroupItemOrder = { field: ATTACHED_AT, direction: DESC }` | The ordering options for the returned history. |

</details>

---

### assetGroupUpdate

Updates an existing asset group.

```graphql
assetGroupUpdate(input: AssetGroupUpdateInput!): AssetGroupPayload
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
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `color` | `HexColorCode` | The new color. |

</details>

**Output types:**

<details>

<summary>AssetGroupPayload</summary>

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](types.md#assetgroup)! | The created or updated asset group. |

</details>

<details>

<summary>AssetGroup (entity)</summary>

A group of assets.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](types.md#assetgrouptype)! | The group type with membership constraints. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `filter` | [AssetFilter](../types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [AssetGroupItemFilter](types.md#assetgroupitemfilter) | Filtering options for the returned history. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetGroupItemOrder = { field: ATTACHED_AT, direction: DESC }` | The ordering options for the returned history. |

</details>

---

### assetGroupDelete

Deletes an asset group.

```graphql
assetGroupDelete(input: AssetGroupDeleteInput!): DeletePayload
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

### assetGroupItemAdd

Adds an asset to a group.

```graphql
assetGroupItemAdd(input: AssetGroupItemAddInput!): AssetGroupItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupItemAddInput!` | The input fields for adding the asset to the group. |

**Input types:**

<details>

<summary>AssetGroupItemAddInput</summary>

Input for adding an asset to a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to add. |

</details>

**Output types:**

<details>

<summary>AssetGroupItemPayload</summary>

The result of an asset group item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupItem` | [AssetGroupItem](types.md#assetgroupitem)! | The created group membership record. |

</details>

<details>

<summary>AssetGroupItem (entity)</summary>

A record of an asset's membership in a group.

**Implements:** [Node](../../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `group` | [AssetGroup](types.md#assetgroup)! | The group containing the asset. |
| `asset` | [Asset](../types.md#asset)! | The asset in the group. |
| `attachedAt` | `DateTime!` | The date and time when the asset was added to the group. |
| `detachedAt` | `DateTime` | The date and time when the asset was removed from the group. Null means the asset is currently attached. |

</details>

---

### assetGroupItemRemove

Removes an asset from a group.

```graphql
assetGroupItemRemove(input: AssetGroupItemRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupItemRemoveInput!` | The input fields for removing the asset from the group. |

**Input types:**

<details>

<summary>AssetGroupItemRemoveInput</summary>

Input for removing an asset from a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to remove. |

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

### assetGroupTypeCreate

Creates a new asset group type.

```graphql
assetGroupTypeCreate(input: AssetGroupTypeCreateInput!): AssetGroupTypePayload
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
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](types.md#assetgrouptypeconstraintinput)!] | The allowed asset types with optional limits. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

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
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>AssetGroupTypePayload</summary>

The result of an asset group type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupType` | [AssetGroupType](types.md#assetgrouptype)! | The created or updated asset group type. |

</details>

<details>

<summary>AssetGroupType (entity)</summary>

A type for asset groups with membership constraints.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](types.md#assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

---

### assetGroupTypeUpdate

Updates an asset group type.

```graphql
assetGroupTypeUpdate(input: AssetGroupTypeUpdateInput!): AssetGroupTypePayload
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
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](types.md#assetgrouptypeconstraintinput)!] | Replace allowed asset types. Null means no change. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

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
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

</details>

**Output types:**

<details>

<summary>AssetGroupTypePayload</summary>

The result of an asset group type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupType` | [AssetGroupType](types.md#assetgrouptype)! | The created or updated asset group type. |

</details>

<details>

<summary>AssetGroupType (entity)</summary>

A type for asset groups with membership constraints.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](types.md#assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

</details>

---

### assetGroupTypeDelete

Deletes an asset group type.

```graphql
assetGroupTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
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
