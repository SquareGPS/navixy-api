# Devices — Types

## Types

### DeviceConnection

A paginated list of Device items.

**Implements:** [`Connection`](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceEdge](./types.md#deviceedge)!]! | A list of edges. |
| `nodes` | [[Device](./types.md#device)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

### DeviceEdge

An edge in the Device connection.

**Implements:** [`Edge`](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Device](./types.md#device)! | The device at the end of the edge. |

### Device

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [`Node`](../common.md#node), [`Titled`](../common.md#titled), [`Customizable`](../common.md#customizable), [`Versioned`](../common.md#versioned), [`InventoryItem`](../inventory.md#inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this device. |
| `type` | [DeviceType](../catalogs/device/types.md#devicetype)! | The device type classification. |
| `model` | [DeviceModel](../catalogs/device/types.md#devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](../catalogs/device/types.md#devicestatus)! | The current operational status. |
| `customFields` | [JSON](../common.md#json)! |  |
| `identifiers` | [[DeviceIdentifier](./types.md#deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory` | [Inventory](../inventory.md#inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](./types.md#devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](./types.md#devicerelation)!]! | The incoming relationships from other devices to this device. |
| `inventoryHistory` | [DeviceInventoryRelationConnection](../inventory.md#deviceinventoryrelationconnection)! | The history of inventory assignments for this device. |

### DeviceIdentifier

A hardware identifier for a device.

**Implements:** [`Node`](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `device` | [Device](./types.md#device)! | The device this identifier belongs to. |
| `type` | [DeviceIdType](./types.md#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | [Code](../common.md#code) | The namespace for uniqueness scope. Null means the identifier is globally unique. |

### DeviceRelation

A relationship between two devices.

**Implements:** [`Node`](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `first` | [Device](./types.md#device)! | The first device in the relationship. |
| `second` | [Device](./types.md#device)! | The second device in the relationship. |
| `type` | [DeviceRelationType](../catalogs/device/types.md#devicerelationtype)! | The type of relationship. |

### DevicePayload

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](./types.md#device)! | The created or updated device. |

### DeviceIdentifierPayload

The result of a device identifier mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceIdentifier` | [DeviceIdentifier](./types.md#deviceidentifier)! | The added device identifier. |

### DeviceRelationPayload

The result of a device relation mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceRelation` | [DeviceRelation](./types.md#devicerelation)! | The created device relationship. |

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

### DeviceOrder

Ordering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceOrderField](./types.md#deviceorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](../common.md#code) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

### DeviceCreateInput

Input for creating a new device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String!` | The device display name. |
| `identifiers` | [[DeviceIdentifierInput](./types.md#deviceidentifierinput)!] | The hardware identifiers. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

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

### DeviceDeleteInput

Input for deleting a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### DeviceIdentifierInput

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](./types.md#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | [Code](../common.md#code) | The namespace for uniqueness scope. Null means globally unique. |

### DeviceIdentifierAddInput

Input for adding an identifier to a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | [DeviceIdentifierInput](./types.md#deviceidentifierinput)! | The identifier details. |

### DeviceIdentifierRemoveInput

Input for removing an identifier from a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

### DeviceRelationCreateInput

Input for creating a relationship between devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `firstId` | `ID!` | The first device ID. |
| `secondId` | `ID!` | The second device ID. |
| `typeId` | `ID!` | The relationship type ID. |

### DeviceRelationRemoveInput

Input for removing a device relationship.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The relationship ID to remove. |

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

### DeviceOrderField

Fields available for ordering devices.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |
