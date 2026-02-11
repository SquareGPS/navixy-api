# Devices — Mutations

### deviceCreate

Creates a new device.

```graphql
deviceCreate("The input fields for creating the device." input: DeviceCreateInput!): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceCreateInput](types.md#devicecreateinput)! | The input fields for creating the device. |

**Input types:**

<details>

<summary><code>DeviceCreateInput</code></summary>

Input for creating a new device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String!` | The device display name. |
| `identifiers` | [[DeviceIdentifierInput](types.md#deviceidentifierinput)!] | The hardware identifiers. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

</details>

<details>

<summary><code>DeviceIdentifierInput</code></summary>

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](types.md#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means globally unique. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>DevicePayload</code></summary>

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](types.md#device)! | The created or updated device. |

</details>

<details>

<summary><code>Device (entity)</code></summary>

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned), [InventoryItem](inventory.md#inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this device. |
| `type` | [DeviceType](types.md#devicetype)! | The device type classification. |
| `model` | [DeviceModel](types.md#devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](types.md#devicestatus)! | The current operational status. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |
| `identifiers` | [[DeviceIdentifier](types.md#deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory` | [Inventory](inventory.md#inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](types.md#devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](types.md#devicerelation)!]! | The incoming relationships from other devices to this device. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceInventoryRelationOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned history. |

</details>

---

### deviceUpdate

Updates an existing device.

```graphql
deviceUpdate("The input fields for updating the device." input: DeviceUpdateInput!): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceUpdateInput](types.md#deviceupdateinput)! | The input fields for updating the device. |

**Input types:**

<details>

<summary><code>DeviceUpdateInput</code></summary>

Input for updating an existing device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `modelId` | `ID` | The new device model. |
| `statusId` | `ID` | The new device status. |
| `title` | `String` | The new display name. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | `JSON` | Fields to set or update as a key-value map. |
| `unset` | `[Code!]` | Field codes to remove. |

</details>

**Output types:**

<details>

<summary><code>DevicePayload</code></summary>

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](types.md#device)! | The created or updated device. |

</details>

<details>

<summary><code>Device (entity)</code></summary>

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned), [InventoryItem](inventory.md#inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this device. |
| `type` | [DeviceType](types.md#devicetype)! | The device type classification. |
| `model` | [DeviceModel](types.md#devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](types.md#devicestatus)! | The current operational status. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |
| `identifiers` | [[DeviceIdentifier](types.md#deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory` | [Inventory](inventory.md#inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](types.md#devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](types.md#devicerelation)!]! | The incoming relationships from other devices to this device. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceInventoryRelationOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned history. |

</details>

---

### deviceDelete

Deletes a device.

```graphql
deviceDelete("The input fields for deleting the device." input: DeviceDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceDeleteInput](types.md#devicedeleteinput)! | The input fields for deleting the device. |

**Input types:**

<details>

<summary><code>DeviceDeleteInput</code></summary>

Input for deleting a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### deviceIdentifierAdd

Adds an identifier to a device.

```graphql
deviceIdentifierAdd("The input fields for adding the identifier." input: DeviceIdentifierAddInput!): DeviceIdentifierPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceIdentifierAddInput](types.md#deviceidentifieraddinput)! | The input fields for adding the identifier. |

**Input types:**

<details>

<summary><code>DeviceIdentifierAddInput</code></summary>

Input for adding an identifier to a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | [DeviceIdentifierInput](types.md#deviceidentifierinput)! | The identifier details. |

</details>

<details>

<summary><code>DeviceIdentifierInput</code></summary>

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](types.md#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means globally unique. |

</details>

**Output types:**

<details>

<summary><code>DeviceIdentifierPayload</code></summary>

The result of a device identifier mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceIdentifier` | [DeviceIdentifier](types.md#deviceidentifier)! | The added device identifier. |

</details>

<details>

<summary><code>DeviceIdentifier (entity)</code></summary>

A hardware identifier for a device.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `device` | [Device](types.md#device)! | The device this identifier belongs to. |
| `type` | [DeviceIdType](types.md#deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means the identifier is globally unique. |

</details>

---

### deviceIdentifierRemove

Removes an identifier from a device.

```graphql
deviceIdentifierRemove("The input fields for removing the identifier." input: DeviceIdentifierRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceIdentifierRemoveInput](types.md#deviceidentifierremoveinput)! | The input fields for removing the identifier. |

**Input types:**

<details>

<summary><code>DeviceIdentifierRemoveInput</code></summary>

Input for removing an identifier from a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### deviceRelationCreate

Creates a relationship between devices.

```graphql
deviceRelationCreate("The input fields for creating the relationship." input: DeviceRelationCreateInput!): DeviceRelationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceRelationCreateInput](types.md#devicerelationcreateinput)! | The input fields for creating the relationship. |

**Input types:**

<details>

<summary><code>DeviceRelationCreateInput</code></summary>

Input for creating a relationship between devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `firstId` | `ID!` | The first device ID. |
| `secondId` | `ID!` | The second device ID. |
| `typeId` | `ID!` | The relationship type ID. |

</details>

**Output types:**

<details>

<summary><code>DeviceRelationPayload</code></summary>

The result of a device relation mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceRelation` | [DeviceRelation](types.md#devicerelation)! | The created device relationship. |

</details>

<details>

<summary><code>DeviceRelation (entity)</code></summary>

A relationship between two devices.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `first` | [Device](types.md#device)! | The first device in the relationship. |
| `second` | [Device](types.md#device)! | The second device in the relationship. |
| `type` | [DeviceRelationType](types.md#devicerelationtype)! | The type of relationship. |

</details>

---

### deviceRelationRemove

Removes a device relationship.

```graphql
deviceRelationRemove("The input fields for removing the relationship." input: DeviceRelationRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceRelationRemoveInput](types.md#devicerelationremoveinput)! | The input fields for removing the relationship. |

**Input types:**

<details>

<summary><code>DeviceRelationRemoveInput</code></summary>

Input for removing a device relationship.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The relationship ID to remove. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### deviceTypeCreate

Creates a new device type.

```graphql
deviceTypeCreate("The input fields for creating the device type." input: DeviceTypeCreateInput!): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceTypeCreateInput](types.md#devicetypecreateinput)! | The input fields for creating the device type. |

**Input types:**

<details>

<summary><code>DeviceTypeCreateInput</code></summary>

Input for creating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>DeviceTypePayload</code></summary>

The result of a device type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](types.md#devicetype)! | The created or updated device type. |

</details>

<details>

<summary><code>DeviceType (entity)</code></summary>

A classification type for devices.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

---

### deviceTypeUpdate

Updates a device type.

```graphql
deviceTypeUpdate("The input fields for updating the device type." input: DeviceTypeUpdateInput!): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceTypeUpdateInput](types.md#devicetypeupdateinput)! | The input fields for updating the device type. |

**Input types:**

<details>

<summary><code>DeviceTypeUpdateInput</code></summary>

Input for updating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>DeviceTypePayload</code></summary>

The result of a device type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](types.md#devicetype)! | The created or updated device type. |

</details>

<details>

<summary><code>DeviceType (entity)</code></summary>

A classification type for devices.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

---

### deviceTypeDelete

Deletes a device type.

```graphql
deviceTypeDelete("The input fields for deleting the device type." input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../catalogs/catalog-items.md#catalogitemdeleteinput)! | The input fields for deleting the device type. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### deviceStatusCreate

Creates a new device status.

```graphql
deviceStatusCreate("The input fields for creating the device status." input: DeviceStatusCreateInput!): DeviceStatusPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceStatusCreateInput](types.md#devicestatuscreateinput)! | The input fields for creating the device status. |

**Input types:**

<details>

<summary><code>DeviceStatusCreateInput</code></summary>

Input for creating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>DeviceStatusPayload</code></summary>

The result of a device status mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](types.md#devicestatus)! | The created or updated device status. |

</details>

<details>

<summary><code>DeviceStatus (entity)</code></summary>

An operational status for devices.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |

</details>

---

### deviceStatusUpdate

Updates a device status.

```graphql
deviceStatusUpdate("The input fields for updating the device status." input: DeviceStatusUpdateInput!): DeviceStatusPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceStatusUpdateInput](types.md#devicestatusupdateinput)! | The input fields for updating the device status. |

**Input types:**

<details>

<summary><code>DeviceStatusUpdateInput</code></summary>

Input for updating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

</details>

<details>

<summary><code>CatalogItemMetaInput</code></summary>

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

<summary><code>DeviceStatusPayload</code></summary>

The result of a device status mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](types.md#devicestatus)! | The created or updated device status. |

</details>

<details>

<summary><code>DeviceStatus (entity)</code></summary>

An operational status for devices.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |

</details>

---

### deviceStatusDelete

Deletes a device status.

```graphql
deviceStatusDelete("The input fields for deleting the device status." input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput](../catalogs/catalog-items.md#catalogitemdeleteinput)! | The input fields for deleting the device status. |

**Input types:**

<details>

<summary><code>CatalogItemDeleteInput</code></summary>

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---
