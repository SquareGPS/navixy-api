# Queries

Queries retrieve data from the Navixy database without modifying it.

{% hint style="warning" %}
List queries return paginated results using the [Relay Cursor Connections](https://relay.dev/graphql/connections.htm) pattern. See the [Pagination guide](../pagination.md) for details on navigating large result sets.
{% endhint %}

## General

### node

Fetch any entity by ID using Node interface. Returns null if not found or no permission.

```graphql
node(id: UUID!): Node
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Node](../api-reference/interfaces.md#node/)

### me

Returns currently authenticated user

```graphql
me: User!
```

**Returns:** [User!](../api-reference/objects.md#user/)

## Devices

### deviceVendor

Fetch device vendor by ID. Returns null if not found.

```graphql
deviceVendor(id: UUID!): DeviceVendor
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [DeviceVendor](../api-reference/objects.md#devicevendor/)

### deviceVendors

List all device vendors

```graphql
deviceVendors: [DeviceVendor!]!
```

**Returns:** [\[DeviceVendor!\]!](../api-reference/objects.md#devicevendor/)

### deviceModel

Fetch device model by ID. Returns null if not found.

```graphql
deviceModel(id: UUID!): DeviceModel
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [DeviceModel](../api-reference/objects.md#devicemodel/)

### deviceModels

List device models. Filter by vendor if provided.

```graphql
deviceModels(vendorId: UUID): [DeviceModel!]!
```

**Arguments**

| Name       | Type                                             | Description |
| ---------- | ------------------------------------------------ | ----------- |
| `vendorId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[DeviceModel!\]!](../api-reference/objects.md#devicemodel/)

### deviceType

Fetch device type by ID. Returns null if not found.

```graphql
deviceType(id: UUID!): DeviceType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [DeviceType](../api-reference/objects.md#devicetype/)

### deviceTypes

List device types. Filter by organization for custom types.

```graphql
deviceTypes(organizationId: UUID): [DeviceType!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[DeviceType!\]!](../api-reference/objects.md#devicetype/)

### deviceStatus

Fetch device status by ID. Returns null if not found.

```graphql
deviceStatus(id: UUID!): DeviceStatus
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [DeviceStatus](../api-reference/objects.md#devicestatus/)

### deviceStatuses

List device statuses. Filter by organization for custom statuses.

```graphql
deviceStatuses(organizationId: UUID): [DeviceStatus!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[DeviceStatus!\]!](../api-reference/objects.md#devicestatus/)

### device

Fetch device by ID. Returns null if not found or no permission.

```graphql
device(id: UUID!): Device
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Device](../api-reference/objects.md#device/)

### devices

Query devices with filtering, pagination, and sorting. Sort format: \["field:ASC", "field:DESC"] Supports: title, createdAt, updatedAt, status.code, type.code

```graphql
devices(
  filter: DeviceFilter
  pagination: PaginationInput
  sort: [String!]
): DeviceConnection!
```

**Arguments**

| Name         | Type              | Description      |
| ------------ | ----------------- | ---------------- |
| `filter`     | `DeviceFilter`    | See fields below |
| `pagination` | `PaginationInput` | See fields below |
| `sort`       | `[String!]`       |                  |

**DeviceFilter fields**

| Field            | Type                                             | Description                                 |
| ---------------- | ------------------------------------------------ | ------------------------------------------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by organization                      |
| `typeId`         | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by device type                       |
| `modelId`        | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by device model                      |
| `statusId`       | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by status                            |
| `title`          | `String`                                         | Search in title (case-insensitive contains) |
| `includeDeleted` | `Boolean`                                        | Include soft-deleted devices                |
| `customFields`   | `[CustomFieldFilter!]`                           | Custom field filters                        |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [DeviceConnection!](../api-reference/objects.md#deviceconnection/)

## Assets

### assetType

Fetch asset type by ID. Returns null if not found.

```graphql
assetType(id: UUID!): AssetType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [AssetType](../api-reference/objects.md#assettype/)

### assetTypes

List asset types. Filter by organization for custom types.

```graphql
assetTypes(organizationId: UUID): [AssetType!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[AssetType!\]!](../api-reference/objects.md#assettype/)

### asset

Fetch asset by ID. Returns null if not found or no permission.

```graphql
asset(id: UUID!): Asset
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Asset](../api-reference/objects.md#asset/)

### assets

Query assets with filtering, pagination, and sorting

```graphql
assets(
  filter: AssetFilter
  pagination: PaginationInput
  sort: [String!]
): AssetConnection!
```

**Arguments**

| Name         | Type              | Description      |
| ------------ | ----------------- | ---------------- |
| `filter`     | `AssetFilter`     | See fields below |
| `pagination` | `PaginationInput` | See fields below |
| `sort`       | `[String!]`       |                  |

**AssetFilter fields**

| Field            | Type                                             | Description                                 |
| ---------------- | ------------------------------------------------ | ------------------------------------------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by organization                      |
| `typeId`         | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by asset type                        |
| `title`          | `String`                                         | Search in title (case-insensitive contains) |
| `includeDeleted` | `Boolean`                                        | Include soft-deleted assets                 |
| `customFields`   | `[CustomFieldFilter!]`                           | Custom field filters                        |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [AssetConnection!](../api-reference/objects.md#assetconnection/)

## Asset groups

### assetGroupType

Fetch asset group type by ID. Returns null if not found.

```graphql
assetGroupType(id: UUID!): AssetGroupType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [AssetGroupType](../api-reference/objects.md#assetgrouptype/)

### assetGroupTypes

List asset group types. Filter by organization for custom types.

```graphql
assetGroupTypes(organizationId: UUID): [AssetGroupType!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[AssetGroupType!\]!](../api-reference/objects.md#assetgrouptype/)

### assetGroup

Fetch asset group by ID. Returns null if not found or no permission.

```graphql
assetGroup(id: UUID!): AssetGroup
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [AssetGroup](../api-reference/objects.md#assetgroup/)

### assetGroups

List asset groups for organization

```graphql
assetGroups(
  organizationId: UUID!
  includeDeleted: Boolean = false
): [AssetGroup!]!
```

**Arguments**

| Name             | Type                                              | Description |
| ---------------- | ------------------------------------------------- | ----------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `includeDeleted` | `Boolean`                                         |             |

**Returns:** [\[AssetGroup!\]!](../api-reference/objects.md#assetgroup/)

## Geo objects

### geoObjectType

Fetch geo object type by ID. Returns null if not found.

```graphql
geoObjectType(id: UUID!): GeoObjectType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [GeoObjectType](../api-reference/objects.md#geoobjecttype/)

### geoObjectTypes

List geo object types. Filter by organization for custom types.

```graphql
geoObjectTypes(organizationId: UUID): [GeoObjectType!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[GeoObjectType!\]!](../api-reference/objects.md#geoobjecttype/)

### geoObject

Fetch geo object by ID. Returns null if not found or no permission.

```graphql
geoObject(id: UUID!): GeoObject
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [GeoObject](../api-reference/objects.md#geoobject/)

### geoObjects

Query geo objects with filtering, pagination, and sorting

```graphql
geoObjects(
  filter: GeoObjectFilter
  pagination: PaginationInput
  sort: [String!]
): GeoObjectConnection!
```

**Arguments**

| Name         | Type              | Description      |
| ------------ | ----------------- | ---------------- |
| `filter`     | `GeoObjectFilter` | See fields below |
| `pagination` | `PaginationInput` | See fields below |
| `sort`       | `[String!]`       |                  |

**GeoObjectFilter fields**

| Field            | Type                                             | Description                                 |
| ---------------- | ------------------------------------------------ | ------------------------------------------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by organization                      |
| `typeId`         | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by geo object type                   |
| `title`          | `String`                                         | Search in title (case-insensitive contains) |
| `includeDeleted` | `Boolean`                                        | Include soft-deleted geo objects            |
| `customFields`   | `[CustomFieldFilter!]`                           | Custom field filters                        |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [GeoObjectConnection!](../api-reference/objects.md#geoobjectconnection/)

## Schedules

### scheduleType

Fetch schedule type by ID. Returns null if not found.

```graphql
scheduleType(id: UUID!): ScheduleType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [ScheduleType](../api-reference/objects.md#scheduletype/)

### scheduleTypes

List schedule types. Filter by organization for custom types.

```graphql
scheduleTypes(organizationId: UUID): [ScheduleType!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[ScheduleType!\]!](../api-reference/objects.md#scheduletype/)

### schedule

Fetch schedule by ID. Returns null if not found or no permission.

```graphql
schedule(id: UUID!): Schedule
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Schedule](../api-reference/objects.md#schedule/)

### schedules

Query schedules with filtering, pagination, and sorting

```graphql
schedules(
  filter: ScheduleFilter
  pagination: PaginationInput
  sort: [String!]
): ScheduleConnection!
```

**Arguments**

| Name         | Type              | Description      |
| ------------ | ----------------- | ---------------- |
| `filter`     | `ScheduleFilter`  | See fields below |
| `pagination` | `PaginationInput` | See fields below |
| `sort`       | `[String!]`       |                  |

**ScheduleFilter fields**

| Field            | Type                                             | Description                                 |
| ---------------- | ------------------------------------------------ | ------------------------------------------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by organization                      |
| `typeId`         | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by schedule type                     |
| `title`          | `String`                                         | Search in title (case-insensitive contains) |
| `includeDeleted` | `Boolean`                                        | Include soft-deleted schedules              |
| `customFields`   | `[CustomFieldFilter!]`                           | Custom field filters                        |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [ScheduleConnection!](../api-reference/objects.md#scheduleconnection/)

## Organizations

### organization

Fetch organization by ID. Returns null if not found or no permission.

```graphql
organization(id: UUID!): Organization
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Organization](../api-reference/objects.md#organization/)

### organizations

Query organizations with filtering and pagination

```graphql
organizations(
  filter: OrganizationFilter
  pagination: PaginationInput
): OrganizationConnection!
```

**Arguments**

| Name         | Type                 | Description      |
| ------------ | -------------------- | ---------------- |
| `filter`     | `OrganizationFilter` | See fields below |
| `pagination` | `PaginationInput`    | See fields below |

**OrganizationFilter fields**

| Field            | Type                                             | Description                        |
| ---------------- | ------------------------------------------------ | ---------------------------------- |
| `parentId`       | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by parent organization      |
| `isActive`       | `Boolean`                                        | Filter by active status            |
| `isDealer`       | `Boolean`                                        | Filter by dealer capability        |
| `includeDeleted` | `Boolean`                                        | Include soft-deleted organizations |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [OrganizationConnection!](../api-reference/objects.md#organizationconnection/)

### catalog

Fetch catalog by ID. Returns null if not found.

```graphql
catalog(id: UUID!): Catalog
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Catalog](../api-reference/objects.md#catalog/)

### catalogs

List catalogs for organization. Optionally filter by module.

```graphql
catalogs(
  organizationId: UUID!
  moduleId: UUID
): [Catalog!]!
```

**Arguments**

| Name             | Type                                              | Description |
| ---------------- | ------------------------------------------------- | ----------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `moduleId`       | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)  |             |

**Returns:** [\[Catalog!\]!](../api-reference/objects.md#catalog/)

## Actors

### actor

Fetch actor by ID. Returns null if not found or no permission.

```graphql
actor(id: UUID!): Actor
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Actor](../api-reference/objects.md#actor/)

### user

Fetch user by ID. Returns null if not found or no permission.

```graphql
user(id: UUID!): User
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [User](../api-reference/objects.md#user/)

### users

Query users with filtering and pagination

```graphql
users(
  filter: UserFilter
  pagination: PaginationInput
): UserConnection!
```

**Arguments**

| Name         | Type              | Description      |
| ------------ | ----------------- | ---------------- |
| `filter`     | `UserFilter`      | See fields below |
| `pagination` | `PaginationInput` | See fields below |

**UserFilter fields**

| Field            | Type                                             | Description                       |
| ---------------- | ------------------------------------------------ | --------------------------------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) | Filter by organization membership |
| `isActive`       | `Boolean`                                        | Filter by active status           |
| `includeDeleted` | `Boolean`                                        | Include soft-deleted users        |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [UserConnection!](../api-reference/objects.md#userconnection/)

### member

Fetch membership by ID. Returns null if not found or no permission.

```graphql
member(id: UUID!): Member
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Member](../api-reference/objects.md#member/)

### members

List memberships. Filter by user and/or organization.

```graphql
members(
  userId: UUID
  organizationId: UUID
  includeDeleted: Boolean = false
): [Member!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `userId`         | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `includeDeleted` | `Boolean`                                        |             |

**Returns:** [\[Member!\]!](../api-reference/objects.md#member/)

### integration

Fetch integration by ID. Returns null if not found or no permission.

```graphql
integration(id: UUID!): Integration
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Integration](../api-reference/objects.md#integration/)

### integrations

List integrations. Optionally filter by active status.

```graphql
integrations(isActive: Boolean): [Integration!]!
```

**Arguments**

| Name       | Type      | Description |
| ---------- | --------- | ----------- |
| `isActive` | `Boolean` |             |

**Returns:** [\[Integration!\]!](../api-reference/objects.md#integration/)

## Access control

### role

Fetch role by ID. Returns null if not found.

```graphql
role(id: UUID!): Role
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Role](../api-reference/objects.md#role/)

### roles

List roles. Filter by organization. Null returns system roles.

```graphql
roles(organizationId: UUID): [Role!]!
```

**Arguments**

| Name             | Type                                             | Description |
| ---------------- | ------------------------------------------------ | ----------- |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[Role!\]!](../api-reference/objects.md#role/)

### permissionScope

Fetch permission scope by ID. Returns null if not found.

```graphql
permissionScope(id: UUID!): PermissionScope
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [PermissionScope](../api-reference/objects.md#permissionscope/)

### permissionScopes

List permission scopes. Filter by module.

```graphql
permissionScopes(moduleId: UUID): [PermissionScope!]!
```

**Arguments**

| Name       | Type                                             | Description |
| ---------- | ------------------------------------------------ | ----------- |
| `moduleId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [\[PermissionScope!\]!](../api-reference/objects.md#permissionscope/)

## Inventory

### inventory

Fetch inventory by ID. Returns null if not found or no permission.

```graphql
inventory(id: UUID!): Inventory
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Inventory](../api-reference/objects.md#inventory/)

## Custom fields

### customFieldDefinition

Fetch custom field definition by ID. Returns null if not found.

```graphql
customFieldDefinition(id: UUID!): CustomFieldDefinition
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [CustomFieldDefinition](../api-reference/objects.md#customfielddefinition/)

### customFieldDefinitions

List custom field definitions with filters

```graphql
customFieldDefinitions(
  organizationId: UUID!
  ownerCatalogItemId: UUID
  targetEntityTypeCode: String
  includeDeleted: Boolean = false
): [CustomFieldDefinition!]!
```

**Arguments**

| Name                   | Type                                              | Description |
| ---------------------- | ------------------------------------------------- | ----------- |
| `organizationId`       | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `ownerCatalogItemId`   | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)  |             |
| `targetEntityTypeCode` | `String`                                          |             |
| `includeDeleted`       | `Boolean`                                         |             |

**Returns:** [\[CustomFieldDefinition!\]!](../api-reference/objects.md#customfielddefinition/)

## Audit

### auditEvents

Query audit events with filtering and pagination

```graphql
auditEvents(
  filter: AuditEventFilter
  pagination: PaginationInput
): AuditEventConnection!
```

**Arguments**

| Name         | Type               | Description      |
| ------------ | ------------------ | ---------------- |
| `filter`     | `AuditEventFilter` | See fields below |
| `pagination` | `PaginationInput`  | See fields below |

**AuditEventFilter fields**

| Field            | Type                                                                 | Description                                |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------------ |
| `organizationId` | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                     | Filter by organization                     |
| `actorId`        | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                     | Filter by actor who triggered the event    |
| `aggregateType`  | `String`                                                             | Filter by entity type                      |
| `aggregateId`    | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                     | Filter by specific entity ID               |
| `eventCategory`  | `String`                                                             | Filter by event category (auth, domain)    |
| `eventType`      | [AuditEventType](/broken/pages/TOdGVmQ3HHnniCOoOsfN#auditeventtype/) | Filter by event type                       |
| `sourceType`     | [SourceType](/broken/pages/TOdGVmQ3HHnniCOoOsfN#sourcetype/)         | Filter by source type                      |
| `traceId`        | [UUID](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/)                     | Filter by trace ID for distributed tracing |
| `from`           | [DateTime](/broken/pages/TOdGVmQ3HHnniCOoOsfN#datetime/)             | Events after this timestamp                |
| `to`             | [DateTime](/broken/pages/TOdGVmQ3HHnniCOoOsfN#datetime/)             | Events before this timestamp               |

**PaginationInput fields**

| Field    | Type     | Description                                |
| -------- | -------- | ------------------------------------------ |
| `first`  | `Int`    | Number of items to fetch from start        |
| `after`  | `String` | Cursor to start after (forward pagination) |
| `last`   | `Int`    | Number of items to fetch from end          |
| `before` | `String` | Cursor to end before (backward pagination) |

**Returns:** [AuditEventConnection!](../api-reference/objects.md#auditeventconnection/)

## Localization

### i18nTexts

Get translations for entity. Optionally filter by locale.

```graphql
i18nTexts(
  entityId: UUID!
  locale: String
): [I18nText!]!
```

**Arguments**

| Name       | Type                                              | Description |
| ---------- | ------------------------------------------------- | ----------- |
| `entityId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `locale`   | `String`                                          |             |

**Returns:** [\[I18nText!\]!](../api-reference/objects.md#i18ntext/)

## Catalog items

### module

Fetch module by ID. Returns null if not found.

```graphql
module(id: UUID!): Module
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Module](../api-reference/objects.md#module/)

### modules

List all system modules

```graphql
modules: [Module!]!
```

**Returns:** [\[Module!\]!](../api-reference/objects.md#module/)

### entityType

Fetch entity type by ID. Returns null if not found.

```graphql
entityType(id: UUID!): EntityType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [EntityType](../api-reference/objects.md#entitytype/)

### entityTypes

List all entity types

```graphql
entityTypes: [EntityType!]!
```

**Returns:** [\[EntityType!\]!](../api-reference/objects.md#entitytype/)

### deviceRelationType

Fetch device relation type by ID. Returns null if not found.

```graphql
deviceRelationType(id: UUID!): DeviceRelationType
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [DeviceRelationType](../api-reference/objects.md#devicerelationtype/)

### deviceRelationTypes

List all device relation types

```graphql
deviceRelationTypes: [DeviceRelationType!]!
```

**Returns:** [\[DeviceRelationType!\]!](../api-reference/objects.md#devicerelationtype/)

### tag

Fetch tag by ID. Returns null if not found.

```graphql
tag(id: UUID!): Tag
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Tag](../api-reference/objects.md#tag/)

### tags

List tags. Filter by organization and optionally by entity type.

```graphql
tags(
  organizationId: UUID!
  entityTypeCode: String
): [Tag!]!
```

**Arguments**

| Name             | Type                                              | Description |
| ---------------- | ------------------------------------------------- | ----------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `entityTypeCode` | `String`                                          |             |

**Returns:** [\[Tag!\]!](../api-reference/objects.md#tag/)

### country

Fetch country by ID. Returns null if not found.

```graphql
country(id: UUID!): Country
```

**Arguments**

| Name | Type                                              | Description |
| ---- | ------------------------------------------------- | ----------- |
| `id` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |

**Returns:** [Country](../api-reference/objects.md#country/)

### countries

List all countries

```graphql
countries: [Country!]!
```

**Returns:** [\[Country!\]!](../api-reference/objects.md#country/)

### inventories

List inventories for organization

```graphql
inventories(
  organizationId: UUID!
  includeDeleted: Boolean = false
): [Inventory!]!
```

**Arguments**

| Name             | Type                                              | Description |
| ---------------- | ------------------------------------------------- | ----------- |
| `organizationId` | [UUID!](/broken/pages/TOdGVmQ3HHnniCOoOsfN#uuid/) |             |
| `includeDeleted` | `Boolean`                                         |             |

**Returns:** [\[Inventory!\]!](../api-reference/objects.md#inventory/)
