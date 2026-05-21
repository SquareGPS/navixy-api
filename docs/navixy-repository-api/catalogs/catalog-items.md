# Catalog items

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

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

**Implements:** [CatalogItem](#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](#type-catalog)! | Self-reference for the meta-catalog. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](system.md#type-module)! | The module this catalog is associated with. |
| `items` | [CatalogItemConnection](#type-catalogitemconnection)! | The items in this catalog. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations/README.md#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations/README.md#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](../organizations/README.md#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](../organizations/members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

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
| `organizationId` | `ID!` | The organization to retrieve catalogs for. |
| `filter` | `CatalogItemFilter` | Filtering options for the returned catalogs. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `CatalogItemOrder` | The ordering options for the returned catalogs. |

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
| `field` | [CatalogItemOrderField](#type-catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>CatalogConnection</summary>

A paginated list of Catalog items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogEdge](#type-catalogedge)!]! | A list of edges. |
| `nodes` | [[Catalog](#type-catalog)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

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

### catalogCreate

Creates a new user-defined catalog.

```graphql
catalogCreate(
    input: CatalogCreateInput!
  ): CatalogPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogCreateInput!` | The input fields for creating the catalog. |

**Input types:**

<details>

<summary>CatalogCreateInput</summary>

Input for creating a user-defined catalog (a container for user catalog items).

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the catalog. |
| `moduleId` | `ID` | The module this catalog belongs to. Defaults to CORE if omitted. |
| `code` | `Code` | The machine-readable code, unique within the organization. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](#type-catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

**Output types:**

<details>

<summary>CatalogPayload</summary>

The result of a catalog mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `catalog` | [Catalog](#type-catalog)! | The created or updated catalog. |

</details>

<details>

<summary>Catalog (entity)</summary>

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](#type-catalog)! | Self-reference for the meta-catalog. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](system.md#type-module)! | The module this catalog is associated with. |
| `items` | [CatalogItemConnection](#type-catalogitemconnection)! | The items in this catalog. |

</details>

---

### catalogUpdate

Updates a user-defined catalog.

```graphql
catalogUpdate(
    input: CatalogUpdateInput!
  ): CatalogPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogUpdateInput!` | The input fields for updating the catalog. |

**Input types:**

<details>

<summary>CatalogUpdateInput</summary>

Input for updating a user-defined catalog.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](#type-catalogitemmetainput) | The display properties. |

</details>

<details>

<summary>CatalogItemMetaInput</summary>

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

</details>

**Output types:**

<details>

<summary>CatalogPayload</summary>

The result of a catalog mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `catalog` | [Catalog](#type-catalog)! | The created or updated catalog. |

</details>

<details>

<summary>Catalog (entity)</summary>

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](#type-catalog)! | Self-reference for the meta-catalog. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](system.md#type-module)! | The module this catalog is associated with. |
| `items` | [CatalogItemConnection](#type-catalogitemconnection)! | The items in this catalog. |

</details>

---

### catalogDelete

Deletes a user-defined catalog.

```graphql
catalogDelete(
    input: CatalogDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `CatalogDeleteInput!` | The input fields for deleting the catalog. |

**Input types:**

<details>

<summary>CatalogDeleteInput</summary>

Input for deleting a user-defined catalog.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, deletes regardless of version. |

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

<a id="type-catalogitemmeta"></a>

### CatalogItemMeta

Metadata about a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | A description of the catalog item. Can be localized. |
| `origin` | [CatalogItemOrigin](#type-catalogitemorigin)! | The origin indicating how this item was created. |
| `canBeDeleted` | `Boolean!` | Whether this item can be deleted. Returns `false` if the item has dependencies or is system-managed. |
| `hidden` | `Boolean!` | Whether this item is hidden from regular UI lists. |

---

<a id="type-catalog"></a>

### Catalog

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](#type-catalog)! | Self-reference for the meta-catalog. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `module` | [Module](system.md#type-module)! | The module this catalog is associated with. |
| `items` | [CatalogItemConnection](#type-catalogitemconnection)! | The items in this catalog. |

---

<a id="type-catalogpayload"></a>

### CatalogPayload

The result of a catalog mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `catalog` | [Catalog](#type-catalog)! | The created or updated catalog. |

---

## Inputs

<a id="type-catalogitemfilter"></a>

### CatalogItemFilter

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | `[Code!]` | Match any of these codes. |

---

<a id="type-catalogitemchildrenfilter"></a>

### CatalogItemChildrenFilter

Filtering options for catalog item children.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

<a id="type-catalogitemorder"></a>

### CatalogItemOrder

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](#type-catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-catalogitemmetainput"></a>

### CatalogItemMetaInput

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |

---

<a id="type-catalogcreateinput"></a>

### CatalogCreateInput

Input for creating a user-defined catalog (a container for user catalog items).

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the catalog. |
| `moduleId` | `ID` | The module this catalog belongs to. Defaults to CORE if omitted. |
| `code` | `Code` | The machine-readable code, unique within the organization. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](#type-catalogitemmetainput) | The display properties. |

---

<a id="type-catalogupdateinput"></a>

### CatalogUpdateInput

Input for updating a user-defined catalog.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](#type-catalogitemmetainput) | The display properties. |

---

<a id="type-catalogdeleteinput"></a>

### CatalogDeleteInput

Input for deleting a user-defined catalog.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, deletes regardless of version. |

---

<a id="type-catalogitemdeleteinput"></a>

### CatalogItemDeleteInput

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

## Enums

<a id="type-catalogitemorigin"></a>

### CatalogItemOrigin

The origin of a catalog item, indicating how it was created.

| Value | Description |
| ----- | ----------- |
| `SYSTEM` | Predefined by platform. Immutable and available to all organizations. |
| `ORGANIZATION` | Created by the current organization. |
| `PARENT_ORGANIZATION` | Inherited from a parent organization in the dealer hierarchy. |

---

<a id="type-catalogitemorderfield"></a>

### CatalogItemOrderField

Fields available for ordering catalog items.

| Value | Description |
| ----- | ----------- |
| `ORDER` | Order by display order. |
| `CODE` | Order by code. |
| `TITLE` | Order by title. |
| `CREATED_AT` | Order by creation date and time. |

---

## Interfaces

<a id="type-catalogitem"></a>

### CatalogItem

A dictionary item that provides reference data for the system.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

---

<a id="type-hierarchicalcatalogitem"></a>

### HierarchicalCatalogItem

A catalog item that supports parent-child hierarchy.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parent` | [CatalogItem](#type-catalogitem) | The parent item in the hierarchy. Null for root items. |

---

## Pagination types

<a id="type-catalogitemconnection"></a>

### CatalogItemConnection

A paginated list of CatalogItem items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogItemEdge](#type-catalogitemedge)!]! | A list of edges. |
| `nodes` | [[CatalogItem](#type-catalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-catalogitemedge"></a>

### CatalogItemEdge

An edge in the CatalogItem connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [CatalogItem](#type-catalogitem)! | The catalog item at the end of the edge. |

---

<a id="type-catalogconnection"></a>

### CatalogConnection

A paginated list of Catalog items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogEdge](#type-catalogedge)!]! | A list of edges. |
| `nodes` | [[Catalog](#type-catalog)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-catalogedge"></a>

### CatalogEdge

An edge in the Catalog connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Catalog](#type-catalog)! | The catalog at the end of the edge. |

---
