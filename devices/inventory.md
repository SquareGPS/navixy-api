# Inventory

Inventory management for device stock, including warehouses, assignments, and device-inventory relationships.

## Queries

### inventory

Retrieves an inventory by its ID.

```graphql
inventory(id: ID!): Inventory
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the inventory to retrieve. |

**Output types:**

<details>

<summary>Inventory</summary>

An inventory or warehouse record for device stock management.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization that owns this inventory. |
| `filter` | [DeviceFilter](../types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](../../organizations/members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](../../schedules/types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

</details>

---

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
| `organizationId` | `ID!` |  |
| `filter` | `InventoryFilter` |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | `InventoryOrder` |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary>InventoryFilter</summary>

Filtering options for inventories.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary>InventoryOrder</summary>

Ordering options for inventories.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [InventoryOrderField](../inventory.md#inventoryorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>InventoryConnection</summary>

A paginated list of Inventory items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[InventoryEdge](../inventory.md#inventoryedge)!]! | A list of edges. |
| `nodes` | [[Inventory](../inventory.md#inventory)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary>PageInfo (entity)</summary>

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

</details>

---

## Mutations

### inventoryCreate

Creates a new inventory.

```graphql
inventoryCreate(input: InventoryCreateInput!): InventoryPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `InventoryCreateInput!` | The input fields for creating the inventory. |

**Input types:**

<details>

<summary>InventoryCreateInput</summary>

Input for creating a new inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the inventory. |
| `title` | `String!` | The display name. |

</details>

**Output types:**

<details>

<summary>InventoryPayload</summary>

The result of an inventory mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `inventory` | [Inventory](../inventory.md#inventory)! | The created or updated inventory. |

</details>

<details>

<summary>Inventory (entity)</summary>

An inventory or warehouse record for device stock management.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization that owns this inventory. |
| `filter` | [DeviceFilter](../types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |

</details>

---

### inventoryUpdate

Updates an existing inventory.

```graphql
inventoryUpdate(input: InventoryUpdateInput!): InventoryPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `InventoryUpdateInput!` | The input fields for updating the inventory. |

**Input types:**

<details>

<summary>InventoryUpdateInput</summary>

Input for updating an existing inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |

</details>

**Output types:**

<details>

<summary>InventoryPayload</summary>

The result of an inventory mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `inventory` | [Inventory](../inventory.md#inventory)! | The created or updated inventory. |

</details>

<details>

<summary>Inventory (entity)</summary>

An inventory or warehouse record for device stock management.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization that owns this inventory. |
| `filter` | [DeviceFilter](../types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |

</details>

---

### inventoryDelete

Deletes an inventory.

```graphql
inventoryDelete(input: InventoryDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `InventoryDeleteInput!` | The input fields for deleting the inventory. |

**Input types:**

<details>

<summary>InventoryDeleteInput</summary>

Input for deleting an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary>DeletePayload</summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

### deviceInventoryLink

Links a device to an inventory.

```graphql
deviceInventoryLink(input: DeviceInventoryLinkInput!): DeviceInventoryRelationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceInventoryLinkInput!` | The input fields for linking the device. |

**Input types:**

<details>

<summary>DeviceInventoryLinkInput</summary>

Input for linking a device to an inventory. Both device and inventory must belong to the same organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `inventoryId` | `ID!` | The inventory ID. Must be in the same organization as the device. |

</details>

**Output types:**

<details>

<summary>DeviceInventoryRelationPayload</summary>

The result of a device inventory link mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceInventoryRelation` | [DeviceInventoryRelation](../inventory.md#deviceinventoryrelation)! | The created inventory assignment. |

</details>

<details>

<summary>DeviceInventoryRelation (entity)</summary>

A record of a device's assignment to an inventory.

**Implements:** [Node](../../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `device` | [Device](../types.md#device)! | The device that was assigned. |
| `inventory` | [Inventory](../inventory.md#inventory)! | The inventory the device was assigned to. |
| `assignedAt` | `DateTime!` | The date and time when the device was assigned. |
| `assignedBy` | [Actor](../../actors.md#actor) | The actor who assigned the device. |

</details>

---

### deviceInventoryUnlink

Unlinks a device from an inventory.

```graphql
deviceInventoryUnlink(input: DeviceInventoryUnlinkInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `DeviceInventoryUnlinkInput!` | The input fields for unlinking the device. |

**Input types:**

<details>

<summary>DeviceInventoryUnlinkInput</summary>

Input for unlinking a device from an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID to unlink. |

</details>

**Output types:**

<details>

<summary>DeletePayload</summary>

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

---

## Objects

### DeviceInventoryRelation

A record of a device's assignment to an inventory.

**Implements:** [Node](../../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `device` | [Device](../types.md#device)! | The device that was assigned. |
| `inventory` | [Inventory](../inventory.md#inventory)! | The inventory the device was assigned to. |
| `assignedAt` | `DateTime!` | The date and time when the device was assigned. |
| `assignedBy` | [Actor](../../actors.md#actor) | The actor who assigned the device. |

---

### Inventory

An inventory or warehouse record for device stock management.

**Implements:** [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../../organizations.md#organization)! | The organization that owns this inventory. |
| `filter` | [DeviceFilter](../types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |

---

### InventoryPayload

The result of an inventory mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `inventory` | [Inventory](../inventory.md#inventory)! | The created or updated inventory. |

---

### DeviceInventoryRelationPayload

The result of a device inventory link mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceInventoryRelation` | [DeviceInventoryRelation](../inventory.md#deviceinventoryrelation)! | The created inventory assignment. |

---

## Inputs

### DeviceInventoryRelationOrder

Ordering options for device inventory relations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [DeviceInventoryRelationOrderField](../inventory.md#deviceinventoryrelationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### InventoryFilter

Filtering options for inventories.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

### InventoryOrder

Ordering options for inventories.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [InventoryOrderField](../inventory.md#inventoryorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### InventoryCreateInput

Input for creating a new inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the inventory. |
| `title` | `String!` | The display name. |

---

### InventoryUpdateInput

Input for updating an existing inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |

---

### InventoryDeleteInput

Input for deleting an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The inventory ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### DeviceInventoryLinkInput

Input for linking a device to an inventory. Both device and inventory must belong to the same organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID. |
| `inventoryId` | `ID!` | The inventory ID. Must be in the same organization as the device. |

---

### DeviceInventoryUnlinkInput

Input for unlinking a device from an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deviceId` | `ID!` | The device ID to unlink. |

---

## Enums

### DeviceInventoryRelationOrderField

Fields available for ordering device inventory relations.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

---

### InventoryOrderField

Fields available for ordering inventories.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Interfaces

### InventoryItem

An object that can be assigned to an inventory.

**Implements:** [Node](../../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `inventory` | [Inventory](../inventory.md#inventory) | The inventory this item is currently assigned to. |

---

## Pagination types

### InventoryConnection

A paginated list of Inventory items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[InventoryEdge](../inventory.md#inventoryedge)!]! | A list of edges. |
| `nodes` | [[Inventory](../inventory.md#inventory)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### InventoryEdge

An edge in the Inventory connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Inventory](../inventory.md#inventory)! | The inventory at the end of the edge. |

---

### DeviceInventoryRelationConnection

A paginated list of DeviceInventoryRelation items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceInventoryRelationEdge](../inventory.md#deviceinventoryrelationedge)!]! | A list of edges. |
| `nodes` | [[DeviceInventoryRelation](../inventory.md#deviceinventoryrelation)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### DeviceInventoryRelationEdge

An edge in the DeviceInventoryRelation connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [DeviceInventoryRelation](../inventory.md#deviceinventoryrelation)! | The device inventory relation at the end of the edge. |

---
