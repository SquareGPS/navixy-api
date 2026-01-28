# System Catalog

System-wide catalog items and configuration.

## Types

### Module

A system module that groups related functionality and permission scopes.
Examples: repo (core), fleet_management (FSM), iot (devices), reports, billing.

**Implements:** [`CatalogItem`](./README.md#catalogitem), [`Node`](../common.md#node), [`Versioned`](../common.md#versioned), [`Titled`](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |

### EntityType

A definition of an entity type in the system.

**Implements:** [`CatalogItem`](./README.md#catalogitem), [`Node`](../common.md#node), [`Versioned`](../common.md#versioned), [`Titled`](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |
| `uuidDiscriminator` | `String!` | The 4-character code embedded in UUIDs for entities of this type. |
| `isCustomizable` | `Boolean!` | Whether entities of this type support custom fields. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions for entities of this type, ordered by display order. |

### Country

A country reference data item.

**Implements:** [`CatalogItem`](./README.md#catalogitem), [`Node`](../common.md#node), [`Versioned`](../common.md#versioned), [`Titled`](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | [Code](../common.md#code)! |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../organizations.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](./README.md#catalogitemmeta)! |  |
| `alpha2Code` | [CountryCode](../common.md#countrycode)! | The [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code. |
