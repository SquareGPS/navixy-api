# Organizations

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

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

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

</details>

<details>

<summary>OrganizationConnection (entity)</summary>

A paginated list of Organization items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](#type-organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](#type-organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

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
| `field` | [OrganizationOrderField](#type-organizationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>OrganizationConnection</summary>

A paginated list of Organization items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](#type-organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](#type-organization)!]! | A list of nodes in the connection (without edge metadata). |
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
| `features` | [[OrganizationFeature](#type-organizationfeature)!] | The feature flags to enable. |

</details>

**Output types:**

<details>

<summary>OrganizationPayload</summary>

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](#type-organization)! | The created or updated organization. |

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
| `features` | [[OrganizationFeature](#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

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
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature](#type-organizationfeature)!] | The new feature flags. |

</details>

**Output types:**

<details>

<summary>OrganizationPayload</summary>

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](#type-organization)! | The created or updated organization. |

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
| `features` | [[OrganizationFeature](#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

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
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

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

<a id="type-organization"></a>

### Organization

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](../devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](../assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](../geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](../schedules.md#type-scheduleconnection)! | The schedules owned by this organization. |

---

<a id="type-organizationpayload"></a>

### OrganizationPayload

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](#type-organization)! | The created or updated organization. |

---

## Inputs

<a id="type-organizationfilter"></a>

### OrganizationFilter

Filtering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentIds` | `[ID!]` | Filter by parent organizations (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

---

<a id="type-organizationchildrenfilter"></a>

### OrganizationChildrenFilter

Filtering options for organization children. Excludes parentId as it is implicit.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isActive` | `Boolean` | Filter by active status. |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

<a id="type-organizationorder"></a>

### OrganizationOrder

Ordering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [OrganizationOrderField](#type-organizationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-organizationcreateinput"></a>

### OrganizationCreateInput

Input for creating a new organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | [[OrganizationFeature](#type-organizationfeature)!] | The feature flags to enable. |

---

<a id="type-organizationupdateinput"></a>

### OrganizationUpdateInput

Input for updating an existing organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature](#type-organizationfeature)!] | The new feature flags. |

---

<a id="type-organizationdeleteinput"></a>

### OrganizationDeleteInput

Input for deleting an organization and all its data.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

## Enums

<a id="type-organizationfeature"></a>

### OrganizationFeature

Feature flags that can be enabled for an organization.

| Value | Description |
| ----- | ----------- |
| `DEALER` | The organization can create and manage child organizations (dealer/reseller model). |
| `WHITELABEL` | The organization has custom branding including domain, logo, and color scheme. |

---

<a id="type-organizationorderfield"></a>

### OrganizationOrderField

Fields available for ordering organizations.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

<a id="type-organizationconnection"></a>

### OrganizationConnection

A paginated list of Organization items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](#type-organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](#type-organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-organizationedge"></a>

### OrganizationEdge

An edge in the Organization connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Organization](#type-organization)! | The organization at the end of the edge. |

---
