# Assets — Types

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

## Objects

<a id="type-assettype"></a>

### AssetType

A classification type for assets.

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
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#type-customfielddefinition)!]! | Custom field definitions specific to this asset type, ordered by display order. |

---

<a id="type-asset"></a>

### Asset

A physical or logical asset being tracked.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Customizable](../common.md#type-customizable), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this asset. |
| `type` | [AssetType](#type-assettype)! | The asset type classification. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. System-reserved codes (`geojson_data`, `schedule_data`, `device`) are excluded from this map and exposed through dedicated typed fields on the entity instead. |
| `device` | [Device](../devices/types.md#type-device) | The primary tracking device linked to this asset. |
| `groups` | [AssetGroupConnection](groups/types.md#type-assetgroupconnection)! | The groups this asset belongs to. |

---

<a id="type-assetpayload"></a>

### AssetPayload

The result of an asset mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `asset` | [Asset](#type-asset)! | The created or updated asset. |

---

<a id="type-assettypepayload"></a>

### AssetTypePayload

The result of an asset type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType](#type-assettype)! | The created or updated asset type. |

---

## Inputs

<a id="type-assetfilter"></a>

### AssetFilter

Filtering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by asset types (OR within field). |
| `deviceIds` | `[ID!]` | Filter by linked devices (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#type-customfieldfilter)!] | Filter by custom field values. |

---

<a id="type-assetorder"></a>

### AssetOrder

Ordering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetOrderField](#type-assetorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-assetcreateinput"></a>

### AssetCreateInput

Input for creating a new asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the asset. |
| `typeId` | `ID!` | The asset type ID. |
| `title` | `String!` | The asset display name. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#type-customfieldspatchinput) | The custom field values. |

---

<a id="type-assetupdateinput"></a>

### AssetUpdateInput

Input for updating an existing asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#type-customfieldspatchinput) | The custom field changes. |

---

<a id="type-assetdeleteinput"></a>

### AssetDeleteInput

Input for deleting an asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

<a id="type-assettypecreateinput"></a>

### AssetTypeCreateInput

Input for creating an asset type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions for this asset type. Only `create` is allowed when creating a new catalog item. |

---

<a id="type-assettypeupdateinput"></a>

### AssetTypeUpdateInput

Input for updating an asset type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions belonging to this asset type. |

---

## Enums

<a id="type-assetorderfield"></a>

### AssetOrderField

Fields available for ordering assets.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

<a id="type-assetconnection"></a>

### AssetConnection

A paginated list of Asset items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetEdge](#type-assetedge)!]! | A list of edges. |
| `nodes` | [[Asset](#type-asset)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-assetedge"></a>

### AssetEdge

An edge in the Asset connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Asset](#type-asset)! | The asset at the end of the edge. |

---

<a id="type-assettypeconnection"></a>

### AssetTypeConnection

A paginated list of AssetType items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetTypeEdge](#type-assettypeedge)!]! | A list of edges. |
| `nodes` | [[AssetType](#type-assettype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-assettypeedge"></a>

### AssetTypeEdge

An edge in the AssetType connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AssetType](#type-assettype)! | The asset type at the end of the edge. |

---
