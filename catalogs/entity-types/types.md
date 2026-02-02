# Types

## Types

### AssetTypeConnection

A paginated list of AssetType items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AssetTypeEdge](types.md#assettypeedge)!]!                        | A list of edges.                                           |
| `nodes`    | \[[AssetType](types.md#assettype)!]!                                | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### AssetTypeEdge

An edge in the AssetType connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                             | Description                            |
| -------- | -------------------------------- | -------------------------------------- |
| `cursor` | `String!`                        | An opaque cursor for this edge.        |
| `node`   | [AssetType](types.md#assettype)! | The asset type at the end of the edge. |

### AssetGroupTypeConnection

A paginated list of AssetGroupType items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AssetGroupTypeEdge](types.md#assetgrouptypeedge)!]!              | A list of edges.                                           |
| `nodes`    | \[[AssetGroupType](types.md#assetgrouptype)!]!                      | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### AssetGroupTypeEdge

An edge in the AssetGroupType connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                                       | Description                                  |
| -------- | ------------------------------------------ | -------------------------------------------- |
| `cursor` | `String!`                                  | An opaque cursor for this edge.              |
| `node`   | [AssetGroupType](types.md#assetgrouptype)! | The asset group type at the end of the edge. |

### GeoObjectTypeConnection

A paginated list of GeoObjectType items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[GeoObjectTypeEdge](types.md#geoobjecttypeedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[GeoObjectType](types.md#geoobjecttype)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### GeoObjectTypeEdge

An edge in the GeoObjectType connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                                     | Description                                 |
| -------- | ---------------------------------------- | ------------------------------------------- |
| `cursor` | `String!`                                | An opaque cursor for this edge.             |
| `node`   | [GeoObjectType](types.md#geoobjecttype)! | The geo object type at the end of the edge. |

### ScheduleTypeConnection

A paginated list of ScheduleType items.

**Implements:** [`Connection`](../../core-api-reference/common-resources.md#connection)

| Field      | Type                                                                | Description                                                |
| ---------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[ScheduleTypeEdge](types.md#scheduletypeedge)!]!                  | A list of edges.                                           |
| `nodes`    | \[[ScheduleType](types.md#scheduletype)!]!                          | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### ScheduleTypeEdge

An edge in the ScheduleType connection.

**Implements:** [`Edge`](../../core-api-reference/common-resources.md#edge)

| Field    | Type                                   | Description                               |
| -------- | -------------------------------------- | ----------------------------------------- |
| `cursor` | `String!`                              | An opaque cursor for this edge.           |
| `node`   | [ScheduleType](types.md#scheduletype)! | The schedule type at the end of the edge. |

### AssetType

A classification type for assets.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field                    | Type                                                                       | Description                                                                     |
| ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                      |                                                                                 |
| `version`                | `Int!`                                                                     |                                                                                 |
| `title`                  | `String!`                                                                  |                                                                                 |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                 |
| `order`                  | `Int!`                                                                     |                                                                                 |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                 |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                 |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                 |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this asset type, ordered by display order. |

### AssetGroupType

A type for asset groups with membership constraints.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field               | Type                                                                 | Description                                                                    |
| ------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `id`                | `ID!`                                                                |                                                                                |
| `version`           | `Int!`                                                               |                                                                                |
| `title`             | `String!`                                                            |                                                                                |
| `code`              | [Code](../../core-api-reference/common-resources.md#code)!           |                                                                                |
| `order`             | `Int!`                                                               |                                                                                |
| `catalog`           | [Catalog](../../core-api-reference/organizations/#catalog)!          |                                                                                |
| `organization`      | [Organization](../../core-api-reference/organizations/#organization) |                                                                                |
| `meta`              | [CatalogItemMeta](../#catalogitemmeta)!                              |                                                                                |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraint](types.md#assetgrouptypeconstraint)!]!   | The asset types allowed in groups of this type, with optional quantity limits. |

### AssetGroupTypeConstraint

A constraint defining which asset types can be included in an asset group type.

| Field       | Type                             | Description                                                                           |
| ----------- | -------------------------------- | ------------------------------------------------------------------------------------- |
| `assetType` | [AssetType](types.md#assettype)! | The asset type allowed in the group.                                                  |
| `maxItems`  | `Int`                            | The maximum number of assets of this type allowed in one group. Null means unlimited. |

### GeoObjectType

A classification type for geographic objects.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field                    | Type                                                                       | Description                                                                          |
| ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `id`                     | `ID!`                                                                      |                                                                                      |
| `version`                | `Int!`                                                                     |                                                                                      |
| `title`                  | `String!`                                                                  |                                                                                      |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                      |
| `order`                  | `Int!`                                                                     |                                                                                      |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                      |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                      |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                      |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

### ScheduleType

A classification type for schedules.

**Implements:** [`CatalogItem`](../#catalogitem), [`Node`](../../core-api-reference/common-resources.md#node), [`Versioned`](../../core-api-reference/common-resources.md#versioned), [`Titled`](../../core-api-reference/common-resources.md#titled)

| Field                    | Type                                                                       | Description                                                                        |
| ------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                                      |                                                                                    |
| `version`                | `Int!`                                                                     |                                                                                    |
| `title`                  | `String!`                                                                  |                                                                                    |
| `code`                   | [Code](../../core-api-reference/common-resources.md#code)!                 |                                                                                    |
| `order`                  | `Int!`                                                                     |                                                                                    |
| `catalog`                | [Catalog](../../core-api-reference/organizations/#catalog)!                |                                                                                    |
| `organization`           | [Organization](../../core-api-reference/organizations/#organization)       |                                                                                    |
| `meta`                   | [CatalogItemMeta](../#catalogitemmeta)!                                    |                                                                                    |
| `customFieldDefinitions` | \[[CustomFieldDefinition](../../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

### AssetTypePayload

The result of an asset type mutation.

| Field       | Type                             | Description                        |
| ----------- | -------------------------------- | ---------------------------------- |
| `assetType` | [AssetType](types.md#assettype)! | The created or updated asset type. |

### AssetGroupTypePayload

The result of an asset group type mutation.

| Field            | Type                                       | Description                              |
| ---------------- | ------------------------------------------ | ---------------------------------------- |
| `assetGroupType` | [AssetGroupType](types.md#assetgrouptype)! | The created or updated asset group type. |

### GeoObjectTypePayload

The result of a geo object type mutation.

| Field           | Type                                     | Description                             |
| --------------- | ---------------------------------------- | --------------------------------------- |
| `geoObjectType` | [GeoObjectType](types.md#geoobjecttype)! | The created or updated geo object type. |

### ScheduleTypePayload

The result of a schedule type mutation.

| Field          | Type                                   | Description                           |
| -------------- | -------------------------------------- | ------------------------------------- |
| `scheduleType` | [ScheduleType](types.md#scheduletype)! | The created or updated schedule type. |

## Inputs

### AssetTypeCreateInput

Input for creating an asset type.

| Field            | Type                                                       | Description                              |
| ---------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `organizationId` | `ID!`                                                      | The organization that will own the item. |
| `code`           | [Code](../../core-api-reference/common-resources.md#code)! | The machine-readable code.               |
| `title`          | `String!`                                                  | The display name.                        |
| `order`          | `Int`                                                      | The display order.                       |
| `meta`           | [CatalogItemMetaInput](../#catalogitemmetainput)           | The display properties.                  |

### AssetTypeUpdateInput

Input for updating an asset type.

| Field     | Type                                             | Description                                 |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                            | The item ID to update.                      |
| `version` | `Int!`                                           | The current version for optimistic locking. |
| `title`   | `String`                                         | The new display name.                       |
| `order`   | `Int`                                            | The new display order.                      |
| `meta`    | [CatalogItemMetaInput](../#catalogitemmetainput) | The display properties.                     |

### AssetGroupTypeCreateInput

Input for creating an asset group type.

| Field               | Type                                                                        | Description                                   |
| ------------------- | --------------------------------------------------------------------------- | --------------------------------------------- |
| `organizationId`    | `ID!`                                                                       | The organization that will own the item.      |
| `code`              | [Code](../../core-api-reference/common-resources.md#code)!                  | The machine-readable code.                    |
| `title`             | `String!`                                                                   | The display name.                             |
| `order`             | `Int`                                                                       | The display order.                            |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraintInput](types.md#assetgrouptypeconstraintinput)!] | The allowed asset types with optional limits. |
| `meta`              | [CatalogItemMetaInput](../#catalogitemmetainput)                            | The display properties.                       |

### AssetGroupTypeUpdateInput

Input for updating an asset group type.

| Field               | Type                                                                        | Description                                        |
| ------------------- | --------------------------------------------------------------------------- | -------------------------------------------------- |
| `id`                | `ID!`                                                                       | The item ID to update.                             |
| `version`           | `Int!`                                                                      | The current version for optimistic locking.        |
| `title`             | `String`                                                                    | The new display name.                              |
| `order`             | `Int`                                                                       | The new display order.                             |
| `allowedAssetTypes` | \[[AssetGroupTypeConstraintInput](types.md#assetgrouptypeconstraintinput)!] | Replace allowed asset types. Null means no change. |
| `meta`              | [CatalogItemMetaInput](../#catalogitemmetainput)                            | The display properties.                            |

### AssetGroupTypeConstraintInput

Input for a constraint defining allowed asset types in an asset group type.

| Field         | Type  | Description                                            |
| ------------- | ----- | ------------------------------------------------------ |
| `assetTypeId` | `ID!` | The asset type ID.                                     |
| `maxItems`    | `Int` | The maximum assets of this type. Null means unlimited. |

### GeoObjectTypeCreateInput

Input for creating a geo object type.

| Field            | Type                                                       | Description                              |
| ---------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `organizationId` | `ID!`                                                      | The organization that will own the item. |
| `code`           | [Code](../../core-api-reference/common-resources.md#code)! | The machine-readable code.               |
| `title`          | `String!`                                                  | The display name.                        |
| `order`          | `Int`                                                      | The display order.                       |
| `meta`           | [CatalogItemMetaInput](../#catalogitemmetainput)           | The display properties.                  |

### GeoObjectTypeUpdateInput

Input for updating a geo object type.

| Field     | Type                                             | Description                                 |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                            | The item ID to update.                      |
| `version` | `Int!`                                           | The current version for optimistic locking. |
| `title`   | `String`                                         | The new display name.                       |
| `order`   | `Int`                                            | The new display order.                      |
| `meta`    | [CatalogItemMetaInput](../#catalogitemmetainput) | The display properties.                     |

### ScheduleTypeCreateInput

Input for creating a schedule type.

| Field            | Type                                                       | Description                              |
| ---------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `organizationId` | `ID!`                                                      | The organization that will own the item. |
| `code`           | [Code](../../core-api-reference/common-resources.md#code)! | The machine-readable code.               |
| `title`          | `String!`                                                  | The display name.                        |
| `order`          | `Int`                                                      | The display order.                       |
| `meta`           | [CatalogItemMetaInput](../#catalogitemmetainput)           | The display properties.                  |

### ScheduleTypeUpdateInput

Input for updating a schedule type.

| Field     | Type                                             | Description                                 |
| --------- | ------------------------------------------------ | ------------------------------------------- |
| `id`      | `ID!`                                            | The item ID to update.                      |
| `version` | `Int!`                                           | The current version for optimistic locking. |
| `title`   | `String`                                         | The new display name.                       |
| `order`   | `Int`                                            | The new display order.                      |
| `meta`    | [CatalogItemMetaInput](../#catalogitemmetainput) | The display properties.                     |
