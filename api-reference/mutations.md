# Mutations

Mutations modify data in the Navixy platform. Most mutations require authentication and appropriate permissions.

### Optimistic locking

{% hint style="info" %}
Update and delete mutations require an `If-Match` header with the entity's current ETag. See [Optimistic Locking](mutations.md#optimistic-locking) for details.
{% endhint %}

### Devices

#### createDevice

Create a new device. Returns ETag in the response header.

```graphql
createDevice(input: CreateDeviceInput!): Device!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `CreateDeviceInput!` | See fields below |

**CreateDeviceInput fields**

| Field            | Type                       | Description                           |
| ---------------- | -------------------------- | ------------------------------------- |
| `organizationId` | UUID!                      | Organization that will own the device |
| `typeId`         | UUID!                      | Device type classification            |
| `modelId`        | UUID                       | Device model (optional)               |
| `statusId`       | UUID!                      | Initial device status                 |
| `title`          | String!                    | Device display name                   |
| `identifiers`    | `[DeviceIdentifierInput!]` | Hardware identifiers                  |
| `customFields`   | JSON                       | Custom field values                   |

**Returns:** Device!

#### updateDevice

Update the device. Requires `If-Match` header with the current ETag.

```graphql
updateDevice(input: UpdateDeviceInput!): Device!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `UpdateDeviceInput!` | See fields below |

**UpdateDeviceInput fields**

| Field          | Type   | Description                 |
| -------------- | ------ | --------------------------- |
| `id`           | UUID!  | Device ID to update         |
| `modelId`      | UUID   | New device model            |
| `statusId`     | UUID   | New device status           |
| `title`        | String | New display name            |
| `customFields` | JSON   | Updated custom field values |

**Returns:** Device!

#### deleteDevice

Soft-delete device. Requires `If-Match` header.

```graphql
deleteDevice(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

#### restoreDevice

Restore a soft-deleted device. Requires `If-Match` header.

```graphql
restoreDevice(id: UUID!): Device!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Device!

#### bulkDeleteDevices

Bulk soft-delete devices.

{% hint style="danger" %}
This operation does NOT use ETag (last write wins).
{% endhint %}

```graphql
bulkDeleteDevices(
  input: BulkDeleteInput!
): BulkDeleteResult!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type      | Description               |
| ----- | --------- | ------------------------- |
| `ids` | \[UUID!]! | IDs of entities to delete |

**Returns:** BulkDeleteResult!

#### addDeviceIdentifier

Add an identifier to a device.

```graphql
addDeviceIdentifier(
  deviceId: UUID!,
  input: DeviceIdentifierInput!
): DeviceIdentifier!
```

**Arguments**

| Name       | Type                     | Description      |
| ---------- | ------------------------ | ---------------- |
| `deviceId` | UUID!                    |                  |
| `input`    | `DeviceIdentifierInput!` | See fields below |

**DeviceIdentifierInput fields**

| Field       | Type          | Description                       |
| ----------- | ------------- | --------------------------------- |
| `type`      | DeviceIdType! | Type of identifier                |
| `value`     | String!       | Identifier value                  |
| `namespace` | String        | Optional namespace for uniqueness |

**Returns:** DeviceIdentifier!

#### removeDeviceIdentifier

Remove an identifier from a device.

```graphql
removeDeviceIdentifier(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Assets

#### createAsset

Create a new asset. Returns ETag in the response header.

```graphql
createAsset(input: CreateAssetInput!): Asset!
```

**Arguments**

| Name    | Type                | Description      |
| ------- | ------------------- | ---------------- |
| `input` | `CreateAssetInput!` | See fields below |

**CreateAssetInput fields**

| Field            | Type    | Description                          |
| ---------------- | ------- | ------------------------------------ |
| `organizationId` | UUID!   | Organization that will own the asset |
| `typeId`         | UUID!   | Asset type classification            |
| `title`          | String! | Asset display name                   |
| `customFields`   | JSON    | Custom field values                  |

**Returns:** Asset!

#### updateAsset

Update an asset. Requires `If-Match` header with the current ETag.

```graphql
updateAsset(input: UpdateAssetInput!): Asset!
```

**Arguments**

| Name    | Type                | Description      |
| ------- | ------------------- | ---------------- |
| `input` | `UpdateAssetInput!` | See fields below |

**UpdateAssetInput fields**

| Field          | Type   | Description                 |
| -------------- | ------ | --------------------------- |
| `id`           | UUID!  | Asset ID to update          |
| `title`        | String | New display name            |
| `customFields` | JSON   | Updated custom field values |

**Returns:** Asset!

#### deleteAsset

Soft-delete asset. Requires If-Match header.

```graphql
deleteAsset(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

#### restoreAsset

Restore soft-deleted asset. Requires If-Match header.

```graphql
restoreAsset(id: UUID!): Asset!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Asset!

#### bulkDeleteAssets

Bulk soft-delete assets. Does NOT use ETag (last write wins).

```graphql
bulkDeleteAssets(input: BulkDeleteInput!): BulkDeleteResult!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type      | Description               |
| ----- | --------- | ------------------------- |
| `ids` | \[UUID!]! | IDs of entities to delete |

**Returns:** BulkDeleteResult!

### Asset groups

#### createAssetGroup

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

| Name             | Type    | Description |
| ---------------- | ------- | ----------- |
| `organizationId` | UUID!   |             |
| `typeId`         | UUID!   |             |
| `title`          | String! |             |
| `color`          | String  |             |

**Returns:** AssetGroup!

#### updateAssetGroup

Update asset group title or color

```graphql
updateAssetGroup(
  id: UUID!,
  title: String,
  color: String
): AssetGroup!
```

**Arguments**

| Name    | Type   | Description |
| ------- | ------ | ----------- |
| `id`    | UUID!  |             |
| `title` | String |             |
| `color` | String |             |

**Returns:** AssetGroup!

#### deleteAssetGroup

Delete asset group. Removes all memberships.

```graphql
deleteAssetGroup(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

#### addAssetToGroup

Add asset to group. Validates type constraints.

```graphql
addAssetToGroup(
  input: AddAssetToGroupInput!
): AssetGroupItem!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `AddAssetToGroupInput!` | See fields below |

**AddAssetToGroupInput fields**

| Field     | Type  | Description  |
| --------- | ----- | ------------ |
| `groupId` | UUID! | Target group |
| `assetId` | UUID! | Asset to add |

**Returns:** AssetGroupItem!

#### removeAssetFromGroup

Remove asset from group

```graphql
removeAssetFromGroup(
  groupId: UUID!,
  assetId: UUID!
): Boolean!
```

**Arguments**

| Name      | Type  | Description |
| --------- | ----- | ----------- |
| `groupId` | UUID! |             |
| `assetId` | UUID! |             |

**Returns:** Boolean!

### Geo objects

#### createGeoObject

Create new geo object. Requires 'geojson' in customFields.

```graphql
createGeoObject(input: CreateGeoObjectInput!): GeoObject!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `CreateGeoObjectInput!` | See fields below |

**CreateGeoObjectInput fields**

| Field            | Type    | Description                                        |
| ---------------- | ------- | -------------------------------------------------- |
| `organizationId` | UUID!   | Organization that will own the geo object          |
| `typeId`         | UUID!   | Geo object type classification                     |
| `title`          | String! | Geo object display name                            |
| `customFields`   | JSON!   | Must include 'geojson' field with GeoJSON geometry |

**Returns:** GeoObject!

#### updateGeoObject

Update geo object. Requires If-Match header with current ETag.

```graphql
updateGeoObject(input: UpdateGeoObjectInput!): GeoObject!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `UpdateGeoObjectInput!` | See fields below |

**UpdateGeoObjectInput fields**

| Field          | Type   | Description                 |
| -------------- | ------ | --------------------------- |
| `id`           | UUID!  | Geo object ID to update     |
| `title`        | String | New display name            |
| `customFields` | JSON   | Updated custom field values |

**Returns:** GeoObject!

#### deleteGeoObject

Soft-delete geo object. Requires If-Match header.

```graphql
deleteGeoObject(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

#### restoreGeoObject

Restore soft-deleted geo object. Requires If-Match header.

```graphql
restoreGeoObject(id: UUID!): GeoObject!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** GeoObject!

#### bulkDeleteGeoObjects

Bulk soft-delete geo objects. Does NOT use ETag (last write wins).

```graphql
bulkDeleteGeoObjects(
  input: BulkDeleteInput!
): BulkDeleteResult!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type      | Description               |
| ----- | --------- | ------------------------- |
| `ids` | \[UUID!]! | IDs of entities to delete |

**Returns:** BulkDeleteResult!

### Schedules

#### createSchedule

Create new schedule

```graphql
createSchedule(input: CreateScheduleInput!): Schedule!
```

**Arguments**

| Name    | Type                   | Description      |
| ------- | ---------------------- | ---------------- |
| `input` | `CreateScheduleInput!` | See fields below |

**CreateScheduleInput fields**

| Field            | Type    | Description                                  |
| ---------------- | ------- | -------------------------------------------- |
| `organizationId` | UUID!   | Organization that will own the schedule      |
| `typeId`         | UUID!   | Schedule type classification                 |
| `title`          | String! | Schedule display name                        |
| `customFields`   | JSON    | Custom field values including schedule\_data |

**Returns:** Schedule!

#### updateSchedule

Update schedule. Requires If-Match header with current ETag.

```graphql
updateSchedule(input: UpdateScheduleInput!): Schedule!
```

**Arguments**

| Name    | Type                   | Description      |
| ------- | ---------------------- | ---------------- |
| `input` | `UpdateScheduleInput!` | See fields below |

**UpdateScheduleInput fields**

| Field          | Type   | Description                 |
| -------------- | ------ | --------------------------- |
| `id`           | UUID!  | Schedule ID to update       |
| `title`        | String | New display name            |
| `customFields` | JSON   | Updated custom field values |

**Returns:** Schedule!

#### deleteSchedule

Soft-delete schedule. Requires If-Match header.

```graphql
deleteSchedule(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

#### restoreSchedule

Restore soft-deleted schedule. Requires If-Match header.

```graphql
restoreSchedule(id: UUID!): Schedule!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Schedule!

### Organizations

#### createOrganization

Create new organization. Parent must be a dealer to have children.

```graphql
createOrganization(
  input: CreateOrganizationInput!
): Organization!
```

**Arguments**

| Name    | Type                       | Description      |
| ------- | -------------------------- | ---------------- |
| `input` | `CreateOrganizationInput!` | See fields below |

**CreateOrganizationInput fields**

| Field        | Type    | Description                                       |
| ------------ | ------- | ------------------------------------------------- |
| `parentId`   | UUID    | Parent organization (null for root)               |
| `code`       | String! | Unique organization code                          |
| `title`      | String! | Organization display name                         |
| `externalId` | String  | External system identifier                        |
| `isDealer`   | Boolean | Whether organization can create sub-organizations |

**Returns:** Organization!

#### updateOrganization

Update organization. Requires If-Match header with current ETag.

```graphql
updateOrganization(
  input: UpdateOrganizationInput!
): Organization!
```

**Arguments**

| Name    | Type                       | Description      |
| ------- | -------------------------- | ---------------- |
| `input` | `UpdateOrganizationInput!` | See fields below |

**UpdateOrganizationInput fields**

| Field        | Type    | Description               |
| ------------ | ------- | ------------------------- |
| `id`         | UUID!   | Organization ID to update |
| `title`      | String  | New display name          |
| `externalId` | String  | New external identifier   |
| `isActive`   | Boolean | New active status         |
| `isDealer`   | Boolean | New dealer capability     |

**Returns:** Organization!

#### deleteOrganization

Soft-delete organization and all its data. Requires If-Match header.

```graphql
deleteOrganization(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Users

#### createUser

Create new user from identity provider data

```graphql
createUser(input: CreateUserInput!): User!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `CreateUserInput!` | See fields below |

**CreateUserInput fields**

| Field                | Type    | Description                                    |
| -------------------- | ------- | ---------------------------------------------- |
| `identityProvider`   | String! | Identity provider name (keycloak, auth0, etc.) |
| `identityProviderId` | UUID!   | User ID in the identity provider               |
| `fullName`           | String! | User display name                              |
| `externalId`         | String  | External system identifier                     |

**Returns:** User!

#### updateUser

Update user. Requires If-Match header with current ETag.

```graphql
updateUser(input: UpdateUserInput!): User!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `UpdateUserInput!` | See fields below |

**UpdateUserInput fields**

| Field        | Type    | Description             |
| ------------ | ------- | ----------------------- |
| `id`         | UUID!   | User ID to update       |
| `fullName`   | String  | New display name        |
| `externalId` | String  | New external identifier |
| `isActive`   | Boolean | New active status       |

**Returns:** User!

#### deleteUser

Soft-delete user. Removes all memberships. Requires If-Match header.

```graphql
deleteUser(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Members

#### createMember

Add user to organization as member

```graphql
createMember(input: CreateMemberInput!): Member!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `CreateMemberInput!` | See fields below |

**CreateMemberInput fields**

| Field            | Type  | Description                       |
| ---------------- | ----- | --------------------------------- |
| `userId`         | UUID! | User to add to organization       |
| `organizationId` | UUID! | Organization to join              |
| `customFields`   | JSON  | Membership-specific custom fields |

**Returns:** Member!

#### updateMember

Update membership custom fields or status

```graphql
updateMember(input: UpdateMemberInput!): Member!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `UpdateMemberInput!` | See fields below |

**UpdateMemberInput fields**

| Field          | Type    | Description                 |
| -------------- | ------- | --------------------------- |
| `id`           | UUID!   | Membership ID to update     |
| `isActive`     | Boolean | New active status           |
| `customFields` | JSON    | Updated custom field values |

**Returns:** Member!

#### removeMember

Remove user from organization

```graphql
removeMember(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Integrations

#### createIntegration

Create new integration

```graphql
createIntegration(
  input: CreateIntegrationInput!
): Integration!
```

**Arguments**

| Name    | Type                      | Description      |
| ------- | ------------------------- | ---------------- |
| `input` | `CreateIntegrationInput!` | See fields below |

**CreateIntegrationInput fields**

| Field           | Type    | Description                              |
| --------------- | ------- | ---------------------------------------- |
| `name`          | String! | Integration display name                 |
| `credentialRef` | String  | Reference to credentials in secure vault |

**Returns:** Integration!

#### updateIntegration

Update integration. Requires If-Match header with current ETag.

```graphql
updateIntegration(
  input: UpdateIntegrationInput!
): Integration!
```

**Arguments**

| Name    | Type                      | Description      |
| ------- | ------------------------- | ---------------- |
| `input` | `UpdateIntegrationInput!` | See fields below |

**UpdateIntegrationInput fields**

| Field           | Type    | Description              |
| --------------- | ------- | ------------------------ |
| `id`            | UUID!   | Integration ID to update |
| `name`          | String  | New display name         |
| `credentialRef` | String  | New credential reference |
| `isActive`      | Boolean | New active status        |

**Returns:** Integration!

#### deleteIntegration

Soft-delete integration. Revokes all permissions. Requires If-Match header.

```graphql
deleteIntegration(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Access control

#### assignRole

Assign role to actor (user or integration)

```graphql
assignRole(input: AssignRoleInput!): ActorRole!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `AssignRoleInput!` | See fields below |

**AssignRoleInput fields**

| Field        | Type     | Description                                       |
| ------------ | -------- | ------------------------------------------------- |
| `actorId`    | UUID!    | Actor (user or integration) to assign role to     |
| `roleId`     | UUID!    | Role to assign                                    |
| `expireDate` | DateTime | Optional expiration date for temporary assignment |

**Returns:** ActorRole!

#### revokeRole

Revoke role from actor

```graphql
revokeRole(actorRoleId: UUID!): Boolean!
```

**Arguments**

| Name          | Type  | Description |
| ------------- | ----- | ----------- |
| `actorRoleId` | UUID! |             |

**Returns:** Boolean!

#### grantPermission

Grant permission to role

```graphql
grantPermission(
  input: GrantPermissionInput!
): RolePermission!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `GrantPermissionInput!` | See fields below |

**GrantPermissionInput fields**

| Field               | Type                  | Description                                       |
| ------------------- | --------------------- | ------------------------------------------------- |
| `roleId`            | UUID!                 | Role to grant permission to                       |
| `permissionScopeId` | UUID!                 | Permission scope to grant                         |
| `targetEntityId`    | UUID                  | Null = permission applies to all entities of type |
| `actions`           | \[ActionPermission!]! | Actions to allow                                  |

**Returns:** RolePermission!

#### revokePermission

Revoke permission from role

```graphql
revokePermission(permissionId: UUID!): Boolean!
```

**Arguments**

| Name           | Type  | Description |
| -------------- | ----- | ----------- |
| `permissionId` | UUID! |             |

**Returns:** Boolean!

#### setUserScope

Set user scope restriction (whitelist filter)

```graphql
setUserScope(input: SetUserScopeInput!): UserScope!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `SetUserScopeInput!` | See fields below |

**SetUserScopeInput fields**

| Field               | Type                  | Description                        |
| ------------------- | --------------------- | ---------------------------------- |
| `actorId`           | UUID!                 | Actor to restrict                  |
| `permissionScopeId` | UUID!                 | Permission scope to filter         |
| `targetEntityId`    | UUID!                 | Specific entity to allow access to |
| `actions`           | \[ActionPermission!]! | Actions allowed on this entity     |

**Returns:** UserScope!

#### removeUserScope

Remove user scope restriction

```graphql
removeUserScope(userScopeId: UUID!): Boolean!
```

**Arguments**

| Name          | Type  | Description |
| ------------- | ----- | ----------- |
| `userScopeId` | UUID! |             |

**Returns:** Boolean!

### Device relations

#### linkDeviceInventory

Link device to inventory

```graphql
linkDeviceInventory(
  input: LinkDeviceInventoryInput!
): DeviceInventoryRelation!
```

**Arguments**

| Name    | Type                        | Description      |
| ------- | --------------------------- | ---------------- |
| `input` | `LinkDeviceInventoryInput!` | See fields below |

**LinkDeviceInventoryInput fields**

| Field         | Type  | Description      |
| ------------- | ----- | ---------------- |
| `deviceId`    | UUID! | Device to assign |
| `inventoryId` | UUID! | Target inventory |

**Returns:** DeviceInventoryRelation!

#### unlinkDeviceInventory

Unlink device from current inventory

```graphql
unlinkDeviceInventory(deviceId: UUID!): Boolean!
```

**Arguments**

| Name       | Type  | Description |
| ---------- | ----- | ----------- |
| `deviceId` | UUID! |             |

**Returns:** Boolean!

#### createDeviceRelation

Create relationship between two devices

```graphql
createDeviceRelation(
  input: CreateDeviceRelationInput!
): DeviceRelation!
```

**Arguments**

| Name    | Type                         | Description      |
| ------- | ---------------------------- | ---------------- |
| `input` | `CreateDeviceRelationInput!` | See fields below |

**CreateDeviceRelationInput fields**

| Field            | Type  | Description                   |
| ---------------- | ----- | ----------------------------- |
| `firstDeviceId`  | UUID! | First device in relationship  |
| `secondDeviceId` | UUID! | Second device in relationship |
| `typeId`         | UUID! | Relationship type             |

**Returns:** DeviceRelation!

#### deleteDeviceRelation

Delete device relationship

```graphql
deleteDeviceRelation(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Custom fields

#### createCustomFieldDefinition

Create custom field definition

```graphql
createCustomFieldDefinition(
  input: CreateCustomFieldDefinitionInput!
): CustomFieldDefinition!
```

**Arguments**

| Name    | Type                                | Description      |
| ------- | ----------------------------------- | ---------------- |
| `input` | `CreateCustomFieldDefinitionInput!` | See fields below |

**CreateCustomFieldDefinitionInput fields**

| Field                | Type                | Description                                      |
| -------------------- | ------------------- | ------------------------------------------------ |
| `organizationId`     | UUID!               | Organization that will own this definition       |
| `ownerCatalogItemId` | UUID!               | Owner catalog item (EntityType or specific type) |
| `targetEntityTypeId` | UUID!               | Target entity type this field applies to         |
| `code`               | String!             | Machine-readable field code                      |
| `title`              | String!             | Human-readable field title                       |
| `description`        | String              | Optional field description                       |
| `fieldType`          | FieldType!          | Data type for the field                          |
| `isSystem`           | Boolean             | Whether this is a system-managed field           |
| `order`              | Int                 | Display order                                    |
| `extra`              | JSON                | Additional metadata                              |
| `params`             | `FieldParamsInput!` | Type-specific parameters                         |

**Returns:** CustomFieldDefinition!

#### updateCustomFieldDefinition

Update custom field definition. Requires If-Match header.

```graphql
updateCustomFieldDefinition(
  input: UpdateCustomFieldDefinitionInput!
): CustomFieldDefinition!
```

**Arguments**

| Name    | Type                                | Description      |
| ------- | ----------------------------------- | ---------------- |
| `input` | `UpdateCustomFieldDefinitionInput!` | See fields below |

**UpdateCustomFieldDefinitionInput fields**

| Field         | Type               | Description             |
| ------------- | ------------------ | ----------------------- |
| `id`          | UUID!              | Definition ID to update |
| `title`       | String             | New title               |
| `description` | String             | New description         |
| `order`       | Int                | New display order       |
| `extra`       | JSON               | New metadata            |
| `params`      | `FieldParamsInput` | Updated parameters      |

**Returns:** CustomFieldDefinition!

#### deleteCustomFieldDefinition

Soft-delete custom field definition. Preserves existing data.

```graphql
deleteCustomFieldDefinition(id: UUID!): Boolean!
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Boolean!

### Localization

#### setTranslation

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

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| `entityId`  | UUID!   |             |
| `fieldCode` | String! |             |
| `locale`    | String! |             |
| `textValue` | String! |             |

**Returns:** I18nText!

#### deleteTranslation

Delete translation for entity field

```graphql
deleteTranslation(
  entityId: UUID!,
  fieldCode: String!,
  locale: String!
): Boolean!
```

**Arguments**

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| `entityId`  | UUID!   |             |
| `fieldCode` | String! |             |
| `locale`    | String! |             |

**Returns:** Boolean!
