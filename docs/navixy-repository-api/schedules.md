---
description: >-
  Complete reference for schedules, including queries, mutations, and type definitions
  for time-based rules using iCalendar (RFC 5545) recurrence.
---

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
| `first` | `Int` | The first `n` elements from the [paginated list](pagination.md). |
| `after` | `String` | The elements that come after the specified [cursor](pagination.md). |
| `last` | `Int` | The last `n` elements from the [paginated list](pagination.md). |
| `before` | `String` | The elements that come before the specified [cursor](pagination.md). |
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

Schedule configuration as a JSON object — time intervals and recurrence. The same shape backs
both the `Schedule` entity (`scheduleData`) and `FieldType.SCHEDULE` custom-field values.

A **JSCalendar-aligned profile** ([RFC 8984](https://www.rfc-editor.org/rfc/rfc8984.html) field names) restricted to the subset that round-trips
to iCalendar / [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545.html) (`.ics`). All date-times are **local wall-clock** (no offset), interpreted
in the schedule-level `timeZone` — never UTC — so recurring events keep their wall-clock time
across DST transitions. Validated on write (rejected with a field-specific message); reads are
tolerant of legacy/empty values.

Field catalogue (NOT a single valid object — `end`/`duration` and `count`/`until` are mutually
exclusive; numeric ranges below are value DOMAINS, not literal arrays). All date-times are local,
e.g. `2025-01-06T09:00:00`; dates for all-day, e.g. `2025-06-10`.

Top level:
- `timeZone`: IANA string, required. Zone for every TIMED event (all-day events are zone-independent).
- `active`: boolean, optional, default true. Manual on/off for schedule checks.
- `description`: string, optional, free text. (The NAME is the entity title, not stored here.)
- `events`: array, required, non-empty.

Each event:
- `uid`: string, optional, stable slot id.
- `title`: string, optional, maps to VEVENT SUMMARY.
- `start`: local date (all-day) or date-time (timed), required. Date-times are exactly
  `yyyy-MM-dd'T'HH:mm:ss` — seconds required, no fractional seconds, no offset/`Z`.
- `end` XOR `duration`: a timed event needs exactly one; an all-day event may omit both.
  `end` is a local date-time (one-off / manual slots); `duration` is a **positive** ISO-8601
  duration (e.g. `PT9H`, preferred for recurring — stable across DST); for an all-day event the
  duration must be whole days (e.g. `P1D`), no time component.
- `showWithoutTime`: boolean, optional. true → all-day: `start`/`end` are dates, FLOATING (ignores
  `timeZone`); an all-day `recurrenceRule` must not use `byHour`/`byMinute`/`bySecond`.
- `recurrenceRule`: object, optional. Absent → a single occurrence at `start`.
- `excludedDates`: array of local date-times, optional. EXDATE — drop whole occurrences.
- `additionalDates`: array of local date-times, optional. RDATE — add one-off occurrences.

`recurrenceRule`:
- `frequency`: one of `secondly|minutely|hourly|daily|weekly|monthly|yearly`, required.
- `interval`: integer >= 1, optional (default 1).
- `count` XOR `until`: optional; never both. Neither → repeats forever. `until` is a local date-time.
- `byDay`: array of `{ "day": <mo|tu|we|th|fr|sa|su>, "nthOfPeriod"?: <non-zero int> }`. An ordinal
  `nthOfPeriod` (e.g. `{day:"mo",nthOfPeriod:1}` = first Monday) is valid only for monthly/yearly.
- `byMonth`: 1..12. `byMonthDay`: -31..-1 or 1..31. `byYearDay`: -366..-1 or 1..366.
  `byWeekNo`: -53..-1 or 1..53. `byHour`: 0..23. `byMinute`: 0..59. `bySecond`: 0..60 (60 = leap second).
- `firstDayOfWeek`: one of `mo..su`, optional (WKST, default mo).

Numeric recurrence domains follow [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545.html) §3.3.10. Maps to a `VEVENT` per `events[]` entry on
`.ics` export (post-MVP). See **Specification** below.

| Property | Value |
| -------- | ----- |
| Format | `JSCalendar-aligned JSON (RFC 8984)` |
| Example | `{"timeZone": "America/New_York", "events": [{"start": "2025-01-06T09:00:00", "duration": "PT8H", "recurrenceRule": {"frequency": "weekly", "byDay": [{"day": "mo"}, {"day": "we"}, {"day": "fr"}]}}]}` |
| Specification | [https://www.navixy.com/docs/navixy-repository-api/core-api-reference/schedules#scheduledata](https://www.navixy.com/docs/navixy-repository-api/core-api-reference/schedules#scheduledata) |

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
