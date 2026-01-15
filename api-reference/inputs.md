# Inputs

Input types define the structure of arguments passed to queries and mutations. They specify what data you can provide when creating, updating, filtering, or ordering entities.

## Devices

### DeviceFilter

Filtering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by device types (OR within field). |
| `modelIds` | `[ID!]` | Filter by device models (OR within field). |
| `statusIds` | `[ID!]` | Filter by statuses (OR within field). |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `identifierValue` | `String` | Search by device identifier value. |
| `inventoryIds` | `[ID!]` | Filter by inventories (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter!]](/api-reference/inputs.md#customfieldfilter) | Filter by custom field values. |

### DeviceOrder

Ordering options for devices.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceOrderField](/api-reference/enums.md#deviceorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### DeviceModelFilter

Filtering options for device models.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `code` | [Code](/api-reference/scalars.md#code) | Exact code match. |

### DeviceCreateInput

Input for creating a new device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the device. |
| `typeId` | `ID!` | The device type ID. |
| `modelId` | `ID!` | The device model ID. |
| `statusId` | `ID!` | The initial device status ID. |
| `title` | `String!` | The device display name. |
| `identifiers` | [[DeviceIdentifierInput!]](/api-reference/inputs.md#deviceidentifierinput) | The hardware identifiers. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field values. |

### DeviceUpdateInput

Input for updating an existing device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The device ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `modelId` | `ID` | The new device model. |
| `statusId` | `ID` | The new device status. |
| `title` | `String` | The new display name. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field changes. |

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
| `type` | [DeviceIdType!](/api-reference/enums.md#deviceidtype) | The type of identifier. |
| `value` | `String!` | The identifier value. |
| `namespace` | `String` | The namespace for uniqueness. Null means globally unique. |

### DeviceIdentifierAddInput

Input for adding an identifier to a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `identifier` | [DeviceIdentifierInput!](/api-reference/inputs.md#deviceidentifierinput) | The identifier details. |

### DeviceIdentifierRemoveInput

Input for removing an identifier from a device.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `identifierId` | `ID!` | The identifier ID to remove. |

### DeviceFieldParamsInput

Parameters for DEVICE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple devices can be selected. |

### DeviceTypeCreateInput

Input for creating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### DeviceTypeUpdateInput

Input for updating a device type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### DeviceStatusCreateInput

Input for creating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### DeviceStatusUpdateInput

Input for updating a device status.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

## Assets

### AssetFilter

Filtering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by asset types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter!]](/api-reference/inputs.md#customfieldfilter) | Filter by custom field values. |

### AssetOrder

Ordering options for assets.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetOrderField](/api-reference/enums.md#assetorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### AssetCreateInput

Input for creating a new asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the asset. |
| `typeId` | `ID!` | The asset type ID. |
| `title` | `String!` | The asset display name. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field values. |

### AssetUpdateInput

Input for updating an existing asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field changes. |

### AssetDeleteInput

Input for deleting an asset.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### AssetTypeCreateInput

Input for creating an asset type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### AssetTypeUpdateInput

Input for updating an asset type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

## Asset groups

### AssetGroupFilter

Filtering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by group types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |

### AssetGroupOrder

Ordering options for asset groups.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupOrderField!](/api-reference/enums.md#assetgrouporderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### AssetGroupItemFilter

Filtering options for asset group items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `activeOnly` | `Boolean` | If true, return only currently attached items. |

### AssetGroupItemOrder

Ordering options for asset group items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupItemOrderField!](/api-reference/enums.md#assetgroupitemorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### AssetGroupCreateInput

Input for creating a new asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the group. |
| `typeId` | `ID!` | The group type ID. |
| `title` | `String!` | The group display name. |
| `color` | [HexColorCode](/api-reference/scalars.md#hexcolorcode) | The color for UI display. |

### AssetGroupUpdateInput

Input for updating an existing asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `color` | [HexColorCode](/api-reference/scalars.md#hexcolorcode) | The new color. |

### AssetGroupDeleteInput

Input for deleting an asset group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The asset group ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### AssetGroupItemAddInput

Input for adding an asset to a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to add. |

### AssetGroupItemRemoveInput

Input for removing an asset from a group.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `groupId` | `ID!` | The group ID. |
| `assetId` | `ID!` | The asset ID to remove. |

### AssetGroupTypeCreateInput

Input for creating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput!]](/api-reference/inputs.md#assetgrouptypeconstraintinput) | The allowed asset types with optional limits. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### AssetGroupTypeUpdateInput

Input for updating an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `allowedAssetTypes` | [[AssetGroupTypeConstraintInput!]](/api-reference/inputs.md#assetgrouptypeconstraintinput) | Replace allowed asset types. Null means no change. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### AssetGroupTypeConstraintInput

Input for a constraint defining allowed asset types in an asset group type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetTypeId` | `ID!` | The asset type ID. |
| `maxItems` | `Int` | The maximum assets of this type. Null means unlimited. |

## Geo objects

### GeoObjectFilter

Filtering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by geo object types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter!]](/api-reference/inputs.md#customfieldfilter) | Filter by custom field values. |

### GeoObjectOrder

Ordering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [GeoObjectOrderField](/api-reference/enums.md#geoobjectorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### GeoObjectCreateInput

Input for creating a new geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geometry` | [GeoJSON!](/api-reference/scalars.md#geojson) | The [GeoJSON](https://geojson.org/) geometry. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field values. |

### GeoObjectUpdateInput

Input for updating an existing geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `geometry` | [GeoJSON](/api-reference/scalars.md#geojson) | The new geometry. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field changes. |

### GeoObjectDeleteInput

Input for deleting a geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### GeoObjectTypeCreateInput

Input for creating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### GeoObjectTypeUpdateInput

Input for updating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

## Schedules

### ScheduleFilter

Filtering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by schedule types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter!]](/api-reference/inputs.md#customfieldfilter) | Filter by custom field values. |

### ScheduleOrder

Ordering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ScheduleOrderField](/api-reference/enums.md#scheduleorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### ScheduleCreateInput

Input for creating a new schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the schedule. |
| `typeId` | `ID!` | The schedule type ID. |
| `title` | `String!` | The schedule display name. |
| `scheduleData` | [ScheduleData!](/api-reference/scalars.md#scheduledata) | The schedule data. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field values. |

### ScheduleUpdateInput

Input for updating an existing schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `scheduleData` | [ScheduleData](/api-reference/scalars.md#scheduledata) | The new schedule data. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field changes. |

### ScheduleDeleteInput

Input for deleting a schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### ScheduleTypeCreateInput

Input for creating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### ScheduleTypeUpdateInput

Input for updating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

## Inventory

### DeviceInventoryRelationOrder

Ordering options for device inventory relations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceInventoryRelationOrderField!](/api-reference/enums.md#deviceinventoryrelationorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### InventoryFilter

Filtering options for inventories.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `code` | [Code](/api-reference/scalars.md#code) | Exact code match. |

### InventoryOrder

Ordering options for inventories.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [InventoryOrderField!](/api-reference/enums.md#inventoryorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### InventoryCreateInput

Input for creating a new inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the inventory. |
| `code` | [Code!](/api-reference/scalars.md#code) | The unique code within the organization. |
| `title` | `String!` | The display name. |

### InventoryUpdateInput

Input for updating an existing inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |

### InventoryDeleteInput

Input for deleting an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### DeviceInventoryLinkInput

Input for linking a device to an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `inventoryId` | `ID!` | The inventory ID. |

### DeviceInventoryUnlinkInput

Input for unlinking a device from an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID to unlink. |

## Organizations

### OrganizationFilter

Filtering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentIds` | `[ID!]` | Filter by parent organizations (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

### OrganizationChildrenFilter

Filtering options for organization children. Excludes parentId as it is implicit.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |
| `title` | `String` | Search in title (case-insensitive contains). |

### OrganizationOrder

Ordering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [OrganizationOrderField!](/api-reference/enums.md#organizationorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### OrganizationCreateInput

Input for creating a new organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `code` | [Code!](/api-reference/scalars.md#code) | The unique organization code. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | [[OrganizationFeature!]](/api-reference/enums.md#organizationfeature) | The feature flags to enable. |

### OrganizationUpdateInput

Input for updating an existing organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature!]](/api-reference/enums.md#organizationfeature) | The new feature flags. |

### OrganizationDeleteInput

Input for deleting an organization and all its data.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

## Members

### MemberFilter

Filtering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userIds` | `[ID!]` | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

### MemberOrder

Ordering options for members.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [MemberOrderField!](/api-reference/enums.md#memberorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### PersonNameInput

Input for structured person name components.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `givenNames` | `String!` | The given name(s). |
| `familyNames` | `String!` | The family name(s). |
| `middleName` | `String` | The middle name or patronymic. |

### MemberCreateInput

Input for creating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `userId` | `ID!` | The user ID to add. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The membership-specific custom fields. |

### MemberUpdateInput

Input for updating a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `isActive` | `Boolean` | The new active status. |
| `customFields` | [CustomFieldsPatchInput](/api-reference/inputs.md#customfieldspatchinput) | The custom field changes. |

### MemberRemoveInput

Input for removing a membership.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The membership ID to remove. |
| `version` | `Int!` | The current version for optimistic locking. |

## Integrations

### IntegrationFilter

Filtering options for integrations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |

### IntegrationOrder

Ordering options for integrations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [IntegrationOrderField!](/api-reference/enums.md#integrationorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### IntegrationCreateInput

Input for creating a new integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the integration. |
| `title` | `String!` | The display name. |
| `credentialRef` | `String` | A reference to credentials in a secure vault. |

### IntegrationUpdateInput

Input for updating an existing integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `credentialRef` | `String` | The new credential reference. |
| `isActive` | `Boolean` | The new active status. |

### IntegrationDeleteInput

Input for deleting an integration.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The integration ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

## Access control

### ActorRoleFilter

Filtering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean` | Include expired role assignments. |

### ActorRoleOrder

Ordering options for actor roles.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField!](/api-reference/enums.md#actorroleorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### RolePermissionFilter

Filtering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

### RolePermissionOrder

Ordering options for role permissions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [RolePermissionOrderField!](/api-reference/enums.md#rolepermissionorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### UserScopeFilter

Filtering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

### UserScopeOrder

Ordering options for user scopes.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [UserScopeOrderField!](/api-reference/enums.md#userscopeorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### RoleAssignInput

Input for assigning a role to an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID (user or integration). |
| `roleId` | `ID!` | The role ID to assign. |
| `expireDate` | [DateTime](/api-reference/scalars.md#datetime) | The expiration date. Null means the role is permanent. |

### RoleRevokeInput

Input for revoking a role from an actor.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorRoleId` | `ID!` | The actor role assignment ID to revoke. |

### PermissionGrantInput

Input for granting a permission to a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleId` | `ID!` | The role ID. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID` | The specific entity ID. Null means all entities of the type. |
| `actions` | [[ActionPermission!]!](/api-reference/enums.md#actionpermission) | The actions to allow. |

### PermissionRevokeInput

Input for revoking a permission from a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `permissionId` | `ID!` | The role permission ID to revoke. |

### UserScopeSetInput

Input for setting a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorId` | `ID!` | The actor ID to restrict. |
| `permissionScopeId` | `ID!` | The permission scope ID. |
| `targetEntityId` | `ID!` | The specific entity ID to allow access to. |
| `actions` | [[ActionPermission!]!](/api-reference/enums.md#actionpermission) | The actions to allow. |

### UserScopeRemoveInput

Input for removing a user scope restriction.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userScopeId` | `ID!` | The user scope ID to remove. |

### RoleCreateInput

Input for creating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### RoleUpdateInput

Input for updating a role.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

## Custom fields

### CustomFieldFilter

A filter condition for a custom field value.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | [Code!](/api-reference/scalars.md#code) | The custom field code to filter by. |
| `operator` | [FieldOperator!](/api-reference/enums.md#fieldoperator) | The comparison operator. |
| `value` | [JSON](/api-reference/scalars.md#json) | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

### CustomFieldsPatchInput

Input for updating custom field values using a patch model.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `set` | [JSON](/api-reference/scalars.md#json) | Fields to set or update as a key-value map. |
| `unset` | [[Code!]](/api-reference/scalars.md#code) | Field codes to remove. |

### CustomFieldDefinitionCreateInput

Input for creating a custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization ID. |
| `ownerCatalogItemId` | `ID!` | The owner catalog item ID (EntityType or a specific type like AssetType). |
| `targetEntityTypeId` | `ID!` | The target entity type ID. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `description` | `String` | The description. |
| `fieldType` | [FieldType!](/api-reference/enums.md#fieldtype) | The data type. Immutable after creation. |
| `order` | `Int` | The display order. |
| `params` | [FieldParamsInput!](/api-reference/inputs.md#fieldparamsinput) | The type-specific parameters. Exactly one variant must be provided. |

### CustomFieldDefinitionUpdateInput

Input for updating a custom field definition. Note: `fieldType` cannot be changed.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `description` | `String` | The new description. |
| `order` | `Int` | The new display order. |
| `params` | [FieldParamsInput](/api-reference/inputs.md#fieldparamsinput) | The updated parameters. Only `isRequired` and type-specific fields can be changed. |

### CustomFieldDefinitionDeleteInput

Input for deleting a custom field definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The definition ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

### FieldParamsInput

Field parameters input. Exactly one field must be provided.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `string` | [StringFieldParamsInput](/api-reference/inputs.md#stringfieldparamsinput) | Parameters for STRING field type. |
| `text` | [TextFieldParamsInput](/api-reference/inputs.md#textfieldparamsinput) | Parameters for TEXT field type. |
| `number` | [NumberFieldParamsInput](/api-reference/inputs.md#numberfieldparamsinput) | Parameters for NUMBER field type. |
| `boolean` | [BooleanFieldParamsInput](/api-reference/inputs.md#booleanfieldparamsinput) | Parameters for BOOLEAN field type. |
| `date` | [DateFieldParamsInput](/api-reference/inputs.md#datefieldparamsinput) | Parameters for DATE field type. |
| `datetime` | [DateTimeFieldParamsInput](/api-reference/inputs.md#datetimefieldparamsinput) | Parameters for DATETIME field type. |
| `geojson` | [GeoJsonFieldParamsInput](/api-reference/inputs.md#geojsonfieldparamsinput) | Parameters for GEOJSON field type. |
| `schedule` | [ScheduleFieldParamsInput](/api-reference/inputs.md#schedulefieldparamsinput) | Parameters for SCHEDULE field type. |
| `options` | [OptionsFieldParamsInput](/api-reference/inputs.md#optionsfieldparamsinput) | Parameters for OPTIONS field type. |
| `device` | [DeviceFieldParamsInput](/api-reference/inputs.md#devicefieldparamsinput) | Parameters for DEVICE field type. |
| `reference` | [ReferenceFieldParamsInput](/api-reference/inputs.md#referencefieldparamsinput) | Parameters for REFERENCE field type. |
| `catalog` | [CatalogFieldParamsInput](/api-reference/inputs.md#catalogfieldparamsinput) | Parameters for CATALOG field type. |
| `tag` | [TagFieldParamsInput](/api-reference/inputs.md#tagfieldparamsinput) | Parameters for TAG field type. |

### StringFieldParamsInput

Parameters for STRING field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `minLength` | `Int` | The minimum character length. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

### TextFieldParamsInput

Parameters for TEXT field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `maxLength` | `Int` | The maximum character length. |
| `defaultValue` | `String` | The default value. |
| `trim` | `Boolean` | Whether to trim whitespace. |

### NumberFieldParamsInput

Parameters for NUMBER field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `min` | `Float` | The minimum allowed value. |
| `max` | `Float` | The maximum allowed value. |
| `precision` | `Int` | The decimal precision. |
| `defaultValue` | `Float` | The default value. |

### BooleanFieldParamsInput

Parameters for BOOLEAN field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | `Boolean` | The default value. |

### DateFieldParamsInput

Parameters for DATE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | [Date](/api-reference/scalars.md#date) | The default value. |

### DateTimeFieldParamsInput

Parameters for DATETIME field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `defaultValue` | [DateTime](/api-reference/scalars.md#datetime) | The default value. |

### GeoJsonFieldParamsInput

Parameters for GEOJSON field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `allowedTypes` | [[GeoJsonGeometryType!]](/api-reference/enums.md#geojsongeometrytype) | The allowed geometry types. Null means all types are allowed. |

### ScheduleFieldParamsInput

Parameters for SCHEDULE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |

### OptionsFieldParamsInput

Parameters for OPTIONS field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple options can be selected. |
| `options` | [[FieldOptionInput!]!](/api-reference/inputs.md#fieldoptioninput) | The available options. |
| `defaultValue` | [Code](/api-reference/scalars.md#code) | The default option code. |

### FieldOptionInput

Input for an option definition.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | [Code!](/api-reference/scalars.md#code) | The unique code. |
| `label` | `String!` | The display label. |
| `description` | `String` | The description. |
| `isArchived` | `Boolean` | Whether this option is archived. |

### ReferenceFieldParamsInput

Parameters for REFERENCE field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple references can be selected. |
| `refEntityTypeCode` | [Code!](/api-reference/scalars.md#code) | The entity type code that can be referenced. |

### CatalogFieldParamsInput

Parameters for CATALOG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple items can be selected. |
| `refCatalogCode` | [Code!](/api-reference/scalars.md#code) | The catalog code that items can be selected from. |
| `defaultValue` | [Code](/api-reference/scalars.md#code) | The default item code. |

### TagFieldParamsInput

Parameters for TAG field type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required. |
| `isMulti` | `Boolean` | Whether multiple tags can be selected. |
| `defaultValue` | [Code](/api-reference/scalars.md#code) | The default tag code. |

## Filtering & ordering

### CatalogItemFilter

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code) | Match any of these codes. |

### CatalogItemChildrenFilter

Filtering options for catalog item children.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |

### CatalogItemOrder

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

### TagFilter

Filtering options for tags.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |

### AuditEventFilter

Filtering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `aggregateTypes` | [[Code!]](/api-reference/scalars.md#code) | Filter by entity types (OR within field). |
| `aggregateIds` | `[ID!]` | Filter by specific entity IDs (OR within field). |
| `eventTypes` | [[AuditEventType!]](/api-reference/enums.md#auditeventtype) | Filter by event types (OR within field). |
| `sourceTypes` | [[SourceType!]](/api-reference/enums.md#sourcetype) | Filter by source types (OR within field). |
| `traceId` | `String` | Filter by trace ID. |
| `from` | [DateTime](/api-reference/scalars.md#datetime) | Return events that occurred after this timestamp. |
| `to` | [DateTime](/api-reference/scalars.md#datetime) | Return events that occurred before this timestamp. |

### AuditEventOrder

Ordering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AuditEventOrderField!](/api-reference/enums.md#auditeventorderfield) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection) | The direction to order. |

## Catalog items

### CatalogItemMetaInput

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](/api-reference/scalars.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](/api-reference/scalars.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

### UserCatalogItemCreateInput

Input for creating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `catalogId` | `ID!` | The catalog to add the item to. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code, unique within the catalog and organization. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `parentId` | `ID` | The parent item ID for hierarchical catalogs. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### UserCatalogItemUpdateInput

Input for updating a user catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `parentId` | `ID` | The new parent ID for hierarchical items. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### TagCreateInput

Input for creating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | [Code!](/api-reference/scalars.md#code) | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. |
| `entityTypeIds` | `[ID!]` | The entity types this tag can be applied to. Empty means universal. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### TagUpdateInput

Input for updating a tag.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `entityTypeIds` | `[ID!]` | Replace entity types. Null means no change, empty means universal. |
| `meta` | [CatalogItemMetaInput](/api-reference/inputs.md#catalogitemmetainput) | The display properties. |

### CatalogItemDeleteInput

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

## Other

### GeoPointInput

Input for a geographic coordinate point.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `lat` | [Latitude!](/api-reference/scalars.md#latitude) | The latitude coordinate (-90 to 90 degrees). |
| `lng` | [Longitude!](/api-reference/scalars.md#longitude) | The longitude coordinate (-180 to 180 degrees). |
| `altitude` | `Float` | The altitude in meters above sea level. |
| `accuracy` | `Float` | The horizontal accuracy in meters. |

### MyProfileUpdateInput

Input for updating the current user's profile.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | [PersonNameInput!](/api-reference/inputs.md#personnameinput) | The structured name components. |

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
