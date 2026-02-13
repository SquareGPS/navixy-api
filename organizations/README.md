# Organizations

Organizations form the top-level container for all business data. Each organization operates as an isolated tenant with its own users, devices, assets, and configuration.

## Queries

### organization

Retrieves an organization by its ID.

```graphql
organization(id: ID!): Organization
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the organization to retrieve. |

**Output types:**

<details>

<summary>Organization</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules/types.md#scheduleconnection)! | The schedules owned by this organization. |

</details>

<details>

<summary>OrganizationConnection (entity)</summary>

A paginated list of Organization items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](#organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](#organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

---

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `filter` | `OrganizationFilter` | Filtering options for the returned organizations. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder` | The ordering options for the returned organizations. |

**Input types:**

<details>

<summary>OrganizationFilter</summary>

Filtering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentIds` | `[ID!]` | Filter by parent organizations (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

</details>

<details>

<summary>OrganizationOrder</summary>

Ordering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [OrganizationOrderField](#organizationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>OrganizationConnection</summary>

A paginated list of Organization items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](#organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](#organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

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

### organizationCreate

Creates a new organization.

```graphql
organizationCreate(
    input: OrganizationCreateInput!
  ): OrganizationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `OrganizationCreateInput!` | The input fields for creating the organization. |

**Input types:**

<details>

<summary>OrganizationCreateInput</summary>

Input for creating a new organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | [[OrganizationFeature](#organizationfeature)!] | The feature flags to enable. |

</details>

**Output types:**

<details>

<summary>OrganizationPayload</summary>

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](#organization)! | The created or updated organization. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules/types.md#scheduleconnection)! | The schedules owned by this organization. |

</details>

---

### organizationUpdate

Updates an existing organization.

```graphql
organizationUpdate(
    input: OrganizationUpdateInput!
  ): OrganizationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `OrganizationUpdateInput!` | The input fields for updating the organization. |

**Input types:**

<details>

<summary>OrganizationUpdateInput</summary>

Input for updating an existing organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature](#organizationfeature)!] | The new feature flags. |

</details>

**Output types:**

<details>

<summary>OrganizationPayload</summary>

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](#organization)! | The created or updated organization. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules/types.md#scheduleconnection)! | The schedules owned by this organization. |

</details>

---

### organizationDelete

Deletes an organization and all its data.

```graphql
organizationDelete(
    input: OrganizationDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `OrganizationDeleteInput!` | The input fields for deleting the organization. |

**Input types:**

<details>

<summary>OrganizationDeleteInput</summary>

Input for deleting an organization and all its data.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

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

### Organization

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules/types.md#scheduleconnection)! | The schedules owned by this organization. |

---

### OrganizationPayload

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](#organization)! | The created or updated organization. |

---

## Inputs

### OrganizationFilter

Filtering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentIds` | `[ID!]` | Filter by parent organizations (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

---

### OrganizationChildrenFilter

Filtering options for organization children. Excludes parentId as it is implicit.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

### OrganizationOrder

Ordering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [OrganizationOrderField](#organizationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### OrganizationCreateInput

Input for creating a new organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | [[OrganizationFeature](#organizationfeature)!] | The feature flags to enable. |

---

### OrganizationUpdateInput

Input for updating an existing organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature](#organizationfeature)!] | The new feature flags. |

---

### OrganizationDeleteInput

Input for deleting an organization and all its data.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

## Enums

### OrganizationFeature

Feature flags that can be enabled for an organization.

| Value | Description |
| ----- | ----------- |
| `DEALER` | The organization can create and manage child organizations (dealer/reseller model). |
| `WHITELABEL` | The organization has custom branding including domain, logo, and color scheme. |

---

### OrganizationOrderField

Fields available for ordering organizations.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

### OrganizationConnection

A paginated list of Organization items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](#organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](#organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### OrganizationEdge

An edge in the Organization connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Organization](#organization)! | The organization at the end of the edge. |

---
