# Audit

Audit trail for tracking changes and access to system resources.

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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | `ID!` |  |
| `filter` | `AuditEventFilter` |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | `AuditEventOrder` |  |
| `direction` | `DESC }` |  |

**Input types:**

<details>

<summary>AuditEventFilter</summary>

Filtering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `aggregateTypes` | `[Code!]` | Filter by entity types (OR within field). |
| `aggregateIds` | `[ID!]` | Filter by specific entity IDs (OR within field). |
| `eventTypes` | [[AuditEventType](../audit.md#auditeventtype)!] | Filter by event types (OR within field). |
| `sourceTypes` | [[SourceType](../audit.md#sourcetype)!] | Filter by source types (OR within field). |
| `traceId` | `String` | Filter by trace ID. |
| `from` | `DateTime` | Return events that occurred after this timestamp. |
| `to` | `DateTime` | Return events that occurred before this timestamp. |

</details>

<details>

<summary>AuditEventOrder</summary>

Ordering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AuditEventOrderField](../audit.md#auditeventorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AuditEventConnection</summary>

A paginated list of AuditEvent items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AuditEventEdge](../audit.md#auditeventedge)!]! | A list of edges. |
| `nodes` | [[AuditEvent](../audit.md#auditevent)!]! | A list of nodes in the connection (without edge metadata). |
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

| Name | Type | Description |
| ---- | ---- | ----------- |
| `entityId` | `ID!` |  |
| `filter` | `AuditEventFilter` |  |
| `first` | `Int` |  |
| `after` | `String` |  |
| `last` | `Int` |  |
| `before` | `String` |  |
| `orderBy` | `AuditEventOrder` |  |
| `direction` | `DESC }` |  |

**Input types:**

<details>

<summary>AuditEventFilter</summary>

Filtering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `aggregateTypes` | `[Code!]` | Filter by entity types (OR within field). |
| `aggregateIds` | `[ID!]` | Filter by specific entity IDs (OR within field). |
| `eventTypes` | [[AuditEventType](../audit.md#auditeventtype)!] | Filter by event types (OR within field). |
| `sourceTypes` | [[SourceType](../audit.md#sourcetype)!] | Filter by source types (OR within field). |
| `traceId` | `String` | Filter by trace ID. |
| `from` | `DateTime` | Return events that occurred after this timestamp. |
| `to` | `DateTime` | Return events that occurred before this timestamp. |

</details>

<details>

<summary>AuditEventOrder</summary>

Ordering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AuditEventOrderField](../audit.md#auditeventorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

</details>

**Output types:**

<details>

<summary>AuditEventConnection</summary>

A paginated list of AuditEvent items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AuditEventEdge](../audit.md#auditeventedge)!]! | A list of edges. |
| `nodes` | [[AuditEvent](../audit.md#auditevent)!]! | A list of nodes in the connection (without edge metadata). |
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

## Objects

### AuditEvent

An audit log entry recording an event that occurred in the system.

**Implements:** [Node](../common.md#node)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `organization` | [Organization](../organizations.md#organization) | The organization context. Null for system events. |
| `actor` | [Actor](../actors.md#actor) | The actor who triggered the event. |
| `ipAddress` | `String` | The client IP address. |
| `userAgent` | `String` | The client User-Agent string. |
| `sourceType` | [SourceType](../audit.md#sourcetype)! | The source type of the request. |
| `traceId` | `String` | The distributed tracing ID (32 hex characters) for log correlation. |
| `aggregateType` | `Code` | The type of entity affected. |
| `aggregateId` | `ID` | The ID of the affected entity. |
| `eventType` | [AuditEventType](../audit.md#auditeventtype)! | The type of event that occurred. |
| `eventData` | `JSON` | The event payload with details such as changed fields. |
| `occurredAt` | `DateTime!` | The date and time when the event occurred. |

---

## Inputs

### AuditEventFilter

Filtering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `actorIds` | `[ID!]` | Filter by actors (OR within field). |
| `aggregateTypes` | `[Code!]` | Filter by entity types (OR within field). |
| `aggregateIds` | `[ID!]` | Filter by specific entity IDs (OR within field). |
| `eventTypes` | [[AuditEventType](../audit.md#auditeventtype)!] | Filter by event types (OR within field). |
| `sourceTypes` | [[SourceType](../audit.md#sourcetype)!] | Filter by source types (OR within field). |
| `traceId` | `String` | Filter by trace ID. |
| `from` | `DateTime` | Return events that occurred after this timestamp. |
| `to` | `DateTime` | Return events that occurred before this timestamp. |

---

### AuditEventOrder

Ordering options for audit events.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [AuditEventOrderField](../audit.md#auditeventorderfield)! | The field to order by. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

## Enums

### SourceType

The source type identifying the origin of an API request.

| Value | Description |
| ----- | ----------- |
| `WEB` | Request originated from a web browser application. |
| `MOBILE` | Request originated from a mobile application (iOS/Android). |
| `API` | Request made directly via the API. |
| `INTERNAL` | Request generated by an internal system process. |
| `INTEGRATION` | Request made by an external integration. |

---

### AuditEventType

The type of event recorded in the audit log.

| Value | Description |
| ----- | ----------- |
| `LOGIN` | A user successfully authenticated. |
| `LOGOUT` | A user ended their session. |
| `FAILED_LOGIN` | An authentication attempt failed. |
| `PASSWORD_RESET` | A password reset was initiated. |
| `SESSION_EXPIRED` | A session was terminated due to inactivity. |
| `CREATED` | A new entity was created. |
| `UPDATED` | An existing entity was modified. |
| `DELETED` | An entity was deleted. |
| `RESTORED` | A soft-deleted entity was restored. |
| `ROLE_ASSIGNED` | A role was assigned to an actor. |
| `ROLE_REVOKED` | A role was removed from an actor. |
| `PERMISSION_GRANTED` | A permission was granted to a role. |
| `PERMISSION_REVOKED` | A permission was removed from a role. |
| `LINKED` | Two entities were linked together. |
| `UNLINKED` | A link between entities was removed. |
| `ATTACHED` | An entity was added to a group. |
| `DETACHED` | An entity was removed from a group. |

---

### AuditEventOrderField

Fields available for ordering audit events.

| Value | Description |
| ----- | ----------- |
| `OCCURRED_AT` | Order by occurrence date. |

---

## Pagination types

### AuditEventConnection

A paginated list of AuditEvent items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AuditEventEdge](../audit.md#auditeventedge)!]! | A list of edges. |
| `nodes` | [[AuditEvent](../audit.md#auditevent)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### AuditEventEdge

An edge in the AuditEvent connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [AuditEvent](../audit.md#auditevent)! | The audit event at the end of the edge. |

---
