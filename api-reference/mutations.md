# Mutations

Mutations modify data in the Navixy database. Most mutations require authentication and appropriate permissions. Update and delete mutations use [optimistic locking](../optimistic-locking.md) via a `version` field in the input.

Argument types link to their definitions on the [Inputs](inputs.md) page. Return types link to [Objects](objects.md).

## Devices

### deviceCreate

Creates a new device.

```graphql
deviceCreate(input: DeviceCreateInput!): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceCreateInput!](/api-reference/inputs.md#devicecreateinput) | The input fields for creating the device. |

**Returns:** [DevicePayload](/api-reference/objects.md#devicepayload)

### deviceUpdate

Updates an existing device.

```graphql
deviceUpdate(input: DeviceUpdateInput!): DevicePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceUpdateInput!](/api-reference/inputs.md#deviceupdateinput) | The input fields for updating the device. |

**Returns:** [DevicePayload](/api-reference/objects.md#devicepayload)

### deviceDelete

Deletes a device.

```graphql
deviceDelete(input: DeviceDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceDeleteInput!](/api-reference/inputs.md#devicedeleteinput) | The input fields for deleting the device. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [DeviceIdentifierAddInput!](/api-reference/inputs.md#deviceidentifieraddinput) | The input fields for adding the identifier. |

**Returns:** [DeviceIdentifierPayload](/api-reference/objects.md#deviceidentifierpayload)

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
| `input` | [DeviceIdentifierRemoveInput!](/api-reference/inputs.md#deviceidentifierremoveinput) | The input fields for removing the identifier. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

### deviceTypeCreate

Creates a new device type.

```graphql
deviceTypeCreate(input: DeviceTypeCreateInput!): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceTypeCreateInput!](/api-reference/inputs.md#devicetypecreateinput) | The input fields for creating the device type. |

**Returns:** [DeviceTypePayload](/api-reference/objects.md#devicetypepayload)

### deviceTypeUpdate

Updates a device type.

```graphql
deviceTypeUpdate(input: DeviceTypeUpdateInput!): DeviceTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceTypeUpdateInput!](/api-reference/inputs.md#devicetypeupdateinput) | The input fields for updating the device type. |

**Returns:** [DeviceTypePayload](/api-reference/objects.md#devicetypepayload)

### deviceTypeDelete

Deletes a device type.

```graphql
deviceTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the device type. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [DeviceStatusCreateInput!](/api-reference/inputs.md#devicestatuscreateinput) | The input fields for creating the device status. |

**Returns:** [DeviceStatusPayload](/api-reference/objects.md#devicestatuspayload)

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
| `input` | [DeviceStatusUpdateInput!](/api-reference/inputs.md#devicestatusupdateinput) | The input fields for updating the device status. |

**Returns:** [DeviceStatusPayload](/api-reference/objects.md#devicestatuspayload)

### deviceStatusDelete

Deletes a device status.

```graphql
deviceStatusDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the device status. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Assets

### assetCreate

Creates a new asset.

```graphql
assetCreate(input: AssetCreateInput!): AssetPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetCreateInput!](/api-reference/inputs.md#assetcreateinput) | The input fields for creating the asset. |

**Returns:** [AssetPayload](/api-reference/objects.md#assetpayload)

### assetUpdate

Updates an existing asset.

```graphql
assetUpdate(input: AssetUpdateInput!): AssetPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetUpdateInput!](/api-reference/inputs.md#assetupdateinput) | The input fields for updating the asset. |

**Returns:** [AssetPayload](/api-reference/objects.md#assetpayload)

### assetDelete

Deletes an asset.

```graphql
assetDelete(input: AssetDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetDeleteInput!](/api-reference/inputs.md#assetdeleteinput) | The input fields for deleting the asset. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

### assetTypeCreate

Creates a new asset type.

```graphql
assetTypeCreate(input: AssetTypeCreateInput!): AssetTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetTypeCreateInput!](/api-reference/inputs.md#assettypecreateinput) | The input fields for creating the asset type. |

**Returns:** [AssetTypePayload](/api-reference/objects.md#assettypepayload)

### assetTypeUpdate

Updates an asset type.

```graphql
assetTypeUpdate(input: AssetTypeUpdateInput!): AssetTypePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetTypeUpdateInput!](/api-reference/inputs.md#assettypeupdateinput) | The input fields for updating the asset type. |

**Returns:** [AssetTypePayload](/api-reference/objects.md#assettypepayload)

### assetTypeDelete

Deletes an asset type.

```graphql
assetTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the asset type. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Asset groups

### assetGroupCreate

Creates a new asset group.

```graphql
assetGroupCreate(input: AssetGroupCreateInput!): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetGroupCreateInput!](/api-reference/inputs.md#assetgroupcreateinput) | The input fields for creating the asset group. |

**Returns:** [AssetGroupPayload](/api-reference/objects.md#assetgrouppayload)

### assetGroupUpdate

Updates an existing asset group.

```graphql
assetGroupUpdate(input: AssetGroupUpdateInput!): AssetGroupPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetGroupUpdateInput!](/api-reference/inputs.md#assetgroupupdateinput) | The input fields for updating the asset group. |

**Returns:** [AssetGroupPayload](/api-reference/objects.md#assetgrouppayload)

### assetGroupDelete

Deletes an asset group.

```graphql
assetGroupDelete(input: AssetGroupDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetGroupDeleteInput!](/api-reference/inputs.md#assetgroupdeleteinput) | The input fields for deleting the asset group. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [AssetGroupItemAddInput!](/api-reference/inputs.md#assetgroupitemaddinput) | The input fields for adding the asset to the group. |

**Returns:** [AssetGroupItemPayload](/api-reference/objects.md#assetgroupitempayload)

### assetGroupItemRemove

Removes an asset from a group.

```graphql
assetGroupItemRemove(input: AssetGroupItemRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [AssetGroupItemRemoveInput!](/api-reference/inputs.md#assetgroupitemremoveinput) | The input fields for removing the asset from the group. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [AssetGroupTypeCreateInput!](/api-reference/inputs.md#assetgrouptypecreateinput) | The input fields for creating the asset group type. |

**Returns:** [AssetGroupTypePayload](/api-reference/objects.md#assetgrouptypepayload)

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
| `input` | [AssetGroupTypeUpdateInput!](/api-reference/inputs.md#assetgrouptypeupdateinput) | The input fields for updating the asset group type. |

**Returns:** [AssetGroupTypePayload](/api-reference/objects.md#assetgrouptypepayload)

### assetGroupTypeDelete

Deletes an asset group type.

```graphql
assetGroupTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the asset group type. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Geo objects

### geoObjectCreate

Creates a new geo object.

```graphql
geoObjectCreate(input: GeoObjectCreateInput!): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectCreateInput!](/api-reference/inputs.md#geoobjectcreateinput) | The input fields for creating the geo object. |

**Returns:** [GeoObjectPayload](/api-reference/objects.md#geoobjectpayload)

### geoObjectUpdate

Updates an existing geo object.

```graphql
geoObjectUpdate(input: GeoObjectUpdateInput!): GeoObjectPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectUpdateInput!](/api-reference/inputs.md#geoobjectupdateinput) | The input fields for updating the geo object. |

**Returns:** [GeoObjectPayload](/api-reference/objects.md#geoobjectpayload)

### geoObjectDelete

Deletes a geo object.

```graphql
geoObjectDelete(input: GeoObjectDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [GeoObjectDeleteInput!](/api-reference/inputs.md#geoobjectdeleteinput) | The input fields for deleting the geo object. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [GeoObjectTypeCreateInput!](/api-reference/inputs.md#geoobjecttypecreateinput) | The input fields for creating the geo object type. |

**Returns:** [GeoObjectTypePayload](/api-reference/objects.md#geoobjecttypepayload)

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
| `input` | [GeoObjectTypeUpdateInput!](/api-reference/inputs.md#geoobjecttypeupdateinput) | The input fields for updating the geo object type. |

**Returns:** [GeoObjectTypePayload](/api-reference/objects.md#geoobjecttypepayload)

### geoObjectTypeDelete

Deletes a geo object type.

```graphql
geoObjectTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the geo object type. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Schedules

### scheduleCreate

Creates a new schedule.

```graphql
scheduleCreate(input: ScheduleCreateInput!): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleCreateInput!](/api-reference/inputs.md#schedulecreateinput) | The input fields for creating the schedule. |

**Returns:** [SchedulePayload](/api-reference/objects.md#schedulepayload)

### scheduleUpdate

Updates an existing schedule.

```graphql
scheduleUpdate(input: ScheduleUpdateInput!): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleUpdateInput!](/api-reference/inputs.md#scheduleupdateinput) | The input fields for updating the schedule. |

**Returns:** [SchedulePayload](/api-reference/objects.md#schedulepayload)

### scheduleDelete

Deletes a schedule.

```graphql
scheduleDelete(input: ScheduleDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [ScheduleDeleteInput!](/api-reference/inputs.md#scheduledeleteinput) | The input fields for deleting the schedule. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Inventory

### inventoryCreate

Creates a new inventory.

```graphql
inventoryCreate(input: InventoryCreateInput!): InventoryPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [InventoryCreateInput!](/api-reference/inputs.md#inventorycreateinput) | The input fields for creating the inventory. |

**Returns:** [InventoryPayload](/api-reference/objects.md#inventorypayload)

### inventoryUpdate

Updates an existing inventory.

```graphql
inventoryUpdate(input: InventoryUpdateInput!): InventoryPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [InventoryUpdateInput!](/api-reference/inputs.md#inventoryupdateinput) | The input fields for updating the inventory. |

**Returns:** [InventoryPayload](/api-reference/objects.md#inventorypayload)

### inventoryDelete

Deletes an inventory.

```graphql
inventoryDelete(input: InventoryDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [InventoryDeleteInput!](/api-reference/inputs.md#inventorydeleteinput) | The input fields for deleting the inventory. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [OrganizationCreateInput!](/api-reference/inputs.md#organizationcreateinput) | The input fields for creating the organization. |

**Returns:** [OrganizationPayload](/api-reference/objects.md#organizationpayload)

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
| `input` | [OrganizationUpdateInput!](/api-reference/inputs.md#organizationupdateinput) | The input fields for updating the organization. |

**Returns:** [OrganizationPayload](/api-reference/objects.md#organizationpayload)

### organizationDelete

Deletes an organization and all its data.

```graphql
organizationDelete(input: OrganizationDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [OrganizationDeleteInput!](/api-reference/inputs.md#organizationdeleteinput) | The input fields for deleting the organization. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## User profile

### myProfileUpdate

Updates the current user's profile (name only).

```graphql
myProfileUpdate(input: MyProfileUpdateInput!): UserPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MyProfileUpdateInput!](/api-reference/inputs.md#myprofileupdateinput) | The input fields for updating the profile. |

**Returns:** [UserPayload](/api-reference/objects.md#userpayload)

## Members

### memberCreate

Adds a user to an organization as a member.

```graphql
memberCreate(input: MemberCreateInput!): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MemberCreateInput!](/api-reference/inputs.md#membercreateinput) | The input fields for creating the membership. |

**Returns:** [MemberPayload](/api-reference/objects.md#memberpayload)

### memberUpdate

Updates a membership.

```graphql
memberUpdate(input: MemberUpdateInput!): MemberPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MemberUpdateInput!](/api-reference/inputs.md#memberupdateinput) | The input fields for updating the membership. |

**Returns:** [MemberPayload](/api-reference/objects.md#memberpayload)

### memberRemove

Removes a user from an organization.

```graphql
memberRemove(input: MemberRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [MemberRemoveInput!](/api-reference/inputs.md#memberremoveinput) | The input fields for removing the membership. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Integrations

### integrationCreate

Creates a new integration.

```graphql
integrationCreate(input: IntegrationCreateInput!): IntegrationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [IntegrationCreateInput!](/api-reference/inputs.md#integrationcreateinput) | The input fields for creating the integration. |

**Returns:** [IntegrationPayload](/api-reference/objects.md#integrationpayload)

### integrationUpdate

Updates an existing integration.

```graphql
integrationUpdate(input: IntegrationUpdateInput!): IntegrationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [IntegrationUpdateInput!](/api-reference/inputs.md#integrationupdateinput) | The input fields for updating the integration. |

**Returns:** [IntegrationPayload](/api-reference/objects.md#integrationpayload)

### integrationDelete

Deletes an integration.

```graphql
integrationDelete(input: IntegrationDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [IntegrationDeleteInput!](/api-reference/inputs.md#integrationdeleteinput) | The input fields for deleting the integration. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

## Access control

### roleAssign

Assigns a role to an actor.

```graphql
roleAssign(input: RoleAssignInput!): ActorRolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleAssignInput!](/api-reference/inputs.md#roleassigninput) | The input fields for assigning the role. |

**Returns:** [ActorRolePayload](/api-reference/objects.md#actorrolepayload)

### roleRevoke

Revokes a role from an actor.

```graphql
roleRevoke(input: RoleRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleRevokeInput!](/api-reference/inputs.md#rolerevokeinput) | The input fields for revoking the role. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

### permissionGrant

Grants a permission to a role.

```graphql
permissionGrant(input: PermissionGrantInput!): RolePermissionPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [PermissionGrantInput!](/api-reference/inputs.md#permissiongrantinput) | The input fields for granting the permission. |

**Returns:** [RolePermissionPayload](/api-reference/objects.md#rolepermissionpayload)

### permissionRevoke

Revokes a permission from a role.

```graphql
permissionRevoke(input: PermissionRevokeInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [PermissionRevokeInput!](/api-reference/inputs.md#permissionrevokeinput) | The input fields for revoking the permission. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

### userScopeSet

Sets a user scope restriction.

```graphql
userScopeSet(input: UserScopeSetInput!): UserScopePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserScopeSetInput!](/api-reference/inputs.md#userscopesetinput) | The input fields for setting the user scope. |

**Returns:** [UserScopePayload](/api-reference/objects.md#userscopepayload)

### userScopeRemove

Removes a user scope restriction.

```graphql
userScopeRemove(input: UserScopeRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [UserScopeRemoveInput!](/api-reference/inputs.md#userscoperemoveinput) | The input fields for removing the user scope. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

### roleCreate

Creates a new role.

```graphql
roleCreate(input: RoleCreateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleCreateInput!](/api-reference/inputs.md#rolecreateinput) | The input fields for creating the role. |

**Returns:** [RolePayload](/api-reference/objects.md#rolepayload)

### roleUpdate

Updates a role.

```graphql
roleUpdate(input: RoleUpdateInput!): RolePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [RoleUpdateInput!](/api-reference/inputs.md#roleupdateinput) | The input fields for updating the role. |

**Returns:** [RolePayload](/api-reference/objects.md#rolepayload)

### roleDelete

Deletes a role.

```graphql
roleDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the role. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [DeviceInventoryLinkInput!](/api-reference/inputs.md#deviceinventorylinkinput) | The input fields for linking the device. |

**Returns:** [DeviceInventoryRelationPayload](/api-reference/objects.md#deviceinventoryrelationpayload)

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
| `input` | [DeviceInventoryUnlinkInput!](/api-reference/inputs.md#deviceinventoryunlinkinput) | The input fields for unlinking the device. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [DeviceRelationCreateInput!](/api-reference/inputs.md#devicerelationcreateinput) | The input fields for creating the relationship. |

**Returns:** [DeviceRelationPayload](/api-reference/objects.md#devicerelationpayload)

### deviceRelationRemove

Removes a device relationship.

```graphql
deviceRelationRemove(input: DeviceRelationRemoveInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [DeviceRelationRemoveInput!](/api-reference/inputs.md#devicerelationremoveinput) | The input fields for removing the relationship. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [CustomFieldDefinitionCreateInput!](/api-reference/inputs.md#customfielddefinitioncreateinput) | The input fields for creating the definition. |

**Returns:** [CustomFieldDefinitionPayload](/api-reference/objects.md#customfielddefinitionpayload)

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
| `input` | [CustomFieldDefinitionUpdateInput!](/api-reference/inputs.md#customfielddefinitionupdateinput) | The input fields for updating the definition. |

**Returns:** [CustomFieldDefinitionPayload](/api-reference/objects.md#customfielddefinitionpayload)

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
| `input` | [CustomFieldDefinitionDeleteInput!](/api-reference/inputs.md#customfielddefinitiondeleteinput) | The input fields for deleting the definition. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [ScheduleTypeCreateInput!](/api-reference/inputs.md#scheduletypecreateinput) | The input fields for creating the schedule type. |

**Returns:** [ScheduleTypePayload](/api-reference/objects.md#scheduletypepayload)

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
| `input` | [ScheduleTypeUpdateInput!](/api-reference/inputs.md#scheduletypeupdateinput) | The input fields for updating the schedule type. |

**Returns:** [ScheduleTypePayload](/api-reference/objects.md#scheduletypepayload)

### scheduleTypeDelete

Deletes a schedule type.

```graphql
scheduleTypeDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the schedule type. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

### tagCreate

Creates a new tag.

```graphql
tagCreate(input: TagCreateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [TagCreateInput!](/api-reference/inputs.md#tagcreateinput) | The input fields for creating the tag. |

**Returns:** [TagPayload](/api-reference/objects.md#tagpayload)

### tagUpdate

Updates a tag.

```graphql
tagUpdate(input: TagUpdateInput!): TagPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [TagUpdateInput!](/api-reference/inputs.md#tagupdateinput) | The input fields for updating the tag. |

**Returns:** [TagPayload](/api-reference/objects.md#tagpayload)

### tagDelete

Deletes a tag.

```graphql
tagDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the tag. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)

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
| `input` | [UserCatalogItemCreateInput!](/api-reference/inputs.md#usercatalogitemcreateinput) | The input fields for creating the item. |

**Returns:** [UserCatalogItemPayload](/api-reference/objects.md#usercatalogitempayload)

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
| `input` | [UserCatalogItemUpdateInput!](/api-reference/inputs.md#usercatalogitemupdateinput) | The input fields for updating the item. |

**Returns:** [UserCatalogItemPayload](/api-reference/objects.md#usercatalogitempayload)

### userCatalogItemDelete

Deletes a user catalog item.

```graphql
userCatalogItemDelete(input: CatalogItemDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [CatalogItemDeleteInput!](/api-reference/inputs.md#catalogitemdeleteinput) | The input fields for deleting the item. |

**Returns:** [DeletePayload](/api-reference/objects.md#deletepayload)
