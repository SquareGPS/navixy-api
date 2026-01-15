# Mutations

Mutations modify data in the Navixy database. Most mutations require authentication and appropriate permissions.

## Optimistic locking

{% hint style="info" %}
Update and delete mutations require an `If-Match` header with the entity's current ETag. See [Optimistic Locking](../optimistic-locking.md) for details.
{% endhint %}

## Devices

### createDevice

Create new device. Returns ETag in response header.

```graphql
createDevice(input: CreateDeviceInput!): Device!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `CreateDeviceInput!` | See fields below |

**CreateDeviceInput fields**

| Field            | Type                                              | Description                           |
| ---------------- | ------------------------------------------------- | ------------------------------------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Organization that will own the device |
| `typeId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Device type classification            |
| `modelId`        | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)  | Device model (optional)               |
| `statusId`       | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Initial device status                 |
| `title`          | `String!`                                         | Device display name                   |
| `identifiers`    | `[DeviceIdentifierInput!]`                        | Hardware identifiers                  |
| `customFields`   | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Custom field values                   |

**Returns:** [Device!](../api-reference/objects.md#device/)

### updateDevice

Update device. Requires If-Match header with current ETag.

```graphql
updateDevice(input: UpdateDeviceInput!): Device!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `UpdateDeviceInput!` | See fields below |

**UpdateDeviceInput fields**

| Field          | Type                                              | Description                 |
| -------------- | ------------------------------------------------- | --------------------------- |
| `id`           | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Device ID to update         |
| `modelId`      | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)  | New device model            |
| `statusId`     | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)  | New device status           |
| `title`        | `String`                                          | New display name            |
| `customFields` | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Updated custom field values |

**Returns:** [Device!](../api-reference/objects.md#device/)

### deleteDevice

Soft-delete device. Requires If-Match header.

```graphql
deleteDevice(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### restoreDevice

Restore soft-deleted device. Requires If-Match header.

```graphql
restoreDevice(id: UUID!): Device!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Device!](../api-reference/objects.md#device/)

### bulkDeleteDevices

Bulk soft-delete devices. Does NOT use ETag (last write wins).

```graphql
bulkDeleteDevices(input: BulkDeleteInput!): BulkDeleteResult!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type                                                   | Description               |
| ----- | ------------------------------------------------------ | ------------------------- |
| `ids` | [\[UUID!\]!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | IDs of entities to delete |

**Returns:** [BulkDeleteResult!](../api-reference/objects.md#bulkdeleteresult/)

### addDeviceIdentifier

Add identifier to device

```graphql
addDeviceIdentifier(
  deviceId: UUID!
  input: DeviceIdentifierInput!
): DeviceIdentifier!
```

**Arguments**

| Name       | Type                                              | Description      |
| ---------- | ------------------------------------------------- | ---------------- |
| `deviceId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |                  |
| `input`    | `DeviceIdentifierInput!`                          | See fields below |

**DeviceIdentifierInput fields**

| Field       | Type                                                              | Description                       |
| ----------- | ----------------------------------------------------------------- | --------------------------------- |
| `type`      | [DeviceIdType!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#deviceidtype/) | Type of identifier                |
| `value`     | `String!`                                                         | Identifier value                  |
| `namespace` | `String`                                                          | Optional namespace for uniqueness |

**Returns:** [DeviceIdentifier!](../api-reference/objects.md#deviceidentifier/)

### removeDeviceIdentifier

Remove identifier from device

```graphql
removeDeviceIdentifier(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Assets

### createAsset

Create new asset. Returns ETag in response header.

```graphql
createAsset(input: CreateAssetInput!): Asset!
```

**Arguments**

| Name    | Type                | Description      |
| ------- | ------------------- | ---------------- |
| `input` | `CreateAssetInput!` | See fields below |

**CreateAssetInput fields**

| Field            | Type                                              | Description                          |
| ---------------- | ------------------------------------------------- | ------------------------------------ |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Organization that will own the asset |
| `typeId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Asset type classification            |
| `title`          | `String!`                                         | Asset display name                   |
| `customFields`   | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Custom field values                  |

**Returns:** [Asset!](../api-reference/objects.md#asset/)

### updateAsset

Update asset. Requires If-Match header with current ETag.

```graphql
updateAsset(input: UpdateAssetInput!): Asset!
```

**Arguments**

| Name    | Type                | Description      |
| ------- | ------------------- | ---------------- |
| `input` | `UpdateAssetInput!` | See fields below |

**UpdateAssetInput fields**

| Field          | Type                                              | Description                 |
| -------------- | ------------------------------------------------- | --------------------------- |
| `id`           | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Asset ID to update          |
| `title`        | `String`                                          | New display name            |
| `customFields` | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Updated custom field values |

**Returns:** [Asset!](../api-reference/objects.md#asset/)

### deleteAsset

Soft-delete asset. Requires If-Match header.

```graphql
deleteAsset(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### restoreAsset

Restore soft-deleted asset. Requires If-Match header.

```graphql
restoreAsset(id: UUID!): Asset!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Asset!](../api-reference/objects.md#asset/)

### bulkDeleteAssets

Bulk soft-delete assets. Does NOT use ETag (last write wins).

```graphql
bulkDeleteAssets(input: BulkDeleteInput!): BulkDeleteResult!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type                                                   | Description               |
| ----- | ------------------------------------------------------ | ------------------------- |
| `ids` | [\[UUID!\]!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | IDs of entities to delete |

**Returns:** [BulkDeleteResult!](../api-reference/objects.md#bulkdeleteresult/)

## Asset groups

### createAssetGroup

Create new asset group

```graphql
createAssetGroup(
  organizationId: UUID!
  typeId: UUID!
  title: String!
  color: String
): AssetGroup!
```

**Arguments**

| Name             | Type                                              | Description |
| ---------------- | ------------------------------------------------- | ----------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `typeId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `title`          | `String!`                                         |             |
| `color`          | `String`                                          |             |

**Returns:** [AssetGroup!](../api-reference/objects.md#assetgroup/)

### updateAssetGroup

Update asset group title or color

```graphql
updateAssetGroup(
  id: UUID!
  title: String
  color: String
): AssetGroup!
```

**Arguments**

| Name    | Type                                              | Description |
| ------- | ------------------------------------------------- | ----------- |
| `id`    | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `title` | `String`                                          |             |
| `color` | `String`                                          |             |

**Returns:** [AssetGroup!](../api-reference/objects.md#assetgroup/)

### deleteAssetGroup

Delete asset group. Removes all memberships.

```graphql
deleteAssetGroup(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### addAssetToGroup

Add asset to group. Validates type constraints.

```graphql
addAssetToGroup(input: AddAssetToGroupInput!): AssetGroupItem!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `AddAssetToGroupInput!` | See fields below |

**AddAssetToGroupInput fields**

| Field     | Type                                              | Description  |
| --------- | ------------------------------------------------- | ------------ |
| `groupId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Target group |
| `assetId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Asset to add |

**Returns:** [AssetGroupItem!](../api-reference/objects.md#assetgroupitem/)

### removeAssetFromGroup

Remove asset from group

```graphql
removeAssetFromGroup(
  groupId: UUID!
  assetId: UUID!
): Boolean!
```

**Arguments**

| Name      | Type                                              | Description |
| --------- | ------------------------------------------------- | ----------- |
| `groupId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `assetId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Geo objects

### createGeoObject

Create new geo object. Requires 'geojson' in customFields.

```graphql
createGeoObject(input: CreateGeoObjectInput!): GeoObject!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `CreateGeoObjectInput!` | See fields below |

**CreateGeoObjectInput fields**

| Field            | Type                                              | Description                                                                |
| ---------------- | ------------------------------------------------- | -------------------------------------------------------------------------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Organization that will own the geo object                                  |
| `typeId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Geo object type classification                                             |
| `title`          | `String!`                                         | Geo object display name                                                    |
| `customFields`   | [JSON!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/) | Must include 'geojson' field with [GeoJSON](https://geojson.org/) geometry |

**Returns:** [GeoObject!](../api-reference/objects.md#geoobject/)

### updateGeoObject

Update geo object. Requires If-Match header with current ETag.

```graphql
updateGeoObject(input: UpdateGeoObjectInput!): GeoObject!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `UpdateGeoObjectInput!` | See fields below |

**UpdateGeoObjectInput fields**

| Field          | Type                                              | Description                 |
| -------------- | ------------------------------------------------- | --------------------------- |
| `id`           | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Geo object ID to update     |
| `title`        | `String`                                          | New display name            |
| `customFields` | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Updated custom field values |

**Returns:** [GeoObject!](../api-reference/objects.md#geoobject/)

### deleteGeoObject

Soft-delete geo object. Requires If-Match header.

```graphql
deleteGeoObject(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### restoreGeoObject

Restore soft-deleted geo object. Requires If-Match header.

```graphql
restoreGeoObject(id: UUID!): GeoObject!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [GeoObject!](../api-reference/objects.md#geoobject/)

### bulkDeleteGeoObjects

Bulk soft-delete geo objects. Does NOT use ETag (last write wins).

```graphql
bulkDeleteGeoObjects(input: BulkDeleteInput!): BulkDeleteResult!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `BulkDeleteInput!` | See fields below |

**BulkDeleteInput fields**

| Field | Type                                                   | Description               |
| ----- | ------------------------------------------------------ | ------------------------- |
| `ids` | [\[UUID!\]!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | IDs of entities to delete |

**Returns:** [BulkDeleteResult!](../api-reference/objects.md#bulkdeleteresult/)

## Schedules

### createSchedule

Create new schedule

```graphql
createSchedule(input: CreateScheduleInput!): Schedule!
```

**Arguments**

| Name    | Type                   | Description      |
| ------- | ---------------------- | ---------------- |
| `input` | `CreateScheduleInput!` | See fields below |

**CreateScheduleInput fields**

| Field            | Type                                              | Description                                  |
| ---------------- | ------------------------------------------------- | -------------------------------------------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Organization that will own the schedule      |
| `typeId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Schedule type classification                 |
| `title`          | `String!`                                         | Schedule display name                        |
| `customFields`   | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Custom field values including schedule\_data |

**Returns:** [Schedule!](../api-reference/objects.md#schedule/)

### updateSchedule

Update schedule. Requires If-Match header with current ETag.

```graphql
updateSchedule(input: UpdateScheduleInput!): Schedule!
```

**Arguments**

| Name    | Type                   | Description      |
| ------- | ---------------------- | ---------------- |
| `input` | `UpdateScheduleInput!` | See fields below |

**UpdateScheduleInput fields**

| Field          | Type                                              | Description                 |
| -------------- | ------------------------------------------------- | --------------------------- |
| `id`           | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Schedule ID to update       |
| `title`        | `String`                                          | New display name            |
| `customFields` | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Updated custom field values |

**Returns:** [Schedule!](../api-reference/objects.md#schedule/)

### deleteSchedule

Soft-delete schedule. Requires If-Match header.

```graphql
deleteSchedule(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### restoreSchedule

Restore soft-deleted schedule. Requires If-Match header.

```graphql
restoreSchedule(id: UUID!): Schedule!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Schedule!](../api-reference/objects.md#schedule/)

## Organizations

### createOrganization

Create new organization. Parent must be a dealer to have children.

```graphql
createOrganization(input: CreateOrganizationInput!): Organization!
```

**Arguments**

| Name    | Type                       | Description      |
| ------- | -------------------------- | ---------------- |
| `input` | `CreateOrganizationInput!` | See fields below |

**CreateOrganizationInput fields**

| Field        | Type                                             | Description                                       |
| ------------ | ------------------------------------------------ | ------------------------------------------------- |
| `parentId`   | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Parent organization (null for root)               |
| `code`       | `String!`                                        | Unique organization code                          |
| `title`      | `String!`                                        | Organization display name                         |
| `externalId` | `String`                                         | External system identifier                        |
| `isDealer`   | `Boolean`                                        | Whether organization can create sub-organizations |

**Returns:** [Organization!](../api-reference/objects.md#organization/)

### updateOrganization

Update organization. Requires If-Match header with current ETag.

```graphql
updateOrganization(input: UpdateOrganizationInput!): Organization!
```

**Arguments**

| Name    | Type                       | Description      |
| ------- | -------------------------- | ---------------- |
| `input` | `UpdateOrganizationInput!` | See fields below |

**UpdateOrganizationInput fields**

| Field        | Type                                              | Description               |
| ------------ | ------------------------------------------------- | ------------------------- |
| `id`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Organization ID to update |
| `title`      | `String`                                          | New display name          |
| `externalId` | `String`                                          | New external identifier   |
| `isActive`   | `Boolean`                                         | New active status         |
| `isDealer`   | `Boolean`                                         | New dealer capability     |

**Returns:** [Organization!](../api-reference/objects.md#organization/)

### deleteOrganization

Soft-delete organization and all its data. Requires If-Match header.

```graphql
deleteOrganization(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Users

### createUser

Create new user from identity provider data

```graphql
createUser(input: CreateUserInput!): User!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `CreateUserInput!` | See fields below |

**CreateUserInput fields**

| Field                | Type                                              | Description                                    |
| -------------------- | ------------------------------------------------- | ---------------------------------------------- |
| `identityProvider`   | `String!`                                         | Identity provider name (keycloak, auth0, etc.) |
| `identityProviderId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | User ID in the identity provider               |
| `fullName`           | `String!`                                         | User display name                              |
| `externalId`         | `String`                                          | External system identifier                     |

**Returns:** [User!](../api-reference/objects.md#user/)

### updateUser

Update user. Requires If-Match header with current ETag.

```graphql
updateUser(input: UpdateUserInput!): User!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `UpdateUserInput!` | See fields below |

**UpdateUserInput fields**

| Field        | Type                                              | Description             |
| ------------ | ------------------------------------------------- | ----------------------- |
| `id`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | User ID to update       |
| `fullName`   | `String`                                          | New display name        |
| `externalId` | `String`                                          | New external identifier |
| `isActive`   | `Boolean`                                         | New active status       |

**Returns:** [User!](../api-reference/objects.md#user/)

### deleteUser

Soft-delete user. Removes all memberships. Requires If-Match header.

```graphql
deleteUser(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Members

### createMember

Add user to organization as member

```graphql
createMember(input: CreateMemberInput!): Member!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `CreateMemberInput!` | See fields below |

**CreateMemberInput fields**

| Field            | Type                                              | Description                       |
| ---------------- | ------------------------------------------------- | --------------------------------- |
| `userId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | User to add to organization       |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Organization to join              |
| `customFields`   | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Membership-specific custom fields |

**Returns:** [Member!](../api-reference/objects.md#member/)

### updateMember

Update membership custom fields or status

```graphql
updateMember(input: UpdateMemberInput!): Member!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `UpdateMemberInput!` | See fields below |

**UpdateMemberInput fields**

| Field          | Type                                              | Description                 |
| -------------- | ------------------------------------------------- | --------------------------- |
| `id`           | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Membership ID to update     |
| `isActive`     | `Boolean`                                         | New active status           |
| `customFields` | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | Updated custom field values |

**Returns:** [Member!](../api-reference/objects.md#member/)

### removeMember

Remove user from organization

```graphql
removeMember(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Integrations

### createIntegration

Create new integration

```graphql
createIntegration(input: CreateIntegrationInput!): Integration!
```

**Arguments**

| Name    | Type                      | Description      |
| ------- | ------------------------- | ---------------- |
| `input` | `CreateIntegrationInput!` | See fields below |

**CreateIntegrationInput fields**

| Field           | Type      | Description                              |
| --------------- | --------- | ---------------------------------------- |
| `name`          | `String!` | Integration display name                 |
| `credentialRef` | `String`  | Reference to credentials in secure vault |

**Returns:** [Integration!](../api-reference/objects.md#integration/)

### updateIntegration

Update integration. Requires If-Match header with current ETag.

```graphql
updateIntegration(input: UpdateIntegrationInput!): Integration!
```

**Arguments**

| Name    | Type                      | Description      |
| ------- | ------------------------- | ---------------- |
| `input` | `UpdateIntegrationInput!` | See fields below |

**UpdateIntegrationInput fields**

| Field           | Type                                              | Description              |
| --------------- | ------------------------------------------------- | ------------------------ |
| `id`            | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Integration ID to update |
| `name`          | `String`                                          | New display name         |
| `credentialRef` | `String`                                          | New credential reference |
| `isActive`      | `Boolean`                                         | New active status        |

**Returns:** [Integration!](../api-reference/objects.md#integration/)

### deleteIntegration

Soft-delete integration. Revokes all permissions. Requires If-Match header.

```graphql
deleteIntegration(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Access control

### assignRole

Assign role to actor (user or integration)

```graphql
assignRole(input: AssignRoleInput!): ActorRole!
```

**Arguments**

| Name    | Type               | Description      |
| ------- | ------------------ | ---------------- |
| `input` | `AssignRoleInput!` | See fields below |

**AssignRoleInput fields**

| Field        | Type                                                     | Description                                       |
| ------------ | -------------------------------------------------------- | ------------------------------------------------- |
| `actorId`    | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)        | Actor (user or integration) to assign role to     |
| `roleId`     | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)        | Role to assign                                    |
| `expireDate` | [DateTime](/broken/pages/TOdGVmQ3HHnniCOoOsfN#datetime/) | Optional expiration date for temporary assignment |

**Returns:** [ActorRole!](../api-reference/objects.md#actorrole/)

### revokeRole

Revoke role from actor

```graphql
revokeRole(actorRoleId: UUID!): Boolean!
```

**Arguments**

| Name          | Type                                              | Description |
| ------------- | ------------------------------------------------- | ----------- |
| `actorRoleId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### grantPermission

Grant permission to role

```graphql
grantPermission(input: GrantPermissionInput!): RolePermission!
```

**Arguments**

| Name    | Type                    | Description      |
| ------- | ----------------------- | ---------------- |
| `input` | `GrantPermissionInput!` | See fields below |

**GrantPermissionInput fields**

| Field               | Type                                                                           | Description                                       |
| ------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------- |
| `roleId`            | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                              | Role to grant permission to                       |
| `permissionScopeId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                              | Permission scope to grant                         |
| `targetEntityId`    | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                               | Null = permission applies to all entities of type |
| `actions`           | [\[ActionPermission!\]!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#actionpermission/) | Actions to allow                                  |

**Returns:** [RolePermission!](../api-reference/objects.md#rolepermission/)

### revokePermission

Revoke permission from role

```graphql
revokePermission(permissionId: UUID!): Boolean!
```

**Arguments**

| Name           | Type                                              | Description |
| -------------- | ------------------------------------------------- | ----------- |
| `permissionId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### setUserScope

Set user scope restriction (whitelist filter)

```graphql
setUserScope(input: SetUserScopeInput!): UserScope!
```

**Arguments**

| Name    | Type                 | Description      |
| ------- | -------------------- | ---------------- |
| `input` | `SetUserScopeInput!` | See fields below |

**SetUserScopeInput fields**

| Field               | Type                                                                           | Description                        |
| ------------------- | ------------------------------------------------------------------------------ | ---------------------------------- |
| `actorId`           | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                              | Actor to restrict                  |
| `permissionScopeId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                              | Permission scope to filter         |
| `targetEntityId`    | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                              | Specific entity to allow access to |
| `actions`           | [\[ActionPermission!\]!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#actionpermission/) | Actions allowed on this entity     |

**Returns:** [UserScope!](../api-reference/objects.md#userscope/)

### removeUserScope

Remove user scope restriction

```graphql
removeUserScope(userScopeId: UUID!): Boolean!
```

**Arguments**

| Name          | Type                                              | Description |
| ------------- | ------------------------------------------------- | ----------- |
| `userScopeId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Device relations

### linkDeviceInventory

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

| Field         | Type                                              | Description      |
| ------------- | ------------------------------------------------- | ---------------- |
| `deviceId`    | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Device to assign |
| `inventoryId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Target inventory |

**Returns:** [DeviceInventoryRelation!](../api-reference/objects.md#deviceinventoryrelation/)

### unlinkDeviceInventory

Unlink device from current inventory

```graphql
unlinkDeviceInventory(deviceId: UUID!): Boolean!
```

**Arguments**

| Name       | Type                                              | Description |
| ---------- | ------------------------------------------------- | ----------- |
| `deviceId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

### createDeviceRelation

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

| Field            | Type                                              | Description                   |
| ---------------- | ------------------------------------------------- | ----------------------------- |
| `firstDeviceId`  | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | First device in relationship  |
| `secondDeviceId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Second device in relationship |
| `typeId`         | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Relationship type             |

**Returns:** [DeviceRelation!](../api-reference/objects.md#devicerelation/)

### deleteDeviceRelation

Delete device relationship

```graphql
deleteDeviceRelation(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Custom fields

### createCustomFieldDefinition

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

| Field                | Type                                                        | Description                                      |
| -------------------- | ----------------------------------------------------------- | ------------------------------------------------ |
| `organizationId`     | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)           | Organization that will own this definition       |
| `ownerCatalogItemId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)           | Owner catalog item (EntityType or specific type) |
| `targetEntityTypeId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)           | Target entity type this field applies to         |
| `code`               | `String!`                                                   | Machine-readable field code                      |
| `title`              | `String!`                                                   | Human-readable field title                       |
| `description`        | `String`                                                    | Optional field description                       |
| `fieldType`          | [FieldType!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#fieldtype/) | Data type for the field                          |
| `isSystem`           | `Boolean`                                                   | Whether this is a system-managed field           |
| `order`              | `Int`                                                       | Display order                                    |
| `extra`              | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)            | Additional metadata                              |
| `params`             | `FieldParamsInput!`                                         | Type-specific parameters                         |

**Returns:** [CustomFieldDefinition!](../api-reference/objects.md#customfielddefinition/)

### updateCustomFieldDefinition

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

| Field         | Type                                              | Description             |
| ------------- | ------------------------------------------------- | ----------------------- |
| `id`          | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Definition ID to update |
| `title`       | `String`                                          | New title               |
| `description` | `String`                                          | New description         |
| `order`       | `Int`                                             | New display order       |
| `extra`       | [JSON](/broken/pages/TOdGVmQ3HHnniCOoOsfN#json/)  | New metadata            |
| `params`      | `FieldParamsInput`                                | Updated parameters      |

**Returns:** [CustomFieldDefinition!](../api-reference/objects.md#customfielddefinition/)

### deleteCustomFieldDefinition

Soft-delete custom field definition. Preserves existing data.

```graphql
deleteCustomFieldDefinition(id: UUID!): Boolean!
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** `Boolean!`

## Localization

### setTranslation

Create or update translation for entity field

```graphql
setTranslation(
  entityId: UUID!
  fieldCode: String!
  locale: String!
  textValue: String!
): I18nText!
```

**Arguments**

| Name        | Type                                              | Description |
| ----------- | ------------------------------------------------- | ----------- |
| `entityId`  | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `fieldCode` | `String!`                                         |             |
| `locale`    | `String!`                                         |             |
| `textValue` | `String!`                                         |             |

**Returns:** [I18nText!](../api-reference/objects.md#i18ntext/)

### deleteTranslation

Delete translation for entity field

```graphql
deleteTranslation(
  entityId: UUID!
  fieldCode: String!
  locale: String!
): Boolean!
```

**Arguments**

| Name        | Type                                              | Description |
| ----------- | ------------------------------------------------- | ----------- |
| `entityId`  | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `fieldCode` | `String!`                                         |             |
| `locale`    | `String!`                                         |             |

**Returns:** `Boolean!`
