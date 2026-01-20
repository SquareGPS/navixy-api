---
description: Understand Navixy Repository API errors based on RFC 9457 format
---

# Error handling

When an operation fails, the API returns an error response with details to help you understand what went wrong and how to fix it. All errors follow the [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) format, providing both human-readable messages and machine-readable codes.

## Error response structure

Errors are returned in the standard GraphQL format with additional details in the `extensions` field:

```json
{
  "errors": [{
    "message": "Human-readable message",
    "locations": [{ "line": 2, "column": 3 }],
    "path": ["device"],
    "extensions": {
      // RFC 9457 standard fields
      "type": "https://api.navixy.com/errors/not-found",
      "title": "Resource Not Found",
      "status": 404,
      "detail": "Device with ID '019a6a3f-...' does not exist",
      "instance": "/graphql",
      
      // Navixy-specific fields
      "code": "NOT_FOUND",
      "entityType": "Device",
      "entityId": "019a6a3f-...",
      "traceId": "0af7651916cd43dd8448eb211c80319c",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }],
  "data": { "device": null }
}
```

### Standard fields

Every error includes these RFC 9457 standard fields:

<table><thead><tr><th width="100">Field</th><th width="100">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>type</code></td><td>URI</td><td>Identifies the error type. Resolves to documentation.</td></tr><tr><td><code>title</code></td><td>String</td><td>Summary of the problem type. Stays the same for all errors of this type.</td></tr><tr><td><code>status</code></td><td>Integer</td><td>HTTP status code (e.g., 400, 404, 409).</td></tr><tr><td><code>detail</code></td><td>String</td><td>Human-readable explanation specific to this occurrence of the problem.</td></tr><tr><td><code>instance</code></td><td>URI</td><td>The request path that caused the error. Useful for logs or support tickets.</td></tr></tbody></table>

### Navixy-specific fields

<table><thead><tr><th width="181.60003662109375">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>code</code></td><td>Machine-readable error code for use in your application logic.</td></tr><tr><td><code>traceId</code></td><td>Distributed tracing ID (32 hex characters). Correlates with the <code>traceparent</code> header if provided.</td></tr><tr><td><code>timestamp</code></td><td>When the error occurred (<a href="https://www.iso.org/iso-8601-date-and-time-format.html"><code>ISO 8601 format</code></a>).</td></tr><tr><td><code>field</code></td><td>For validation errors: the field that failed validation (e.g., <code>input.title</code>).</td></tr><tr><td><code>entityType</code></td><td>For entity-related errors: type of entity involved (e.g., <code>Device</code>).</td></tr><tr><td><code>entityId</code></td><td>For entity-related errors: ID of entity involved.</td></tr><tr><td><code>expectedVersion</code></td><td>For conflict errors: the version you provided.</td></tr><tr><td><code>currentVersion</code></td><td>For conflict errors: the actual current version.</td></tr><tr><td><code>constraint</code></td><td>For duplicate errors: the database constraint that was violated.</td></tr><tr><td><code>allowedValues</code></td><td>For enum validation errors: the list of valid options.</td></tr></tbody></table>

## Error codes

<table><thead><tr><th width="190.79998779296875">Code</th><th width="69.39996337890625">Status</th><th width="263">Type URI</th><th>Description</th></tr></thead><tbody><tr><td><code>UNAUTHORIZED</code></td><td>401</td><td><code>.../errors/unauthorized</code></td><td>Authentication is missing or invalid.</td></tr><tr><td><code>PERMISSION_DENIED</code></td><td>403</td><td><code>.../errors/forbidden</code></td><td>You don't have permission to perform this action.</td></tr><tr><td><code>NOT_FOUND</code></td><td>404</td><td><code>.../errors/not-found</code></td><td>The requested entity does not exist.</td></tr><tr><td><code>VALIDATION_ERROR</code></td><td>400</td><td><code>.../errors/validation</code></td><td>Input data failed validation.</td></tr><tr><td><code>CONFLICT</code></td><td>409</td><td><code>.../errors/conflict</code></td><td>The entity was modified by another request. See <a href="optimistic-locking.md">Optimistic locking</a>.</td></tr><tr><td><code>DUPLICATE</code></td><td>409</td><td><code>.../errors/duplicate</code></td><td>A unique constraint was violated (e.g., duplicate identifier).</td></tr><tr><td><code>RATE_LIMITED</code></td><td>429</td><td><code>.../errors/rate-limited</code></td><td>Request limit exceeded. Wait and retry.</td></tr><tr><td><code>QUERY_TOO_COMPLEX</code></td><td>400</td><td><code>.../errors/query-too-complex</code></td><td>Query exceeds the allowed complexity limit.</td></tr><tr><td><code>QUERY_TOO_DEEP</code></td><td>400</td><td><code>.../errors/query-too-deep</code></td><td>Query exceeds the allowed nesting depth.</td></tr><tr><td><code>INTERNAL_ERROR</code></td><td>500</td><td><code>.../errors/internal</code></td><td>An internal error has occurred.</td></tr><tr><td><code>SERVICE_UNAVAILABLE</code></td><td>503</td><td><code>.../errors/service-unavailable</code></td><td>A downstream service is temporarily unavailable.</td></tr></tbody></table>

## HTTP status codes

Navixy Repository API follows the [GraphQL-over-HTTP specification](https://graphql.github.io/graphql-over-http/draft/), which means HTTP status codes reflect transport-level results, not domain-level errors.

<table><thead><tr><th width="128.4000244140625">HTTP Status</th><th>Meaning</th></tr></thead><tbody><tr><td>200</td><td>Request processed successfully. Check the <code>errors</code> array for any domain-level failures.</td></tr><tr><td>400</td><td>Invalid HTTP or GraphQL request (parse or validation error).</td></tr><tr><td>401</td><td>Authentication required or invalid.</td></tr><tr><td>403</td><td>Authorization failed (forbidden).</td></tr><tr><td>429</td><td>Rate limit exceeded.</td></tr><tr><td>5xx</td><td>Infrastructure or system error.</td></tr></tbody></table>

All business logic errors (such as `NOT_FOUND`, `CONFLICT`, or `VALIDATION_ERROR`) return HTTP 200 with the semantic status code in `extensions.status`. Use `extensions.code` for programmatic error handling, not the HTTP status.

## Common error scenarios

### **Validation error (400)**

Returned when the input data doesn't meet requirements.

```json
{
  "errors": [{
    "message": "Validation failed",
    "path": ["createDevice", "input", "title"],
    "extensions": {
      "type": "https://api.navixy.com/errors/validation",
      "title": "Validation Error",
      "status": 400,
      "detail": "Field 'title' must not be empty",
      "instance": "/graphql",
      "code": "VALIDATION_ERROR",
      "field": "title",
      "traceId": "0af7651916cd43dd8448eb211c80319c",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** Check the `field` to identify which input failed, and `detail` for the specific requirement.

### **Permission denied (403)**

Returned when you lack the permission for an operation.

```json
{
  "errors": [{
    "message": "Access denied",
    "path": ["deleteDevice"],
    "extensions": {
      "type": "https://api.navixy.com/errors/forbidden",
      "title": "Forbidden",
      "status": 403,
      "detail": "Actor lacks DELETE permission on device 550e8400-...",
      "instance": "/graphql",
      "code": "PERMISSION_DENIED",
      "entityType": "device",
      "entityId": "550e8400-e29b-41d4-a716-446655440001",
      "requiredAction": "DELETE",
      "traceId": "0af7651916cd43dd8448eb211c80319c",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** The `requiredAction` tells you what permission is needed. Contact your administrator to request access.

### **Entity not found (404)**

Returned when you request an entity that doesn't exist or has been deleted.

```json
{
  "errors": [{
    "message": "Device not found",
    "path": ["device"],
    "locations": [{ "line": 1, "column": 9 }],
    "extensions": {
      "type": "https://api.navixy.com/errors/not-found",
      "title": "Resource Not Found",
      "status": 404,
      "detail": "Device with ID '019a6a3f-793e-807b-8001-555345529b44' does not exist",
      "code": "NOT_FOUND",
      "entityType": "Device",
      "entityId": "019a6a3f-793e-807b-8001-555345529b44",
      "traceId": "0af7651916cd43dd8448eb211c80319c"
    }
  }],
  "data": { "device": null }
}
```

**How to handle:** Check that the ID is correct. If you're using an ID from a previous response, the entity may have been deleted.

### **Version conflict (409)**

Returned when the entity was modified by another request since you last fetched it. See Optimistic locking for details.

```json
{
  "errors": [{
    "message": "Entity has been modified by another request",
    "path": ["updateDevice"],
    "extensions": {
      "type": "https://api.navixy.com/errors/conflict",
      "title": "Conflict",
      "status": 409,
      "detail": "Device 550e8400-... was modified. Expected version 5, current version 6.",
      "instance": "/graphql",
      "code": "CONFLICT",
      "entityType": "device",
      "entityId": "550e8400-e29b-41d4-a716-446655440001",
      "expectedVersion": 5,
      "currentVersion": 6,
      "traceId": "0af7651916cd43dd8448eb211c80319c",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** Fetch the entity again to get the current version, merge your changes if needed, and retry with the new version in your update input.

## Best practices

1. **Always check for errors.** Inspect the `errors` array in every response, even when the HTTP status is 200 (GraphQL can return partial data with errors).
2. **Use `code` for logic, `detail` for display.** The `code` field is stable and safe for programmatic handling. The `detail` field is human-readable and suitable for showing to users.
3. **Log the `traceId`.** When users report issues, `trace ID` helps the support quickly locate the relevant logs. Include it in your bug reports.
4. **Handle conflicts gracefully.** In collaborative applications, version conflicts are expected. Implement retry logic or prompt users to review changes.
