# Catalogs

Catalogs provide configurable lookup tables for entity types, statuses, and other classification systems.

## Objects

### CatalogItemMeta

Metadata about a catalog item.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | `String` | A description of the catalog item. Can be localized. |
| `origin` | [CatalogItemOrigin](../catalogs.md#catalogitemorigin)! | The origin indicating how this item was created. |
| `canBeDeleted` | `Boolean!` | Whether this item can be deleted. Returns `false` if the item has dependencies or is system-managed. |
| `hidden` | `Boolean!` | Whether this item is hidden from regular UI lists. |
| `textColor` | `HexColorCode` | The text color for UI display. |
| `backgroundColor` | `HexColorCode` | The background color for UI display. |
| `icon` | `String` | A relative URL to the icon for this item. |

---

## Enums

### CatalogItemOrigin

The origin of a catalog item, indicating how it was created.

| Value | Description |
| ----- | ----------- |
| `SYSTEM` | Predefined by platform. Immutable and available to all organizations. |
| `ORGANIZATION` | Created by the current organization. |
| `PARENT_ORGANIZATION` | Inherited from a parent organization in the dealer hierarchy. |

---

## Interfaces

### CatalogItem

A dictionary item that provides reference data for the system.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

---

### HierarchicalCatalogItem

A catalog item that supports parent-child hierarchy.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parent` | [CatalogItem](../catalogs.md#catalogitem) | The parent item in the hierarchy. Null for root items. |

---
