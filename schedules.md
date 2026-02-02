# Schedules

Schedules define time-based rules using RFC 5545 (iCalendar) recurrence patterns.

## Queries

### schedule

Retrieves a schedule by its ID.

```graphql
schedule(id: ID!): Schedule
```

**Arguments**

| Name | Type  | Description                         |
| ---- | ----- | ----------------------------------- |
| `id` | `ID!` | The ID of the schedule to retrieve. |

**Output types:**

<details>

<summary><code>Schedule</code></summary>

| Field          | Type                                                            | Description                               |
| -------------- | --------------------------------------------------------------- | ----------------------------------------- |
| `id`           | `ID!`                                                           |                                           |
| `version`      | `Int!`                                                          |                                           |
| `title`        | `String!`                                                       |                                           |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this schedule. |
| `type`         | [ScheduleType](catalogs/entity-types/types.md#scheduletype)!    | The schedule type classification.         |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)!                      |                                           |
| `customFields` | [JSON](core-api-reference/common-resources.md#json)!            |                                           |

</details>

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

| Name             | Type                                          | Description                                                                                   |
| ---------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                         | The organization to retrieve schedules for.                                                   |
| `filter`         | [ScheduleFilter](schedules.md#schedulefilter) | Filtering options for the returned schedules.                                                 |
| `first`          | `Int`                                         | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                      | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                         | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                      | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [ScheduleOrder](schedules.md#scheduleorder)   | The ordering options for the returned schedules.                                              |

**Input types:**

<details>

<summary><code>ScheduleFilter</code></summary>

| Field           | Type                                                        | Description                                         |
| --------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`                                                     | Filter by schedule types (OR within field).         |
| `titleContains` | `String`                                                    | Partial match on title (case-insensitive contains). |
| `customFields`  | \[[CustomFieldFilter](custom-fields.md#customfieldfilter)!] | Filter by custom field values.                      |

</details>

<details>

<summary><code>CustomFieldFilter</code></summary>

| Field      | Type                                                 | Description                                                                   |
| ---------- | ---------------------------------------------------- | ----------------------------------------------------------------------------- |
| `code`     | [Code](core-api-reference/common-resources.md#code)! | The custom field code to filter by.                                           |
| `operator` | [FieldOperator](custom-fields.md#fieldoperator)!     | The comparison operator.                                                      |
| `value`    | [JSON](core-api-reference/common-resources.md#json)  | The value to compare against. Null for `IS_NULL` and `IS_NOT_NULL` operators. |

</details>

<details>

<summary><code>ScheduleOrder</code></summary>

| Field             | Type                                                                     | Description                                                                |
| ----------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| `field`           | [ScheduleOrderField](schedules.md#scheduleorderfield)                    | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](core-api-reference/common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order.                                                    |

</details>

**Output types:**

<details>

<summary><code>ScheduleConnection</code></summary>

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[ScheduleEdge](schedules.md#scheduleedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[Schedule](schedules.md#schedule)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>Schedule (node)</code></summary>

| Field          | Type                                                            | Description                               |
| -------------- | --------------------------------------------------------------- | ----------------------------------------- |
| `id`           | `ID!`                                                           |                                           |
| `version`      | `Int!`                                                          |                                           |
| `title`        | `String!`                                                       |                                           |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this schedule. |
| `type`         | [ScheduleType](catalogs/entity-types/types.md#scheduletype)!    | The schedule type classification.         |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)!                      |                                           |
| `customFields` | [JSON](core-api-reference/common-resources.md#json)!            |                                           |

</details>

## Mutations

### scheduleCreate

Creates a new schedule.

```graphql
scheduleCreate(input: ScheduleCreateInput!): SchedulePayload
```

**Arguments**

| Name    | Type                                                     | Description                                 |
| ------- | -------------------------------------------------------- | ------------------------------------------- |
| `input` | [ScheduleCreateInput](schedules.md#schedulecreateinput)! | The input fields for creating the schedule. |

**Input types:**

<details>

<summary><code>ScheduleCreateInput</code></summary>

| Field            | Type                                                              | Description                                  |
| ---------------- | ----------------------------------------------------------------- | -------------------------------------------- |
| `organizationId` | `ID!`                                                             | The organization that will own the schedule. |
| `typeId`         | `ID!`                                                             | The schedule type ID.                        |
| `title`          | `String!`                                                         | The schedule display name.                   |
| `scheduleData`   | [ScheduleData](schedules.md#scheduledata)!                        | The schedule data.                           |
| `customFields`   | [CustomFieldsPatchInput](custom-fields.md#customfieldspatchinput) | The custom field values.                     |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                                    | Description                                 |
| ------- | ------------------------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](core-api-reference/common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](core-api-reference/common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>SchedulePayload</code></summary>

| Field      | Type                               | Description                      |
| ---------- | ---------------------------------- | -------------------------------- |
| `schedule` | [Schedule](schedules.md#schedule)! | The created or updated schedule. |

</details>

<details>

<summary><code>Schedule (entity)</code></summary>

| Field          | Type                                                            | Description                               |
| -------------- | --------------------------------------------------------------- | ----------------------------------------- |
| `id`           | `ID!`                                                           |                                           |
| `version`      | `Int!`                                                          |                                           |
| `title`        | `String!`                                                       |                                           |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this schedule. |
| `type`         | [ScheduleType](catalogs/entity-types/types.md#scheduletype)!    | The schedule type classification.         |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)!                      |                                           |
| `customFields` | [JSON](core-api-reference/common-resources.md#json)!            |                                           |

</details>

### scheduleUpdate

Updates an existing schedule.

```graphql
scheduleUpdate(input: ScheduleUpdateInput!): SchedulePayload
```

**Arguments**

| Name    | Type                                                     | Description                                 |
| ------- | -------------------------------------------------------- | ------------------------------------------- |
| `input` | [ScheduleUpdateInput](schedules.md#scheduleupdateinput)! | The input fields for updating the schedule. |

**Input types:**

<details>

<summary><code>ScheduleUpdateInput</code></summary>

| Field          | Type                                                              | Description                                 |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                             | The schedule ID to update.                  |
| `version`      | `Int!`                                                            | The current version for optimistic locking. |
| `title`        | `String`                                                          | The new display name.                       |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)                         | The new schedule data.                      |
| `customFields` | [CustomFieldsPatchInput](custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

</details>

<details>

<summary><code>CustomFieldsPatchInput</code></summary>

| Field   | Type                                                    | Description                                 |
| ------- | ------------------------------------------------------- | ------------------------------------------- |
| `set`   | [JSON](core-api-reference/common-resources.md#json)     | Fields to set or update as a key-value map. |
| `unset` | \[[Code](core-api-reference/common-resources.md#code)!] | Field codes to remove.                      |

</details>

**Output types:**

<details>

<summary><code>SchedulePayload</code></summary>

| Field      | Type                               | Description                      |
| ---------- | ---------------------------------- | -------------------------------- |
| `schedule` | [Schedule](schedules.md#schedule)! | The created or updated schedule. |

</details>

<details>

<summary><code>Schedule (entity)</code></summary>

| Field          | Type                                                            | Description                               |
| -------------- | --------------------------------------------------------------- | ----------------------------------------- |
| `id`           | `ID!`                                                           |                                           |
| `version`      | `Int!`                                                          |                                           |
| `title`        | `String!`                                                       |                                           |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this schedule. |
| `type`         | [ScheduleType](catalogs/entity-types/types.md#scheduletype)!    | The schedule type classification.         |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)!                      |                                           |
| `customFields` | [JSON](core-api-reference/common-resources.md#json)!            |                                           |

</details>

### scheduleDelete

Deletes a schedule.

```graphql
scheduleDelete(input: ScheduleDeleteInput!): DeletePayload
```

**Arguments**

| Name    | Type                                                     | Description                                 |
| ------- | -------------------------------------------------------- | ------------------------------------------- |
| `input` | [ScheduleDeleteInput](schedules.md#scheduledeleteinput)! | The input fields for deleting the schedule. |

**Input types:**

<details>

<summary><code>ScheduleDeleteInput</code></summary>

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The schedule ID to delete.                  |
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

### ScheduleConnection

A paginated list of Schedule items.

**Implements:** [`Connection`](core-api-reference/common-resources.md#connection)

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[ScheduleEdge](schedules.md#scheduleedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[Schedule](schedules.md#schedule)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### ScheduleEdge

An edge in the Schedule connection.

**Implements:** [`Edge`](core-api-reference/common-resources.md#edge)

| Field    | Type                               | Description                          |
| -------- | ---------------------------------- | ------------------------------------ |
| `cursor` | `String!`                          | An opaque cursor for this edge.      |
| `node`   | [Schedule](schedules.md#schedule)! | The schedule at the end of the edge. |

### Schedule

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [`Node`](core-api-reference/common-resources.md#node), [`Titled`](core-api-reference/common-resources.md#titled), [`Customizable`](core-api-reference/common-resources.md#customizable), [`Versioned`](core-api-reference/common-resources.md#versioned)

| Field          | Type                                                            | Description                               |
| -------------- | --------------------------------------------------------------- | ----------------------------------------- |
| `id`           | `ID!`                                                           |                                           |
| `version`      | `Int!`                                                          |                                           |
| `title`        | `String!`                                                       |                                           |
| `organization` | [Organization](core-api-reference/organizations/#organization)! | The organization that owns this schedule. |
| `type`         | [ScheduleType](catalogs/entity-types/types.md#scheduletype)!    | The schedule type classification.         |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)!                      |                                           |
| `customFields` | [JSON](core-api-reference/common-resources.md#json)!            |                                           |

### SchedulePayload

The result of a schedule mutation.

| Field      | Type                               | Description                      |
| ---------- | ---------------------------------- | -------------------------------- |
| `schedule` | [Schedule](schedules.md#schedule)! | The created or updated schedule. |

## Inputs

### ScheduleFilter

Filtering options for schedules.

| Field           | Type                                                        | Description                                         |
| --------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`                                                     | Filter by schedule types (OR within field).         |
| `titleContains` | `String`                                                    | Partial match on title (case-insensitive contains). |
| `customFields`  | \[[CustomFieldFilter](custom-fields.md#customfieldfilter)!] | Filter by custom field values.                      |

### ScheduleOrder

Ordering options for schedules.

| Field             | Type                                                                     | Description                                                                |
| ----------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| `field`           | [ScheduleOrderField](schedules.md#scheduleorderfield)                    | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](core-api-reference/common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order.                                                    |

### ScheduleCreateInput

Input for creating a new schedule.

| Field            | Type                                                              | Description                                  |
| ---------------- | ----------------------------------------------------------------- | -------------------------------------------- |
| `organizationId` | `ID!`                                                             | The organization that will own the schedule. |
| `typeId`         | `ID!`                                                             | The schedule type ID.                        |
| `title`          | `String!`                                                         | The schedule display name.                   |
| `scheduleData`   | [ScheduleData](schedules.md#scheduledata)!                        | The schedule data.                           |
| `customFields`   | [CustomFieldsPatchInput](custom-fields.md#customfieldspatchinput) | The custom field values.                     |

### ScheduleUpdateInput

Input for updating an existing schedule.

| Field          | Type                                                              | Description                                 |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                             | The schedule ID to update.                  |
| `version`      | `Int!`                                                            | The current version for optimistic locking. |
| `title`        | `String`                                                          | The new display name.                       |
| `scheduleData` | [ScheduleData](schedules.md#scheduledata)                         | The new schedule data.                      |
| `customFields` | [CustomFieldsPatchInput](custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

### ScheduleDeleteInput

Input for deleting a schedule.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The schedule ID to delete.                  |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### ScheduleOrderField

Fields available for ordering schedules.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |

## Scalars

### ScheduleData

**Specification:** [https://api.navixy.com/spec/scalars/schedule-data](https://api.navixy.com/spec/scalars/schedule-data)
