# Queries

Queries retrieve data from the Navixy platform without modifying it.

{% hint style="warning" %}
List queries return paginated results using the [Relay Cursor Connections](https://relay.dev/graphql/connections.htm) pattern. See the [Pagination guide](../pagination.md) for details on navigating large result sets.
{% endhint %}

### General

#### node

Fetch any entity by ID using the [Node interface](scalars-and-enums.md#node). Returns null if not found or no permission.

```graphql
node(id: UUID!): Node
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** [Node](scalars-and-enums.md#node)

#### me

Returns the currently authenticated user.

```graphql
me: User!
```

**Returns:** User!

### Devices

#### device

Fetch device by ID. Returns null if not found or no permission.

```graphql
device(id: UUID!): Device
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Device

#### devices

Query devices with filtering, pagination, and sorting. Sort format: \["field:ASC", "field:DESC"] Supports: title, createdAt, updatedAt, status.code, type.code

```graphql
devices(
  filter: DeviceFilter,
  pagination: PaginationInput,
  sort: [String!]
): DeviceConnection!
```

**Arguments**

| Name         | Type              | Description |
| ------------ | ----------------- | ----------- |
| `filter`     | `DeviceFilter`    |             |
| `pagination` | `PaginationInput` |             |
| `sort`       | \[String!]        |             |

**Returns:** DeviceConnection!

#### deviceVendor

Fetch device vendor by ID. Returns null if not found.

```graphql
deviceVendor(id: UUID!): DeviceVendor
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** DeviceVendor

#### deviceVendors

List all device vendors

```graphql
deviceVendors: [DeviceVendor!]!
```

**Returns:** \[DeviceVendor!]!

#### deviceModel

Fetch device model by ID. Returns null if not found.

```graphql
deviceModel(id: UUID!): DeviceModel
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** DeviceModel

#### deviceModels

List device models. Filter by vendor if provided.

```graphql
deviceModels(vendorId: UUID): [DeviceModel!]!
```

**Arguments**

| Name       | Type | Description |
| ---------- | ---- | ----------- |
| `vendorId` | UUID |             |

**Returns:** \[DeviceModel!]!

#### deviceType

Fetch device type by ID. Returns null if not found.

```graphql
deviceType(id: UUID!): DeviceType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** DeviceType

#### deviceTypes

List device types. Filter by organization for custom types.

```graphql
deviceTypes(organizationId: UUID): [DeviceType!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[DeviceType!]!

#### deviceStatus

Fetch device status by ID. Returns null if not found.

```graphql
deviceStatus(id: UUID!): DeviceStatus
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** DeviceStatus

#### deviceStatuses

List device statuses. Filter by organization for custom statuses.

```graphql
deviceStatuses(organizationId: UUID): [DeviceStatus!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[DeviceStatus!]!

### Assets

#### assetType

Fetch asset type by ID. Returns null if not found.

```graphql
assetType(id: UUID!): AssetType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** AssetType

#### assetTypes

List asset types. Filter by organization for custom types.

```graphql
assetTypes(organizationId: UUID): [AssetType!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[AssetType!]!

#### asset

Fetch asset by ID. Returns null if not found or no permission.

```graphql
asset(id: UUID!): Asset
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Asset

#### assets

Query assets with filtering, pagination, and sorting

```graphql
assets(
  filter: AssetFilter,
  pagination: PaginationInput,
  sort: [String!]
): AssetConnection!
```

**Arguments**

| Name         | Type              | Description |
| ------------ | ----------------- | ----------- |
| `filter`     | `AssetFilter`     |             |
| `pagination` | `PaginationInput` |             |
| `sort`       | \[String!]        |             |

**Returns:** AssetConnection!

### Asset groups

#### assetGroupType

Fetch asset group type by ID. Returns null if not found.

```graphql
assetGroupType(id: UUID!): AssetGroupType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** AssetGroupType

#### assetGroupTypes

List asset group types. Filter by organization for custom types.

```graphql
assetGroupTypes(organizationId: UUID): [AssetGroupType!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[AssetGroupType!]!

#### assetGroup

Fetch asset group by ID. Returns null if not found or no permission.

```graphql
assetGroup(id: UUID!): AssetGroup
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** AssetGroup

#### assetGroups

List asset groups for organization

```graphql
assetGroups(
  organizationId: UUID!,
  includeDeleted: Boolean = false
): [AssetGroup!]!
```

**Arguments**

| Name             | Type    | Description |
| ---------------- | ------- | ----------- |
| `organizationId` | UUID!   |             |
| `includeDeleted` | Boolean |             |

**Returns:** \[AssetGroup!]!

### Geo objects

#### geoObjectType

Fetch geo object type by ID. Returns null if not found.

```graphql
geoObjectType(id: UUID!): GeoObjectType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** GeoObjectType

#### geoObjectTypes

List geo object types. Filter by organization for custom types.

```graphql
geoObjectTypes(organizationId: UUID): [GeoObjectType!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[GeoObjectType!]!

#### geoObject

Fetch geo object by ID. Returns null if not found or no permission.

```graphql
geoObject(id: UUID!): GeoObject
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** GeoObject

#### geoObjects

Query geo objects with filtering, pagination, and sorting

```graphql
geoObjects(
  filter: GeoObjectFilter,
  pagination: PaginationInput,
  sort: [String!]
): GeoObjectConnection!
```

**Arguments**

| Name         | Type              | Description |
| ------------ | ----------------- | ----------- |
| `filter`     | `GeoObjectFilter` |             |
| `pagination` | `PaginationInput` |             |
| `sort`       | \[String!]        |             |

**Returns:** GeoObjectConnection!

### Schedules

#### scheduleType

Fetch schedule type by ID. Returns null if not found.

```graphql
scheduleType(id: UUID!): ScheduleType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** ScheduleType

#### scheduleTypes

List schedule types. Filter by organization for custom types.

```graphql
scheduleTypes(organizationId: UUID): [ScheduleType!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[ScheduleType!]!

#### schedule

Fetch schedule by ID. Returns null if not found or no permission.

```graphql
schedule(id: UUID!): Schedule
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Schedule

#### schedules

Query schedules with filtering, pagination, and sorting

```graphql
schedules(
  filter: ScheduleFilter,
  pagination: PaginationInput,
  sort: [String!]
): ScheduleConnection!
```

**Arguments**

| Name         | Type              | Description |
| ------------ | ----------------- | ----------- |
| `filter`     | `ScheduleFilter`  |             |
| `pagination` | `PaginationInput` |             |
| `sort`       | \[String!]        |             |

**Returns:** ScheduleConnection!

### Organizations

#### organization

Fetch organization by ID. Returns null if not found or no permission.

```graphql
organization(id: UUID!): Organization
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Organization

#### organizations

Query organizations with filtering and pagination

```graphql
organizations(
  filter: OrganizationFilter,
  pagination: PaginationInput
): OrganizationConnection!
```

**Arguments**

| Name         | Type                 | Description |
| ------------ | -------------------- | ----------- |
| `filter`     | `OrganizationFilter` |             |
| `pagination` | `PaginationInput`    |             |

**Returns:** OrganizationConnection!

#### catalog

Fetch catalog by ID. Returns null if not found.

```graphql
catalog(id: UUID!): Catalog
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Catalog

#### catalogs

List catalogs for organization. Optionally filter by module.

```graphql
catalogs(
  organizationId: UUID!,
  moduleId: UUID
): [Catalog!]!
```

**Arguments**

| Name             | Type  | Description |
| ---------------- | ----- | ----------- |
| `organizationId` | UUID! |             |
| `moduleId`       | UUID  |             |

**Returns:** \[Catalog!]!

### Actors

#### actor

Fetch actor by ID. Returns null if not found or no permission.

```graphql
actor(id: UUID!): Actor
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Actor

#### user

Fetch user by ID. Returns null if not found or no permission.

```graphql
user(id: UUID!): User
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** User

#### users

Query users with filtering and pagination

```graphql
users(
  filter: UserFilter,
  pagination: PaginationInput
): UserConnection!
```

**Arguments**

| Name         | Type              | Description |
| ------------ | ----------------- | ----------- |
| `filter`     | `UserFilter`      |             |
| `pagination` | `PaginationInput` |             |

**Returns:** UserConnection!

#### member

Fetch membership by ID. Returns null if not found or no permission.

```graphql
member(id: UUID!): Member
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Member

#### members

List memberships. Filter by user and/or organization.

```graphql
members(
  userId: UUID,
  organizationId: UUID,
  includeDeleted: Boolean = false
): [Member!]!
```

**Arguments**

| Name             | Type    | Description |
| ---------------- | ------- | ----------- |
| `userId`         | UUID    |             |
| `organizationId` | UUID    |             |
| `includeDeleted` | Boolean |             |

**Returns:** \[Member!]!

#### integration

Fetch integration by ID. Returns null if not found or no permission.

```graphql
integration(id: UUID!): Integration
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Integration

#### integrations

List integrations. Optionally filter by active status.

```graphql
integrations(isActive: Boolean): [Integration!]!
```

**Arguments**

| Name       | Type    | Description |
| ---------- | ------- | ----------- |
| `isActive` | Boolean |             |

**Returns:** \[Integration!]!

### Access control

#### role

Fetch role by ID. Returns null if not found.

```graphql
role(id: UUID!): Role
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Role

#### roles

List roles. Filter by organization. Null returns system roles.

```graphql
roles(organizationId: UUID): [Role!]!
```

**Arguments**

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| `organizationId` | UUID |             |

**Returns:** \[Role!]!

#### permissionScope

Fetch permission scope by ID. Returns null if not found.

```graphql
permissionScope(id: UUID!): PermissionScope
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** PermissionScope

#### permissionScopes

List permission scopes. Filter by module.

```graphql
permissionScopes(moduleId: UUID): [PermissionScope!]!
```

**Arguments**

| Name       | Type | Description |
| ---------- | ---- | ----------- |
| `moduleId` | UUID |             |

**Returns:** \[PermissionScope!]!

### Inventory

#### inventory

Fetch inventory by ID. Returns null if not found or no permission.

```graphql
inventory(id: UUID!): Inventory
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Inventory

### Custom fields

#### customFieldDefinition

Fetch custom field definition by ID. Returns null if not found.

```graphql
customFieldDefinition(id: UUID!): CustomFieldDefinition
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** CustomFieldDefinition

#### customFieldDefinitions

List custom field definitions with filters

```graphql
customFieldDefinitions(
  organizationId: UUID!,
  ownerCatalogItemId: UUID,
  targetEntityTypeCode: String,
  includeDeleted: Boolean = false
): [CustomFieldDefinition!]!
```

**Arguments**

| Name                   | Type    | Description |
| ---------------------- | ------- | ----------- |
| `organizationId`       | UUID!   |             |
| `ownerCatalogItemId`   | UUID    |             |
| `targetEntityTypeCode` | String  |             |
| `includeDeleted`       | Boolean |             |

**Returns:** \[CustomFieldDefinition!]!

### Audit

#### auditEvents

Query audit events with filtering and pagination

```graphql
auditEvents(
  filter: AuditEventFilter,
  pagination: PaginationInput
): AuditEventConnection!
```

**Arguments**

| Name         | Type               | Description |
| ------------ | ------------------ | ----------- |
| `filter`     | `AuditEventFilter` |             |
| `pagination` | `PaginationInput`  |             |

**Returns:** AuditEventConnection!

### Localization

#### i18nTexts

Get translations for entity. Optionally filter by locale.

```graphql
i18nTexts(
  entityId: UUID!,
  locale: String
): [I18nText!]!
```

**Arguments**

| Name       | Type   | Description |
| ---------- | ------ | ----------- |
| `entityId` | UUID!  |             |
| `locale`   | String |             |

**Returns:** \[I18nText!]!

### Catalog items

#### module

Fetch module by ID. Returns null if not found.

```graphql
module(id: UUID!): Module
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Module

#### modules

List all system modules

```graphql
modules: [Module!]!
```

**Returns:** \[Module!]!

#### entityType

Fetch entity type by ID. Returns null if not found.

```graphql
entityType(id: UUID!): EntityType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** EntityType

#### entityTypes

List all entity types

```graphql
entityTypes: [EntityType!]!
```

**Returns:** \[EntityType!]!

#### deviceRelationType

Fetch device relation type by ID. Returns null if not found.

```graphql
deviceRelationType(id: UUID!): DeviceRelationType
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** DeviceRelationType

#### deviceRelationTypes

List all device relation types

```graphql
deviceRelationTypes: [DeviceRelationType!]!
```

**Returns:** \[DeviceRelationType!]!

#### tag

Fetch tag by ID. Returns null if not found.

```graphql
tag(id: UUID!): Tag
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Tag

#### tags

List tags. Filter by organization and optionally by entity type.

```graphql
tags(
  organizationId: UUID!,
  entityTypeCode: String
): [Tag!]!
```

**Arguments**

| Name             | Type   | Description |
| ---------------- | ------ | ----------- |
| `organizationId` | UUID!  |             |
| `entityTypeCode` | String |             |

**Returns:** \[Tag!]!

#### country

Fetch country by ID. Returns null if not found.

```graphql
country(id: UUID!): Country
```

**Arguments**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | UUID! |             |

**Returns:** Country

#### countries

List all countries

```graphql
countries: [Country!]!
```

**Returns:** \[Country!]!

#### inventories

List inventories for organization

```graphql
inventories(
  organizationId: UUID!,
  includeDeleted: Boolean = false
): [Inventory!]!
```

**Arguments**

| Name             | Type    | Description |
| ---------------- | ------- | ----------- |
| `organizationId` | UUID!   |             |
| `includeDeleted` | Boolean |             |

**Returns:** \[Inventory!]!
