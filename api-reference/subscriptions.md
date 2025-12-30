# Subscriptions

Subscriptions provide real-time updates via WebSocket connections.

## WebSocket endpoint

```
wss://api.navixy.com/v4/graphql/ws
```

### domainEvent

Subscribe to domain events. Filter by organization, entity type, and/or event type. All parameters are optional - omit for broader subscription.

```graphql
domainEvent(
  organizationId: UUID
  aggregateType: String
  eventType: AuditEventType
): DomainEvent!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | [UUID](/api-reference/scalars-and-enums.md#uuid/) | |
| `aggregateType` | `String` | |
| `eventType` | [AuditEventType](/api-reference/scalars-and-enums.md#auditeventtype/) | |

**Returns:** [DomainEvent!](/api-reference/objects.md#domainevent/)

### auditEventOccurred

Subscribe to audit events including auth events. Useful for security monitoring and compliance.

```graphql
auditEventOccurred(
  organizationId: UUID
  eventCategory: String
): AuditEvent!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `organizationId` | [UUID](/api-reference/scalars-and-enums.md#uuid/) | |
| `eventCategory` | `String` | |

**Returns:** [AuditEvent!](/api-reference/objects.md#auditevent/)
