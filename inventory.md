# Inventory

Inventory management for tracking device assignments and stock.

## Queries

### inventory

Retrieves an inventory by its ID.

```graphql
inventory(id: ID!): Inventory
```

**Arguments**

| Name | Type  | Description                          |
| ---- | ----- | ------------------------------------ |
| `id` | `ID!` | The ID of the inventory to retrieve. |

**Output types:**

<details>

<summary><code>Inventory</code></summary>

| Field          | Type                                                            | Description                                |
| -------------- | --------------------------------------------------------------- | ------------------------------------------ |
| `id`           | `ID!`                                                           |                                            |
| `version`      | `Int!`                                                          |                                            |
| `title`        | `String!`                                                       |                                            |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this inventory. |
| `devices`      | [DeviceConnection](devices/types.md#deviceconnection)!          | The devices assigned to this inventory.    |

</details>

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

| Name             | Type                                            | Description                                                                                   |
| ---------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                           | The organization to retrieve inventories for.                                                 |
| `filter`         | [InventoryFilter](inventory.md#inventoryfilter) | Filtering options for the returned inventories.                                               |
| `first`          | `Int`                                           | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                        | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                           | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                        | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [InventoryOrder](inventory.md#inventoryorder)   | The ordering options for the returned inventories.                                            |

**Input types:**

<details>

<summary><code>InventoryFilter</code></summary>

| Field           | Type     | Description                                         |
| --------------- | -------- | --------------------------------------------------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary><code>InventoryOrder</code></summary>

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [InventoryOrderField](inventory.md#inventoryorderfield)!                 | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>InventoryConnection</code></summary>

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[InventoryEdge](inventory.md#inventoryedge)!]!              | A list of edges.                                           |
| `nodes`    | \[[Inventory](inventory.md#inventory)!]!                      | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Inventory (node)</code></summary>

| Field          | Type                                                            | Description                                |
| -------------- | --------------------------------------------------------------- | ------------------------------------------ |
| `id`           | `ID!`                                                           |                                            |
| `version`      | `Int!`                                                          |                                            |
| `title`        | `String!`                                                       |                                            |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this inventory. |
| `devices`      | [DeviceConnection](devices/types.md#deviceconnection)!          | The devices assigned to this inventory.    |

</details>

## Mutations

### inventoryCreate

Creates a new inventory.

```graphql
inventoryCreate(
  input: InventoryCreateInput!
): InventoryPayload
```

**Arguments**

| Name    | Type                                                       | Description                                  |
| ------- | ---------------------------------------------------------- | -------------------------------------------- |
| `input` | [InventoryCreateInput](inventory.md#inventorycreateinput)! | The input fields for creating the inventory. |

**Input types:**

<details>

<summary><code>InventoryCreateInput</code></summary>

| Field            | Type      | Description                                   |
| ---------------- | --------- | --------------------------------------------- |
| `organizationId` | `ID!`     | The organization that will own the inventory. |
| `title`          | `String!` | The display name.                             |

</details>

**Output types:**

<details>

<summary><code>InventoryPayload</code></summary>

| Field       | Type                                 | Description                       |
| ----------- | ------------------------------------ | --------------------------------- |
| `inventory` | [Inventory](inventory.md#inventory)! | The created or updated inventory. |

</details>

<details>

<summary><code>Inventory (entity)</code></summary>

| Field          | Type                                                            | Description                                |
| -------------- | --------------------------------------------------------------- | ------------------------------------------ |
| `id`           | `ID!`                                                           |                                            |
| `version`      | `Int!`                                                          |                                            |
| `title`        | `String!`                                                       |                                            |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this inventory. |
| `devices`      | [DeviceConnection](devices/types.md#deviceconnection)!          | The devices assigned to this inventory.    |

</details>

### inventoryUpdate

Updates an existing inventory.

```graphql
inventoryUpdate(
  input: InventoryUpdateInput!
): InventoryPayload
```

**Arguments**

| Name    | Type                                                       | Description                                  |
| ------- | ---------------------------------------------------------- | -------------------------------------------- |
| `input` | [InventoryUpdateInput](inventory.md#inventoryupdateinput)! | The input fields for updating the inventory. |

**Input types:**

<details>

<summary><code>InventoryUpdateInput</code></summary>

| Field     | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `id`      | `ID!`    | The inventory ID to update.                 |
| `version` | `Int!`   | The current version for optimistic locking. |
| `title`   | `String` | The new display name.                       |

</details>

**Output types:**

<details>

<summary><code>InventoryPayload</code></summary>

| Field       | Type                                 | Description                       |
| ----------- | ------------------------------------ | --------------------------------- |
| `inventory` | [Inventory](inventory.md#inventory)! | The created or updated inventory. |

</details>

<details>

<summary><code>Inventory (entity)</code></summary>

| Field          | Type                                                            | Description                                |
| -------------- | --------------------------------------------------------------- | ------------------------------------------ |
| `id`           | `ID!`                                                           |                                            |
| `version`      | `Int!`                                                          |                                            |
| `title`        | `String!`                                                       |                                            |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this inventory. |
| `devices`      | [DeviceConnection](devices/types.md#deviceconnection)!          | The devices assigned to this inventory.    |

</details>

### inventoryDelete

Deletes an inventory.

```graphql
inventoryDelete(
  input: InventoryDeleteInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                       | Description                                  |
| ------- | ---------------------------------------------------------- | -------------------------------------------- |
| `input` | [InventoryDeleteInput](inventory.md#inventorydeleteinput)! | The input fields for deleting the inventory. |

**Input types:**

<details>

<summary><code>InventoryDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The inventory ID to delete.                 |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

### deviceInventoryLink

Links a device to an inventory.

```graphql
deviceInventoryLink(
  input: DeviceInventoryLinkInput!
): DeviceInventoryRelationPayload
```

**Arguments**

| Name    | Type                                                               | Description                              |
| ------- | ------------------------------------------------------------------ | ---------------------------------------- |
| `input` | [DeviceInventoryLinkInput](inventory.md#deviceinventorylinkinput)! | The input fields for linking the device. |

**Input types:**

<details>

<summary><code>DeviceInventoryLinkInput</code></summary>

| Field         | Type  | Description                                                       |
| ------------- | ----- | ----------------------------------------------------------------- |
| `deviceId`    | `ID!` | The device ID.                                                    |
| `inventoryId` | `ID!` | The inventory ID. Must be in the same organization as the device. |

</details>

**Output types:**

<details>

<summary><code>DeviceInventoryRelationPayload</code></summary>

| Field                     | Type                                                             | Description                       |
| ------------------------- | ---------------------------------------------------------------- | --------------------------------- |
| `deviceInventoryRelation` | [DeviceInventoryRelation](inventory.md#deviceinventoryrelation)! | The created inventory assignment. |

</details>

<details>

<summary><code>DeviceInventoryRelation (entity)</code></summary>

| Field        | Type                                                         | Description                                     |
| ------------ | ------------------------------------------------------------ | ----------------------------------------------- |
| `id`         | `ID!`                                                        |                                                 |
| `device`     | [Device](devices/types.md#device)!                           | The device that was assigned.                   |
| `inventory`  | [Inventory](inventory.md#inventory)!                         | The inventory the device was assigned to.       |
| `assignedAt` | [DateTime](core-api-reference/common-resources.md#datetime)! | The date and time when the device was assigned. |
| `assignedBy` | [Actor](access-control/types.md#actor)                       | The actor who assigned the device.              |

</details>

### deviceInventoryUnlink

Unlinks a device from an inventory.

```graphql
deviceInventoryUnlink(
  input: DeviceInventoryUnlinkInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                                   | Description                                |
| ------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| `input` | [DeviceInventoryUnlinkInput](inventory.md#deviceinventoryunlinkinput)! | The input fields for unlinking the device. |

**Input types:**

<details>

<summary><code>DeviceInventoryUnlinkInput</code></summary>

| Field      | Type  | Description              |
| ---------- | ----- | ------------------------ |
| `deviceId` | `ID!` | The device ID to unlink. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

## Types

### InventoryConnection

A paginated list of Inventory items.

**Implements:** [`Connection`](core-api-reference/common-resources.md#connection)

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[InventoryEdge](inventory.md#inventoryedge)!]!              | A list of edges.                                           |
| `nodes`    | \[[Inventory](inventory.md#inventory)!]!                      | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### InventoryEdge

An edge in the Inventory connection.

**Implements:** [`Edge`](core-api-reference/common-resources.md#edge)

| Field    | Type                                 | Description                           |
| -------- | ------------------------------------ | ------------------------------------- |
| `cursor` | `String!`                            | An opaque cursor for this edge.       |
| `node`   | [Inventory](inventory.md#inventory)! | The inventory at the end of the edge. |

### DeviceInventoryRelationConnection

A paginated list of DeviceInventoryRelation items.

**Implements:** [`Connection`](core-api-reference/common-resources.md#connection)

| Field      | Type                                                                         | Description                                                |
| ---------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceInventoryRelationEdge](inventory.md#deviceinventoryrelationedge)!]! | A list of edges.                                           |
| `nodes`    | \[[DeviceInventoryRelation](inventory.md#deviceinventoryrelation)!]!         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!                 | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo)                | The total count of items matching the filter.              |

### DeviceInventoryRelationEdge

An edge in the DeviceInventoryRelation connection.

**Implements:** [`Edge`](core-api-reference/common-resources.md#edge)

| Field    | Type                                                             | Description                                           |
| -------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| `cursor` | `String!`                                                        | An opaque cursor for this edge.                       |
| `node`   | [DeviceInventoryRelation](inventory.md#deviceinventoryrelation)! | The device inventory relation at the end of the edge. |

### DeviceInventoryRelation

A record of a device's assignment to an inventory.

**Implements:** [`Node`](core-api-reference/common-resources.md#node)

| Field        | Type                                                         | Description                                     |
| ------------ | ------------------------------------------------------------ | ----------------------------------------------- |
| `id`         | `ID!`                                                        |                                                 |
| `device`     | [Device](devices/types.md#device)!                           | The device that was assigned.                   |
| `inventory`  | [Inventory](inventory.md#inventory)!                         | The inventory the device was assigned to.       |
| `assignedAt` | [DateTime](core-api-reference/common-resources.md#datetime)! | The date and time when the device was assigned. |
| `assignedBy` | [Actor](access-control/types.md#actor)                       | The actor who assigned the device.              |

### Inventory

An inventory or warehouse record for device stock management.

**Implements:** [`Node`](core-api-reference/common-resources.md#node), [`Versioned`](core-api-reference/common-resources.md#versioned), [`Titled`](core-api-reference/common-resources.md#titled)

| Field          | Type                                                            | Description                                |
| -------------- | --------------------------------------------------------------- | ------------------------------------------ |
| `id`           | `ID!`                                                           |                                            |
| `version`      | `Int!`                                                          |                                            |
| `title`        | `String!`                                                       |                                            |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this inventory. |
| `devices`      | [DeviceConnection](devices/types.md#deviceconnection)!          | The devices assigned to this inventory.    |

### InventoryPayload

The result of an inventory mutation.

| Field       | Type                                 | Description                       |
| ----------- | ------------------------------------ | --------------------------------- |
| `inventory` | [Inventory](inventory.md#inventory)! | The created or updated inventory. |

### DeviceInventoryRelationPayload

The result of a device inventory link mutation.

| Field                     | Type                                                             | Description                       |
| ------------------------- | ---------------------------------------------------------------- | --------------------------------- |
| `deviceInventoryRelation` | [DeviceInventoryRelation](inventory.md#deviceinventoryrelation)! | The created inventory assignment. |

## Inputs

### DeviceInventoryRelationOrder

Ordering options for device inventory relations.

| Field       | Type                                                                                 | Description             |
| ----------- | ------------------------------------------------------------------------------------ | ----------------------- |
| `field`     | [DeviceInventoryRelationOrderField](inventory.md#deviceinventoryrelationorderfield)! | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)!             | The direction to order. |

### InventoryFilter

Filtering options for inventories.

| Field           | Type     | Description                                         |
| --------------- | -------- | --------------------------------------------------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

### InventoryOrder

Ordering options for inventories.

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [InventoryOrderField](inventory.md#inventoryorderfield)!                 | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

### InventoryCreateInput

Input for creating a new inventory.

| Field            | Type      | Description                                   |
| ---------------- | --------- | --------------------------------------------- |
| `organizationId` | `ID!`     | The organization that will own the inventory. |
| `title`          | `String!` | The display name.                             |

### InventoryUpdateInput

Input for updating an existing inventory.

| Field     | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `id`      | `ID!`    | The inventory ID to update.                 |
| `version` | `Int!`   | The current version for optimistic locking. |
| `title`   | `String` | The new display name.                       |

### InventoryDeleteInput

Input for deleting an inventory.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The inventory ID to delete.                 |
| `version` | `Int!` | The current version for optimistic locking. |

### DeviceInventoryLinkInput

Input for linking a device to an inventory. Both device and inventory must belong to the same organization.

| Field         | Type  | Description                                                       |
| ------------- | ----- | ----------------------------------------------------------------- |
| `deviceId`    | `ID!` | The device ID.                                                    |
| `inventoryId` | `ID!` | The inventory ID. Must be in the same organization as the device. |

### DeviceInventoryUnlinkInput

Input for unlinking a device from an inventory.

| Field      | Type  | Description              |
| ---------- | ----- | ------------------------ |
| `deviceId` | `ID!` | The device ID to unlink. |

## Enums

### DeviceInventoryRelationOrderField

Fields available for ordering device inventory relations.

| Value         | Description               |
| ------------- | ------------------------- |
| `ASSIGNED_AT` | Order by assignment date. |

### InventoryOrderField

Fields available for ordering inventories.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |

## Interfaces

### InventoryItem

An object that can be assigned to an inventory.

| Field       | Type                                | Description                                       |
| ----------- | ----------------------------------- | ------------------------------------------------- |
| `id`        | `ID!`                               | A globally unique identifier.                     |
| `inventory` | [Inventory](inventory.md#inventory) | The inventory this item is currently assigned to. |
