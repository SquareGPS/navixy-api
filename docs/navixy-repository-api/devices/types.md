# Devices — Types

## Objects

### DeviceVendor

A device manufacturer or vendor.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `models` | [DeviceModelConnection](#devicemodelconnection)! | Device models produced by this vendor. |

---

### DeviceModel

A specific device model produced by a vendor.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `vendor` | [DeviceVendor](#devicevendor)! | The vendor that manufactures this model. |

---

### DeviceType

A classification type for devices.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

---

### DeviceStatus

An operational status for devices.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

---

### DeviceRelationType

A type of relationship between two devices.

**Implements:** [CatalogItem](../catalogs/README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

---

### Device

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned), [InventoryItem](inventory.md#inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#organization)! | The organization that owns this device. |
| `type` | [DeviceType](#devicetype)! | The device type classification. |
| `model` | [DeviceModel](#devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](#devicestatus)! | The current operational status. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |
| `identifiers` | [[DeviceIdentifier](#deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory` | [Inventory](inventory.md#inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](#devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](#devicerelation)!]! | The incoming relationships from other devices to this device. |
| `inventoryHistory` | [DeviceInventoryRelationConnection](inventory.md#deviceinventoryrelationconnection)! | The history of inventory assignments for this device. |

---

### DeviceIdentifier

A hardware identifier for a device.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `device` | [Device](#device)! | The device this identifier belongs to. |
| `type` | [DeviceIdType](#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means the identifier is globally unique. |

---

### DeviceRelation

A relationship between two devices.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `first` | [Device](#device)! | The first device in the relationship. |
| `second` | [Device](#device)! | The second device in the relationship. |
| `type` | [DeviceRelationType](#devicerelationtype)! | The type of relationship. |

---

### DevicePayload

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](#device)! | The created or updated device. |

---

### DeviceIdentifierPayload

The result of a device identifier mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceIdentifier` | [DeviceIdentifier](#deviceidentifier)! | The added device identifier. |

---

### DeviceRelationPayload

The result of a device relation mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceRelation` | [DeviceRelation](#devicerelation)! | The created device relationship. |

---

### DeviceTypePayload

The result of a device type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](#devicetype)! | The created or updated device type. |

---

### DeviceStatusPayload

The result of a device status mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](#devicestatus)! | The created or updated device status. |

---

## Inputs

### DeviceFilter

Filtering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by device types (OR within field). |
| `modelIds` | `[ID!]` | Filter by device models (OR within field). |
| `statusIds` | `[ID!]` | Filter by statuses (OR within field). |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `identifierContains` | `String` | Partial match on device identifier value (case-sensitive contains). |
| `inventoryIds` | `[ID!]` | Filter by inventories (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values. |

---

### DeviceOrder

Ordering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceOrderField](#deviceorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### DeviceModelFilter

Filtering options for device models.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `code` | `Code` | Exact code match. |

---

### DeviceCreateInput

Input for creating a new device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String!` | The device display name. |
| `identifiers` | [[DeviceIdentifierInput](#deviceidentifierinput)!] | The hardware identifiers. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

---

### DeviceUpdateInput

Input for updating an existing device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `modelId` | `ID` | The new device model. |
| `statusId` | `ID` | The new device status. |
| `title` | `String` | The new display name. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

---

### DeviceDeleteInput

Input for deleting a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### DeviceIdentifierInput

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means globally unique. |

---

### DeviceIdentifierAddInput

Input for adding an identifier to a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | [DeviceIdentifierInput](#deviceidentifierinput)! | The identifier details. |

---

### DeviceIdentifierRemoveInput

Input for removing an identifier from a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

---

### DeviceRelationCreateInput

Input for creating a relationship between devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `firstId` | `ID!` | The first device ID. |
| `secondId` | `ID!` | The second device ID. |
| `typeId` | `ID!` | The relationship type ID. |

---

### DeviceRelationRemoveInput

Input for removing a device relationship.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The relationship ID to remove. |

---

### DeviceTypeCreateInput

Input for creating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### DeviceTypeUpdateInput

Input for updating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### DeviceStatusCreateInput

Input for creating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### DeviceStatusUpdateInput

Input for updating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Enums

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

### DeviceOrderField

Fields available for ordering devices.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

### DeviceConnection

A paginated list of Device items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceEdge](#deviceedge)!]! | A list of edges. |
| `nodes` | [[Device](#device)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### DeviceEdge

An edge in the Device connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Device](#device)! | The device at the end of the edge. |

---

### DeviceTypeConnection

A paginated list of DeviceType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceTypeEdge](#devicetypeedge)!]! | A list of edges. |
| `nodes` | [[DeviceType](#devicetype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### DeviceTypeEdge

An edge in the DeviceType connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceType](#devicetype)! | The device type at the end of the edge. |

---

### DeviceStatusConnection

A paginated list of DeviceStatus items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceStatusEdge](#devicestatusedge)!]! | A list of edges. |
| `nodes` | [[DeviceStatus](#devicestatus)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### DeviceStatusEdge

An edge in the DeviceStatus connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceStatus](#devicestatus)! | The device status at the end of the edge. |

---

### DeviceModelConnection

A paginated list of DeviceModel items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceModelEdge](#devicemodeledge)!]! | A list of edges. |
| `nodes` | [[DeviceModel](#devicemodel)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### DeviceModelEdge

An edge in the DeviceModel connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceModel](#devicemodel)! | The device model at the end of the edge. |

---
