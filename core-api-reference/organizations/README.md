# Organizations

Organizations represent companies or business units in the hierarchy.

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

<summary><code>Catalog</code></summary>

| Field          | Type                                                            | Description                                 |
| -------------- | --------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                           |                                             |
| `version`      | `Int!`                                                          |                                             |
| `title`        | `String!`                                                       |                                             |
| `code`         | [Code](../common-resources.md#code)!                            |                                             |
| `order`        | `Int!`                                                          |                                             |
| `catalog`      | [Catalog](./#catalog)!                                          | Self-reference for the meta-catalog.        |
| `organization` | [Organization](./#organization)                                 |                                             |
| `meta`         | [CatalogItemMeta](../../catalogs/#catalogitemmeta)!             |                                             |
| `module`       | [Module](../../catalogs/system.md#module)!                      | The module this catalog is associated with. |
| `items`        | [CatalogItemConnection](../../catalogs/#catalogitemconnection)! | The items in this catalog.                  |

</details>

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

| Name             | Type                                                   | Description                                                                                   |
| ---------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                                  | The organization to retrieve catalogs for.                                                    |
| `filter`         | [CatalogItemFilter](../../catalogs/#catalogitemfilter) | Filtering options for the returned catalogs.                                                  |
| `first`          | `Int`                                                  | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                               | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                                  | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                               | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [CatalogItemOrder](../../catalogs/#catalogitemorder)   | The ordering options for the returned catalogs.                                               |

**Input types:**

<details>

<summary><code>CatalogItemFilter</code></summary>

| Field           | Type                                    | Description                                         |
| --------------- | --------------------------------------- | --------------------------------------------------- |
| `titleContains` | `String`                                | Partial match on title (case-insensitive contains). |
| `codes`         | \[[Code](../common-resources.md#code)!] | Match any of these codes.                           |

</details>

<details>

<summary><code>CatalogItemOrder</code></summary>

| Field       | Type                                                            | Description             |
| ----------- | --------------------------------------------------------------- | ----------------------- |
| `field`     | [CatalogItemOrderField](../../catalogs/#catalogitemorderfield)! | The field to order by.  |
| `direction` | [OrderDirection](../common-resources.md#orderdirection)!        | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>CatalogConnection</code></summary>

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[CatalogEdge](./#catalogedge)!]!            | A list of edges.                                           |
| `nodes`    | \[[Catalog](./#catalog)!]!                    | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Catalog (node)</code></summary>

| Field          | Type                                                            | Description                                 |
| -------------- | --------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                           |                                             |
| `version`      | `Int!`                                                          |                                             |
| `title`        | `String!`                                                       |                                             |
| `code`         | [Code](../common-resources.md#code)!                            |                                             |
| `order`        | `Int!`                                                          |                                             |
| `catalog`      | [Catalog](./#catalog)!                                          | Self-reference for the meta-catalog.        |
| `organization` | [Organization](./#organization)                                 |                                             |
| `meta`         | [CatalogItemMeta](../../catalogs/#catalogitemmeta)!             |                                             |
| `module`       | [Module](../../catalogs/system.md#module)!                      | The module this catalog is associated with. |
| `items`        | [CatalogItemConnection](../../catalogs/#catalogitemconnection)! | The items in this catalog.                  |

</details>

### organization

Retrieves an organization by its ID.

```graphql
organization(id: ID!): Organization
```

**Arguments**

| Name | Type  | Description                             |
| ---- | ----- | --------------------------------------- |
| `id` | `ID!` | The ID of the organization to retrieve. |

**Output types:**

<details>

<summary><code>Organization</code></summary>

| Field        | Type                                                                   | Description                                                            |
| ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`         | `ID!`                                                                  |                                                                        |
| `version`    | `Int!`                                                                 |                                                                        |
| `title`      | `String!`                                                              |                                                                        |
| `externalId` | `String`                                                               | An external system identifier for integration purposes.                |
| `isActive`   | `Boolean!`                                                             | Whether this organization is active.                                   |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!]!                     | The feature flags enabled for this organization.                       |
| `parent`     | [Organization](./#organization)                                        | The parent organization in the hierarchy. Null for root organizations. |
| `children`   | [OrganizationConnection](./#organizationconnection)!                   | The child organizations.                                               |
| `members`    | [MemberConnection](members.md#memberconnection)!                       | The members of this organization.                                      |
| `devices`    | [DeviceConnection](../../devices/types.md#deviceconnection)!           | The devices owned by this organization.                                |
| `assets`     | [AssetConnection](../assets/#assetconnection)!                         | The assets owned by this organization.                                 |
| `geoObjects` | [GeoObjectConnection](../../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization.                     |
| `schedules`  | [ScheduleConnection](../../schedules.md#scheduleconnection)!           | The schedules owned by this organization.                              |

</details>

### organizations

Lists organizations.

```graphql
organizations(
  filter: OrganizationFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: OrganizationOrder = { field: TITLE, direction: ASC }
): OrganizationConnection!
```

**Arguments**

| Name      | Type                                        | Description                                                                                   |
| --------- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `filter`  | [OrganizationFilter](./#organizationfilter) | Filtering options for the returned organizations.                                             |
| `first`   | `Int`                                       | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`   | `String`                                    | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`    | `Int`                                       | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`  | `String`                                    | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | [OrganizationOrder](./#organizationorder)   | The ordering options for the returned organizations.                                          |

**Input types:**

<details>

<summary><code>OrganizationFilter</code></summary>

| Field       | Type      | Description                                       |
| ----------- | --------- | ------------------------------------------------- |
| `parentIds` | `[ID!]`   | Filter by parent organizations (OR within field). |
| `isActive`  | `Boolean` | Filter by active status.                          |

</details>

<details>

<summary><code>OrganizationOrder</code></summary>

| Field       | Type                                                     | Description             |
| ----------- | -------------------------------------------------------- | ----------------------- |
| `field`     | [OrganizationOrderField](./#organizationorderfield)!     | The field to order by.  |
| `direction` | [OrderDirection](../common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>OrganizationConnection</code></summary>

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[OrganizationEdge](./#organizationedge)!]!  | A list of edges.                                           |
| `nodes`    | \[[Organization](./#organization)!]!          | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Organization (node)</code></summary>

| Field        | Type                                                                   | Description                                                            |
| ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`         | `ID!`                                                                  |                                                                        |
| `version`    | `Int!`                                                                 |                                                                        |
| `title`      | `String!`                                                              |                                                                        |
| `externalId` | `String`                                                               | An external system identifier for integration purposes.                |
| `isActive`   | `Boolean!`                                                             | Whether this organization is active.                                   |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!]!                     | The feature flags enabled for this organization.                       |
| `parent`     | [Organization](./#organization)                                        | The parent organization in the hierarchy. Null for root organizations. |
| `children`   | [OrganizationConnection](./#organizationconnection)!                   | The child organizations.                                               |
| `members`    | [MemberConnection](members.md#memberconnection)!                       | The members of this organization.                                      |
| `devices`    | [DeviceConnection](../../devices/types.md#deviceconnection)!           | The devices owned by this organization.                                |
| `assets`     | [AssetConnection](../assets/#assetconnection)!                         | The assets owned by this organization.                                 |
| `geoObjects` | [GeoObjectConnection](../../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization.                     |
| `schedules`  | [ScheduleConnection](../../schedules.md#scheduleconnection)!           | The schedules owned by this organization.                              |

</details>

## Mutations

### organizationCreate

Creates a new organization.

```graphql
organizationCreate(
  input: OrganizationCreateInput!
): OrganizationPayload
```

**Arguments**

| Name    | Type                                                   | Description                                     |
| ------- | ------------------------------------------------------ | ----------------------------------------------- |
| `input` | [OrganizationCreateInput](./#organizationcreateinput)! | The input fields for creating the organization. |

**Input types:**

<details>

<summary><code>OrganizationCreateInput</code></summary>

| Field        | Type                                              | Description                                              |
| ------------ | ------------------------------------------------- | -------------------------------------------------------- |
| `parentId`   | `ID`                                              | The parent organization ID. Null for root organizations. |
| `title`      | `String!`                                         | The display name.                                        |
| `externalId` | `String`                                          | An external system identifier.                           |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!] | The feature flags to enable.                             |

</details>

**Output types:**

<details>

<summary><code>OrganizationPayload</code></summary>

| Field          | Type                             | Description                          |
| -------------- | -------------------------------- | ------------------------------------ |
| `organization` | [Organization](./#organization)! | The created or updated organization. |

</details>

<details>

<summary><code>Organization (entity)</code></summary>

| Field        | Type                                                                   | Description                                                            |
| ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`         | `ID!`                                                                  |                                                                        |
| `version`    | `Int!`                                                                 |                                                                        |
| `title`      | `String!`                                                              |                                                                        |
| `externalId` | `String`                                                               | An external system identifier for integration purposes.                |
| `isActive`   | `Boolean!`                                                             | Whether this organization is active.                                   |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!]!                     | The feature flags enabled for this organization.                       |
| `parent`     | [Organization](./#organization)                                        | The parent organization in the hierarchy. Null for root organizations. |
| `children`   | [OrganizationConnection](./#organizationconnection)!                   | The child organizations.                                               |
| `members`    | [MemberConnection](members.md#memberconnection)!                       | The members of this organization.                                      |
| `devices`    | [DeviceConnection](../../devices/types.md#deviceconnection)!           | The devices owned by this organization.                                |
| `assets`     | [AssetConnection](../assets/#assetconnection)!                         | The assets owned by this organization.                                 |
| `geoObjects` | [GeoObjectConnection](../../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization.                     |
| `schedules`  | [ScheduleConnection](../../schedules.md#scheduleconnection)!           | The schedules owned by this organization.                              |

</details>

### organizationUpdate

Updates an existing organization.

```graphql
organizationUpdate(
  input: OrganizationUpdateInput!
): OrganizationPayload
```

**Arguments**

| Name    | Type                                                   | Description                                     |
| ------- | ------------------------------------------------------ | ----------------------------------------------- |
| `input` | [OrganizationUpdateInput](./#organizationupdateinput)! | The input fields for updating the organization. |

**Input types:**

<details>

<summary><code>OrganizationUpdateInput</code></summary>

| Field        | Type                                              | Description                                 |
| ------------ | ------------------------------------------------- | ------------------------------------------- |
| `id`         | `ID!`                                             | The organization ID to update.              |
| `version`    | `Int!`                                            | The current version for optimistic locking. |
| `title`      | `String`                                          | The new display name.                       |
| `externalId` | `String`                                          | The new external identifier.                |
| `isActive`   | `Boolean`                                         | The new active status.                      |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!] | The new feature flags.                      |

</details>

**Output types:**

<details>

<summary><code>OrganizationPayload</code></summary>

| Field          | Type                             | Description                          |
| -------------- | -------------------------------- | ------------------------------------ |
| `organization` | [Organization](./#organization)! | The created or updated organization. |

</details>

<details>

<summary><code>Organization (entity)</code></summary>

| Field        | Type                                                                   | Description                                                            |
| ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`         | `ID!`                                                                  |                                                                        |
| `version`    | `Int!`                                                                 |                                                                        |
| `title`      | `String!`                                                              |                                                                        |
| `externalId` | `String`                                                               | An external system identifier for integration purposes.                |
| `isActive`   | `Boolean!`                                                             | Whether this organization is active.                                   |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!]!                     | The feature flags enabled for this organization.                       |
| `parent`     | [Organization](./#organization)                                        | The parent organization in the hierarchy. Null for root organizations. |
| `children`   | [OrganizationConnection](./#organizationconnection)!                   | The child organizations.                                               |
| `members`    | [MemberConnection](members.md#memberconnection)!                       | The members of this organization.                                      |
| `devices`    | [DeviceConnection](../../devices/types.md#deviceconnection)!           | The devices owned by this organization.                                |
| `assets`     | [AssetConnection](../assets/#assetconnection)!                         | The assets owned by this organization.                                 |
| `geoObjects` | [GeoObjectConnection](../../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization.                     |
| `schedules`  | [ScheduleConnection](../../schedules.md#scheduleconnection)!           | The schedules owned by this organization.                              |

</details>

### organizationDelete

Deletes an organization and all its data.

```graphql
organizationDelete(
  input: OrganizationDeleteInput!
): DeletePayload
```

**Arguments**

| Name    | Type                                                   | Description                                     |
| ------- | ------------------------------------------------------ | ----------------------------------------------- |
| `input` | [OrganizationDeleteInput](./#organizationdeleteinput)! | The input fields for deleting the organization. |

**Input types:**

<details>

<summary><code>OrganizationDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The organization ID to delete.              |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

</details>

## Types

### OrganizationConnection

A paginated list of Organization items.

**Implements:** [`Connection`](../common-resources.md#connection)

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[OrganizationEdge](./#organizationedge)!]!  | A list of edges.                                           |
| `nodes`    | \[[Organization](./#organization)!]!          | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

### OrganizationEdge

An edge in the Organization connection.

**Implements:** [`Edge`](../common-resources.md#edge)

| Field    | Type                             | Description                              |
| -------- | -------------------------------- | ---------------------------------------- |
| `cursor` | `String!`                        | An opaque cursor for this edge.          |
| `node`   | [Organization](./#organization)! | The organization at the end of the edge. |

### CatalogConnection

A paginated list of Catalog items.

**Implements:** [`Connection`](../common-resources.md#connection)

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[CatalogEdge](./#catalogedge)!]!            | A list of edges.                                           |
| `nodes`    | \[[Catalog](./#catalog)!]!                    | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../common-resources.md#countinfo) | The total count of items matching the filter.              |

### CatalogEdge

An edge in the Catalog connection.

**Implements:** [`Edge`](../common-resources.md#edge)

| Field    | Type                   | Description                         |
| -------- | ---------------------- | ----------------------------------- |
| `cursor` | `String!`              | An opaque cursor for this edge.     |
| `node`   | [Catalog](./#catalog)! | The catalog at the end of the edge. |

### Catalog

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [`CatalogItem`](../../catalogs/#catalogitem), [`Node`](../common-resources.md#node), [`Versioned`](../common-resources.md#versioned), [`Titled`](../common-resources.md#titled)

| Field          | Type                                                            | Description                                 |
| -------------- | --------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                           |                                             |
| `version`      | `Int!`                                                          |                                             |
| `title`        | `String!`                                                       |                                             |
| `code`         | [Code](../common-resources.md#code)!                            |                                             |
| `order`        | `Int!`                                                          |                                             |
| `catalog`      | [Catalog](./#catalog)!                                          | Self-reference for the meta-catalog.        |
| `organization` | [Organization](./#organization)                                 |                                             |
| `meta`         | [CatalogItemMeta](../../catalogs/#catalogitemmeta)!             |                                             |
| `module`       | [Module](../../catalogs/system.md#module)!                      | The module this catalog is associated with. |
| `items`        | [CatalogItemConnection](../../catalogs/#catalogitemconnection)! | The items in this catalog.                  |

### Organization

An organization in the hierarchy that owns entities and users.

**Implements:** [`Node`](../common-resources.md#node), [`Versioned`](../common-resources.md#versioned), [`Titled`](../common-resources.md#titled)

| Field        | Type                                                                   | Description                                                            |
| ------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`         | `ID!`                                                                  |                                                                        |
| `version`    | `Int!`                                                                 |                                                                        |
| `title`      | `String!`                                                              |                                                                        |
| `externalId` | `String`                                                               | An external system identifier for integration purposes.                |
| `isActive`   | `Boolean!`                                                             | Whether this organization is active.                                   |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!]!                     | The feature flags enabled for this organization.                       |
| `parent`     | [Organization](./#organization)                                        | The parent organization in the hierarchy. Null for root organizations. |
| `children`   | [OrganizationConnection](./#organizationconnection)!                   | The child organizations.                                               |
| `members`    | [MemberConnection](members.md#memberconnection)!                       | The members of this organization.                                      |
| `devices`    | [DeviceConnection](../../devices/types.md#deviceconnection)!           | The devices owned by this organization.                                |
| `assets`     | [AssetConnection](../assets/#assetconnection)!                         | The assets owned by this organization.                                 |
| `geoObjects` | [GeoObjectConnection](../../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization.                     |
| `schedules`  | [ScheduleConnection](../../schedules.md#scheduleconnection)!           | The schedules owned by this organization.                              |

### OrganizationPayload

The result of an organization mutation.

| Field          | Type                             | Description                          |
| -------------- | -------------------------------- | ------------------------------------ |
| `organization` | [Organization](./#organization)! | The created or updated organization. |

## Inputs

### OrganizationFilter

Filtering options for organizations.

| Field       | Type      | Description                                       |
| ----------- | --------- | ------------------------------------------------- |
| `parentIds` | `[ID!]`   | Filter by parent organizations (OR within field). |
| `isActive`  | `Boolean` | Filter by active status.                          |

### OrganizationChildrenFilter

Filtering options for organization children. Excludes parentId as it is implicit.

| Field           | Type      | Description                                         |
| --------------- | --------- | --------------------------------------------------- |
| `isActive`      | `Boolean` | Filter by active status.                            |
| `titleContains` | `String`  | Partial match on title (case-insensitive contains). |

### OrganizationOrder

Ordering options for organizations.

| Field       | Type                                                     | Description             |
| ----------- | -------------------------------------------------------- | ----------------------- |
| `field`     | [OrganizationOrderField](./#organizationorderfield)!     | The field to order by.  |
| `direction` | [OrderDirection](../common-resources.md#orderdirection)! | The direction to order. |

### OrganizationCreateInput

Input for creating a new organization.

| Field        | Type                                              | Description                                              |
| ------------ | ------------------------------------------------- | -------------------------------------------------------- |
| `parentId`   | `ID`                                              | The parent organization ID. Null for root organizations. |
| `title`      | `String!`                                         | The display name.                                        |
| `externalId` | `String`                                          | An external system identifier.                           |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!] | The feature flags to enable.                             |

### OrganizationUpdateInput

Input for updating an existing organization.

| Field        | Type                                              | Description                                 |
| ------------ | ------------------------------------------------- | ------------------------------------------- |
| `id`         | `ID!`                                             | The organization ID to update.              |
| `version`    | `Int!`                                            | The current version for optimistic locking. |
| `title`      | `String`                                          | The new display name.                       |
| `externalId` | `String`                                          | The new external identifier.                |
| `isActive`   | `Boolean`                                         | The new active status.                      |
| `features`   | \[[OrganizationFeature](./#organizationfeature)!] | The new feature flags.                      |

### OrganizationDeleteInput

Input for deleting an organization and all its data.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The organization ID to delete.              |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### OrganizationFeature

Feature flags that can be enabled for an organization.

| Value        | Description                                                                         |
| ------------ | ----------------------------------------------------------------------------------- |
| `DEALER`     | The organization can create and manage child organizations (dealer/reseller model). |
| `WHITELABEL` | The organization has custom branding including domain, logo, and color scheme.      |

### OrganizationOrderField

Fields available for ordering organizations.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |
