# Audit

Audit logging and change tracking.

## Queries

### auditEvents

Lists audit events for an organization.

```graphql
auditEvents(
  organizationId: ID!
  filter: AuditEventFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AuditEventOrder = { field: OCCURRED_AT, direction: DESC }
): AuditEventConnection!
```

**Arguments**

| Name             | Type                                          | Description                                                                                   |
| ---------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organizationId` | `ID!`                                         | The organization to retrieve audit events for.                                                |
| `filter`         | [AuditEventFilter](audit.md#auditeventfilter) | Filtering options for the returned audit events.                                              |
| `first`          | `Int`                                         | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`          | `String`                                      | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`           | `Int`                                         | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`         | `String`                                      | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`        | [AuditEventOrder](audit.md#auditeventorder)   | The ordering options for the returned audit events.                                           |

**Input types:**

<details>

<summary><code>AuditEventFilter</code></summary>

| Field            | Type                                                        | Description                                        |
| ---------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| `actorIds`       | `[ID!]`                                                     | Filter by actors (OR within field).                |
| `aggregateTypes` | \[[Code](core-api-reference/common-resources.md#code)!]     | Filter by entity types (OR within field).          |
| `aggregateIds`   | `[ID!]`                                                     | Filter by specific entity IDs (OR within field).   |
| `eventTypes`     | \[[AuditEventType](audit.md#auditeventtype)!]               | Filter by event types (OR within field).           |
| `sourceTypes`    | \[[SourceType](audit.md#sourcetype)!]                       | Filter by source types (OR within field).          |
| `traceId`        | `String`                                                    | Filter by trace ID.                                |
| `from`           | [DateTime](core-api-reference/common-resources.md#datetime) | Return events that occurred after this timestamp.  |
| `to`             | [DateTime](core-api-reference/common-resources.md#datetime) | Return events that occurred before this timestamp. |

</details>

<details>

<summary><code>AuditEventOrder</code></summary>

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [AuditEventOrderField](audit.md#auditeventorderfield)!                   | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>AuditEventConnection</code></summary>

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AuditEventEdge](audit.md#auditeventedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[AuditEvent](audit.md#auditevent)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>AuditEvent (node)</code></summary>

| Field           | Type                                                           | Description                                                         |
| --------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`            | `ID!`                                                          |                                                                     |
| `organization`  | [Organization](core-api-reference/organizations/#organization) | The organization context. Null for system events.                   |
| `actor`         | [Actor](access-control/types.md#actor)                         | The actor who triggered the event.                                  |
| `ipAddress`     | `String`                                                       | The client IP address.                                              |
| `userAgent`     | `String`                                                       | The client User-Agent string.                                       |
| `sourceType`    | [SourceType](audit.md#sourcetype)!                             | The source type of the request.                                     |
| `traceId`       | `String`                                                       | The distributed tracing ID (32 hex characters) for log correlation. |
| `aggregateType` | [Code](core-api-reference/common-resources.md#code)            | The type of entity affected.                                        |
| `aggregateId`   | `ID`                                                           | The ID of the affected entity.                                      |
| `eventType`     | [AuditEventType](audit.md#auditeventtype)!                     | The type of event that occurred.                                    |
| `eventData`     | [JSON](core-api-reference/common-resources.md#json)            | The event payload with details such as changed fields.              |
| `occurredAt`    | [DateTime](core-api-reference/common-resources.md#datetime)!   | The date and time when the event occurred.                          |

</details>

### entityHistory

Retrieves the change history for any entity.

```graphql
entityHistory(
  entityId: ID!
  filter: AuditEventFilter
  first: Int
  after: String
  last: Int
  before: String
  orderBy: AuditEventOrder = { field: OCCURRED_AT, direction: DESC }
): AuditEventConnection!
```

**Arguments**

| Name       | Type                                          | Description                                                                                   |
| ---------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `entityId` | `ID!`                                         | The ID of the entity to retrieve history for.                                                 |
| `filter`   | [AuditEventFilter](audit.md#auditeventfilter) | Filtering options for the returned audit events.                                              |
| `first`    | `Int`                                         | The first `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).     |
| `after`    | `String`                                      | The elements that come after the specified [cursor](https://docs.navixy.com/api/pagination).  |
| `last`     | `Int`                                         | The last `n` elements from the [paginated list](https://docs.navixy.com/api/pagination).      |
| `before`   | `String`                                      | The elements that come before the specified [cursor](https://docs.navixy.com/api/pagination). |
| `orderBy`  | [AuditEventOrder](audit.md#auditeventorder)   | The ordering options for the returned audit events.                                           |

**Input types:**

<details>

<summary><code>AuditEventFilter</code></summary>

| Field            | Type                                                        | Description                                        |
| ---------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| `actorIds`       | `[ID!]`                                                     | Filter by actors (OR within field).                |
| `aggregateTypes` | \[[Code](core-api-reference/common-resources.md#code)!]     | Filter by entity types (OR within field).          |
| `aggregateIds`   | `[ID!]`                                                     | Filter by specific entity IDs (OR within field).   |
| `eventTypes`     | \[[AuditEventType](audit.md#auditeventtype)!]               | Filter by event types (OR within field).           |
| `sourceTypes`    | \[[SourceType](audit.md#sourcetype)!]                       | Filter by source types (OR within field).          |
| `traceId`        | `String`                                                    | Filter by trace ID.                                |
| `from`           | [DateTime](core-api-reference/common-resources.md#datetime) | Return events that occurred after this timestamp.  |
| `to`             | [DateTime](core-api-reference/common-resources.md#datetime) | Return events that occurred before this timestamp. |

</details>

<details>

<summary><code>AuditEventOrder</code></summary>

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [AuditEventOrderField](audit.md#auditeventorderfield)!                   | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary><code>AuditEventConnection</code></summary>

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AuditEventEdge](audit.md#auditeventedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[AuditEvent](audit.md#auditevent)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

</details>

<details>

<summary><code>AuditEvent (node)</code></summary>

| Field           | Type                                                           | Description                                                         |
| --------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`            | `ID!`                                                          |                                                                     |
| `organization`  | [Organization](core-api-reference/organizations/#organization) | The organization context. Null for system events.                   |
| `actor`         | [Actor](access-control/types.md#actor)                         | The actor who triggered the event.                                  |
| `ipAddress`     | `String`                                                       | The client IP address.                                              |
| `userAgent`     | `String`                                                       | The client User-Agent string.                                       |
| `sourceType`    | [SourceType](audit.md#sourcetype)!                             | The source type of the request.                                     |
| `traceId`       | `String`                                                       | The distributed tracing ID (32 hex characters) for log correlation. |
| `aggregateType` | [Code](core-api-reference/common-resources.md#code)            | The type of entity affected.                                        |
| `aggregateId`   | `ID`                                                           | The ID of the affected entity.                                      |
| `eventType`     | [AuditEventType](audit.md#auditeventtype)!                     | The type of event that occurred.                                    |
| `eventData`     | [JSON](core-api-reference/common-resources.md#json)            | The event payload with details such as changed fields.              |
| `occurredAt`    | [DateTime](core-api-reference/common-resources.md#datetime)!   | The date and time when the event occurred.                          |

</details>

## Types

### AuditEventConnection

A paginated list of AuditEvent items.

**Implements:** [`Connection`](core-api-reference/common-resources.md#connection)

| Field      | Type                                                          | Description                                                |
| ---------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[AuditEventEdge](audit.md#auditeventedge)!]!                | A list of edges.                                           |
| `nodes`    | \[[AuditEvent](audit.md#auditevent)!]!                        | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### AuditEventEdge

An edge in the AuditEvent connection.

**Implements:** [`Edge`](core-api-reference/common-resources.md#edge)

| Field    | Type                               | Description                             |
| -------- | ---------------------------------- | --------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.         |
| `node`   | [AuditEvent](audit.md#auditevent)! | The audit event at the end of the edge. |

### AuditEvent

An audit log entry recording an event that occurred in the system.

**Implements:** [`Node`](core-api-reference/common-resources.md#node)

| Field           | Type                                                           | Description                                                         |
| --------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`            | `ID!`                                                          |                                                                     |
| `organization`  | [Organization](core-api-reference/organizations/#organization) | The organization context. Null for system events.                   |
| `actor`         | [Actor](access-control/types.md#actor)                         | The actor who triggered the event.                                  |
| `ipAddress`     | `String`                                                       | The client IP address.                                              |
| `userAgent`     | `String`                                                       | The client User-Agent string.                                       |
| `sourceType`    | [SourceType](audit.md#sourcetype)!                             | The source type of the request.                                     |
| `traceId`       | `String`                                                       | The distributed tracing ID (32 hex characters) for log correlation. |
| `aggregateType` | [Code](core-api-reference/common-resources.md#code)            | The type of entity affected.                                        |
| `aggregateId`   | `ID`                                                           | The ID of the affected entity.                                      |
| `eventType`     | [AuditEventType](audit.md#auditeventtype)!                     | The type of event that occurred.                                    |
| `eventData`     | [JSON](core-api-reference/common-resources.md#json)            | The event payload with details such as changed fields.              |
| `occurredAt`    | [DateTime](core-api-reference/common-resources.md#datetime)!   | The date and time when the event occurred.                          |

## Inputs

### AuditEventFilter

Filtering options for audit events.

| Field            | Type                                                        | Description                                        |
| ---------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| `actorIds`       | `[ID!]`                                                     | Filter by actors (OR within field).                |
| `aggregateTypes` | \[[Code](core-api-reference/common-resources.md#code)!]     | Filter by entity types (OR within field).          |
| `aggregateIds`   | `[ID!]`                                                     | Filter by specific entity IDs (OR within field).   |
| `eventTypes`     | \[[AuditEventType](audit.md#auditeventtype)!]               | Filter by event types (OR within field).           |
| `sourceTypes`    | \[[SourceType](audit.md#sourcetype)!]                       | Filter by source types (OR within field).          |
| `traceId`        | `String`                                                    | Filter by trace ID.                                |
| `from`           | [DateTime](core-api-reference/common-resources.md#datetime) | Return events that occurred after this timestamp.  |
| `to`             | [DateTime](core-api-reference/common-resources.md#datetime) | Return events that occurred before this timestamp. |

### AuditEventOrder

Ordering options for audit events.

| Field       | Type                                                                     | Description             |
| ----------- | ------------------------------------------------------------------------ | ----------------------- |
| `field`     | [AuditEventOrderField](audit.md#auditeventorderfield)!                   | The field to order by.  |
| `direction` | [OrderDirection](core-api-reference/common-resources.md#orderdirection)! | The direction to order. |

## Enums

### SourceType

The source type identifying the origin of an API request.

| Value         | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `WEB`         | Request originated from a web browser application.          |
| `MOBILE`      | Request originated from a mobile application (iOS/Android). |
| `API`         | Request made directly via the API.                          |
| `INTERNAL`    | Request generated by an internal system process.            |
| `INTEGRATION` | Request made by an external integration.                    |

### AuditEventType

The type of event recorded in the audit log.

| Value                | Description                                 |
| -------------------- | ------------------------------------------- |
| `LOGIN`              | A user successfully authenticated.          |
| `LOGOUT`             | A user ended their session.                 |
| `FAILED_LOGIN`       | An authentication attempt failed.           |
| `PASSWORD_RESET`     | A password reset was initiated.             |
| `SESSION_EXPIRED`    | A session was terminated due to inactivity. |
| `CREATED`            | A new entity was created.                   |
| `UPDATED`            | An existing entity was modified.            |
| `DELETED`            | An entity was deleted.                      |
| `RESTORED`           | A soft-deleted entity was restored.         |
| `ROLE_ASSIGNED`      | A role was assigned to an actor.            |
| `ROLE_REVOKED`       | A role was removed from an actor.           |
| `PERMISSION_GRANTED` | A permission was granted to a role.         |
| `PERMISSION_REVOKED` | A permission was removed from a role.       |
| `LINKED`             | Two entities were linked together.          |
| `UNLINKED`           | A link between entities was removed.        |
| `ATTACHED`           | An entity was added to a group.             |
| `DETACHED`           | An entity was removed from a group.         |

### AuditEventOrderField

Fields available for ordering audit events.

| Value         | Description               |
| ------------- | ------------------------- |
| `OCCURRED_AT` | Order by occurrence date. |
