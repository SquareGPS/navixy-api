# Organizations

Organizations form the top-level container for all business data. Each organization operates as an isolated tenant with its own users, devices, assets, and configuration.

## Queries

### organization

Retrieves an organization by its ID.

```graphql
organization("The ID of the organization to retrieve." id: ID!): Organization
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the organization to retrieve. |

**Output types:**

<details>

<summary><code>Organization</code></summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../devices/types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](../schedules/types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

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
| `filter` | [OrganizationFilter](../organizations.md#organizationfilter) |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | [OrganizationOrder](../organizations.md#organizationorder) |  |
| `direction` | `ASC }` |  |

**Input types:**

<details>

<summary><code>OrganizationFilter</code></summary>

Filtering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentIds` | `[ID!]` | Filter by parent organizations (OR within field). |
| `isActive` | `Boolean` | Filter by active status. |

</details>

<details>

<summary><code>OrganizationOrder</code></summary>

Ordering options for organizations.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [OrganizationOrderField](../organizations.md#organizationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>OrganizationConnection</code></summary>

A paginated list of Organization items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge](../organizations.md#organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](../organizations.md#organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

</details>

<details>

<summary><code>PageInfo (entity)</code></summary>

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
organizationCreate("The input fields for creating the organization." input: OrganizationCreateInput!): OrganizationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [OrganizationCreateInput](../organizations.md#organizationcreateinput)! | The input fields for creating the organization. |

**Input types:**

<details>

<summary><code>OrganizationCreateInput</code></summary>

Input for creating a new organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | `[OrganizationFeature!] = []` | The feature flags to enable. |

</details>

**Output types:**

<details>

<summary><code>OrganizationPayload</code></summary>

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](../organizations.md#organization)! | The created or updated organization. |

</details>

<details>

<summary><code>Organization (entity)</code></summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../devices/types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](../schedules/types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

</details>

---

### organizationUpdate

Updates an existing organization.

```graphql
organizationUpdate("The input fields for updating the organization." input: OrganizationUpdateInput!): OrganizationPayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [OrganizationUpdateInput](../organizations.md#organizationupdateinput)! | The input fields for updating the organization. |

**Input types:**

<details>

<summary><code>OrganizationUpdateInput</code></summary>

Input for updating an existing organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `externalId` | `String` | The new external identifier. |
| `isActive` | `Boolean` | The new active status. |
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!] | The new feature flags. |

</details>

**Output types:**

<details>

<summary><code>OrganizationPayload</code></summary>

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](../organizations.md#organization)! | The created or updated organization. |

</details>

<details>

<summary><code>Organization (entity)</code></summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../devices/types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](../schedules/types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

</details>

---

### organizationDelete

Deletes an organization and all its data.

```graphql
organizationDelete("The input fields for deleting the organization." input: OrganizationDeleteInput!): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | [OrganizationDeleteInput](../organizations.md#organizationdeleteinput)! | The input fields for deleting the organization. |

**Input types:**

<details>

<summary><code>OrganizationDeleteInput</code></summary>

Input for deleting an organization and all its data.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The organization ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

</details>

**Output types:**

<details>

<summary><code>DeletePayload</code></summary>

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
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](../organizations.md#organization) | The parent organization in the hierarchy. Null for root organizations. |
| `filter` | [OrganizationChildrenFilter](../organizations.md#organizationchildrenfilter) | Filtering options for the returned children. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `OrganizationOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned children. |
| `filter` | [MemberFilter](members.md#memberfilter) | Filtering options for the returned members. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `MemberOrder = { field: ASSIGNED_AT, direction: DESC }` | The ordering options for the returned members. |
| `filter` | [DeviceFilter](../devices/types.md#devicefilter) | Filtering options for the returned devices. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `DeviceOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned devices. |
| `filter` | [AssetFilter](../assets/types.md#assetfilter) | Filtering options for the returned assets. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `AssetOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned assets. |
| `filter` | [GeoObjectFilter](../geo-objects/types.md#geoobjectfilter) | Filtering options for the returned geo objects. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `GeoObjectOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned geo objects. |
| `filter` | [ScheduleFilter](../schedules/types.md#schedulefilter) | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder = { field: TITLE, direction: ASC }` | The ordering options for the returned schedules. |

---

### OrganizationPayload

The result of an organization mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organization` | [Organization](../organizations.md#organization)! | The created or updated organization. |

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
| `field` | [OrganizationOrderField](../organizations.md#organizationorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### OrganizationCreateInput

Input for creating a new organization.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parentId` | `ID` | The parent organization ID. Null for root organizations. |
| `title` | `String!` | The display name. |
| `externalId` | `String` | An external system identifier. |
| `features` | `[OrganizationFeature!] = []` | The feature flags to enable. |

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
| `features` | [[OrganizationFeature](../organizations.md#organizationfeature)!] | The new feature flags. |

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
| `edges` | [[OrganizationEdge](../organizations.md#organizationedge)!]! | A list of edges. |
| `nodes` | [[Organization](../organizations.md#organization)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### OrganizationEdge

An edge in the Organization connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Organization](../organizations.md#organization)! | The organization at the end of the edge. |

---
