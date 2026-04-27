# Devices — Types

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

## Objects

<a id="type-devicevendor"></a>

### DeviceVendor

A device manufacturer or vendor.

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
| `models` | [DeviceModelConnection](#type-devicemodelconnection)! | Device models produced by this vendor. |

---

<a id="type-devicemodel"></a>

### DeviceModel

A specific device model produced by a vendor.

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
| `vendor` | [DeviceVendor](#type-devicevendor)! | The vendor that manufactures this model. |

---

<a id="type-devicetype"></a>

### DeviceType

A classification type for devices.

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

---

<a id="type-devicestatus"></a>

### DeviceStatus

An operational status for devices.

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

---

<a id="type-devicerelationtype"></a>

### DeviceRelationType

A type of relationship between two devices.

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

---

<a id="type-device"></a>

### Device

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Versioned](../common.md#type-versioned), [InventoryItem](inventory.md#type-inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this device. |
| `type` | [DeviceType](#type-devicetype)! | The device type classification. |
| `model` | [DeviceModel](#type-devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](#type-devicestatus)! | The current operational status. |
| `identifiers` | [[DeviceIdentifier](#type-deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `asset` | [Asset](../assets/types.md#type-asset) | The asset this device is currently linked to. |
| `inventory` | [Inventory](inventory.md#type-inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](#type-devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](#type-devicerelation)!]! | The incoming relationships from other devices to this device. |
| `inventoryHistory` | [DeviceInventoryRelationConnection](inventory.md#type-deviceinventoryrelationconnection)! | The history of inventory assignments for this device. |

---

<a id="type-deviceidentifier"></a>

### DeviceIdentifier

A hardware identifier for a device.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `device` | [Device](#type-device)! | The device this identifier belongs to. |
| `type` | [DeviceIdType](#type-deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means the identifier is globally unique. |

---

<a id="type-devicerelation"></a>

### DeviceRelation

A relationship between two devices.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `first` | [Device](#type-device)! | The first device in the relationship. |
| `second` | [Device](#type-device)! | The second device in the relationship. |
| `type` | [DeviceRelationType](#type-devicerelationtype)! | The type of relationship. |

---

<a id="type-devicepayload"></a>

### DevicePayload

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](#type-device)! | The created or updated device. |

---

<a id="type-deviceidentifierpayload"></a>

### DeviceIdentifierPayload

The result of a device identifier mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceIdentifier` | [DeviceIdentifier](#type-deviceidentifier)! | The added device identifier. |

---

<a id="type-devicerelationpayload"></a>

### DeviceRelationPayload

The result of a device relation mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceRelation` | [DeviceRelation](#type-devicerelation)! | The created device relationship. |

---

<a id="type-devicetypepayload"></a>

### DeviceTypePayload

The result of a device type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](#type-devicetype)! | The created or updated device type. |

---

<a id="type-devicestatuspayload"></a>

### DeviceStatusPayload

The result of a device status mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](#type-devicestatus)! | The created or updated device status. |

---

## Inputs

<a id="type-devicefilter"></a>

### DeviceFilter

Filtering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by device types (OR within field). |
| `modelIds` | `[ID!]` | Filter by device models (OR within field). |
| `statusIds` | `[ID!]` | Filter by statuses (OR within field). |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `identifierContains` | `String` | Partial match on device identifier value (case-insensitive contains). |
| `inventoryIds` | `[ID!]` | Filter by inventories (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

<a id="type-deviceorder"></a>

### DeviceOrder

Ordering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceOrderField](#type-deviceorderfield) | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-devicemodelfilter"></a>

### DeviceModelFilter

Filtering options for device models.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `code` | `Code` | Exact code match. |

---

<a id="type-devicecreateinput"></a>

### DeviceCreateInput

Input for creating a new device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String` | The device display name. If omitted or blank, the server generates "<vendorTitleEn> <modelTitleEn> <identifier.value>" where the identifier is chosen by type priority: IMEI > SERIAL_NUMBER > MAC_ADDRESS, with fallback to identifiers[0] when none of the priority types are present. |
| `identifiers` | [[DeviceIdentifierInput](#type-deviceidentifierinput)!]! | The hardware identifiers. At least one entry is required. |

---

<a id="type-deviceupdateinput"></a>

### DeviceUpdateInput

Input for updating an existing device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `modelId` | `ID` | The new device model. |
| `statusId` | `ID` | The new device status. |
| `title` | `String` | The new display name. |

---

<a id="type-devicedeleteinput"></a>

### DeviceDeleteInput

Input for deleting a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

<a id="type-deviceidentifierinput"></a>

### DeviceIdentifierInput

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](#type-deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means globally unique. |

---

<a id="type-deviceidentifieraddinput"></a>

### DeviceIdentifierAddInput

Input for adding an identifier to a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | [DeviceIdentifierInput](#type-deviceidentifierinput)! | The identifier details. |

---

<a id="type-deviceidentifierremoveinput"></a>

### DeviceIdentifierRemoveInput

Input for removing an identifier from a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

---

<a id="type-devicerelationcreateinput"></a>

### DeviceRelationCreateInput

Input for creating a relationship between devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `firstId` | `ID!` | The first device ID. |
| `secondId` | `ID!` | The second device ID. |
| `typeId` | `ID!` | The relationship type ID. |

---

<a id="type-devicerelationremoveinput"></a>

### DeviceRelationRemoveInput

Input for removing a device relationship.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The relationship ID to remove. |

---

<a id="type-devicetypecreateinput"></a>

### DeviceTypeCreateInput

Input for creating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-devicetypeupdateinput"></a>

### DeviceTypeUpdateInput

Input for updating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-devicestatuscreateinput"></a>

### DeviceStatusCreateInput

Input for creating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

<a id="type-devicestatusupdateinput"></a>

### DeviceStatusUpdateInput

Input for updating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

---

## Enums

<a id="type-deviceidtype"></a>

### DeviceIdType

The type of hardware identifier used to identify a device.

| Value | Description |
| ----- | ----------- |
| `GUID` | A GUID/UUID identifier. |
| `IMEI` | International Mobile Equipment Identity. A 15-digit number. |
| `MEID_HEX` | Mobile Equipment Identifier in hexadecimal format. |
| `MEID_DEC` | Mobile Equipment Identifier in decimal format. |
| `MAC_ADDRESS` | Media Access Control address of a network interface. |
| `SERIAL_NUMBER` | Manufacturer-assigned serial number. |
| `CUSTOM` | A custom identifier type defined by the organization. |

---

<a id="type-deviceorderfield"></a>

### DeviceOrderField

Fields available for ordering devices.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

<a id="type-deviceconnection"></a>

### DeviceConnection

A paginated list of Device items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceEdge](#type-deviceedge)!]! | A list of edges. |
| `nodes` | [[Device](#type-device)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-deviceedge"></a>

### DeviceEdge

An edge in the Device connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Device](#type-device)! | The device at the end of the edge. |

---

<a id="type-devicetypeconnection"></a>

### DeviceTypeConnection

A paginated list of DeviceType items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceTypeEdge](#type-devicetypeedge)!]! | A list of edges. |
| `nodes` | [[DeviceType](#type-devicetype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-devicetypeedge"></a>

### DeviceTypeEdge

An edge in the DeviceType connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceType](#type-devicetype)! | The device type at the end of the edge. |

---

<a id="type-devicestatusconnection"></a>

### DeviceStatusConnection

A paginated list of DeviceStatus items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceStatusEdge](#type-devicestatusedge)!]! | A list of edges. |
| `nodes` | [[DeviceStatus](#type-devicestatus)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-devicestatusedge"></a>

### DeviceStatusEdge

An edge in the DeviceStatus connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceStatus](#type-devicestatus)! | The device status at the end of the edge. |

---

<a id="type-devicemodelconnection"></a>

### DeviceModelConnection

A paginated list of DeviceModel items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceModelEdge](#type-devicemodeledge)!]! | A list of edges. |
| `nodes` | [[DeviceModel](#type-devicemodel)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-devicemodeledge"></a>

### DeviceModelEdge

An edge in the DeviceModel connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceModel](#type-devicemodel)! | The device model at the end of the edge. |

---

<a id="type-devicevendorconnection"></a>

### DeviceVendorConnection

A paginated list of DeviceVendor items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceVendorEdge](#type-devicevendoredge)!]! | A list of edges. |
| `nodes` | [[DeviceVendor](#type-devicevendor)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-devicevendoredge"></a>

### DeviceVendorEdge

An edge in the DeviceVendor connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceVendor](#type-devicevendor)! | The device vendor at the end of the edge. |

---

<a id="type-devicerelationtypeconnection"></a>

### DeviceRelationTypeConnection

A paginated list of DeviceRelationType items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceRelationTypeEdge](#type-devicerelationtypeedge)!]! | A list of edges. |
| `nodes` | [[DeviceRelationType](#type-devicerelationtype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-devicerelationtypeedge"></a>

### DeviceRelationTypeEdge

An edge in the DeviceRelationType connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceRelationType](#type-devicerelationtype)! | The device relation type at the end of the edge. |

---
