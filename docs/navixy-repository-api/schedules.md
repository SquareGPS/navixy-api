# Schedules

{% include ".gitbook/includes/navixy-repository-api-is-a-....md" %}

Schedules define time-based rules using iCalendar ([RFC 5545](https://www.rfc-editor.org/rfc/rfc5545.html)) format for recurring events, working hours, and time-triggered automation.

## Queries

### schedule

Retrieves a schedule by its ID.

```graphql
schedule(id: ID!): Schedule
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the schedule to retrieve. |

**Output types:**

<details>

<summary>Schedule</summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](common.md#type-node), [Titled](common.md#type-titled), [Versioned](common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](organizations/README.md#type-organization)! | The organization that owns this schedule. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule. |

</details>

<details>

<summary>Organization (entity)</summary>

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](common.md#type-node), [Versioned](common.md#type-versioned), [Titled](common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `externalId` | `String` | An external system identifier for integration purposes. |
| `isActive` | `Boolean!` | Whether this organization is active. |
| `features` | [[OrganizationFeature](organizations/README.md#type-organizationfeature)!]! | The feature flags enabled for this organization. |
| `parent` | [Organization](organizations/README.md#type-organization) | The parent organization in the hierarchy. Null for root organizations. |
| `children` | [OrganizationConnection](organizations/README.md#type-organizationconnection)! | The child organizations. |
| `members` | [MemberConnection](organizations/members.md#type-memberconnection)! | The members of this organization. |
| `devices` | [DeviceConnection](devices/types.md#type-deviceconnection)! | The devices owned by this organization. |
| `assets` | [AssetConnection](assets/types.md#type-assetconnection)! | The assets owned by this organization. |
| `geoObjects` | [GeoObjectConnection](geo-objects/types.md#type-geoobjectconnection)! | The geographic objects owned by this organization. |
| `schedules` | [ScheduleConnection](#type-scheduleconnection)! | The schedules owned by this organization. |

</details>

---

### schedules

Lists schedules for an organization.

```graphql
schedules(
    organizationId: ID!
    filter: ScheduleFilter
    first: Int
    after: String
    last: Int
    before: String
    orderBy: ScheduleOrder = { field: TITLE, direction: ASC }
  ): ScheduleConnection!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` | The organization to retrieve schedules for. |
| `filter` | `ScheduleFilter` | Filtering options for the returned schedules. |
| `first` | `Int` | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `after` | `String` | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination). |
| `last` | `Int` | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination). |
| `before` | `String` | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy` | `ScheduleOrder` | The ordering options for the returned schedules. |

**Input types:**

<details>

<summary>ScheduleFilter</summary>

Filtering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

</details>

<details>

<summary>ScheduleOrder</summary>

Ordering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ScheduleOrderField](#type-scheduleorderfield) | The standard field to order by. |
| `direction` | [OrderDirection](common.md#type-orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>ScheduleConnection</summary>

A paginated list of Schedule items.

**Implements:** [Connection](common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleEdge](#type-scheduleedge)!]! | A list of edges. |
| `nodes` | [[Schedule](#type-schedule)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](common.md#type-countinfo) | The total count of items matching the filter. |

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

### scheduleCreate

Creates a new schedule.

```graphql
scheduleCreate(
    input: ScheduleCreateInput!
  ): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleCreateInput!` | The input fields for creating the schedule. |

**Input types:**

<details>

<summary>ScheduleCreateInput</summary>

Input for creating a new schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the schedule. |
| `title` | `String!` | The schedule display name. |
| `scheduleData` | `ScheduleData!` | The schedule data. |

</details>

**Output types:**

<details>

<summary>SchedulePayload</summary>

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](#type-schedule)! | The created or updated schedule. |

</details>

<details>

<summary>Schedule (entity)</summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](common.md#type-node), [Titled](common.md#type-titled), [Versioned](common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](organizations/README.md#type-organization)! | The organization that owns this schedule. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule. |

</details>

---

### scheduleUpdate

Updates an existing schedule.

```graphql
scheduleUpdate(
    input: ScheduleUpdateInput!
  ): SchedulePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleUpdateInput!` | The input fields for updating the schedule. |

**Input types:**

<details>

<summary>ScheduleUpdateInput</summary>

Input for updating an existing schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `scheduleData` | `ScheduleData` | The new schedule data. |

</details>

**Output types:**

<details>

<summary>SchedulePayload</summary>

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](#type-schedule)! | The created or updated schedule. |

</details>

<details>

<summary>Schedule (entity)</summary>

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](common.md#type-node), [Titled](common.md#type-titled), [Versioned](common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](organizations/README.md#type-organization)! | The organization that owns this schedule. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule. |

</details>

---

### scheduleDelete

Deletes a schedule.

```graphql
scheduleDelete(
    input: ScheduleDeleteInput!
  ): DeletePayload
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `input` | `ScheduleDeleteInput!` | The input fields for deleting the schedule. |

**Input types:**

<details>

<summary>ScheduleDeleteInput</summary>

Input for deleting a schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
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

<a id="type-schedule"></a>

### Schedule

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](common.md#type-node), [Titled](common.md#type-titled), [Versioned](common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](organizations/README.md#type-organization)! | The organization that owns this schedule. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule. |

---

<a id="type-schedulepayload"></a>

### SchedulePayload

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](#type-schedule)! | The created or updated schedule. |

---

## Inputs

<a id="type-schedulefilter"></a>

### ScheduleFilter

Filtering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |

---

<a id="type-scheduleorder"></a>

### ScheduleOrder

Ordering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ScheduleOrderField](#type-scheduleorderfield) | The standard field to order by. |
| `direction` | [OrderDirection](common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-schedulecreateinput"></a>

### ScheduleCreateInput

Input for creating a new schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the schedule. |
| `title` | `String!` | The schedule display name. |
| `scheduleData` | `ScheduleData!` | The schedule data. |

---

<a id="type-scheduleupdateinput"></a>

### ScheduleUpdateInput

Input for updating an existing schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `scheduleData` | `ScheduleData` | The new schedule data. |

---

<a id="type-scheduledeleteinput"></a>

### ScheduleDeleteInput

Input for deleting a schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

## Enums

<a id="type-scheduleorderfield"></a>

### ScheduleOrderField

Fields available for ordering schedules.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Scalars

<a id="type-scheduledata"></a>

### ScheduleData

A schedule data structure containing time intervals and recurrence rules.

| Property | Value |
| -------- | ----- |
| Format | `iCalendar-compatible JSON` |
| Example | `{"intervals": [...], "rrule": "FREQ=WEEKLY;BYDAY=MO,WE,FR"}` |
| Specification | [https://api.navixy.com/spec/scalars/schedule-data](https://api.navixy.com/spec/scalars/schedule-data) |

---

## Pagination types

<a id="type-scheduleconnection"></a>

### ScheduleConnection

A paginated list of Schedule items.

**Implements:** [Connection](common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleEdge](#type-scheduleedge)!]! | A list of edges. |
| `nodes` | [[Schedule](#type-schedule)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-scheduleedge"></a>

### ScheduleEdge

An edge in the Schedule connection.

**Implements:** [Edge](common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Schedule](#type-schedule)! | The schedule at the end of the edge. |

---
