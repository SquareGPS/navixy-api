# Devices — Mutations

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

### deviceCreate

Creates a new device.

```graphql
deviceCreate(
    input: DeviceCreateInput!
  ): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceCreateInput!` | The input fields for creating the device. |

**Input types:**

<details>

<summary>DeviceCreateInput</summary>

Input for creating a new device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String!` | The device display name. |
| `identifiers` | [[DeviceIdentifierInput](types.md#type-deviceidentifierinput)!] | The hardware identifiers. |

</details>

<details>

<summary>DeviceIdentifierInput</summary>

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](types.md#type-deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means globally unique. |

</details>

**Output types:**

<details>

<summary>DevicePayload</summary>

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](types.md#type-device)! | The created or updated device. |

</details>

<details>

<summary>Device (entity)</summary>

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Versioned](../common.md#type-versioned), [InventoryItem](inventory.md#type-inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this device. |
| `type` | [DeviceType](types.md#type-devicetype)! | The device type classification. |
| `model` | [DeviceModel](types.md#type-devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](types.md#type-devicestatus)! | The current operational status. |
| `identifiers` | [[DeviceIdentifier](types.md#type-deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory` | [Inventory](inventory.md#type-inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](types.md#type-devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](types.md#type-devicerelation)!]! | The incoming relationships from other devices to this device. |
| `inventoryHistory` | [DeviceInventoryRelationConnection](inventory.md#type-deviceinventoryrelationconnection)! | The history of inventory assignments for this device. |

</details>

---

### deviceUpdate

Updates an existing device.

```graphql
deviceUpdate(
    input: DeviceUpdateInput!
  ): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceUpdateInput!` | The input fields for updating the device. |

**Input types:**

<details>

<summary>DeviceUpdateInput</summary>

Input for updating an existing device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `modelId` | `ID` | The new device model. |
| `statusId` | `ID` | The new device status. |
| `title` | `String` | The new display name. |

</details>

**Output types:**

<details>

<summary>DevicePayload</summary>

The result of a device mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `device` | [Device](types.md#type-device)! | The created or updated device. |

</details>

<details>

<summary>Device (entity)</summary>

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Versioned](../common.md#type-versioned), [InventoryItem](inventory.md#type-inventoryitem)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this device. |
| `type` | [DeviceType](types.md#type-devicetype)! | The device type classification. |
| `model` | [DeviceModel](types.md#type-devicemodel)! | The specific device model. |
| `status` | [DeviceStatus](types.md#type-devicestatus)! | The current operational status. |
| `identifiers` | [[DeviceIdentifier](types.md#type-deviceidentifier)!]! | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory` | [Inventory](inventory.md#type-inventory) | The inventory this device is currently assigned to. |
| `relationsFrom` | [[DeviceRelation](types.md#type-devicerelation)!]! | The outgoing relationships from this device to other devices. |
| `relationsTo` | [[DeviceRelation](types.md#type-devicerelation)!]! | The incoming relationships from other devices to this device. |
| `inventoryHistory` | [DeviceInventoryRelationConnection](inventory.md#type-deviceinventoryrelationconnection)! | The history of inventory assignments for this device. |

</details>

---

### deviceDelete

Deletes a device.

```graphql
deviceDelete(
    input: DeviceDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceDeleteInput!` | The input fields for deleting the device. |

**Input types:**

<details>

<summary>DeviceDeleteInput</summary>

Input for deleting a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to delete. |
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

### deviceIdentifierAdd

Adds an identifier to a device.

```graphql
deviceIdentifierAdd(
    input: DeviceIdentifierAddInput!
  ): DeviceIdentifierPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceIdentifierAddInput!` | The input fields for adding the identifier. |

**Input types:**

<details>

<summary>DeviceIdentifierAddInput</summary>

Input for adding an identifier to a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | [DeviceIdentifierInput](types.md#type-deviceidentifierinput)! | The identifier details. |

</details>

<details>

<summary>DeviceIdentifierInput</summary>

Input for a device identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | [DeviceIdType](types.md#type-deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means globally unique. |

</details>

**Output types:**

<details>

<summary>DeviceIdentifierPayload</summary>

The result of a device identifier mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceIdentifier` | [DeviceIdentifier](types.md#type-deviceidentifier)! | The added device identifier. |

</details>

<details>

<summary>DeviceIdentifier (entity)</summary>

A hardware identifier for a device.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `device` | [Device](types.md#type-device)! | The device this identifier belongs to. |
| `type` | [DeviceIdType](types.md#type-deviceidtype)! | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `Code` | The namespace for uniqueness scope. Null means the identifier is globally unique. |

</details>

---

### deviceIdentifierRemove

Removes an identifier from a device.

```graphql
deviceIdentifierRemove(
    input: DeviceIdentifierRemoveInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceIdentifierRemoveInput!` | The input fields for removing the identifier. |

**Input types:**

<details>

<summary>DeviceIdentifierRemoveInput</summary>

Input for removing an identifier from a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

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

### deviceRelationCreate

Creates a relationship between devices.

```graphql
deviceRelationCreate(
    input: DeviceRelationCreateInput!
  ): DeviceRelationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceRelationCreateInput!` | The input fields for creating the relationship. |

**Input types:**

<details>

<summary>DeviceRelationCreateInput</summary>

Input for creating a relationship between devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `firstId` | `ID!` | The first device ID. |
| `secondId` | `ID!` | The second device ID. |
| `typeId` | `ID!` | The relationship type ID. |

</details>

**Output types:**

<details>

<summary>DeviceRelationPayload</summary>

The result of a device relation mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceRelation` | [DeviceRelation](types.md#type-devicerelation)! | The created device relationship. |

</details>

<details>

<summary>DeviceRelation (entity)</summary>

A relationship between two devices.

**Implements:** [Node](../common.md#type-node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `first` | [Device](types.md#type-device)! | The first device in the relationship. |
| `second` | [Device](types.md#type-device)! | The second device in the relationship. |
| `type` | [DeviceRelationType](types.md#type-devicerelationtype)! | The type of relationship. |

</details>

---

### deviceRelationRemove

Removes a device relationship.

```graphql
deviceRelationRemove(
    input: DeviceRelationRemoveInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceRelationRemoveInput!` | The input fields for removing the relationship. |

**Input types:**

<details>

<summary>DeviceRelationRemoveInput</summary>

Input for removing a device relationship.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The relationship ID to remove. |

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

### deviceTypeCreate

Creates a new device type.

```graphql
deviceTypeCreate(
    input: DeviceTypeCreateInput!
  ): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceTypeCreateInput!` | The input fields for creating the device type. |

**Input types:**

<details>

<summary>DeviceTypeCreateInput</summary>

Input for creating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions for this device type. Only `create` is allowed when creating a new catalog item. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

<details>

<summary>CustomFieldDefinitionInput</summary>

A single operation on a custom field definition within the parent catalog item.
Exactly one action must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `create` | [CustomFieldDefinitionCreateData](../custom-fields.md#type-customfielddefinitioncreatedata) | Create a new custom field definition. |
| `update` | [CustomFieldDefinitionUpdateData](../custom-fields.md#type-customfielddefinitionupdatedata) | Update an existing custom field definition. |
| `delete` | [CustomFieldDefinitionDeleteData](../custom-fields.md#type-customfielddefinitiondeletedata) | Delete a custom field definition. |
| `archive` | [CustomFieldDefinitionArchiveData](../custom-fields.md#type-customfielddefinitionarchivedata) | Archive a custom field definition (non-destructive deactivation). |
| `restore` | [CustomFieldDefinitionRestoreData](../custom-fields.md#type-customfielddefinitionrestoredata) | Restore a previously archived custom field definition. |

</details>

<details>

<summary>CustomFieldDefinitionCreateData</summary>

Data for creating a custom field definition within its parent catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](../custom-fields.md#type-fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

</details>

<details>

<summary>FieldParamsInput</summary>

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](../custom-fields.md#type-stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](../custom-fields.md#type-textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](../custom-fields.md#type-numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](../custom-fields.md#type-booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](../custom-fields.md#type-datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](../custom-fields.md#type-datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](../custom-fields.md#type-geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](../custom-fields.md#type-schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](../custom-fields.md#type-optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](../custom-fields.md#type-devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](../custom-fields.md#type-referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](../custom-fields.md#type-catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](../custom-fields.md#type-tagfieldparamsinput) | Parameters for TAG field type. |

</details>

<details>

<summary>StringFieldParamsInput</summary>

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>TextFieldParamsInput</summary>

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>NumberFieldParamsInput</summary>

Parameters for NUMBER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

</details>

<details>

<summary>BooleanFieldParamsInput</summary>

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

</details>

<details>

<summary>DateFieldParamsInput</summary>

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Date` | The default value. |

</details>

<details>

<summary>DateTimeFieldParamsInput</summary>

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `DateTime` | The default value. |

</details>

<details>

<summary>GeoJsonFieldParamsInput</summary>

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](../geo-objects/types.md#type-geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

</details>

<details>

<summary>ScheduleFieldParamsInput</summary>

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>OptionsFieldParamsInput</summary>

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput](../custom-fields.md#type-fieldoptioninput)!]! | The available options. |
| `defaultValue` | `Code` | The default option code. |

</details>

<details>

<summary>FieldOptionInput</summary>

Input for an option definition.
When updating options: if an entry without `code` is provided, a new option is created.
If the label already exists within this field, an error is returned.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The unique code. Auto-generated from label if omitted. |
| `label` | `String!` | The display label. Must be unique within the custom field. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

</details>

<details>

<summary>DeviceFieldParamsInput</summary>

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>ReferenceFieldParamsInput</summary>

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

</details>

<details>

<summary>CatalogFieldParamsInput</summary>

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultValue` | `Code` | The default item code. |

</details>

<details>

<summary>TagFieldParamsInput</summary>

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple tags can be selected. |
| `defaultValue` | `Code` | The default tag code. |

</details>

<details>

<summary>CustomFieldDefinitionUpdateData</summary>

Data for updating an existing custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to update. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

</details>

<details>

<summary>CustomFieldDefinitionDeleteData</summary>

Data for permanently deleting a custom field definition.

If entities have values for this field, the default behavior is to reject the deletion.
Use `onValues: CASCADE` to explicitly allow deletion with all associated values.

Prefer archiving for non-destructive deactivation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to delete. |
| `onValues` | [CustomFieldDefinitionDeleteBehavior](../custom-fields.md#type-customfielddefinitiondeletebehavior) | What to do when existing entities have values for this field. Defaults to `REJECT` to prevent accidental data loss. |

</details>

<details>

<summary>CustomFieldDefinitionArchiveData</summary>

Data for archiving or restoring a custom field definition.

Archiving deactivates the field without data loss:
- The field definition and all its values are preserved.
- The field no longer appears in forms and accepts no new values.
- Existing values remain readable and visible in history/exports.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to archive. |

</details>

<details>

<summary>CustomFieldDefinitionRestoreData</summary>

Data for restoring a previously archived custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to restore. |

</details>

**Output types:**

<details>

<summary>DeviceTypePayload</summary>

The result of a device type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](types.md#type-devicetype)! | The created or updated device type. |

</details>

<details>

<summary>DeviceType (entity)</summary>

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
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#type-customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

---

### deviceTypeUpdate

Updates a device type.

```graphql
deviceTypeUpdate(
    input: DeviceTypeUpdateInput!
  ): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceTypeUpdateInput!` | The input fields for updating the device type. |

**Input types:**

<details>

<summary>DeviceTypeUpdateInput</summary>

Input for updating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions belonging to this device type. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

<details>

<summary>CustomFieldDefinitionInput</summary>

A single operation on a custom field definition within the parent catalog item.
Exactly one action must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `create` | [CustomFieldDefinitionCreateData](../custom-fields.md#type-customfielddefinitioncreatedata) | Create a new custom field definition. |
| `update` | [CustomFieldDefinitionUpdateData](../custom-fields.md#type-customfielddefinitionupdatedata) | Update an existing custom field definition. |
| `delete` | [CustomFieldDefinitionDeleteData](../custom-fields.md#type-customfielddefinitiondeletedata) | Delete a custom field definition. |
| `archive` | [CustomFieldDefinitionArchiveData](../custom-fields.md#type-customfielddefinitionarchivedata) | Archive a custom field definition (non-destructive deactivation). |
| `restore` | [CustomFieldDefinitionRestoreData](../custom-fields.md#type-customfielddefinitionrestoredata) | Restore a previously archived custom field definition. |

</details>

<details>

<summary>CustomFieldDefinitionCreateData</summary>

Data for creating a custom field definition within its parent catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType](../custom-fields.md#type-fieldtype)! | The data type. Immutable after creation. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput)! | The type-specific parameters. Exactly one variant must be provided. |

</details>

<details>

<summary>FieldParamsInput</summary>

Field parameters input. Exactly one field must be provided.

*This input type uses `@oneOf` - exactly one field must be provided.*

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](../custom-fields.md#type-stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](../custom-fields.md#type-textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](../custom-fields.md#type-numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](../custom-fields.md#type-booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](../custom-fields.md#type-datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](../custom-fields.md#type-datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](../custom-fields.md#type-geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](../custom-fields.md#type-schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](../custom-fields.md#type-optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](../custom-fields.md#type-devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](../custom-fields.md#type-referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](../custom-fields.md#type-catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](../custom-fields.md#type-tagfieldparamsinput) | Parameters for TAG field type. |

</details>

<details>

<summary>StringFieldParamsInput</summary>

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>TextFieldParamsInput</summary>

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

</details>

<details>

<summary>NumberFieldParamsInput</summary>

Parameters for NUMBER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

</details>

<details>

<summary>BooleanFieldParamsInput</summary>

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

</details>

<details>

<summary>DateFieldParamsInput</summary>

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Date` | The default value. |

</details>

<details>

<summary>DateTimeFieldParamsInput</summary>

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `DateTime` | The default value. |

</details>

<details>

<summary>GeoJsonFieldParamsInput</summary>

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType](../geo-objects/types.md#type-geojsongeometrytype)!] | The allowed geometry types. Null means all types are allowed. |

</details>

<details>

<summary>ScheduleFieldParamsInput</summary>

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>OptionsFieldParamsInput</summary>

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput](../custom-fields.md#type-fieldoptioninput)!]! | The available options. |
| `defaultValue` | `Code` | The default option code. |

</details>

<details>

<summary>FieldOptionInput</summary>

Input for an option definition.
When updating options: if an entry without `code` is provided, a new option is created.
If the label already exists within this field, an error is returned.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code` | The unique code. Auto-generated from label if omitted. |
| `label` | `String!` | The display label. Must be unique within the custom field. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

</details>

<details>

<summary>DeviceFieldParamsInput</summary>

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

</details>

<details>

<summary>ReferenceFieldParamsInput</summary>

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `refEntityTypeCode` | `Code!` | The entity type code that can be referenced. |

</details>

<details>

<summary>CatalogFieldParamsInput</summary>

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | `Code!` | The catalog code that items can be selected from. |
| `defaultValue` | `Code` | The default item code. |

</details>

<details>

<summary>TagFieldParamsInput</summary>

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple tags can be selected. |
| `defaultValue` | `Code` | The default tag code. |

</details>

<details>

<summary>CustomFieldDefinitionUpdateData</summary>

Data for updating an existing custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to update. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](../custom-fields.md#type-fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

</details>

<details>

<summary>CustomFieldDefinitionDeleteData</summary>

Data for permanently deleting a custom field definition.

If entities have values for this field, the default behavior is to reject the deletion.
Use `onValues: CASCADE` to explicitly allow deletion with all associated values.

Prefer archiving for non-destructive deactivation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to delete. |
| `onValues` | [CustomFieldDefinitionDeleteBehavior](../custom-fields.md#type-customfielddefinitiondeletebehavior) | What to do when existing entities have values for this field. Defaults to `REJECT` to prevent accidental data loss. |

</details>

<details>

<summary>CustomFieldDefinitionArchiveData</summary>

Data for archiving or restoring a custom field definition.

Archiving deactivates the field without data loss:
- The field definition and all its values are preserved.
- The field no longer appears in forms and accepts no new values.
- Existing values remain readable and visible in history/exports.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to archive. |

</details>

<details>

<summary>CustomFieldDefinitionRestoreData</summary>

Data for restoring a previously archived custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `Code!` | The code of the field definition to restore. |

</details>

**Output types:**

<details>

<summary>DeviceTypePayload</summary>

The result of a device type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceType` | [DeviceType](types.md#type-devicetype)! | The created or updated device type. |

</details>

<details>

<summary>DeviceType (entity)</summary>

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
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#type-customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

</details>

---

### deviceTypeDelete

Deletes a device type.

```graphql
deviceTypeDelete(
    input: CatalogItemDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the device type. |

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

### deviceStatusCreate

Creates a new device status.

```graphql
deviceStatusCreate(
    input: DeviceStatusCreateInput!
  ): DeviceStatusPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceStatusCreateInput!` | The input fields for creating the device status. |

**Input types:**

<details>

<summary>DeviceStatusCreateInput</summary>

Input for creating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

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

<summary>DeviceStatusPayload</summary>

The result of a device status mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](types.md#type-devicestatus)! | The created or updated device status. |

</details>

<details>

<summary>DeviceStatus (entity)</summary>

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

</details>

---

### deviceStatusUpdate

Updates a device status.

```graphql
deviceStatusUpdate(
    input: DeviceStatusUpdateInput!
  ): DeviceStatusPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceStatusUpdateInput!` | The input fields for updating the device status. |

**Input types:**

<details>

<summary>DeviceStatusUpdateInput</summary>

Input for updating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |

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

<summary>DeviceStatusPayload</summary>

The result of a device status mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceStatus` | [DeviceStatus](types.md#type-devicestatus)! | The created or updated device status. |

</details>

<details>

<summary>DeviceStatus (entity)</summary>

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

</details>

---

### deviceStatusDelete

Deletes a device status.

```graphql
deviceStatusDelete(
    input: CatalogItemDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the device status. |

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
