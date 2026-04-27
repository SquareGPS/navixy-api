# Asset groups — Types

{% include "../../.gitbook/includes/navixy-repository-api-is-a-....md" %}

## Objects

<a id="type-assetgrouptype"></a>

### AssetGroupType

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
| `allowedAssetTypes` | [[AssetGroupTypeConstraint](#type-assetgrouptypeconstraint)!]! | The asset types allowed in groups of this type, with optional quantity limits. |

---

<a id="type-assetgrouptypeconstraint"></a>

### AssetGroupTypeConstraint

A constraint defining which asset types can be included in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType](../types.md#type-assettype)! | The asset type allowed in the group. |
| `maxItems` | `Int` | The maximum number of assets of this type allowed in one group. Null means unlimited. |

---

<a id="type-assetgroup"></a>

### AssetGroup

A group of assets.

**Implements:** [Node](../../common.md#type-node), [Versioned](../../common.md#type-versioned), [Titled](../../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations/README.md#type-organization)! | The organization that owns this group. |
| `type` | [AssetGroupType](#type-assetgrouptype) | The group type with membership constraints. Immutable after creation. |
| `color` | `HexColorCode` | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection](../types.md#type-assetconnection)! | The assets currently in this group. |
| `history` | [AssetGroupItemConnection](#type-assetgroupitemconnection)! | The full membership history for this group. |

---

<a id="type-assetgroupitem"></a>

### AssetGroupItem

A record of an asset's membership in a group.

**Implements:** [Node](../../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `group` | [AssetGroup](#type-assetgroup)! | The group containing the asset. |
| `asset` | [Asset](../types.md#type-asset)! | The asset in the group. |
| `attachedAt` | `DateTime!` | The date and time when the asset was added to the group. |
| `detachedAt` | `DateTime` | The date and time when the asset was removed from the group. Null means the asset is currently attached. |

---

<a id="type-assetgrouppayload"></a>

### AssetGroupPayload

The result of an asset group mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroup` | [AssetGroup](#type-assetgroup)! | The created or updated asset group. |

---

<a id="type-assetgrouptypepayload"></a>

### AssetGroupTypePayload

The result of an asset group type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetGroupType` | [AssetGroupType](#type-assetgrouptype)! | The created or updated asset group type. |

---

## Inputs

<a id="type-assetgroupfilter"></a>

### AssetGroupFilter

Filtering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by group types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

<a id="type-assetgrouporder"></a>

### AssetGroupOrder

Ordering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupOrderField](#type-assetgrouporderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-assetgroupitemfilter"></a>

### AssetGroupItemFilter

Filtering options for asset group items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `activeOnly` | `Boolean` | If true, return only currently attached items. |

---

<a id="type-assetgroupitemorder"></a>

### AssetGroupItemOrder

Ordering options for asset group items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupItemOrderField](#type-assetgroupitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-assetgroupcreateinput"></a>

### AssetGroupCreateInput

Input for creating a new asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the group. |
| `typeId` | `ID` | The group type ID. Immutable after creation. |
| `title` | `String!` | The group display name. |
| `color` | `HexColorCode` | The color for UI display. |
| `assetIds` | `[ID!]` | Initial list of asset IDs to add to the group. |

---

<a id="type-assetgroupupdateinput"></a>

### AssetGroupUpdateInput

Input for updating an existing asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `color` | `HexColorCode` | The new color. |
| `assetIds` | `[ID!]` | Full replacement list of asset IDs in the group. If provided, replaces all current memberships. |

---

<a id="type-assetgroupdeleteinput"></a>

### AssetGroupDeleteInput

Input for deleting an asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

<a id="type-assetgroupitemsaddinput"></a>

### AssetGroupItemsAddInput

Input for adding assets to a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetIds` | `[ID!]!` | The asset IDs to add. |

---

<a id="type-assetgroupitemsremoveinput"></a>

### AssetGroupItemsRemoveInput

Input for removing assets from a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetIds` | `[ID!]!` | The asset IDs to remove. |

---

<a id="type-assetgrouptypecreateinput"></a>

### AssetGroupTypeCreateInput

Input for creating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](#type-assetgrouptypeconstraintinput)!] | The allowed asset types with optional limits. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-assetgrouptypeupdateinput"></a>

### AssetGroupTypeUpdateInput

Input for updating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput](#type-assetgrouptypeconstraintinput)!] | Replace allowed asset types. Null means no change. |
| `meta` | [CatalogItemMetaInput](../../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-assetgrouptypeconstraintinput"></a>

### AssetGroupTypeConstraintInput

Input for a constraint defining allowed asset types in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetTypeId` | `ID!` | The asset type ID. |
| `maxItems` | `Int` | The maximum assets of this type. Null means unlimited. |

---

## Enums

<a id="type-assetgrouporderfield"></a>

### AssetGroupOrderField

Fields available for ordering asset groups.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

<a id="type-assetgroupitemorderfield"></a>

### AssetGroupItemOrderField

Fields available for ordering asset group items.

| Value | Description |
| ----- | ----------- |
| `ATTACHED_AT` | Order by attachment date. |

---

## Pagination types

<a id="type-assetgroupconnection"></a>

### AssetGroupConnection

A paginated list of AssetGroup items.

**Implements:** [Connection](../../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupEdge](#type-assetgroupedge)!]! | A list of edges. |
| `nodes` | [[AssetGroup](#type-assetgroup)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-assetgroupedge"></a>

### AssetGroupEdge

An edge in the AssetGroup connection.

**Implements:** [Edge](../../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetGroup](#type-assetgroup)! | The asset group at the end of the edge. |

---

<a id="type-assetgroupitemconnection"></a>

### AssetGroupItemConnection

A paginated list of AssetGroupItem items.

**Implements:** [Connection](../../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupItemEdge](#type-assetgroupitemedge)!]! | A list of edges. |
| `nodes` | [[AssetGroupItem](#type-assetgroupitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-assetgroupitemedge"></a>

### AssetGroupItemEdge

An edge in the AssetGroupItem connection.

**Implements:** [Edge](../../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetGroupItem](#type-assetgroupitem)! | The asset group item at the end of the edge. |

---

<a id="type-assetgrouptypeconnection"></a>

### AssetGroupTypeConnection

A paginated list of AssetGroupType items.

**Implements:** [Connection](../../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupTypeEdge](#type-assetgrouptypeedge)!]! | A list of edges. |
| `nodes` | [[AssetGroupType](#type-assetgrouptype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-assetgrouptypeedge"></a>

### AssetGroupTypeEdge

An edge in the AssetGroupType connection.

**Implements:** [Edge](../../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetGroupType](#type-assetgrouptype)! | The asset group type at the end of the edge. |

---
