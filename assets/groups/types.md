# Asset groups — Types

## Objects

### AssetGroupType

A type for asset groups with membership constraints.

**Implements:** [CatalogItem](../../catalogs/README.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](#assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

---

### AssetGroupTypeConstraint

A constraint defining which asset types can be included in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType](../types.md#assettype)! | The asset type allowed in the group. |
| `maxItems` | `Int` | The maximum number of assets of this type allowed in one group. Null means unlimited. |

---

### AssetGroup

A group of assets.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](#assetgrouptype)! | The group type with membership constraints. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](#assetgroupitemconnection)! | The full membership history for this group. |

---

### AssetGroupItem

A record of an asset's membership in a group.

**Implements:** [Node](../../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `group` | [AssetGroup](#assetgroup)! | The group containing the asset. |
| `asset` | [Asset](../types.md#asset)! | The asset in the group. |
| `attachedAt` | `DateTime!` | The date and time when the asset was added to the group. |
| `detachedAt` | `DateTime` | The date and time when the asset was removed from the group. Null means the asset is currently attached. |

---

### AssetGroupPayload

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](#assetgroup)! | The created or updated asset group. |

---

### AssetGroupItemPayload

The result of an asset group item mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupItem` | [AssetGroupItem](#assetgroupitem)! | The created group membership record. |

---

### AssetGroupTypePayload

The result of an asset group type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupType` | [AssetGroupType](#assetgrouptype)! | The created or updated asset group type. |

---

## Inputs

### AssetGroupFilter

Filtering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by group types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

### AssetGroupOrder

Ordering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupOrderField](#assetgrouporderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### AssetGroupItemFilter

Filtering options for asset group items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `activeOnly` | `Boolean` | If true, return only currently attached items. |

---

### AssetGroupItemOrder

Ordering options for asset group items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupItemOrderField](#assetgroupitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### AssetGroupCreateInput

Input for creating a new asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the group. |
| `typeId` | `ID!` | The group type ID. |
| `title` | `String!` | The group display name. |
| `color` | `HexColorCode` | The color for UI display. |

---

### AssetGroupUpdateInput

Input for updating an existing asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `color` | `HexColorCode` | The new color. |

---

### AssetGroupDeleteInput

Input for deleting an asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### AssetGroupItemAddInput

Input for adding an asset to a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to add. |

---

### AssetGroupItemRemoveInput

Input for removing an asset from a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to remove. |

---

### AssetGroupTypeCreateInput

Input for creating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](#assetgrouptypeconstraintinput)!] | The allowed asset types with optional limits. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### AssetGroupTypeUpdateInput

Input for updating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](#assetgrouptypeconstraintinput)!] | Replace allowed asset types. Null means no change. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### AssetGroupTypeConstraintInput

Input for a constraint defining allowed asset types in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetTypeId` | `ID!` | The asset type ID. |
| `maxItems` | `Int` | The maximum assets of this type. Null means unlimited. |

---

## Enums

### AssetGroupOrderField

Fields available for ordering asset groups.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

### AssetGroupItemOrderField

Fields available for ordering asset group items.

| Value | Description |
| ----- | ----------- |
| `ATTACHED_AT` | Order by attachment date. |

---

## Pagination types

### AssetGroupConnection

A paginated list of AssetGroup items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupEdge](#assetgroupedge)!]! | A list of edges. |
| `nodes` | [[AssetGroup](#assetgroup)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### AssetGroupEdge

An edge in the AssetGroup connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetGroup](#assetgroup)! | The asset group at the end of the edge. |

---

### AssetGroupItemConnection

A paginated list of AssetGroupItem items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupItemEdge](#assetgroupitemedge)!]! | A list of edges. |
| `nodes` | [[AssetGroupItem](#assetgroupitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### AssetGroupItemEdge

An edge in the AssetGroupItem connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetGroupItem](#assetgroupitem)! | The asset group item at the end of the edge. |

---

### AssetGroupTypeConnection

A paginated list of AssetGroupType items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupTypeEdge](#assetgrouptypeedge)!]! | A list of edges. |
| `nodes` | [[AssetGroupType](#assetgrouptype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### AssetGroupTypeEdge

An edge in the AssetGroupType connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetGroupType](#assetgrouptype)! | The asset group type at the end of the edge. |

---
