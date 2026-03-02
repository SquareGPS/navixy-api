# System catalogs

System-defined catalog items that cannot be modified by users.

## Objects

### Module

A system module that groups related functionality and permission scopes.
Examples: repo (core), fleet_management (FSM), iot (devices), reports, billing.

**Implements:** [CatalogItem](README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |

---

### EntityType

A definition of an entity type in the system.

**Implements:** [CatalogItem](README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `uuidDiscriminator` | `String!` | The 4-character code embedded in UUIDs for entities of this type. |
| `isCustomizable` | `Boolean!` | Whether entities of this type support custom fields. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions for entities of this type, ordered by display order. |

---

### Country

A country reference data item.

**Implements:** [CatalogItem](README.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](README.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `alpha2Code` | `CountryCode!` | The [ISO 3166](https://www.iso.org/standard/3166.html)-1 alpha-2 country code. |

---
