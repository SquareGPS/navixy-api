# Queries

### device

Retrieves a device by its ID.

```graphql
device(id: ID!): Device
```

**Arguments**

| Name | Type  | Description                       |
| ---- | ----- | --------------------------------- |
| `id` | `ID!` | The ID of the device to retrieve. |

**Output types:**

<details>

<summary><code>Device</code></summary>

| Field              | Type                                                                                    | Description                                                                        |
| ------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`               | `ID!`                                                                                   |                                                                                    |
| `version`          | `Int!`                                                                                  |                                                                                    |
| `title`            | `String!`                                                                               |                                                                                    |
| `organization`     | [Organization](../core-api-reference/organizations/#organization)!                      | The organization that owns this device.                                            |
| `type`             | [DeviceType](../catalogs/device/types.md#devicetype)!                                   | The device type classification.                                                    |
| `model`            | [DeviceModel](../catalogs/device/types.md#devicemodel)!                                 | The specific device model.                                                         |
| `status`           | [DeviceStatus](../catalogs/device/types.md#devicestatus)!                               | The current operational status.                                                    |
| `customFields`     | [JSON](../core-api-reference/common-resources.md#json)!                                 |                                                                                    |
| `identifiers`      | \[[DeviceIdentifier](types.md#deviceidentifier)!]!                                      | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory`        | [Inventory](../inventory.md#inventory)                                                  | The inventory this device is currently assigned to.                                |
| `relationsFrom`    | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The outgoing relationships from this device to other devices.                      |
| `relationsTo`      | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The incoming relationships from other devices to this device.                      |
| `inventoryHistory` | [DeviceInventoryRelationConnection](../inventory.md#deviceinventoryrelationconnection)! | The history of inventory assignments for this device.                              |

</details>

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

| Name             | Type                                  | Description                                                                                   |
| ---------------- | ------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                 | The organization to retrieve devices for.                                                     |
| `filter`         | [DeviceFilter](types.md#devicefilter) | Filtering options for the returned devices.                                                   |
| `first`          | `Int`                                 | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                              | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                 | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                              | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [DeviceOrder](types.md#deviceorder)   | The ordering options for the returned devices.                                                |

**Input types:**

<details>

<summary><code>DeviceFilter</code></summary>

| Field                | Type                                                           | Description                                                         |
| -------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| `typeIds`            | `[ID!]`                                                        | Filter by device types (OR within field).                           |
| `modelIds`           | `[ID!]`                                                        | Filter by device models (OR within field).                          |
| `statusIds`          | `[ID!]`                                                        | Filter by statuses (OR within field).                               |
| `vendorIds`          | `[ID!]`                                                        | Filter by vendors (OR within field).                                |
| `identifierContains` | `String`                                                       | Partial match on device identifier value (case-sensitive contains). |
| `inventoryIds`       | `[ID!]`                                                        | Filter by inventories (OR within field).                            |
| `titleContains`      | `String`                                                       | Partial match on title (case-insensitive contains).                 |
| `customFields`       | \[[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values.                                      |

</details>

<details>

<summary><code>CustomFieldFilter</code></summary>

| Field      | Type                                                    | Description                                                                   |
| ---------- | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `code`     | [Code](../core-api-reference/common-resources.md#code)! | The custom field code to filter by.                                           |
| `operator` | [FieldOperator](../custom-fields.md#fieldoperator)!     | The comparison operator.                                                      |
| `value`    | [JSON](../core-api-reference/common-resources.md#json)  | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary><code>DeviceOrder</code></summary>

| Field             | Type                                                                        | Description                                                                |
| ----------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `field`           | [DeviceOrderField](types.md#deviceorderfield)                               | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](../core-api-reference/common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](../core-api-reference/common-resources.md#orderdirection)! | The direction to order.                                                    |

</details>

**Output types:**

<details>

<summary><code>DeviceConnection</code></summary>

| Field      | Type                                                             | Description                                                |
| ---------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceEdge](types.md#deviceedge)!]!                           | A list of edges.                                           |
| `nodes`    | \[[Device](types.md#device)!]!                                   | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Device (node)</code></summary>

| Field              | Type                                                                                    | Description                                                                        |
| ------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`               | `ID!`                                                                                   |                                                                                    |
| `version`          | `Int!`                                                                                  |                                                                                    |
| `title`            | `String!`                                                                               |                                                                                    |
| `organization`     | [Organization](../core-api-reference/organizations/#organization)!                      | The organization that owns this device.                                            |
| `type`             | [DeviceType](../catalogs/device/types.md#devicetype)!                                   | The device type classification.                                                    |
| `model`            | [DeviceModel](../catalogs/device/types.md#devicemodel)!                                 | The specific device model.                                                         |
| `status`           | [DeviceStatus](../catalogs/device/types.md#devicestatus)!                               | The current operational status.                                                    |
| `customFields`     | [JSON](../core-api-reference/common-resources.md#json)!                                 |                                                                                    |
| `identifiers`      | \[[DeviceIdentifier](types.md#deviceidentifier)!]!                                      | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory`        | [Inventory](../inventory.md#inventory)                                                  | The inventory this device is currently assigned to.                                |
| `relationsFrom`    | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The outgoing relationships from this device to other devices.                      |
| `relationsTo`      | \[[DeviceRelation](types.md#devicerelation)!]!                                          | The incoming relationships from other devices to this device.                      |
| `inventoryHistory` | [DeviceInventoryRelationConnection](../inventory.md#deviceinventoryrelationconnection)! | The history of inventory assignments for this device.                              |

</details>
