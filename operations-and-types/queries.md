# Queries

Queries retrieve data from the Navixy database without modifying it. List queries return paginated results using the [Relay Cursor Connections](https://relay.dev/graphql/connections.htm) pattern — see the [Pagination guide](../pagination.md) for details.

Argument types link to their definitions on the [Inputs](inputs.md) page. Return types link to [Objects](objects.md) or [Interfaces](interfaces.md).

## General

### node

Retrieves any entity by its globally unique identifier.

```graphql
node(id: ID!): Node
```

**Arguments**

| Name | Type  | Description                       |
| ---- | ----- | --------------------------------- |
| `id` | `ID!` | The ID of the entity to retrieve. |

**Returns:** [Node](interfaces.md#node)

### nodes

Retrieves multiple entities by their globally unique identifiers. Returns items in the same order as the input IDs.

```graphql
nodes(ids: [ID!]!): [Node]!
```

**Arguments**

| Name  | Type     | Description                          |
| ----- | -------- | ------------------------------------ |
| `ids` | `[ID!]!` | The IDs of the entities to retrieve. |

**Returns:** [\[Node\]!](interfaces.md#node)

### me

Retrieves the currently authenticated actor.

```graphql
me: Actor!
```

**Returns:** [Actor!](interfaces.md#actor)

## Devices

### deviceTypes

Lists device types for an organization.

```graphql
deviceTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): DeviceTypeConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve device types for.                                                |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned device types.                                              |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned device types.                                           |

**Returns:** [DeviceTypeConnection!](objects.md#devicetypeconnection)

### deviceStatuses

Lists device statuses for an organization.

```graphql
deviceStatuses(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): DeviceStatusConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve device statuses for.                                             |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned device statuses.                                           |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned device statuses.                                        |

**Returns:** [DeviceStatusConnection!](objects.md#devicestatusconnection)

### deviceModels

Lists device models with optional vendor filter.

```graphql
deviceModels(
  organizationId: ID!
  filter: DeviceModelFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: TITLE, direction: ASC }
): DeviceModelConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve device models for.                                               |
| `filter`         | [DeviceModelFilter](inputs.md#devicemodelfilter) | Filtering options for the returned device models.                                             |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned device models.                                          |

**Returns:** [DeviceModelConnection!](objects.md#devicemodelconnection)

### device

Retrieves a device by its ID.

```graphql
device(id: ID!): Device
```

**Arguments**

| Name | Type  | Description                       |
| ---- | ----- | --------------------------------- |
| `id` | `ID!` | The ID of the device to retrieve. |

**Returns:** [Device](objects.md#device)

### devices

Lists devices for an organization.

```graphql
devices(
  organizationId: ID!
  filter: DeviceFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: DeviceOrder = { field: TITLE, direction: ASC }
): DeviceConnection!
```

**Arguments**

| Name             | Type                                   | Description                                                                                   |
| ---------------- | -------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                  | The organization to retrieve devices for.                                                     |
| `filter`         | [DeviceFilter](inputs.md#devicefilter) | Filtering options for the returned devices.                                                   |
| `first`          | `Int`                                  | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                               | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                  | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                               | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [DeviceOrder](inputs.md#deviceorder)   | The ordering options for the returned devices.                                                |

**Returns:** [DeviceConnection!](objects.md#deviceconnection)

## Assets

### assetTypes

Lists asset types for an organization.

```graphql
assetTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): AssetTypeConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve asset types for.                                                 |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned asset types.                                               |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned asset types.                                            |

**Returns:** [AssetTypeConnection!](objects.md#assettypeconnection)

### asset

Retrieves an asset by its ID.

```graphql
asset(id: ID!): Asset
```

**Arguments**

| Name | Type  | Description                      |
| ---- | ----- | -------------------------------- |
| `id` | `ID!` | The ID of the asset to retrieve. |

**Returns:** [Asset](objects.md#asset)

### assets

Lists assets for an organization.

```graphql
assets(
  organizationId: ID!
  filter: AssetFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AssetOrder = { field: TITLE, direction: ASC }
): AssetConnection!
```

**Arguments**

| Name             | Type                                 | Description                                                                                   |
| ---------------- | ------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                | The organization to retrieve assets for.                                                      |
| `filter`         | [AssetFilter](inputs.md#assetfilter) | Filtering options for the returned assets.                                                    |
| `first`          | `Int`                                | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                             | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                             | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [AssetOrder](inputs.md#assetorder)   | The ordering options for the returned assets.                                                 |

**Returns:** [AssetConnection!](objects.md#assetconnection)

## Asset groups

### assetGroupTypes

Lists asset group types for an organization.

```graphql
assetGroupTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): AssetGroupTypeConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve asset group types for.                                           |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned asset group types.                                         |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned asset group types.                                      |

**Returns:** [AssetGroupTypeConnection!](objects.md#assetgrouptypeconnection)

### assetGroup

Retrieves an asset group by its ID.

```graphql
assetGroup(id: ID!): AssetGroup
```

**Arguments**

| Name | Type  | Description                            |
| ---- | ----- | -------------------------------------- |
| `id` | `ID!` | The ID of the asset group to retrieve. |

**Returns:** [AssetGroup](objects.md#assetgroup)

### assetGroups

Lists asset groups for an organization.

```graphql
assetGroups(
  organizationId: ID!
  filter: AssetGroupFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AssetGroupOrder = { field: TITLE, direction: ASC }
): AssetGroupConnection!
```

**Arguments**

| Name             | Type                                           | Description                                                                                   |
| ---------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                          | The organization to retrieve asset groups for.                                                |
| `filter`         | [AssetGroupFilter](inputs.md#assetgroupfilter) | Filtering options for the returned asset groups.                                              |
| `first`          | `Int`                                          | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                       | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                          | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                       | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [AssetGroupOrder](inputs.md#assetgrouporder)   | The ordering options for the returned asset groups.                                           |

**Returns:** [AssetGroupConnection!](objects.md#assetgroupconnection)

## Geo objects

### geoObjectTypes

Lists geo object types for an organization.

```graphql
geoObjectTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): GeoObjectTypeConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve geo object types for.                                            |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned geo object types.                                          |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned geo object types.                                       |

**Returns:** [GeoObjectTypeConnection!](objects.md#geoobjecttypeconnection)

### geoObject

Retrieves a geo object by its ID.

```graphql
geoObject(id: ID!): GeoObject
```

**Arguments**

| Name | Type  | Description                           |
| ---- | ----- | ------------------------------------- |
| `id` | `ID!` | The ID of the geo object to retrieve. |

**Returns:** [GeoObject](objects.md#geoobject)

### geoObjects

Lists geo objects for an organization.

```graphql
geoObjects(
  organizationId: ID!
  filter: GeoObjectFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: GeoObjectOrder = { field: TITLE, direction: ASC }
): GeoObjectConnection!
```

**Arguments**

| Name             | Type                                         | Description                                                                                   |
| ---------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                        | The organization to retrieve geo objects for.                                                 |
| `filter`         | [GeoObjectFilter](inputs.md#geoobjectfilter) | Filtering options for the returned geo objects.                                               |
| `first`          | `Int`                                        | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                     | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                        | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                     | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [GeoObjectOrder](inputs.md#geoobjectorder)   | The ordering options for the returned geo objects.                                            |

**Returns:** [GeoObjectConnection!](objects.md#geoobjectconnection)

## Schedules

### scheduleTypes

Lists schedule types for an organization.

```graphql
scheduleTypes(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): ScheduleTypeConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve schedule types for.                                              |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned schedule types.                                            |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned schedule types.                                         |

**Returns:** [ScheduleTypeConnection!](objects.md#scheduletypeconnection)

### schedule

Retrieves a schedule by its ID.

```graphql
schedule(id: ID!): Schedule
```

**Arguments**

| Name | Type  | Description                         |
| ---- | ----- | ----------------------------------- |
| `id` | `ID!` | The ID of the schedule to retrieve. |

**Returns:** [Schedule](objects.md#schedule)

### schedules

Lists schedules for an organization.

```graphql
schedules(
  organizationId: ID!
  filter: ScheduleFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: ScheduleOrder = { field: TITLE, direction: ASC }
): ScheduleConnection!
```

**Arguments**

| Name             | Type                                       | Description                                                                                   |
| ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                      | The organization to retrieve schedules for.                                                   |
| `filter`         | [ScheduleFilter](inputs.md#schedulefilter) | Filtering options for the returned schedules.                                                 |
| `first`          | `Int`                                      | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                   | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                      | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                   | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [ScheduleOrder](inputs.md#scheduleorder)   | The ordering options for the returned schedules.                                              |

**Returns:** [ScheduleConnection!](objects.md#scheduleconnection)

## Organizations

### catalog

Retrieves a catalog by its ID.

```graphql
catalog(id: ID!): Catalog
```

**Arguments**

| Name | Type  | Description                        |
| ---- | ----- | ---------------------------------- |
| `id` | `ID!` | The ID of the catalog to retrieve. |

**Returns:** [Catalog](objects.md#catalog)

### catalogs

Lists catalogs for an organization.

```graphql
catalogs(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): CatalogConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve catalogs for.                                                    |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned catalogs.                                                  |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned catalogs.                                               |

**Returns:** [CatalogConnection!](objects.md#catalogconnection)

### organization

Retrieves an organization by its ID.

```graphql
organization(id: ID!): Organization
```

**Arguments**

| Name | Type  | Description                             |
| ---- | ----- | --------------------------------------- |
| `id` | `ID!` | The ID of the organization to retrieve. |

**Returns:** [Organization](objects.md#organization)

### organizations

Lists organizations.

```graphql
organizations(
  filter: OrganizationFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: OrganizationOrder = { field: TITLE, direction: ASC }
): OrganizationConnection!
```

**Arguments**

| Name      | Type                                               | Description                                                                                   |
| --------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `filter`  | [OrganizationFilter](inputs.md#organizationfilter) | Filtering options for the returned organizations.                                             |
| `first`   | `Int`                                              | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`   | `String`                                           | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`    | `Int`                                              | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`  | `String`                                           | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [OrganizationOrder](inputs.md#organizationorder)   | The ordering options for the returned organizations.                                          |

**Returns:** [OrganizationConnection!](objects.md#organizationconnection)

## Actors

### member

Retrieves a member by its ID.

```graphql
member(id: ID!): Member
```

**Arguments**

| Name | Type  | Description                       |
| ---- | ----- | --------------------------------- |
| `id` | `ID!` | The ID of the member to retrieve. |

**Returns:** [Member](objects.md#member)

### members

Lists members of an organization.

```graphql
members(
  organizationId: ID!
  filter: MemberFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: MemberOrder = { field: ASSIGNED_AT, direction: DESC }
): MemberConnection!
```

**Arguments**

| Name             | Type                                   | Description                                                                                   |
| ---------------- | -------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                  | The organization to retrieve members for.                                                     |
| `filter`         | [MemberFilter](inputs.md#memberfilter) | Filtering options for the returned members.                                                   |
| `first`          | `Int`                                  | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                               | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                  | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                               | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [MemberOrder](inputs.md#memberorder)   | The ordering options for the returned members.                                                |

**Returns:** [MemberConnection!](objects.md#memberconnection)

### integration

Retrieves an integration by its ID.

```graphql
integration(id: ID!): Integration
```

**Arguments**

| Name | Type  | Description                            |
| ---- | ----- | -------------------------------------- |
| `id` | `ID!` | The ID of the integration to retrieve. |

**Returns:** [Integration](objects.md#integration)

### integrations

Lists integrations for an organization.

```graphql
integrations(
  organizationId: ID!
  filter: IntegrationFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: IntegrationOrder = { field: TITLE, direction: ASC }
): IntegrationConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve integrations for.                                                |
| `filter`         | [IntegrationFilter](inputs.md#integrationfilter) | Filtering options for the returned integrations.                                              |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [IntegrationOrder](inputs.md#integrationorder)   | The ordering options for the returned integrations.                                           |

**Returns:** [IntegrationConnection!](objects.md#integrationconnection)

### actorRoles

Lists actor role assignments for an organization.

```graphql
actorRoles(
  organizationId: ID!
  filter: ActorRoleFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: ActorRoleOrder = { field: ASSIGNED_AT, direction: DESC }
): ActorRoleConnection!
```

**Arguments**

| Name             | Type                                         | Description                                                                                   |
| ---------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                        | The organization to retrieve actor roles for.                                                 |
| `filter`         | [ActorRoleFilter](inputs.md#actorrolefilter) | Filtering options for the returned actor roles.                                               |
| `first`          | `Int`                                        | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                     | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                        | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                     | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [ActorRoleOrder](inputs.md#actorroleorder)   | The ordering options for the returned actor roles.                                            |

**Returns:** [ActorRoleConnection!](objects.md#actorroleconnection)

### userScopes

Lists user scope restrictions for an organization.

```graphql
userScopes(
  organizationId: ID!
  filter: UserScopeFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: UserScopeOrder = { field: ID, direction: ASC }
): UserScopeConnection!
```

**Arguments**

| Name             | Type                                         | Description                                                                                   |
| ---------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                        | The organization to retrieve user scopes for.                                                 |
| `filter`         | [UserScopeFilter](inputs.md#userscopefilter) | Filtering options for the returned user scopes.                                               |
| `first`          | `Int`                                        | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                     | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                        | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                     | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [UserScopeOrder](inputs.md#userscopeorder)   | The ordering options for the returned user scopes.                                            |

**Returns:** [UserScopeConnection!](objects.md#userscopeconnection)

## Access control

### roles

Lists roles for an organization.

```graphql
roles(
  organizationId: ID!
  filter: CatalogItemFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: ORDER, direction: ASC }
): RoleConnection!
```

**Arguments**

| Name             | Type                                             | Description                                                                                   |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                            | The organization to retrieve roles for.                                                       |
| `filter`         | [CatalogItemFilter](inputs.md#catalogitemfilter) | Filtering options for the returned roles.                                                     |
| `first`          | `Int`                                            | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                         | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                            | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                         | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder)   | The ordering options for the returned roles.                                                  |

**Returns:** [RoleConnection!](objects.md#roleconnection)

### rolePermissions

Lists role permissions for an organization.

```graphql
rolePermissions(
  organizationId: ID!
  filter: RolePermissionFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: RolePermissionOrder = { field: GRANTED_AT, direction: DESC }
): RolePermissionConnection!
```

**Arguments**

| Name             | Type                                                   | Description                                                                                   |
| ---------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                                  | The organization to retrieve role permissions for.                                            |
| `filter`         | [RolePermissionFilter](inputs.md#rolepermissionfilter) | Filtering options for the returned role permissions.                                          |
| `first`          | `Int`                                                  | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                               | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                                  | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                               | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [RolePermissionOrder](inputs.md#rolepermissionorder)   | The ordering options for the returned role permissions.                                       |

**Returns:** [RolePermissionConnection!](objects.md#rolepermissionconnection)

## Inventory

### inventory

Retrieves an inventory by its ID.

```graphql
inventory(id: ID!): Inventory
```

**Arguments**

| Name | Type  | Description                          |
| ---- | ----- | ------------------------------------ |
| `id` | `ID!` | The ID of the inventory to retrieve. |

**Returns:** [Inventory](objects.md#inventory)

## Audit

### auditEvents

Lists audit events for an organization.

```graphql
auditEvents(
  organizationId: ID!
  filter: AuditEventFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AuditEventOrder = { field: OCCURRED_AT, direction: DESC }
): AuditEventConnection!
```

**Arguments**

| Name             | Type                                           | Description                                                                                   |
| ---------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                          | The organization to retrieve audit events for.                                                |
| `filter`         | [AuditEventFilter](inputs.md#auditeventfilter) | Filtering options for the returned audit events.                                              |
| `first`          | `Int`                                          | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                       | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                          | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                       | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [AuditEventOrder](inputs.md#auditeventorder)   | The ordering options for the returned audit events.                                           |

**Returns:** [AuditEventConnection!](objects.md#auditeventconnection)

## Catalog items

### tags

Lists tags for an organization.

```graphql
tags(
  organizationId: ID!
  filter: TagFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: CatalogItemOrder = { field: TITLE, direction: ASC }
): TagConnection!
```

**Arguments**

| Name             | Type                                           | Description                                                                                   |
| ---------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                          | The organization to retrieve tags for.                                                        |
| `filter`         | [TagFilter](inputs.md#tagfilter)               | Filtering options for the returned tags.                                                      |
| `first`          | `Int`                                          | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                       | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                          | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                       | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](inputs.md#catalogitemorder) | The ordering options for the returned tags.                                                   |

**Returns:** [TagConnection!](objects.md#tagconnection)

### inventories

Lists inventories for an organization.

```graphql
inventories(
  organizationId: ID!
  filter: InventoryFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: InventoryOrder = { field: TITLE, direction: ASC }
): InventoryConnection!
```

**Arguments**

| Name             | Type                                         | Description                                                                                   |
| ---------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                        | The organization to retrieve inventories for.                                                 |
| `filter`         | [InventoryFilter](inputs.md#inventoryfilter) | Filtering options for the returned inventories.                                               |
| `first`          | `Int`                                        | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                     | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                        | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                     | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [InventoryOrder](inputs.md#inventoryorder)   | The ordering options for the returned inventories.                                            |

**Returns:** [InventoryConnection!](objects.md#inventoryconnection)

### entityHistory

Retrieves the change history for any entity.

```graphql
entityHistory(
  entityId: ID!
  filter: AuditEventFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AuditEventOrder = { field: OCCURRED_AT, direction: DESC }
): AuditEventConnection!
```

**Arguments**

| Name       | Type                                           | Description                                                                                   |
| ---------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `entityId` | `ID!`                                          | The ID of the entity to retrieve history for.                                                 |
| `filter`   | [AuditEventFilter](inputs.md#auditeventfilter) | Filtering options for the returned audit events.                                              |
| `first`    | `Int`                                          | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`    | `String`                                       | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`     | `Int`                                          | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`   | `String`                                       | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`  | [AuditEventOrder](inputs.md#auditeventorder)   | The ordering options for the returned audit events.                                           |

**Returns:** [AuditEventConnection!](objects.md#auditeventconnection)
