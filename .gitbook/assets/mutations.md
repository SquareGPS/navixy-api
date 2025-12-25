# Mutations

Mutations modify data in the Navixy platform. Most mutations require authentication and appropriate permissions.

## Optimistic locking

Update and delete mutations require an `If-Match` header with the entity's current ETag. See [Optimistic Locking](../optimistic-locking.md) for details.

## Devices

### createDevice

Create new device. Returns ETag in response header.

```graphql
createDevice(input: CreateDeviceInput!): Device!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateDeviceInput!` | See fields below |

**CreateDeviceInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `organizationId` | [UUID!](types.md#uuid) | Organization that will own the device |
| `typeId` | [UUID!](types.md#uuid) | Device type classification |
| `modelId` | [UUID](types.md#uuid) | Device model (optional) |
| `statusId` | [UUID!](types.md#uuid) | Initial device status |
| `title` | [String!](types.md#string) | Device display name |
| `identifiers` | `[DeviceIdentifierInput!]` | Hardware identifiers |
| `customFields` | [JSON](types.md#json) | Custom field values |

**Returns:** [Device!](objects.md#device)

### updateDevice

Update device. Requires If-Match header with current ETag.

```graphql
updateDevice(input: UpdateDeviceInput!): Device!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateDeviceInput!` | See fields below |

**UpdateDeviceInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Device ID to update |
| `modelId` | [UUID](types.md#uuid) | New device model |
| `statusId` | [UUID](types.md#uuid) | New device status |
| `title` | [String](types.md#string) | New display name |
| `customFields` | [JSON](types.md#json) | Updated custom field values |

**Returns:** [Device!](objects.md#device)

### deleteDevice

Soft-delete device. Requires If-Match header.

```graphql
deleteDevice(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### restoreDevice

Restore soft-deleted device. Requires If-Match header.

```graphql
restoreDevice(id: UUID!): Device!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Device!](objects.md#device)

### bulkDeleteDevices

Bulk soft-delete devices. Does NOT use ETag (last write wins).

```graphql
bulkDeleteDevices(
  input: BulkDeleteInput!
): BulkDeleteResult!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `ids` | [[UUID!]!](types.md#uuid) | IDs of entities to delete |

**Returns:** [BulkDeleteResult!](objects.md#bulkdeleteresult)

### addDeviceIdentifier

Add identifier to device

```graphql
addDeviceIdentifier(
  deviceId: UUID!,
  input: DeviceIdentifierInput!
): DeviceIdentifier!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `deviceId` | [UUID!](types.md#uuid) | |
| `input` | `DeviceIdentifierInput!` | See fields below |

**DeviceIdentifierInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `type` | [DeviceIdType!](types.md#deviceidtype) | Type of identifier |
| `value` | [String!](types.md#string) | Identifier value |
| `namespace` | [String](types.md#string) | Optional namespace for uniqueness |

**Returns:** [DeviceIdentifier!](objects.md#deviceidentifier)

### removeDeviceIdentifier

Remove identifier from device

```graphql
removeDeviceIdentifier(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Assets

### createAsset

Create new asset. Returns ETag in response header.

```graphql
createAsset(input: CreateAssetInput!): Asset!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateAssetInput!` | See fields below |

**CreateAssetInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `organizationId` | [UUID!](types.md#uuid) | Organization that will own the asset |
| `typeId` | [UUID!](types.md#uuid) | Asset type classification |
| `title` | [String!](types.md#string) | Asset display name |
| `customFields` | [JSON](types.md#json) | Custom field values |

**Returns:** [Asset!](objects.md#asset)

### updateAsset

Update asset. Requires If-Match header with current ETag.

```graphql
updateAsset(input: UpdateAssetInput!): Asset!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateAssetInput!` | See fields below |

**UpdateAssetInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Asset ID to update |
| `title` | [String](types.md#string) | New display name |
| `customFields` | [JSON](types.md#json) | Updated custom field values |

**Returns:** [Asset!](objects.md#asset)

### deleteAsset

Soft-delete asset. Requires If-Match header.

```graphql
deleteAsset(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### restoreAsset

Restore soft-deleted asset. Requires If-Match header.

```graphql
restoreAsset(id: UUID!): Asset!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Asset!](objects.md#asset)

### bulkDeleteAssets

Bulk soft-delete assets. Does NOT use ETag (last write wins).

```graphql
bulkDeleteAssets(input: BulkDeleteInput!): BulkDeleteResult!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `ids` | [[UUID!]!](types.md#uuid) | IDs of entities to delete |

**Returns:** [BulkDeleteResult!](objects.md#bulkdeleteresult)

## Asset groups

### createAssetGroup

Create new asset group

```graphql
createAssetGroup(
  organizationId: UUID!,
  typeId: UUID!,
  title: String!,
  color: String
): AssetGroup!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `organizationId` | [UUID!](types.md#uuid) | |
| `typeId` | [UUID!](types.md#uuid) | |
| `title` | [String!](types.md#string) | |
| `color` | [String](types.md#string) | |

**Returns:** [AssetGroup!](objects.md#assetgroup)

### updateAssetGroup

Update asset group title or color

```graphql
updateAssetGroup(
  id: UUID!,
  title: String,
  color: String
): AssetGroup!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |
| `title` | [String](types.md#string) | |
| `color` | [String](types.md#string) | |

**Returns:** [AssetGroup!](objects.md#assetgroup)

### deleteAssetGroup

Delete asset group. Removes all memberships.

```graphql
deleteAssetGroup(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### addAssetToGroup

Add asset to group. Validates type constraints.

```graphql
addAssetToGroup(
  input: AddAssetToGroupInput!
): AssetGroupItem!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `AddAssetToGroupInput!` | See fields below |

**AddAssetToGroupInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `groupId` | [UUID!](types.md#uuid) | Target group |
| `assetId` | [UUID!](types.md#uuid) | Asset to add |

**Returns:** [AssetGroupItem!](objects.md#assetgroupitem)

### removeAssetFromGroup

Remove asset from group

```graphql
removeAssetFromGroup(
  groupId: UUID!,
  assetId: UUID!
): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `groupId` | [UUID!](types.md#uuid) | |
| `assetId` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Geo objects

### createGeoObject

Create new geo object. Requires 'geojson' in customFields.

```graphql
createGeoObject(input: CreateGeoObjectInput!): GeoObject!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateGeoObjectInput!` | See fields below |

**CreateGeoObjectInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `organizationId` | [UUID!](types.md#uuid) | Organization that will own the geo object |
| `typeId` | [UUID!](types.md#uuid) | Geo object type classification |
| `title` | [String!](types.md#string) | Geo object display name |
| `customFields` | [JSON!](types.md#json) | Must include 'geojson' field with GeoJSON geometry |

**Returns:** [GeoObject!](objects.md#geoobject)

### updateGeoObject

Update geo object. Requires If-Match header with current ETag.

```graphql
updateGeoObject(input: UpdateGeoObjectInput!): GeoObject!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateGeoObjectInput!` | See fields below |

**UpdateGeoObjectInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Geo object ID to update |
| `title` | [String](types.md#string) | New display name |
| `customFields` | [JSON](types.md#json) | Updated custom field values |

**Returns:** [GeoObject!](objects.md#geoobject)

### deleteGeoObject

Soft-delete geo object. Requires If-Match header.

```graphql
deleteGeoObject(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### restoreGeoObject

Restore soft-deleted geo object. Requires If-Match header.

```graphql
restoreGeoObject(id: UUID!): GeoObject!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [GeoObject!](objects.md#geoobject)

### bulkDeleteGeoObjects

Bulk soft-delete geo objects. Does NOT use ETag (last write wins).

```graphql
bulkDeleteGeoObjects(
  input: BulkDeleteInput!
): BulkDeleteResult!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `ids` | [[UUID!]!](types.md#uuid) | IDs of entities to delete |

**Returns:** [BulkDeleteResult!](objects.md#bulkdeleteresult)

## Schedules

### createSchedule

Create new schedule

```graphql
createSchedule(input: CreateScheduleInput!): Schedule!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateScheduleInput!` | See fields below |

**CreateScheduleInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `organizationId` | [UUID!](types.md#uuid) | Organization that will own the schedule |
| `typeId` | [UUID!](types.md#uuid) | Schedule type classification |
| `title` | [String!](types.md#string) | Schedule display name |
| `customFields` | [JSON](types.md#json) | Custom field values including schedule_data |

**Returns:** [Schedule!](objects.md#schedule)

### updateSchedule

Update schedule. Requires If-Match header with current ETag.

```graphql
updateSchedule(input: UpdateScheduleInput!): Schedule!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateScheduleInput!` | See fields below |

**UpdateScheduleInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Schedule ID to update |
| `title` | [String](types.md#string) | New display name |
| `customFields` | [JSON](types.md#json) | Updated custom field values |

**Returns:** [Schedule!](objects.md#schedule)

### deleteSchedule

Soft-delete schedule. Requires If-Match header.

```graphql
deleteSchedule(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### restoreSchedule

Restore soft-deleted schedule. Requires If-Match header.

```graphql
restoreSchedule(id: UUID!): Schedule!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Schedule!](objects.md#schedule)

## Organizations

### createOrganization

Create new organization. Parent must be a dealer to have children.

```graphql
createOrganization(
  input: CreateOrganizationInput!
): Organization!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateOrganizationInput!` | See fields below |

**CreateOrganizationInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `parentId` | [UUID](types.md#uuid) | Parent organization (null for root) |
| `code` | [String!](types.md#string) | Unique organization code |
| `title` | [String!](types.md#string) | Organization display name |
| `externalId` | [String](types.md#string) | External system identifier |
| `isDealer` | [Boolean](types.md#boolean) | Whether organization can create sub-organizations |

**Returns:** [Organization!](objects.md#organization)

### updateOrganization

Update organization. Requires If-Match header with current ETag.

```graphql
updateOrganization(
  input: UpdateOrganizationInput!
): Organization!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateOrganizationInput!` | See fields below |

**UpdateOrganizationInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Organization ID to update |
| `title` | [String](types.md#string) | New display name |
| `externalId` | [String](types.md#string) | New external identifier |
| `isActive` | [Boolean](types.md#boolean) | New active status |
| `isDealer` | [Boolean](types.md#boolean) | New dealer capability |

**Returns:** [Organization!](objects.md#organization)

### deleteOrganization

Soft-delete organization and all its data. Requires If-Match header.

```graphql
deleteOrganization(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Users

### createUser

Create new user from identity provider data

```graphql
createUser(input: CreateUserInput!): User!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateUserInput!` | See fields below |

**CreateUserInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `identityProvider` | [String!](types.md#string) | Identity provider name (keycloak, auth0, etc.) |
| `identityProviderId` | [UUID!](types.md#uuid) | User ID in the identity provider |
| `fullName` | [String!](types.md#string) | User display name |
| `externalId` | [String](types.md#string) | External system identifier |

**Returns:** [User!](objects.md#user)

### updateUser

Update user. Requires If-Match header with current ETag.

```graphql
updateUser(input: UpdateUserInput!): User!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateUserInput!` | See fields below |

**UpdateUserInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | User ID to update |
| `fullName` | [String](types.md#string) | New display name |
| `externalId` | [String](types.md#string) | New external identifier |
| `isActive` | [Boolean](types.md#boolean) | New active status |

**Returns:** [User!](objects.md#user)

### deleteUser

Soft-delete user. Removes all memberships. Requires If-Match header.

```graphql
deleteUser(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Members

### createMember

Add user to organization as member

```graphql
createMember(input: CreateMemberInput!): Member!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateMemberInput!` | See fields below |

**CreateMemberInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `userId` | [UUID!](types.md#uuid) | User to add to organization |
| `organizationId` | [UUID!](types.md#uuid) | Organization to join |
| `customFields` | [JSON](types.md#json) | Membership-specific custom fields |

**Returns:** [Member!](objects.md#member)

### updateMember

Update membership custom fields or status

```graphql
updateMember(input: UpdateMemberInput!): Member!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateMemberInput!` | See fields below |

**UpdateMemberInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Membership ID to update |
| `isActive` | [Boolean](types.md#boolean) | New active status |
| `customFields` | [JSON](types.md#json) | Updated custom field values |

**Returns:** [Member!](objects.md#member)

### removeMember

Remove user from organization

```graphql
removeMember(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Integrations

### createIntegration

Create new integration

```graphql
createIntegration(
  input: CreateIntegrationInput!
): Integration!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateIntegrationInput!` | See fields below |

**CreateIntegrationInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `name` | [String!](types.md#string) | Integration display name |
| `credentialRef` | [String](types.md#string) | Reference to credentials in secure vault |

**Returns:** [Integration!](objects.md#integration)

### updateIntegration

Update integration. Requires If-Match header with current ETag.

```graphql
updateIntegration(
  input: UpdateIntegrationInput!
): Integration!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateIntegrationInput!` | See fields below |

**UpdateIntegrationInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Integration ID to update |
| `name` | [String](types.md#string) | New display name |
| `credentialRef` | [String](types.md#string) | New credential reference |
| `isActive` | [Boolean](types.md#boolean) | New active status |

**Returns:** [Integration!](objects.md#integration)

### deleteIntegration

Soft-delete integration. Revokes all permissions. Requires If-Match header.

```graphql
deleteIntegration(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Access control

### assignRole

Assign role to actor (user or integration)

```graphql
assignRole(input: AssignRoleInput!): ActorRole!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `AssignRoleInput!` | See fields below |

**AssignRoleInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `actorId` | [UUID!](types.md#uuid) | Actor (user or integration) to assign role to |
| `roleId` | [UUID!](types.md#uuid) | Role to assign |
| `expireDate` | [DateTime](types.md#datetime) | Optional expiration date for temporary assignment |

**Returns:** [ActorRole!](objects.md#actorrole)

### revokeRole

Revoke role from actor

```graphql
revokeRole(actorRoleId: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `actorRoleId` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### grantPermission

Grant permission to role

```graphql
grantPermission(
  input: GrantPermissionInput!
): RolePermission!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `GrantPermissionInput!` | See fields below |

**GrantPermissionInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `roleId` | [UUID!](types.md#uuid) | Role to grant permission to |
| `permissionScopeId` | [UUID!](types.md#uuid) | Permission scope to grant |
| `targetEntityId` | [UUID](types.md#uuid) | Null = permission applies to all entities of type |
| `actions` | [[ActionPermission!]!](types.md#actionpermission) | Actions to allow |

**Returns:** [RolePermission!](objects.md#rolepermission)

### revokePermission

Revoke permission from role

```graphql
revokePermission(permissionId: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `permissionId` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### setUserScope

Set user scope restriction (whitelist filter)

```graphql
setUserScope(input: SetUserScopeInput!): UserScope!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `SetUserScopeInput!` | See fields below |

**SetUserScopeInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `actorId` | [UUID!](types.md#uuid) | Actor to restrict |
| `permissionScopeId` | [UUID!](types.md#uuid) | Permission scope to filter |
| `targetEntityId` | [UUID!](types.md#uuid) | Specific entity to allow access to |
| `actions` | [[ActionPermission!]!](types.md#actionpermission) | Actions allowed on this entity |

**Returns:** [UserScope!](objects.md#userscope)

### removeUserScope

Remove user scope restriction

```graphql
removeUserScope(userScopeId: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `userScopeId` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Device relations

### linkDeviceInventory

Link device to inventory

```graphql
linkDeviceInventory(
  input: LinkDeviceInventoryInput!
): DeviceInventoryRelation!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `LinkDeviceInventoryInput!` | See fields below |

**LinkDeviceInventoryInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `deviceId` | [UUID!](types.md#uuid) | Device to assign |
| `inventoryId` | [UUID!](types.md#uuid) | Target inventory |

**Returns:** [DeviceInventoryRelation!](objects.md#deviceinventoryrelation)

### unlinkDeviceInventory

Unlink device from current inventory

```graphql
unlinkDeviceInventory(deviceId: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `deviceId` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

### createDeviceRelation

Create relationship between two devices

```graphql
createDeviceRelation(
  input: CreateDeviceRelationInput!
): DeviceRelation!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateDeviceRelationInput!` | See fields below |

**CreateDeviceRelationInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `firstDeviceId` | [UUID!](types.md#uuid) | First device in relationship |
| `secondDeviceId` | [UUID!](types.md#uuid) | Second device in relationship |
| `typeId` | [UUID!](types.md#uuid) | Relationship type |

**Returns:** [DeviceRelation!](objects.md#devicerelation)

### deleteDeviceRelation

Delete device relationship

```graphql
deleteDeviceRelation(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Custom fields

### createCustomFieldDefinition

Create custom field definition

```graphql
createCustomFieldDefinition(
  input: CreateCustomFieldDefinitionInput!
): CustomFieldDefinition!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `CreateCustomFieldDefinitionInput!` | See fields below |

**CreateCustomFieldDefinitionInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `organizationId` | [UUID!](types.md#uuid) | Organization that will own this definition |
| `ownerCatalogItemId` | [UUID!](types.md#uuid) | Owner catalog item (EntityType or specific type) |
| `targetEntityTypeId` | [UUID!](types.md#uuid) | Target entity type this field applies to |
| `code` | [String!](types.md#string) | Machine-readable field code |
| `title` | [String!](types.md#string) | Human-readable field title |
| `description` | [String](types.md#string) | Optional field description |
| `fieldType` | [FieldType!](types.md#fieldtype) | Data type for the field |
| `isSystem` | [Boolean](types.md#boolean) | Whether this is a system-managed field |
| `order` | [Int](types.md#int) | Display order |
| `extra` | [JSON](types.md#json) | Additional metadata |
| `params` | `FieldParamsInput!` | Type-specific parameters |

**Returns:** [CustomFieldDefinition!](objects.md#customfielddefinition)

### updateCustomFieldDefinition

Update custom field definition. Requires If-Match header.

```graphql
updateCustomFieldDefinition(
  input: UpdateCustomFieldDefinitionInput!
): CustomFieldDefinition!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `input` | `UpdateCustomFieldDefinitionInput!` | See fields below |

**UpdateCustomFieldDefinitionInput fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | [UUID!](types.md#uuid) | Definition ID to update |
| `title` | [String](types.md#string) | New title |
| `description` | [String](types.md#string) | New description |
| `order` | [Int](types.md#int) | New display order |
| `extra` | [JSON](types.md#json) | New metadata |
| `params` | `FieldParamsInput` | Updated parameters |

**Returns:** [CustomFieldDefinition!](objects.md#customfielddefinition)

### deleteCustomFieldDefinition

Soft-delete custom field definition. Preserves existing data.

```graphql
deleteCustomFieldDefinition(id: UUID!): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `id` | [UUID!](types.md#uuid) | |

**Returns:** [Boolean!](types.md#boolean)

## Localization

### setTranslation

Create or update translation for entity field

```graphql
setTranslation(
  entityId: UUID!,
  fieldCode: String!,
  locale: String!,
  textValue: String!
): I18nText!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `entityId` | [UUID!](types.md#uuid) | |
| `fieldCode` | [String!](types.md#string) | |
| `locale` | [String!](types.md#string) | |
| `textValue` | [String!](types.md#string) | |

**Returns:** [I18nText!](../objects.md#i18ntext)

### deleteTranslation

Delete translation for entity field

```graphql
deleteTranslation(
  entityId: UUID!,
  fieldCode: String!,
  locale: String!
): Boolean!
```

**Arguments**

| Name | Type | Description |
|------|------|-------------|
| `entityId` | [UUID!](types.md#uuid) | |
| `fieldCode` | [String!](types.md#string) | |
| `locale` | [String!](types.md#string) | |

**Returns:** [Boolean!](types.md#boolean)
