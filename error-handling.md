# Error handling

When an operation fails, the API returns an error response with details to help you understand what went wrong and how to fix it. All errors follow the [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) format, providing both human-readable messages and machine-readable codes.

### Error response structure

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
      "title": "Not Found",
      "status": 404,
      "detail": "Device with ID 550e8400-... not found",
      "instance": "/graphql",
      
      // Navixy-specific fields
      "code": "NOT_FOUND",
      "entityType": "device",
      "entityId": "550e8400-...",
      "traceId": "7c9e6679-...",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

### Standard fields

Every error includes these standard fields:

<table><thead><tr><th width="134.60003662109375">Field</th><th width="116.4000244140625">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>type</code></td><td>URI</td><td>Identifies the error type. Resolves to documentation.</td></tr><tr><td><code>title</code></td><td>String</td><td>Summary of the problem type. Stays the same for all errors of this type.</td></tr><tr><td><code>status</code></td><td>Integer</td><td>HTTP status code (e.g., 400, 404, 409).</td></tr><tr><td><code>detail</code></td><td>String</td><td>Human-readable explanation specific to this occurrence of the problem.</td></tr><tr><td><code>instance</code></td><td>URI</td><td>The request path that caused the error. Useful for logs or support tickets.</td></tr></tbody></table>

### Navixy-specific fields

<table><thead><tr><th width="134.60003662109375">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>code</code></td><td>Machine-readable error code for use in your application logic.</td></tr><tr><td><code>traceId</code></td><td>Trace ID for debugging. Correlates with X-Trace-ID.</td></tr><tr><td><code>field</code></td><td>The field that failed validation.</td></tr><tr><td><code>entityType</code></td><td>Type of entity involved.</td></tr><tr><td><code>entityId</code></td><td>ID of entity involved.</td></tr><tr><td><code>timestamp</code></td><td>When the error occurred (ISO 8601 format).</td></tr></tbody></table>

### Error codes

<table><thead><tr><th width="172.20001220703125">Code</th><th width="59.7999267578125" data-type="number">HTTP Status</th><th width="230"></th><th>Description</th></tr></thead><tbody><tr><td><code>NOT_FOUND</code></td><td>404</td><td><code>.../errors/not-found</code></td><td>The requested entity does not exist.</td></tr><tr><td><code>VALIDATION_ERROR</code></td><td>400</td><td><code>.../errors/validation</code></td><td>Input data failed validation.</td></tr><tr><td><code>PERMISSION_DENIED</code></td><td>403</td><td><code>.../errors/forbidden</code></td><td>You don't have permission to perform this action.</td></tr><tr><td><code>UNAUTHORIZED</code></td><td>401</td><td><code>.../errors/unauthorized</code></td><td>Authentication is missing or invalid.</td></tr><tr><td><code>CONFLICT</code></td><td>409</td><td><code>.../errors/conflict</code></td><td>The entity was modified by another request. See <a href="optimistic-locking.md">Optimistic locking.</a></td></tr><tr><td><code>DUPLICATE</code></td><td>409</td><td><code>.../errors/duplicate</code></td><td>A unique constraint was violated (e.g., duplicate code or identifier).</td></tr><tr><td><code>RATE_LIMITED</code></td><td>429</td><td><code>.../errors/rate-limited</code></td><td>Request limit exceeded. Wait and retry.</td></tr><tr><td><code>INTERNAL_ERROR</code></td><td>500</td><td><code>.../errors/internal</code></td><td>An internal error has occurred.</td></tr></tbody></table>

### Common error scenarios

#### Entity not found (404)

Returned when you request an entity that doesn't exist or has been deleted.

```json
{
  "errors": [{
    "message": "Device not found",
    "path": ["device"],
    "extensions": {
      "type": "https://api.navixy.com/errors/not-found",
      "title": "Not Found",
      "status": 404,
      "detail": "Device with ID 550e8400-e29b-41d4-a716-446655440001 not found",
      "instance": "/graphql",
      "code": "NOT_FOUND",
      "entityType": "device",
      "entityId": "550e8400-e29b-41d4-a716-446655440001",
      "traceId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** Check that the ID is correct. If you're using an ID from a previous response, the entity may have been deleted.

#### Validation error (400)

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
      "traceId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** Check the `field` to identify which input failed, and `detail` for the specific requirement.

#### Permission denied (403)

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
      "traceId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** The `requiredAction` tells you what permission is needed. Contact your administrator to request access.

#### Version conflict (409)

Returned when the entity was modified by another request since you last fetched it. See [Optimistic locking](optimistic-locking.md) for details.

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
      "traceId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "timestamp": "2025-01-15T14:30:00.000Z"
    }
  }]
}
```

**How to handle:** Fetch the entity again to get the current version, merge your changes if needed, and retry with the new version in your update input.

### Best practices

1. Always check for errors. View the HTTP status code and the `errors` array in every response.
2. Use `code` for logic, `detail` for display. The `code` field is stable and safe for programmatic handling. The `detail` field is localized and suitable for showing to users.
3. Log the `traceId`. When users report issues, trace ID helps support quickly locate the relevant logs.
4. Handle conflicts gracefully. In collaborative applications, version conflicts are expected. Implement retry logic or prompt users to review changes.
