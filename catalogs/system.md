# System catalog

System-wide catalog items and configuration.

## Types

### Module

A system module that groups related functionality and permission scopes. Examples: repo (core), fleet\_management (FSM), iot (devices), reports, billing.

**Implements:** [`CatalogItem`](./#catalogitem), [`Node`](../core-api-reference/common-resources.md#node), [`Versioned`](../core-api-reference/common-resources.md#versioned), [`Titled`](../core-api-reference/common-resources.md#titled)

| Field          | Type                                                              | Description |
| -------------- | ----------------------------------------------------------------- | ----------- |
| `id`           | `ID!`                                                             |             |
| `version`      | `Int!`                                                            |             |
| `title`        | `String!`                                                         |             |
| `code`         | [Code](../core-api-reference/common-resources.md#code)!           |             |
| `order`        | `Int!`                                                            |             |
| `catalog`      | [Catalog](../core-api-reference/organizations/#catalog)!          |             |
| `organization` | [Organization](../core-api-reference/organizations/#organization) |             |
| `meta`         | [CatalogItemMeta](./#catalogitemmeta)!                            |             |

### EntityType

A definition of an entity type in the system.

**Implements:** [`CatalogItem`](./#catalogitem), [`Node`](../core-api-reference/common-resources.md#node), [`Versioned`](../core-api-reference/common-resources.md#versioned), [`Titled`](../core-api-reference/common-resources.md#titled)

| Field                    | Type                                                                    | Description                                                                   |
| ------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                   |                                                                               |
| `version`                | `Int!`                                                                  |                                                                               |
| `title`                  | `String!`                                                               |                                                                               |
| `code`                   | [Code](../core-api-reference/common-resources.md#code)!                 |                                                                               |
| `order`                  | `Int!`                                                                  |                                                                               |
| `catalog`                | [Catalog](../core-api-reference/organizations/#catalog)!                |                                                                               |
| `organization`           | [Organization](../core-api-reference/organizations/#organization)       |                                                                               |
| `meta`                   | [CatalogItemMeta](./#catalogitemmeta)!                                  |                                                                               |
| `uuidDiscriminator`      | `String!`                                                               | The 4-character code embedded in UUIDs for entities of this type.             |
| `isCustomizable`         | `Boolean!`                                                              | Whether entities of this type support custom fields.                          |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions for entities of this type, ordered by display order. |

### Country

A country reference data item.

**Implements:** [`CatalogItem`](./#catalogitem), [`Node`](../core-api-reference/common-resources.md#node), [`Versioned`](../core-api-reference/common-resources.md#versioned), [`Titled`](../core-api-reference/common-resources.md#titled)

| Field          | Type                                                                  | Description                                                                      |
| -------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`           | `ID!`                                                                 |                                                                                  |
| `version`      | `Int!`                                                                |                                                                                  |
| `title`        | `String!`                                                             |                                                                                  |
| `code`         | [Code](../core-api-reference/common-resources.md#code)!               |                                                                                  |
| `order`        | `Int!`                                                                |                                                                                  |
| `catalog`      | [Catalog](../core-api-reference/organizations/#catalog)!              |                                                                                  |
| `organization` | [Organization](../core-api-reference/organizations/#organization)     |                                                                                  |
| `meta`         | [CatalogItemMeta](./#catalogitemmeta)!                                |                                                                                  |
| `alpha2Code`   | [CountryCode](../core-api-reference/common-resources.md#countrycode)! | The [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code. |
