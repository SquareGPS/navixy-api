# Catalog items

Operations and types for managing catalog items - the configurable lookup entries.

## Queries

### catalog

Retrieves a catalog by its ID.

```graphql
catalog(id: ID!): Catalog
```

**Arguments**

| Name | Type  | Description                        |
| ---- | ----- | ---------------------------------- |
| `id` | `ID!` | The ID of the catalog to retrieve. |

**Output types:**

<details>

<summary>Catalog</summary>

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](./#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field          | Type                                                             | Description                                                                     |
| -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`           | `ID!`                                                            | A globally unique identifier.                                                   |
| `version`      | `Int!`                                                           | The version number for optimistic locking.                                      |
| `title`        | `String!`                                                        | The human-readable display name. Can be localized.                              |
| `code`         | `Code!`                                                          | A machine-readable code, unique within the catalog scope.                       |
| `order`        | `Int!`                                                           | The display order within the same level or category.                            |
| `catalog`      | [Catalog](catalog-items.md#catalog)!                             | Self-reference for the meta-catalog.                                            |
| `organization` | [Organization](../organizations/#organization)                   | The organization that owns this item. Null for system items.                    |
| `meta`         | [CatalogItemMeta](./#catalogitemmeta)!                           | Metadata about this item including description, origin, and display properties. |
| `module`       | [Module](system.md#module)!                                      | The module this catalog is associated with.                                     |
| `items`        | [CatalogItemConnection](catalog-items.md#catalogitemconnection)! | The items in this catalog.                                                      |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field        | Type                                                                | Description                                                                                                                                 |
| ------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`         | `ID!`                                                               | A globally unique identifier. This ID is opaque and should not be parsed by clients.                                                        |
| `version`    | `Int!`                                                              | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title`      | `String!`                                                           | The human-readable display name.                                                                                                            |
| `externalId` | `String`                                                            | An external system identifier for integration purposes.                                                                                     |
| `isActive`   | `Boolean!`                                                          | Whether this organization is active.                                                                                                        |
| `features`   | \[[OrganizationFeature](../organizations/#organizationfeature)!]!   | The feature flags enabled for this organization.                                                                                            |
| `parent`     | [Organization](../organizations/#organization)                      | The parent organization in the hierarchy. Null for root organizations.                                                                      |
| `children`   | [OrganizationConnection](../organizations/#organizationconnection)! | The child organizations.                                                                                                                    |
| `members`    | [MemberConnection](../organizations/members.md#memberconnection)!   | The members of this organization.                                                                                                           |
| `devices`    | [DeviceConnection](../devices/types.md#deviceconnection)!           | The devices owned by this organization.                                                                                                     |
| `assets`     | [AssetConnection](../assets/types.md#assetconnection)!              | The assets owned by this organization.                                                                                                      |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization.                                                                                          |
| `schedules`  | [ScheduleConnection](../schedules/types.md#scheduleconnection)!     | The schedules owned by this organization.                                                                                                   |

</details>

***

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

| Name             | Type                | Description                                                                                   |
| ---------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`               | The organization to retrieve catalogs for.                                                    |
| `filter`         | `CatalogItemFilter` | Filtering options for the returned catalogs.                                                  |
| `first`          | `Int`               | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`            | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`               | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`            | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | `CatalogItemOrder`  | The ordering options for the returned catalogs.                                               |

**Input types:**

<details>

<summary>CatalogItemFilter</summary>

Filtering options for catalog items.

| Field           | Type      | Description                                         |
| --------------- | --------- | --------------------------------------------------- |
| `titleContains` | `String`  | Partial match on title (case-insensitive contains). |
| `codes`         | `[Code!]` | Match any of these codes.                           |

</details>

<details>

<summary>CatalogItemOrder</summary>

Ordering options for catalog items.

| Field       | Type                                                             | Description             |
| ----------- | ---------------------------------------------------------------- | ----------------------- |
| `field`     | [CatalogItemOrderField](catalog-items.md#catalogitemorderfield)! | The field to order by.  |
| `direction` | [OrderDirection](../common.md#orderdirection)!                   | The direction to order. |

</details>

**Output types:**

<details>

<summary>CatalogConnection</summary>

A paginated list of Catalog items.

**Implements:** [Connection](../common.md#connection)

| Field      | Type                                             | Description                                                |
| ---------- | ------------------------------------------------ | ---------------------------------------------------------- |
| `edges`    | \[[CatalogEdge](catalog-items.md#catalogedge)!]! | A list of edges.                                           |
| `nodes`    | \[[Catalog](catalog-items.md#catalog)!]!         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)!               | Information about the current page.                        |
| `total`    | [CountInfo](../common.md#countinfo)              | The total count of items matching the filter.              |

</details>

<details>

<summary>PageInfo (entity)</summary>

Information about the current page in a paginated connection.

| Field             | Type       | Description                                                |
| ----------------- | ---------- | ---------------------------------------------------------- |
| `hasNextPage`     | `Boolean!` | Whether more items exist after the current page.           |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page.          |
| `startCursor`     | `String`   | The cursor pointing to the first item in the current page. |
| `endCursor`       | `String`   | The cursor pointing to the last item in the current page.  |

</details>

***

## Objects

### Catalog

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](./#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field          | Type                                                             | Description                                                                     |
| -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`           | `ID!`                                                            | A globally unique identifier.                                                   |
| `version`      | `Int!`                                                           | The version number for optimistic locking.                                      |
| `title`        | `String!`                                                        | The human-readable display name. Can be localized.                              |
| `code`         | `Code!`                                                          | A machine-readable code, unique within the catalog scope.                       |
| `order`        | `Int!`                                                           | The display order within the same level or category.                            |
| `catalog`      | [Catalog](catalog-items.md#catalog)!                             | Self-reference for the meta-catalog.                                            |
| `organization` | [Organization](../organizations/#organization)                   | The organization that owns this item. Null for system items.                    |
| `meta`         | [CatalogItemMeta](./#catalogitemmeta)!                           | Metadata about this item including description, origin, and display properties. |
| `module`       | [Module](system.md#module)!                                      | The module this catalog is associated with.                                     |
| `items`        | [CatalogItemConnection](catalog-items.md#catalogitemconnection)! | The items in this catalog.                                                      |

***

### CatalogItemMeta

Metadata about a catalog item.

| Field             | Type                                                     | Description                                                                                          |
| ----------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `description`     | `String`                                                 | A description of the catalog item. Can be localized.                                                 |
| `origin`          | [CatalogItemOrigin](catalog-items.md#catalogitemorigin)! | The origin indicating how this item was created.                                                     |
| `canBeDeleted`    | `Boolean!`                                               | Whether this item can be deleted. Returns `false` if the item has dependencies or is system-managed. |
| `hidden`          | `Boolean!`                                               | Whether this item is hidden from regular UI lists.                                                   |
| `textColor`       | `HexColorCode`                                           | The text color for UI display.                                                                       |
| `backgroundColor` | `HexColorCode`                                           | The background color for UI display.                                                                 |
| `icon`            | `String`                                                 | A relative URL to the icon for this item.                                                            |

***

## Inputs

### CatalogItemFilter

Filtering options for catalog items.

| Field           | Type      | Description                                         |
| --------------- | --------- | --------------------------------------------------- |
| `titleContains` | `String`  | Partial match on title (case-insensitive contains). |
| `codes`         | `[Code!]` | Match any of these codes.                           |

***

### CatalogItemChildrenFilter

Filtering options for catalog item children.

| Field           | Type     | Description                                         |
| --------------- | -------- | --------------------------------------------------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

***

### CatalogItemOrder

Ordering options for catalog items.

| Field       | Type                                                             | Description             |
| ----------- | ---------------------------------------------------------------- | ----------------------- |
| `field`     | [CatalogItemOrderField](catalog-items.md#catalogitemorderfield)! | The field to order by.  |
| `direction` | [OrderDirection](../common.md#orderdirection)!                   | The direction to order. |

***

### CatalogItemMetaInput

Display properties for catalog items.

| Field             | Type           | Description                                       |
| ----------------- | -------------- | ------------------------------------------------- |
| `description`     | `String`       | The description.                                  |
| `hidden`          | `Boolean`      | Whether the item is hidden from regular UI lists. |
| `textColor`       | `HexColorCode` | The text color for UI display.                    |
| `backgroundColor` | `HexColorCode` | The background color for UI display.              |
| `icon`            | `String`       | A relative URL to the icon.                       |

***

### CatalogItemDeleteInput

Input for deleting a catalog item.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The catalog item ID to delete.              |
| `version` | `Int!` | The current version for optimistic locking. |

***

## Enums

### CatalogItemOrderField

Fields available for ordering catalog items.

| Value        | Description                      |
| ------------ | -------------------------------- |
| `ORDER`      | Order by display order.          |
| `CODE`       | Order by code.                   |
| `TITLE`      | Order by title.                  |
| `CREATED_AT` | Order by creation date and time. |

***

### CatalogItemOrigin

The origin of a catalog item, indicating how it was created.

| Value                 | Description                                                           |
| --------------------- | --------------------------------------------------------------------- |
| `SYSTEM`              | Predefined by platform. Immutable and available to all organizations. |
| `ORGANIZATION`        | Created by the current organization.                                  |
| `PARENT_ORGANIZATION` | Inherited from a parent organization in the dealer hierarchy.         |

***

## Interfaces

### CatalogItem

A dictionary item that provides reference data for the system.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field          | Type                                                 | Description                                                                     |
| -------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`           | `ID!`                                                | A globally unique identifier.                                                   |
| `version`      | `Int!`                                               | The version number for optimistic locking.                                      |
| `title`        | `String!`                                            | The human-readable display name. Can be localized.                              |
| `code`         | `Code!`                                              | A machine-readable code, unique within the catalog scope.                       |
| `order`        | `Int!`                                               | The display order within the same level or category.                            |
| `catalog`      | [Catalog](catalog-items.md#catalog)!                 | The catalog this item belongs to.                                               |
| `organization` | [Organization](../organizations/#organization)       | The organization that owns this item. Null for system items.                    |
| `meta`         | [CatalogItemMeta](catalog-items.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

***

### HierarchicalCatalogItem

A catalog item that supports parent-child hierarchy.

| Field    | Type                                        | Description                                            |
| -------- | ------------------------------------------- | ------------------------------------------------------ |
| `parent` | [CatalogItem](catalog-items.md#catalogitem) | The parent item in the hierarchy. Null for root items. |

***

## Pagination types

### CatalogItemConnection

A paginated list of CatalogItem items.

**Implements:** [Connection](../common.md#connection)

| Field      | Type                                                     | Description                                                |
| ---------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[CatalogItemEdge](catalog-items.md#catalogitemedge)!]! | A list of edges.                                           |
| `nodes`    | \[[CatalogItem](./#catalogitem)!]!                       | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)!                       | Information about the current page.                        |
| `total`    | [CountInfo](../common.md#countinfo)                      | The total count of items matching the filter.              |

***

### CatalogItemEdge

An edge in the CatalogItem connection.

**Implements:** [Edge](../common.md#edge)

| Field    | Type                           | Description                              |
| -------- | ------------------------------ | ---------------------------------------- |
| `cursor` | `String!`                      | An opaque cursor for this edge.          |
| `node`   | [CatalogItem](./#catalogitem)! | The catalog item at the end of the edge. |

***

### CatalogConnection

A paginated list of Catalog items.

**Implements:** [Connection](../common.md#connection)

| Field      | Type                                             | Description                                                |
| ---------- | ------------------------------------------------ | ---------------------------------------------------------- |
| `edges`    | \[[CatalogEdge](catalog-items.md#catalogedge)!]! | A list of edges.                                           |
| `nodes`    | \[[Catalog](catalog-items.md#catalog)!]!         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)!               | Information about the current page.                        |
| `total`    | [CountInfo](../common.md#countinfo)              | The total count of items matching the filter.              |

***

### CatalogEdge

An edge in the Catalog connection.

**Implements:** [Edge](../common.md#edge)

| Field    | Type                                 | Description                         |
| -------- | ------------------------------------ | ----------------------------------- |
| `cursor` | `String!`                            | An opaque cursor for this edge.     |
| `node`   | [Catalog](catalog-items.md#catalog)! | The catalog at the end of the edge. |

***
