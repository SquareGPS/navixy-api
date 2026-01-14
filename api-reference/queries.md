# Queries

Queries retrieve data from the Navixy database without modifying it.

{% hint style="info" %}
**Input types:** Query arguments like filters and ordering use dedicated input types (e.g., `DeviceFilter`). For convenience, input type fields are expanded inline below each query rather than on a separate page.
{% endhint %}

{% hint style="warning" %}
**Pagination:** List queries return paginated results using the [Relay Cursor Connections](https://relay.dev/graphql/connections.htm) pattern. See the [Pagination guide](../pagination.md) for details on navigating large result sets.
{% endhint %}

## General

### node

Retrieves any entity by its globally unique identifier.

```graphql
node(id: ID!): Node
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the entity to retrieve. |

**Returns:** [Node](/api-reference/interfaces.md#node/)

### nodes

Retrieves multiple entities by their globally unique identifiers. Returns items in the same order as the input IDs.

```graphql
nodes(ids: [ID!]!): [Node]!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `ids` | `[ID!]!` | The IDs of the entities to retrieve. |

**Returns:** [[Node]!](/api-reference/interfaces.md#node/)

### me

Retrieves the currently authenticated actor.

```graphql
me: Actor!
```

**Returns:** [Actor!](/api-reference/interfaces.md#actor/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve device types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned device types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned device types. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [DeviceTypeConnection!](/api-reference/objects.md#devicetypeconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve device statuses for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned device statuses. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned device statuses. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [DeviceStatusConnection!](/api-reference/objects.md#devicestatusconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve device models for. |
| `filter` | `DeviceModelFilter` | Filtering options for the returned device models. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned device models. |

**DeviceModelFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `code` | [Code](/api-reference/scalars.md#code/) | Exact code match. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [DeviceModelConnection!](/api-reference/objects.md#devicemodelconnection/)

### device

Retrieves a device by its ID.

```graphql
device(id: ID!): Device
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the device to retrieve. |

**Returns:** [Device](/api-reference/objects.md#device/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve devices for. |
| `filter` | `DeviceFilter` | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder` | The ordering options for the returned devices. |

**DeviceFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by device types (OR within field). |
| `modelIds` | `[ID!]` | Filter by device models (OR within field). |
| `statusIds` | `[ID!]` | Filter by statuses (OR within field). |
| `vendorIds` | `[ID!]` | Filter by vendors (OR within field). |
| `identifierValue` | `String` | Search by device identifier value. |
| `inventoryIds` | `[ID!]` | Filter by inventories (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | `[CustomFieldFilter!]` | Filter by custom field values. |

**DeviceOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceOrderField](/api-reference/enums.md#deviceorderfield/) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code/) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [DeviceConnection!](/api-reference/objects.md#deviceconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve asset types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned asset types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned asset types. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [AssetTypeConnection!](/api-reference/objects.md#assettypeconnection/)

### asset

Retrieves an asset by its ID.

```graphql
asset(id: ID!): Asset
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the asset to retrieve. |

**Returns:** [Asset](/api-reference/objects.md#asset/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve assets for. |
| `filter` | `AssetFilter` | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder` | The ordering options for the returned assets. |

**AssetFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by asset types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | `[CustomFieldFilter!]` | Filter by custom field values. |

**AssetOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetOrderField](/api-reference/enums.md#assetorderfield/) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code/) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [AssetConnection!](/api-reference/objects.md#assetconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve asset group types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned asset group types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned asset group types. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [AssetGroupTypeConnection!](/api-reference/objects.md#assetgrouptypeconnection/)

### assetGroup

Retrieves an asset group by its ID.

```graphql
assetGroup(id: ID!): AssetGroup
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the asset group to retrieve. |

**Returns:** [AssetGroup](/api-reference/objects.md#assetgroup/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve asset groups for. |
| `filter` | `AssetGroupFilter` | Filtering options for the returned asset groups. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetGroupOrder` | The ordering options for the returned asset groups. |

**AssetGroupFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by group types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |

**AssetGroupOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AssetGroupOrderField!](/api-reference/enums.md#assetgrouporderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [AssetGroupConnection!](/api-reference/objects.md#assetgroupconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve geo object types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned geo object types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned geo object types. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [GeoObjectTypeConnection!](/api-reference/objects.md#geoobjecttypeconnection/)

### geoObject

Retrieves a geo object by its ID.

```graphql
geoObject(id: ID!): GeoObject
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the geo object to retrieve. |

**Returns:** [GeoObject](/api-reference/objects.md#geoobject/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve geo objects for. |
| `filter` | `GeoObjectFilter` | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder` | The ordering options for the returned geo objects. |

**GeoObjectFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by geo object types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | `[CustomFieldFilter!]` | Filter by custom field values. |

**GeoObjectOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [GeoObjectOrderField](/api-reference/enums.md#geoobjectorderfield/) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code/) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [GeoObjectConnection!](/api-reference/objects.md#geoobjectconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve schedule types for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned schedule types. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned schedule types. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [ScheduleTypeConnection!](/api-reference/objects.md#scheduletypeconnection/)

### schedule

Retrieves a schedule by its ID.

```graphql
schedule(id: ID!): Schedule
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the schedule to retrieve. |

**Returns:** [Schedule](/api-reference/objects.md#schedule/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve schedules for. |
| `filter` | `ScheduleFilter` | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder` | The ordering options for the returned schedules. |

**ScheduleFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by schedule types (OR within field). |
| `title` | `String` | Search in title (case-insensitive contains). |
| `customFields` | `[CustomFieldFilter!]` | Filter by custom field values. |

**ScheduleOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ScheduleOrderField](/api-reference/enums.md#scheduleorderfield/) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](/api-reference/scalars.md#code/) | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [ScheduleConnection!](/api-reference/objects.md#scheduleconnection/)

## Organizations

### catalog

Retrieves a catalog by its ID.

```graphql
catalog(id: ID!): Catalog
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the catalog to retrieve. |

**Returns:** [Catalog](/api-reference/objects.md#catalog/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve catalogs for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned catalogs. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned catalogs. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [CatalogConnection!](/api-reference/objects.md#catalogconnection/)

### organization

Retrieves an organization by its ID.

```graphql
organization(id: ID!): Organization
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the organization to retrieve. |

**Returns:** [Organization](/api-reference/objects.md#organization/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `filter` | `OrganizationFilter` | Filtering options for the returned organizations. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder` | The ordering options for the returned organizations. |

**OrganizationFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentIds` | `[ID!]` | Filter by parent organizations (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

**OrganizationOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [OrganizationOrderField!](/api-reference/enums.md#organizationorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [OrganizationConnection!](/api-reference/objects.md#organizationconnection/)

## Actors

### member

Retrieves a member by its ID.

```graphql
member(id: ID!): Member
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the member to retrieve. |

**Returns:** [Member](/api-reference/objects.md#member/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve members for. |
| `filter` | `MemberFilter` | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder` | The ordering options for the returned members. |

**MemberFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `userIds` | `[ID!]` | Filter by users (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

**MemberOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [MemberOrderField!](/api-reference/enums.md#memberorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [MemberConnection!](/api-reference/objects.md#memberconnection/)

### integration

Retrieves an integration by its ID.

```graphql
integration(id: ID!): Integration
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the integration to retrieve. |

**Returns:** [Integration](/api-reference/objects.md#integration/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve integrations for. |
| `filter` | `IntegrationFilter` | Filtering options for the returned integrations. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `IntegrationOrder` | The ordering options for the returned integrations. |

**IntegrationFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |

**IntegrationOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [IntegrationOrderField!](/api-reference/enums.md#integrationorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [IntegrationConnection!](/api-reference/objects.md#integrationconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve actor roles for. |
| `filter` | `ActorRoleFilter` | Filtering options for the returned actor roles. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ActorRoleOrder` | The ordering options for the returned actor roles. |

**ActorRoleFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `includeExpired` | `Boolean` | Include expired role assignments. |

**ActorRoleOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ActorRoleOrderField!](/api-reference/enums.md#actorroleorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [ActorRoleConnection!](/api-reference/objects.md#actorroleconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve user scopes for. |
| `filter` | `UserScopeFilter` | Filtering options for the returned user scopes. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `UserScopeOrder` | The ordering options for the returned user scopes. |

**UserScopeFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

**UserScopeOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [UserScopeOrderField!](/api-reference/enums.md#userscopeorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [UserScopeConnection!](/api-reference/objects.md#userscopeconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve roles for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned roles. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned roles. |

**CatalogItemFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `codes` | [[Code!]](/api-reference/scalars.md#code/) | Match any of these codes. |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [RoleConnection!](/api-reference/objects.md#roleconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve role permissions for. |
| `filter` | `RolePermissionFilter` | Filtering options for the returned role permissions. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `RolePermissionOrder` | The ordering options for the returned role permissions. |

**RolePermissionFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `roleIds` | `[ID!]` | Filter by roles (OR within field). |
| `permissionScopeIds` | `[ID!]` | Filter by permission scopes (OR within field). |
| `targetEntityIds` | `[ID!]` | Filter by target entities (OR within field). |

**RolePermissionOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [RolePermissionOrderField!](/api-reference/enums.md#rolepermissionorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [RolePermissionConnection!](/api-reference/objects.md#rolepermissionconnection/)

## Inventory

### inventory

Retrieves an inventory by its ID.

```graphql
inventory(id: ID!): Inventory
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the inventory to retrieve. |

**Returns:** [Inventory](/api-reference/objects.md#inventory/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve audit events for. |
| `filter` | `AuditEventFilter` | Filtering options for the returned audit events. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AuditEventOrder` | The ordering options for the returned audit events. |

**AuditEventFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `aggregateTypes` | [[Code!]](/api-reference/scalars.md#code/) | Filter by entity types (OR within field). |
| `aggregateIds` | `[ID!]` | Filter by specific entity IDs (OR within field). |
| `eventTypes` | [[AuditEventType!]](/api-reference/enums.md#auditeventtype/) | Filter by event types (OR within field). |
| `sourceTypes` | [[SourceType!]](/api-reference/enums.md#sourcetype/) | Filter by source types (OR within field). |
| `traceId` | `String` | Filter by trace ID. |
| `from` | [DateTime](/api-reference/scalars.md#datetime/) | Return events that occurred after this timestamp. |
| `to` | [DateTime](/api-reference/scalars.md#datetime/) | Return events that occurred before this timestamp. |

**AuditEventOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AuditEventOrderField!](/api-reference/enums.md#auditeventorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [AuditEventConnection!](/api-reference/objects.md#auditeventconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve tags for. |
| `filter` | `TagFilter` | Filtering options for the returned tags. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned tags. |

**TagFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |

**CatalogItemOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField!](/api-reference/enums.md#catalogitemorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [TagConnection!](/api-reference/objects.md#tagconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve inventories for. |
| `filter` | `InventoryFilter` | Filtering options for the returned inventories. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `InventoryOrder` | The ordering options for the returned inventories. |

**InventoryFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String` | Search in title (case-insensitive contains). |
| `code` | [Code](/api-reference/scalars.md#code/) | Exact code match. |

**InventoryOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [InventoryOrderField!](/api-reference/enums.md#inventoryorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [InventoryConnection!](/api-reference/objects.md#inventoryconnection/)

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `entityId` | `ID!` | The ID of the entity to retrieve history for. |
| `filter` | `AuditEventFilter` | Filtering options for the returned audit events. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AuditEventOrder` | The ordering options for the returned audit events. |

**AuditEventFilter** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `aggregateTypes` | [[Code!]](/api-reference/scalars.md#code/) | Filter by entity types (OR within field). |
| `aggregateIds` | `[ID!]` | Filter by specific entity IDs (OR within field). |
| `eventTypes` | [[AuditEventType!]](/api-reference/enums.md#auditeventtype/) | Filter by event types (OR within field). |
| `sourceTypes` | [[SourceType!]](/api-reference/enums.md#sourcetype/) | Filter by source types (OR within field). |
| `traceId` | `String` | Filter by trace ID. |
| `from` | [DateTime](/api-reference/scalars.md#datetime/) | Return events that occurred after this timestamp. |
| `to` | [DateTime](/api-reference/scalars.md#datetime/) | Return events that occurred before this timestamp. |

**AuditEventOrder** (input type)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AuditEventOrderField!](/api-reference/enums.md#auditeventorderfield/) | The field to order by. |
| `direction` | [OrderDirection!](/api-reference/enums.md#orderdirection/) | The direction to order. |

**Returns:** [AuditEventConnection!](/api-reference/objects.md#auditeventconnection/)
