# Assets — Types

## Objects

### AssetType

A classification type for assets.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this asset type, ordered by display order. |

---

### Asset

A physical or logical asset being tracked.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this asset. |
| `type` | [AssetType](types.md#assettype)! | The asset type classification. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |
| `device` | [Device](../devices/types.md#device) | The primary tracking device linked to this asset.
  This is an alias for the `device` custom field. |
| `filter` | [AssetGroupFilter](groups/types.md#assetgroupfilter) | Filtering options for the returned groups. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetGroupOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned groups. |

---

### AssetPayload

The result of an asset mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `asset` | [Asset](types.md#asset)! | The created or updated asset. |

---

### AssetTypePayload

The result of an asset type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType](types.md#assettype)! | The created or updated asset type. |

---

## Inputs

### AssetFilter

Filtering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by asset types (OR within field). |
| `deviceIds` | `[ID!]` | Filter by linked devices (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values. |

---

### AssetOrder

Ordering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetOrderField](types.md#assetorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### AssetCreateInput

Input for creating a new asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the asset. |
| `typeId` | `ID!` | The asset type ID. |
| `title` | `String!` | The asset display name. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

---

### AssetUpdateInput

Input for updating an existing asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

---

### AssetDeleteInput

Input for deleting an asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### AssetTypeCreateInput

Input for creating an asset type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### AssetTypeUpdateInput

Input for updating an asset type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Enums

### AssetOrderField

Fields available for ordering assets.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

### AssetConnection

A paginated list of Asset items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetEdge](types.md#assetedge)!]! | A list of edges. |
| `nodes` | [[Asset](types.md#asset)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### AssetEdge

An edge in the Asset connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Asset](types.md#asset)! | The asset at the end of the edge. |

---

### AssetTypeConnection

A paginated list of AssetType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetTypeEdge](types.md#assettypeedge)!]! | A list of edges. |
| `nodes` | [[AssetType](types.md#assettype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### AssetTypeEdge

An edge in the AssetType connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetType](types.md#assettype)! | The asset type at the end of the edge. |

---
