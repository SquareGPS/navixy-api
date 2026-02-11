# Catalog items

Operations and types for managing catalog items - the configurable lookup entries.

## Queries

### catalog

Retrieves a catalog by its ID.

```graphql
catalog(id: ID!): Catalog
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the catalog to retrieve. |

**Output types:**

<details>

<summary>Catalog</summary>

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalog-items.md#catalog)! | Self-reference for the meta-catalog. |
| `organization` | [Organization](../../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](../system.md#module)! | The module this catalog is associated with. |
| `filter` | [CatalogItemFilter](../catalog-items.md#catalogitemfilter) | Filtering options for the returned items. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder = { field: ORDER, direction: ASC }` | The ordering options for the returned items. |

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
| `filter` | [DeviceFilter](../../devices/types.md#devicefilter) | Filtering options for the returned devices. |
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
| `organizationId` | `ID!` |  |
| `filter` | `CatalogItemFilter` |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | `CatalogItemOrder` |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary>CatalogItemFilter</summary>

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | `[Code!]` | Match any of these codes. |

</details>

<details>

<summary>CatalogItemOrder</summary>

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>CatalogConnection</summary>

A paginated list of Catalog items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogEdge](../catalog-items.md#catalogedge)!]! | A list of edges. |
| `nodes` | [[Catalog](../catalog-items.md#catalog)!]! | A list of nodes in the connection (without edge metadata). |
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

## Objects

### Catalog

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalog-items.md#catalog)! | Self-reference for the meta-catalog. |
| `organization` | [Organization](../../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](../system.md#module)! | The module this catalog is associated with. |
| `filter` | [CatalogItemFilter](../catalog-items.md#catalogitemfilter) | Filtering options for the returned items. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder = { field: ORDER, direction: ASC }` | The ordering options for the returned items. |

---

## Inputs

### CatalogItemFilter

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | `[Code!]` | Match any of these codes. |

---

### CatalogItemChildrenFilter

Filtering options for catalog item children.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

### CatalogItemOrder

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](../catalog-items.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../../common.md#orderdirection)! | The direction to order. |

---

### CatalogItemMetaInput

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

---

### CatalogItemDeleteInput

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

## Enums

### CatalogItemOrderField

Fields available for ordering catalog items.

| Value | Description |
| ----- | ----------- |
| `ORDER` | Order by display order. |
| `CODE` | Order by code. |
| `TITLE` | Order by title. |
| `CREATED_AT` | Order by creation date and time. |

---

## Pagination types

### CatalogItemConnection

A paginated list of CatalogItem items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogItemEdge](../catalog-items.md#catalogitemedge)!]! | A list of edges. |
| `nodes` | [[CatalogItem](../../catalogs.md#catalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### CatalogItemEdge

An edge in the CatalogItem connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [CatalogItem](../../catalogs.md#catalogitem)! | The catalog item at the end of the edge. |

---

### CatalogConnection

A paginated list of Catalog items.

**Implements:** [Connection](../../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogEdge](../catalog-items.md#catalogedge)!]! | A list of edges. |
| `nodes` | [[Catalog](../catalog-items.md#catalog)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../../common.md#countinfo) | The total count of items matching the filter. |

---

### CatalogEdge

An edge in the Catalog connection.

**Implements:** [Edge](../../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Catalog](../catalog-items.md#catalog)! | The catalog at the end of the edge. |

---
