# Mutations

Mutations modify data in the Navixy database. Most mutations require authentication and appropriate permissions.

{% hint style="info" %}
**Input types:** Mutation arguments use dedicated input types (e.g., `DeviceCreateInput`). For convenience, input type fields are expanded inline below each mutation rather than on a separate page.
{% endhint %}

{% hint style="warning" %}
**Optimistic locking:** Update and delete mutations require a `version` field in the input. See [Optimistic Locking](../optimistic-locking.md) for details.
{% endhint %}

## Devices

### deviceCreate

Creates a new device.

```graphql
deviceCreate(input: DeviceCreateInput!): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceCreateInput!` | The input fields for creating the device. |

**DeviceCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String!` | The device display name. |
| `identifiers` | `[DeviceIdentifierInput!]` | The hardware identifiers. |
| `customFields` | `CustomFieldsPatchInput` | The custom field values. |

**Returns:** [DevicePayload](/api-reference/objects.md#devicepayload/)

### deviceUpdate

Updates an existing device.

```graphql
deviceUpdate(input: DeviceUpdateInput!): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceUpdateInput!` | The input fields for updating the device. |

**DeviceUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `modelId` | `ID` | The new device model. |
| `statusId` | `ID` | The new device status. |
| `title` | `String` | The new display name. |
| `customFields` | `CustomFieldsPatchInput` | The custom field changes. |

**Returns:** [DevicePayload](/api-reference/objects.md#devicepayload/)

### deviceDelete

Deletes a device.

```graphql
deviceDelete(input: DeviceDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceDeleteInput!` | The input fields for deleting the device. |

**DeviceDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

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

**DeviceIdentifierAddInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | `DeviceIdentifierInput!` | The identifier details. |

**Returns:** [DeviceIdentifierPayload](/api-reference/objects.md#deviceidentifierpayload/)

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

**DeviceIdentifierRemoveInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### deviceTypeCreate

Creates a new device type.

```graphql
deviceTypeCreate(input: DeviceTypeCreateInput!): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceTypeCreateInput!` | The input fields for creating the device type. |

**DeviceTypeCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [DeviceTypePayload](/api-reference/objects.md#devicetypepayload/)

### deviceTypeUpdate

Updates a device type.

```graphql
deviceTypeUpdate(input: DeviceTypeUpdateInput!): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceTypeUpdateInput!` | The input fields for updating the device type. |

**DeviceTypeUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [DeviceTypePayload](/api-reference/objects.md#devicetypepayload/)

### deviceTypeDelete

Deletes a device type.

```graphql
deviceTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the device type. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

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

**DeviceStatusCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [DeviceStatusPayload](/api-reference/objects.md#devicestatuspayload/)

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

**DeviceStatusUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [DeviceStatusPayload](/api-reference/objects.md#devicestatuspayload/)

### deviceStatusDelete

Deletes a device status.

```graphql
deviceStatusDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the device status. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Assets

### assetCreate

Creates a new asset.

```graphql
assetCreate(input: AssetCreateInput!): AssetPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetCreateInput!` | The input fields for creating the asset. |

**AssetCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the asset. |
| `typeId` | `ID!` | The asset type ID. |
| `title` | `String!` | The asset display name. |
| `customFields` | `CustomFieldsPatchInput` | The custom field values. |

**Returns:** [AssetPayload](/api-reference/objects.md#assetpayload/)

### assetUpdate

Updates an existing asset.

```graphql
assetUpdate(input: AssetUpdateInput!): AssetPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetUpdateInput!` | The input fields for updating the asset. |

**AssetUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `customFields` | `CustomFieldsPatchInput` | The custom field changes. |

**Returns:** [AssetPayload](/api-reference/objects.md#assetpayload/)

### assetDelete

Deletes an asset.

```graphql
assetDelete(input: AssetDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetDeleteInput!` | The input fields for deleting the asset. |

**AssetDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### assetTypeCreate

Creates a new asset type.

```graphql
assetTypeCreate(input: AssetTypeCreateInput!): AssetTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetTypeCreateInput!` | The input fields for creating the asset type. |

**AssetTypeCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [AssetTypePayload](/api-reference/objects.md#assettypepayload/)

### assetTypeUpdate

Updates an asset type.

```graphql
assetTypeUpdate(input: AssetTypeUpdateInput!): AssetTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetTypeUpdateInput!` | The input fields for updating the asset type. |

**AssetTypeUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [AssetTypePayload](/api-reference/objects.md#assettypepayload/)

### assetTypeDelete

Deletes an asset type.

```graphql
assetTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the asset type. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Asset groups

### assetGroupCreate

Creates a new asset group.

```graphql
assetGroupCreate(input: AssetGroupCreateInput!): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupCreateInput!` | The input fields for creating the asset group. |

**AssetGroupCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the group. |
| `typeId` | `ID!` | The group type ID. |
| `title` | `String!` | The group display name. |
| `color` | [HexColorCode](/api-reference/scalars.md#hexcolorcode/) | The color for UI display. |

**Returns:** [AssetGroupPayload](/api-reference/objects.md#assetgrouppayload/)

### assetGroupUpdate

Updates an existing asset group.

```graphql
assetGroupUpdate(input: AssetGroupUpdateInput!): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupUpdateInput!` | The input fields for updating the asset group. |

**AssetGroupUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `color` | [HexColorCode](/api-reference/scalars.md#hexcolorcode/) | The new color. |

**Returns:** [AssetGroupPayload](/api-reference/objects.md#assetgrouppayload/)

### assetGroupDelete

Deletes an asset group.

```graphql
assetGroupDelete(input: AssetGroupDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupDeleteInput!` | The input fields for deleting the asset group. |

**AssetGroupDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### assetGroupItemAdd

Adds an asset to a group.

```graphql
assetGroupItemAdd(
  input: AssetGroupItemAddInput!
): AssetGroupItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupItemAddInput!` | The input fields for adding the asset to the group. |

**AssetGroupItemAddInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to add. |

**Returns:** [AssetGroupItemPayload](/api-reference/objects.md#assetgroupitempayload/)

### assetGroupItemRemove

Removes an asset from a group.

```graphql
assetGroupItemRemove(input: AssetGroupItemRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupItemRemoveInput!` | The input fields for removing the asset from the group. |

**AssetGroupItemRemoveInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to remove. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### assetGroupTypeCreate

Creates a new asset group type.

```graphql
assetGroupTypeCreate(
  input: AssetGroupTypeCreateInput!
): AssetGroupTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupTypeCreateInput!` | The input fields for creating the asset group type. |

**AssetGroupTypeCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `allowedAssetTypes` | `[AssetGroupTypeConstraintInput!]` | The allowed asset types with optional limits. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [AssetGroupTypePayload](/api-reference/objects.md#assetgrouptypepayload/)

### assetGroupTypeUpdate

Updates an asset group type.

```graphql
assetGroupTypeUpdate(
  input: AssetGroupTypeUpdateInput!
): AssetGroupTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `AssetGroupTypeUpdateInput!` | The input fields for updating the asset group type. |

**AssetGroupTypeUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `allowedAssetTypes` | `[AssetGroupTypeConstraintInput!]` | Replace allowed asset types. Null means no change. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [AssetGroupTypePayload](/api-reference/objects.md#assetgrouptypepayload/)

### assetGroupTypeDelete

Deletes an asset group type.

```graphql
assetGroupTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the asset group type. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Geo objects

### geoObjectCreate

Creates a new geo object.

```graphql
geoObjectCreate(input: GeoObjectCreateInput!): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectCreateInput!` | The input fields for creating the geo object. |

**GeoObjectCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geometry` | [GeoJSON!](/api-reference/scalars.md#geojson/) | The [GeoJSON](https://geojson.org/) geometry. |
| `customFields` | `CustomFieldsPatchInput` | The custom field values. |

**Returns:** [GeoObjectPayload](/api-reference/objects.md#geoobjectpayload/)

### geoObjectUpdate

Updates an existing geo object.

```graphql
geoObjectUpdate(input: GeoObjectUpdateInput!): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectUpdateInput!` | The input fields for updating the geo object. |

**GeoObjectUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `geometry` | [GeoJSON](/api-reference/scalars.md#geojson/) | The new geometry. |
| `customFields` | `CustomFieldsPatchInput` | The custom field changes. |

**Returns:** [GeoObjectPayload](/api-reference/objects.md#geoobjectpayload/)

### geoObjectDelete

Deletes a geo object.

```graphql
geoObjectDelete(input: GeoObjectDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectDeleteInput!` | The input fields for deleting the geo object. |

**GeoObjectDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### geoObjectTypeCreate

Creates a new geo object type.

```graphql
geoObjectTypeCreate(
  input: GeoObjectTypeCreateInput!
): GeoObjectTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectTypeCreateInput!` | The input fields for creating the geo object type. |

**GeoObjectTypeCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [GeoObjectTypePayload](/api-reference/objects.md#geoobjecttypepayload/)

### geoObjectTypeUpdate

Updates a geo object type.

```graphql
geoObjectTypeUpdate(
  input: GeoObjectTypeUpdateInput!
): GeoObjectTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `GeoObjectTypeUpdateInput!` | The input fields for updating the geo object type. |

**GeoObjectTypeUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [GeoObjectTypePayload](/api-reference/objects.md#geoobjecttypepayload/)

### geoObjectTypeDelete

Deletes a geo object type.

```graphql
geoObjectTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the geo object type. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Schedules

### scheduleCreate

Creates a new schedule.

```graphql
scheduleCreate(input: ScheduleCreateInput!): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleCreateInput!` | The input fields for creating the schedule. |

**ScheduleCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the schedule. |
| `typeId` | `ID!` | The schedule type ID. |
| `title` | `String!` | The schedule display name. |
| `scheduleData` | [ScheduleData!](/api-reference/scalars.md#scheduledata/) | The schedule data. |
| `customFields` | `CustomFieldsPatchInput` | The custom field values. |

**Returns:** [SchedulePayload](/api-reference/objects.md#schedulepayload/)

### scheduleUpdate

Updates an existing schedule.

```graphql
scheduleUpdate(input: ScheduleUpdateInput!): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleUpdateInput!` | The input fields for updating the schedule. |

**ScheduleUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `scheduleData` | [ScheduleData](/api-reference/scalars.md#scheduledata/) | The new schedule data. |
| `customFields` | `CustomFieldsPatchInput` | The custom field changes. |

**Returns:** [SchedulePayload](/api-reference/objects.md#schedulepayload/)

### scheduleDelete

Deletes a schedule.

```graphql
scheduleDelete(input: ScheduleDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleDeleteInput!` | The input fields for deleting the schedule. |

**ScheduleDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Inventory

### inventoryCreate

Creates a new inventory.

```graphql
inventoryCreate(input: InventoryCreateInput!): InventoryPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `InventoryCreateInput!` | The input fields for creating the inventory. |

**InventoryCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the inventory. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The unique code within the organization. |
| `title` | `String!` | The display name. |

**Returns:** [InventoryPayload](/api-reference/objects.md#inventorypayload/)

### inventoryUpdate

Updates an existing inventory.

```graphql
inventoryUpdate(input: InventoryUpdateInput!): InventoryPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `InventoryUpdateInput!` | The input fields for updating the inventory. |

**InventoryUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |

**Returns:** [InventoryPayload](/api-reference/objects.md#inventorypayload/)

### inventoryDelete

Deletes an inventory.

```graphql
inventoryDelete(input: InventoryDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `InventoryDeleteInput!` | The input fields for deleting the inventory. |

**InventoryDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Organizations

### organizationCreate

Creates a new organization.

```graphql
organizationCreate(
  input: OrganizationCreateInput!
): OrganizationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `OrganizationCreateInput!` | The input fields for creating the organization. |

**OrganizationCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The unique organization code. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | [[OrganizationFeature!]](/api-reference/enums.md#organizationfeature/) | The feature flags to enable. |

**Returns:** [OrganizationPayload](/api-reference/objects.md#organizationpayload/)

### organizationUpdate

Updates an existing organization.

```graphql
organizationUpdate(
  input: OrganizationUpdateInput!
): OrganizationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `OrganizationUpdateInput!` | The input fields for updating the organization. |

**OrganizationUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature!]](/api-reference/enums.md#organizationfeature/) | The new feature flags. |

**Returns:** [OrganizationPayload](/api-reference/objects.md#organizationpayload/)

### organizationDelete

Deletes an organization and all its data.

```graphql
organizationDelete(input: OrganizationDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `OrganizationDeleteInput!` | The input fields for deleting the organization. |

**OrganizationDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## User profile

### myProfileUpdate

Updates the current user's profile (name only).

```graphql
myProfileUpdate(input: MyProfileUpdateInput!): UserPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MyProfileUpdateInput!` | The input fields for updating the profile. |

**MyProfileUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | `PersonNameInput!` | The structured name components. |

**Returns:** [UserPayload](/api-reference/objects.md#userpayload/)

## Members

### memberCreate

Adds a user to an organization as a member.

```graphql
memberCreate(input: MemberCreateInput!): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MemberCreateInput!` | The input fields for creating the membership. |

**MemberCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `userId` | `ID!` | The user ID to add. |
| `customFields` | `CustomFieldsPatchInput` | The membership-specific custom fields. |

**Returns:** [MemberPayload](/api-reference/objects.md#memberpayload/)

### memberUpdate

Updates a membership.

```graphql
memberUpdate(input: MemberUpdateInput!): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MemberUpdateInput!` | The input fields for updating the membership. |

**MemberUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `isActive` | `Boolean` | The new active status. |
| `customFields` | `CustomFieldsPatchInput` | The custom field changes. |

**Returns:** [MemberPayload](/api-reference/objects.md#memberpayload/)

### memberRemove

Removes a user from an organization.

```graphql
memberRemove(input: MemberRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `MemberRemoveInput!` | The input fields for removing the membership. |

**MemberRemoveInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to remove. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Integrations

### integrationCreate

Creates a new integration.

```graphql
integrationCreate(input: IntegrationCreateInput!): IntegrationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `IntegrationCreateInput!` | The input fields for creating the integration. |

**IntegrationCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the integration. |
| `title` | `String!` | The display name. |
| `credentialRef` | `String` | A reference to credentials in a secure vault. |

**Returns:** [IntegrationPayload](/api-reference/objects.md#integrationpayload/)

### integrationUpdate

Updates an existing integration.

```graphql
integrationUpdate(input: IntegrationUpdateInput!): IntegrationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `IntegrationUpdateInput!` | The input fields for updating the integration. |

**IntegrationUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `credentialRef` | `String` | The new credential reference. |
| `isActive` | `Boolean` | The new active status. |

**Returns:** [IntegrationPayload](/api-reference/objects.md#integrationpayload/)

### integrationDelete

Deletes an integration.

```graphql
integrationDelete(input: IntegrationDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `IntegrationDeleteInput!` | The input fields for deleting the integration. |

**IntegrationDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Access control

### roleAssign

Assigns a role to an actor.

```graphql
roleAssign(input: RoleAssignInput!): ActorRolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleAssignInput!` | The input fields for assigning the role. |

**RoleAssignInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID (user or integration). |
| `roleId` | `ID!` | The role ID to assign. |
| `expireDate` | [DateTime](/api-reference/scalars.md#datetime/) | The expiration date. Null means the role is permanent. |

**Returns:** [ActorRolePayload](/api-reference/objects.md#actorrolepayload/)

### roleRevoke

Revokes a role from an actor.

```graphql
roleRevoke(input: RoleRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleRevokeInput!` | The input fields for revoking the role. |

**RoleRevokeInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### permissionGrant

Grants a permission to a role.

```graphql
permissionGrant(input: PermissionGrantInput!): RolePermissionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `PermissionGrantInput!` | The input fields for granting the permission. |

**PermissionGrantInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleId` | `ID!` | The role ID. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID` | The specific entity ID. Null means all entities of the type. |
| `actions` | [[ActionPermission!]!](/api-reference/enums.md#actionpermission/) | The actions to allow. |

**Returns:** [RolePermissionPayload](/api-reference/objects.md#rolepermissionpayload/)

### permissionRevoke

Revokes a permission from a role.

```graphql
permissionRevoke(input: PermissionRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `PermissionRevokeInput!` | The input fields for revoking the permission. |

**PermissionRevokeInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### userScopeSet

Sets a user scope restriction.

```graphql
userScopeSet(input: UserScopeSetInput!): UserScopePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserScopeSetInput!` | The input fields for setting the user scope. |

**UserScopeSetInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID to restrict. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID!` | The specific entity ID to allow access to. |
| `actions` | [[ActionPermission!]!](/api-reference/enums.md#actionpermission/) | The actions to allow. |

**Returns:** [UserScopePayload](/api-reference/objects.md#userscopepayload/)

### userScopeRemove

Removes a user scope restriction.

```graphql
userScopeRemove(input: UserScopeRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserScopeRemoveInput!` | The input fields for removing the user scope. |

**UserScopeRemoveInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### roleCreate

Creates a new role.

```graphql
roleCreate(input: RoleCreateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleCreateInput!` | The input fields for creating the role. |

**RoleCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [RolePayload](/api-reference/objects.md#rolepayload/)

### roleUpdate

Updates a role.

```graphql
roleUpdate(input: RoleUpdateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `RoleUpdateInput!` | The input fields for updating the role. |

**RoleUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [RolePayload](/api-reference/objects.md#rolepayload/)

### roleDelete

Deletes a role.

```graphql
roleDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the role. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Device relations

### deviceInventoryLink

Links a device to an inventory.

```graphql
deviceInventoryLink(
  input: DeviceInventoryLinkInput!
): DeviceInventoryRelationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceInventoryLinkInput!` | The input fields for linking the device. |

**DeviceInventoryLinkInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `inventoryId` | `ID!` | The inventory ID. |

**Returns:** [DeviceInventoryRelationPayload](/api-reference/objects.md#deviceinventoryrelationpayload/)

### deviceInventoryUnlink

Unlinks a device from an inventory.

```graphql
deviceInventoryUnlink(
  input: DeviceInventoryUnlinkInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceInventoryUnlinkInput!` | The input fields for unlinking the device. |

**DeviceInventoryUnlinkInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID to unlink. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

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

**DeviceRelationCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `firstId` | `ID!` | The first device ID. |
| `secondId` | `ID!` | The second device ID. |
| `typeId` | `ID!` | The relationship type ID. |

**Returns:** [DeviceRelationPayload](/api-reference/objects.md#devicerelationpayload/)

### deviceRelationRemove

Removes a device relationship.

```graphql
deviceRelationRemove(input: DeviceRelationRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceRelationRemoveInput!` | The input fields for removing the relationship. |

**DeviceRelationRemoveInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The relationship ID to remove. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Custom fields

### customFieldDefinitionCreate

Creates a custom field definition.

```graphql
customFieldDefinitionCreate(
  input: CustomFieldDefinitionCreateInput!
): CustomFieldDefinitionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CustomFieldDefinitionCreateInput!` | The input fields for creating the definition. |

**CustomFieldDefinitionCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `ownerCatalogItemId` | `ID!` | The owner catalog item ID (EntityType or a specific type like AssetType). |
| `targetEntityTypeId` | `ID!` | The target entity type ID. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType!](/api-reference/enums.md#fieldtype/) | The data type. Immutable after creation. |
| `order` | `Int` | The display order. |
| `params` | `FieldParamsInput!` | The type-specific parameters. Exactly one variant must be provided. |

**Returns:** [CustomFieldDefinitionPayload](/api-reference/objects.md#customfielddefinitionpayload/)

### customFieldDefinitionUpdate

Updates a custom field definition. Note: `fieldType` cannot be changed.

```graphql
customFieldDefinitionUpdate(
  input: CustomFieldDefinitionUpdateInput!
): CustomFieldDefinitionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CustomFieldDefinitionUpdateInput!` | The input fields for updating the definition. |

**CustomFieldDefinitionUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | `FieldParamsInput` | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

**Returns:** [CustomFieldDefinitionPayload](/api-reference/objects.md#customfielddefinitionpayload/)

### customFieldDefinitionDelete

Deletes a custom field definition.

```graphql
customFieldDefinitionDelete(
  input: CustomFieldDefinitionDeleteInput!
): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CustomFieldDefinitionDeleteInput!` | The input fields for deleting the definition. |

**CustomFieldDefinitionDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

## Catalog items

### scheduleTypeCreate

Creates a new schedule type.

```graphql
scheduleTypeCreate(
  input: ScheduleTypeCreateInput!
): ScheduleTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleTypeCreateInput!` | The input fields for creating the schedule type. |

**ScheduleTypeCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [ScheduleTypePayload](/api-reference/objects.md#scheduletypepayload/)

### scheduleTypeUpdate

Updates a schedule type.

```graphql
scheduleTypeUpdate(
  input: ScheduleTypeUpdateInput!
): ScheduleTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleTypeUpdateInput!` | The input fields for updating the schedule type. |

**ScheduleTypeUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [ScheduleTypePayload](/api-reference/objects.md#scheduletypepayload/)

### scheduleTypeDelete

Deletes a schedule type.

```graphql
scheduleTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the schedule type. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### tagCreate

Creates a new tag.

```graphql
tagCreate(input: TagCreateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `TagCreateInput!` | The input fields for creating the tag. |

**TagCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [TagPayload](/api-reference/objects.md#tagpayload/)

### tagUpdate

Updates a tag.

```graphql
tagUpdate(input: TagUpdateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `TagUpdateInput!` | The input fields for updating the tag. |

**TagUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [TagPayload](/api-reference/objects.md#tagpayload/)

### tagDelete

Deletes a tag.

```graphql
tagDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the tag. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)

### userCatalogItemCreate

Creates a new user catalog item.

```graphql
userCatalogItemCreate(
  input: UserCatalogItemCreateInput!
): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserCatalogItemCreateInput!` | The input fields for creating the item. |

**UserCatalogItemCreateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | [Code!](/api-reference/scalars.md#code/) | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [UserCatalogItemPayload](/api-reference/objects.md#usercatalogitempayload/)

### userCatalogItemUpdate

Updates a user catalog item.

```graphql
userCatalogItemUpdate(
  input: UserCatalogItemUpdateInput!
): UserCatalogItemPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `UserCatalogItemUpdateInput!` | The input fields for updating the item. |

**UserCatalogItemUpdateInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | `CatalogItemMetaInput` | The display properties. |

**Returns:** [UserCatalogItemPayload](/api-reference/objects.md#usercatalogitempayload/)

### userCatalogItemDelete

Deletes a user catalog item.

```graphql
userCatalogItemDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogItemDeleteInput!` | The input fields for deleting the item. |

**CatalogItemDeleteInput** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload/)
