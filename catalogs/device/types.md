# Types

## Types

### DeviceTypeConnection

A paginated list of DeviceType items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceTypeEdge](types.md#devicetypeedge)!]!                      | A list of edges.                                           |
| `nodes`    | \[[DeviceType](types.md#devicetype)!]!                              | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### DeviceTypeEdge

An edge in the DeviceType connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                               | Description                             |
| -------- | ---------------------------------- | --------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.         |
| `node`   | [DeviceType](types.md#devicetype)! | The device type at the end of the edge. |

### DeviceStatusConnection

A paginated list of DeviceStatus items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceStatusEdge](types.md#devicestatusedge)!]!                  | A list of edges.                                           |
| `nodes`    | \[[DeviceStatus](types.md#devicestatus)!]!                          | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### DeviceStatusEdge

An edge in the DeviceStatus connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                                   | Description                               |
| -------- | -------------------------------------- | ----------------------------------------- |
| `cursor` | `String!`                              | An opaque cursor for this edge.           |
| `node`   | [DeviceStatus](types.md#devicestatus)! | The device status at the end of the edge. |

### DeviceModelConnection

A paginated list of DeviceModel items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[DeviceModelEdge](types.md#devicemodeledge)!]!                    | A list of edges.                                           |
| `nodes`    | \[[DeviceModel](types.md#devicemodel)!]!                            | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### DeviceModelEdge

An edge in the DeviceModel connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                                 | Description                              |
| -------- | ------------------------------------ | ---------------------------------------- |
| `cursor` | `String!`                            | An opaque cursor for this edge.          |
| `node`   | [DeviceModel](types.md#devicemodel)! | The device model at the end of the edge. |

### DeviceVendor

A device manufacturer or vendor.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field          | Type                                                                 | Description                            |
| -------------- | -------------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                                |                                        |
| `version`      | `Int!`                                                               |                                        |
| `title`        | `String!`                                                            |                                        |
| `code`         | [Code](../../core-api-reference/common-resources.md#code)!           |                                        |
| `order`        | `Int!`                                                               |                                        |
| `catalog`      | [Catalog](../../core-api-reference/organizations/#catalog)!          |                                        |
| `organization` | [Organization](../../core-api-reference/organizations/#organization) |                                        |
| `meta`         | [CatalogItemMeta](../#catalogitemmeta)!                              |                                        |
| `models`       | [DeviceModelConnection](types.md#devicemodelconnection)!             | Device models produced by this vendor. |

### DeviceModel

A specific device model produced by a vendor.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field          | Type                                                                 | Description                              |
| -------------- | -------------------------------------------------------------------- | ---------------------------------------- |
| `id`           | `ID!`                                                                |                                          |
| `version`      | `Int!`                                                               |                                          |
| `title`        | `String!`                                                            |                                          |
| `code`         | [Code](../../core-api-reference/common-resources.md#code)!           |                                          |
| `order`        | `Int!`                                                               |                                          |
| `catalog`      | [Catalog](../../core-api-reference/organizations/#catalog)!          |                                          |
| `organization` | [Organization](../../core-api-reference/organizations/#organization) |                                          |
| `meta`         | [CatalogItemMeta](../#catalogitemmeta)!                              |                                          |
| `vendor`       | [DeviceVendor](types.md#devicevendor)!                               | The vendor that manufactures this model. |

### DeviceType

A classification type for devices.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field                    | Type                                                                       | Description                                                                      |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                      |                                                                                  |
| `version`                | `Int!`                                                                     |                                                                                  |
| `title`                  | `String!`                                                                  |                                                                                  |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                  |
| `order`                  | `Int!`                                                                     |                                                                                  |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                  |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                  |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                  |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this device type, ordered by display order. |

### DeviceStatus

An operational status for devices.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field          | Type                                                                 | Description |
| -------------- | -------------------------------------------------------------------- | ----------- |
| `id`           | `ID!`                                                                |             |
| `version`      | `Int!`                                                               |             |
| `title`        | `String!`                                                            |             |
| `code`         | [Code](../../core-api-reference/common-resources.md#code)!           |             |
| `order`        | `Int!`                                                               |             |
| `catalog`      | [Catalog](../../core-api-reference/organizations/#catalog)!          |             |
| `organization` | [Organization](../../core-api-reference/organizations/#organization) |             |
| `meta`         | [CatalogItemMeta](../#catalogitemmeta)!                              |             |

### DeviceRelationType

A type of relationship between two devices.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field          | Type                                                                 | Description |
| -------------- | -------------------------------------------------------------------- | ----------- |
| `id`           | `ID!`                                                                |             |
| `version`      | `Int!`                                                               |             |
| `title`        | `String!`                                                            |             |
| `code`         | [Code](../../core-api-reference/common-resources.md#code)!           |             |
| `order`        | `Int!`                                                               |             |
| `catalog`      | [Catalog](../../core-api-reference/organizations/#catalog)!          |             |
| `organization` | [Organization](../../core-api-reference/organizations/#organization) |             |
| `meta`         | [CatalogItemMeta](../#catalogitemmeta)!                              |             |

### DeviceTypePayload

The result of a device type mutation.

| Field        | Type                               | Description                         |
| ------------ | ---------------------------------- | ----------------------------------- |
| `deviceType` | [DeviceType](types.md#devicetype)! | The created or updated device type. |

### DeviceStatusPayload

The result of a device status mutation.

| Field          | Type                                   | Description                           |
| -------------- | -------------------------------------- | ------------------------------------- |
| `deviceStatus` | [DeviceStatus](types.md#devicestatus)! | The created or updated device status. |

## Inputs

### DeviceModelFilter

Filtering options for device models.

| Field           | Type                                                      | Description                                         |
| --------------- | --------------------------------------------------------- | --------------------------------------------------- |
| `vendorIds`     | `[ID!]`                                                   | Filter by vendors (OR within field).                |
| `titleContains` | `String`                                                  | Partial match on title (case-insensitive contains). |
| `code`          | [Code](../../core-api-reference/common-resources.md#code) | Exact code match.                                   |

### DeviceTypeCreateInput

Input for creating a device type.

| Field            | Type                                                       | Description                              |
| ---------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `organizationId` | `ID!`                                                      | The organization that will own the item. |
| `code`           | [Code](../../core-api-reference/common-resources.md#code)! | The machine-readable code.               |
| `title`          | `String!`                                                  | The display name.                        |
| `order`          | `Int`                                                      | The display order.                       |
| `meta`           | [CatalogItemMetaInput](../#catalogitemmetainput)           | The display properties.                  |

### DeviceTypeUpdateInput

Input for updating a device type.

| Field     | Type                                             | Description                                 |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                            | The item ID to update.                      |
| `version` | `Int!`                                           | The current version for optimistic locking. |
| `title`   | `String`                                         | The new display name.                       |
| `order`   | `Int`                                            | The new display order.                      |
| `meta`    | [CatalogItemMetaInput](../#catalogitemmetainput) | The display properties.                     |

### DeviceStatusCreateInput

Input for creating a device status.

| Field            | Type                                                       | Description                              |
| ---------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `organizationId` | `ID!`                                                      | The organization that will own the item. |
| `code`           | [Code](../../core-api-reference/common-resources.md#code)! | The machine-readable code.               |
| `title`          | `String!`                                                  | The display name.                        |
| `order`          | `Int`                                                      | The display order.                       |
| `meta`           | [CatalogItemMetaInput](../#catalogitemmetainput)           | The display properties.                  |

### DeviceStatusUpdateInput

Input for updating a device status.

| Field     | Type                                             | Description                                 |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                            | The item ID to update.                      |
| `version` | `Int!`                                           | The current version for optimistic locking. |
| `title`   | `String`                                         | The new display name.                       |
| `order`   | `Int`                                            | The new display order.                      |
| `meta`    | [CatalogItemMetaInput](../#catalogitemmetainput) | The display properties.                     |
