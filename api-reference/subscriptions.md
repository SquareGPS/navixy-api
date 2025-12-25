# Subscriptions

Subscriptions provide real-time updates via WebSocket connections.

### WebSocket endpoint

```
wss://api.navixy.com/v4/graphql/ws
```

#### domainEvent

Subscribe to domain events. Filter by organization, entity type, and/or event type. All parameters are optional - omit for broader subscription.

```graphql
subscription {
  domainEvent(
    organizationId: UUID,
    aggregateType: String,
    eventType: AuditEventType
  ) {
    # fields...
  }
}
```

**Arguments**

| Name             | Type           | Description     |
| ---------------- | -------------- | --------------- |
| `organizationId` | UUID           | Optional filter |
| `aggregateType`  | String         | Optional filter |
| `eventType`      | AuditEventType | Optional filter |

**Returns:** DomainEvent!

#### auditEventOccurred

Subscribe to audit events, including auth events. Useful for security monitoring and compliance.

```graphql
subscription {
  auditEventOccurred(
    organizationId: UUID,
    eventCategory: String
  ) {
    # fields...
  }
}
```

**Arguments**

| Name             | Type   | Description     |
| ---------------- | ------ | --------------- |
| `organizationId` | UUID   | Optional filter |
| `eventCategory`  | String | Optional filter |

**Returns:** AuditEvent!
