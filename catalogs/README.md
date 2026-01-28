# Catalogs

Catalog items are reference data (dictionaries) used throughout the system. They define the vocabulary for entity classification, status tracking, and access control.

## Types

### CatalogItemMeta

Metadata about a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | A description of the catalog item. Can be localized. |
| `origin` | [CatalogItemOrigin](./README.md#catalogitemorigin)! | The origin indicating how this item was created. |
| `canBeDeleted` | `Boolean!` | Whether this item can be deleted. Returns `false` if the item has dependencies or is system-managed. |
| `hidden` | `Boolean!` | Whether this item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon for this item. |

### CatalogItemConnection

A paginated list of CatalogItem items.

**Implements:** [`Connection`](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[CatalogItemEdge](./README.md#catalogitemedge)!]! | A list of edges. |
| `nodes` | [[CatalogItem](./README.md#catalogitem)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

### CatalogItemEdge

An edge in the CatalogItem connection.

**Implements:** [`Edge`](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [CatalogItem](./README.md#catalogitem)! | The catalog item at the end of the edge. |

## Inputs

### CatalogItemFilter

Filtering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `codes` | [[Code](../common.md#code)!] | Match any of these codes. |

### CatalogItemChildrenFilter

Filtering options for catalog item children.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

### CatalogItemOrder

Ordering options for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [CatalogItemOrderField](./README.md#catalogitemorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

### CatalogItemMetaInput

Display properties for catalog items.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | The description. |
| `hidden` | `Boolean` | Whether the item is hidden from regular UI lists. |
| `textColor` | [HexColorCode](../common.md#hexcolorcode) | The text color for UI display. |
| `backgroundColor` | [HexColorCode](../common.md#hexcolorcode) | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon. |

### CatalogItemDeleteInput

Input for deleting a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The catalog item ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### CatalogItemOrigin

The origin of a catalog item, indicating how it was created.

| Value | Description |
| ----- | ----------- |
| `SYSTEM` | Predefined by platform. Immutable and available to all organizations. |
| `ORGANIZATION` | Created by the current organization. |
| `PARENT_ORGANIZATION` | Inherited from a parent organization in the dealer hierarchy. |

### CatalogItemOrderField

Fields available for ordering catalog items.

| Value | Description |
| ----- | ----------- |
| `ORDER` | Order by display order. |
| `CODE` | Order by code. |
| `TITLE` | Order by title. |

## Interfaces

### CatalogItem

A dictionary item that provides reference data for the system.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | [Code](../common.md#code)! | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../organizations.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

### HierarchicalCatalogItem

A catalog item that supports parent-child hierarchy.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parent` | [CatalogItem](./README.md#catalogitem) | The parent item in the hierarchy. Null for root items. |
