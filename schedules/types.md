# Schedules — Types

## Objects

### ScheduleType

A classification type for schedules.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `code` | `Code!` |  |
| `order` | `Int!` |  |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! |  |
| `organization` | [Organization](../organizations.md#organization) |  |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! |  |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this schedule type, ordered by display order. |

---

### Schedule

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` |  |
| `version` | `Int!` |  |
| `title` | `String!` |  |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this schedule. |
| `type` | [ScheduleType](types.md#scheduletype)! | The schedule type classification. |
| `scheduleData` | `ScheduleData!` | The calendar and time interval definitions for this schedule.
  This is an alias for the `schedule_data` custom field. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

---

### SchedulePayload

The result of a schedule mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `schedule` | [Schedule](types.md#schedule)! | The created or updated schedule. |

---

### ScheduleTypePayload

The result of a schedule type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `scheduleType` | [ScheduleType](types.md#scheduletype)! | The created or updated schedule type. |

---

## Inputs

### ScheduleFilter

Filtering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by schedule types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values. |

---

### ScheduleOrder

Ordering options for schedules.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [ScheduleOrderField](types.md#scheduleorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### ScheduleCreateInput

Input for creating a new schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the schedule. |
| `typeId` | `ID!` | The schedule type ID. |
| `title` | `String!` | The schedule display name. |
| `scheduleData` | `ScheduleData!` | The schedule data. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

---

### ScheduleUpdateInput

Input for updating an existing schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `scheduleData` | `ScheduleData` | The new schedule data. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

---

### ScheduleDeleteInput

Input for deleting a schedule.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The schedule ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### ScheduleTypeCreateInput

Input for creating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### ScheduleTypeUpdateInput

Input for updating a schedule type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Enums

### ScheduleOrderField

Fields available for ordering schedules.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Scalars

### ScheduleData

**Specification:** [https://api.navixy.com/spec/scalars/schedule-data](https://api.navixy.com/spec/scalars/schedule-data)

---

## Pagination types

### ScheduleConnection

A paginated list of Schedule items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleEdge](types.md#scheduleedge)!]! | A list of edges. |
| `nodes` | [[Schedule](types.md#schedule)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### ScheduleEdge

An edge in the Schedule connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [Schedule](types.md#schedule)! | The schedule at the end of the edge. |

---

### ScheduleTypeConnection

A paginated list of ScheduleType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleTypeEdge](types.md#scheduletypeedge)!]! | A list of edges. |
| `nodes` | [[ScheduleType](types.md#scheduletype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### ScheduleTypeEdge

An edge in the ScheduleType connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [ScheduleType](types.md#scheduletype)! | The schedule type at the end of the edge. |

---
