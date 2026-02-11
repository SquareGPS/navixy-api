# System catalogs

System-defined catalog items that cannot be modified by users.

## Objects

### Module

A system module that groups related functionality and permission scopes.
Examples: repo (core), fleet_management (FSM), iot (devices), reports, billing.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |

---

### EntityType

A definition of an entity type in the system.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `uuidDiscriminator` | `String!` | The 4-character code embedded in UUIDs for entities of this type. |
| `isCustomizable` | `Boolean!` | Whether entities of this type support custom fields. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions for entities of this type, ordered by display order. |

---

### Country

A country reference data item.

**Implements:** [CatalogItem](../../catalogs.md#catalogitem), [Node](../../common.md#node), [Versioned](../../common.md#versioned), [Titled](../../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalog-items.md#catalog)! |  |
| `organization` | [Organization](../../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../../catalogs.md#catalogitemmeta)! |  |
| `alpha2Code` | `CountryCode!` | The [ISO 3166](https://www.iso.org/standard/3166.html)-1 alpha-2 country code. |

---
