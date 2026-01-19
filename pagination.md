# Pagination

When querying lists of entities (devices, assets, users, etc.), the API returns paginated results. This prevents overwhelming responses when you have thousands of records.

## The Connection pattern

Navixy Repository API uses [Relay Cursor Connections](https://relay.dev/graphql/connections.htm), a pagination standard from the GraphQL community. Instead of traditional page numbers, it uses opaque cursors that point to specific positions in the result set.

Using cursors instead of page numbers enables the following:

* Stable results: If new items are added while you're paginating, you won't see duplicates or miss items.
* Efficient: The database can resume from exact positions without re-scanning.
* Flexible: Works well with real-time data that changes frequently.

### Structure

Every paginated query returns a **Connection** type with this structure:

```graphql
type DeviceConnection {
  edges: [DeviceEdge!]!           # List of results with cursors
  nodes: [Device!]!               # Direct access to entities (shorthand)
  pageInfo: PageInfo!             # Pagination metadata
  totalCount: Int                 # Total matching items (may be null)
  totalCountPrecision: CountPrecision  # Precision of totalCount
}

type DeviceEdge {
  node: Device!                   # The actual entity
  cursor: String!                 # Position marker for this item
}

type PageInfo {
  hasNextPage: Boolean!           # More items after this page?
  hasPreviousPage: Boolean!       # More items before this page?
  startCursor: String             # Cursor of first item in this page
  endCursor: String               # Cursor of last item in this page
}
```

### Reading results

You can access entities in two ways:

* `edges[].node` : includes cursor for each item (useful when you need cursors)
* `nodes[]` : direct array of entities (simpler when you only need the data)

Check `pageInfo.hasNextPage` to determine if more data is available.

## Pagination parameters

Use `PaginationInput` to control which page of results you receive:

<table><thead><tr><th width="100">Parameter</th><th width="100">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>first</code></td><td>Int</td><td>Number of items to fetch from the start (default: 20, max: 100)</td></tr><tr><td><code>after</code></td><td>String</td><td>Cursor — fetch items after this position</td></tr><tr><td><code>last</code></td><td>Int</td><td>Number of items to fetch from the end</td></tr><tr><td><code>before</code></td><td>String</td><td>Cursor — fetch items before this position</td></tr></tbody></table>

Use `first`/`after` for forward pagination (most common). Use `last`/`before` for backward pagination.

## Sorting

Use the `orderBy` parameter to control the order of results. Each entity type has its own order input with supported fields:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    orderBy: { field: TITLE, direction: ASC }
  ) {
    nodes {
      id
      title
    }
  }
}
```

The `direction` can be `ASC` (ascending) or `DESC` (descending).

Some entity types also support sorting by custom fields:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    orderBy: { customFieldCode: "priority", direction: DESC }
  ) {
    nodes {
      id
      title
    }
  }
}
```

## Forward pagination

Start by requesting the first page, then use `endCursor` to get subsequent pages.

### First page

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    pagination: { first: 20 }
  ) {
    nodes {
      id
      title
      status { code title }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
    totalCountPrecision
  }
}
```

### Next page

To fetch the next page, pass `endCursor` from the previous response as the `after` parameter:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    pagination: { 
      first: 20
      after: "cursor-from-previous-response"
    }
  ) {
    nodes {
      id
      title
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Repeat this pattern — using each response's `endCursor` as the next request's `after` — until `hasNextPage` is `false`.

## Backward pagination

Use `last` and `before` to paginate from the end of the result set. This is useful for showing the most recent items first.

```graphql
query {
  auditEvents(
    organizationId: "your-organization-uuid"
    pagination: { last: 20 }
  ) {
    nodes {
      eventType
      occurredAt
    }
    pageInfo {
      hasPreviousPage
      startCursor
    }
  }
}
```

To get the previous page, use `startCursor` as the `before` parameter:

```graphql
query {
  auditEvents(
    organizationId: "your-organization-uuid"
    pagination: { 
      last: 20
      before: "cursor-from-previous-response"
    }
  ) {
    nodes {
      eventType
      occurredAt
    }
    pageInfo {
      hasPreviousPage
      startCursor
    }
  }
}
```

## Understanding totalCount

The `totalCount` field returns the total number of items matching your filter. Because counting can be expensive for large datasets, the API provides a `totalCountPrecision` field that indicates how the count was determined:

<table><thead><tr><th width="159.20001220703125">Precision</th><th>Meaning</th></tr></thead><tbody><tr><td><code>EXACT</code></td><td>Precise count from a full database scan</td></tr><tr><td><code>APPROXIMATE</code></td><td>Estimate from table statistics (faster but less accurate)</td></tr><tr><td><code>AT_LEAST</code></td><td>Counting stopped early; at least this many items exist</td></tr></tbody></table>

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    pagination: { first: 50 }
  ) {
    nodes {
      id
      title
    }
    totalCount           # e.g., 1523
    totalCountPrecision  # e.g., EXACT or APPROXIMATE
  }
}
```

For large datasets, the API may return an approximate count or `null` to maintain performance. Design your UI to handle these cases gracefully — for example, display "About 10,000 results" or "1,000+ results" instead of requiring an exact number.

## Best practices

### Choose an appropriate page size

* **UI lists**: 20–50 items per page
* **Background sync**: Up to 100 items per page
* **Default**: 20 items if not specified
* **Maximum**: 100 items per request

### Keep sort parameters consistent

Cursors encode the sort position, so changing `orderBy` between requests invalidates existing cursors. Always use the same `orderBy` value when paginating through a result set. If you need a different sort order, start pagination from the beginning.

### Don't store cursors long-term

Cursors are meant for immediate pagination within a session. They may become invalid after:

* Data changes affecting sort order
* Server updates
* Extended time periods

### Handle empty results

Always check for empty `nodes` or `edges` arrays before processing results.

### No random page access

Cursor-based pagination doesn't support "jump to page 50" — you can only navigate sequentially through results. This is a deliberate trade-off for stability and performance. If you need random access to pages, consider limiting the result set with filters first.

## Paginated queries reference

These queries support pagination:

<table><thead><tr><th width="262.4000244140625">Query</th><th>Returns</th></tr></thead><tbody><tr><td><code>devices</code></td><td><a href="api-reference/objects.md#deviceconnection">DeviceConnection</a></td></tr><tr><td><code>assets</code></td><td><a href="api-reference/objects.md#assetconnection">AssetConnection</a></td></tr><tr><td><code>assetGroups</code></td><td><a href="api-reference/objects.md#assetgroupconnection">AssetGroupConnection</a></td></tr><tr><td><code>organizations</code></td><td><a href="api-reference/objects.md#organizationconnection">OrganizationConnection</a></td></tr><tr><td><code>members</code></td><td><a href="api-reference/objects.md#memberconnection">MemberConnection</a></td></tr><tr><td><code>integrations</code></td><td><a href="api-reference/objects.md#integrationconnection">IntegrationConnection</a></td></tr><tr><td><code>geoObjects</code></td><td><a href="api-reference/objects.md#geoobjectconnection">GeoObjectConnection</a></td></tr><tr><td><code>schedules</code></td><td><a href="api-reference/objects.md#scheduleconnection">ScheduleConnection</a></td></tr><tr><td><code>inventories</code></td><td><a href="api-reference/objects.md#inventoryconnection">InventoryConnection</a></td></tr><tr><td><code>auditEvents</code></td><td><a href="api-reference/objects.md#auditeventconnection">AuditEventConnection</a></td></tr><tr><td><code>customFieldDefinitions</code></td><td><a href="api-reference/objects.md#customfielddefinitionpayload">CustomFieldDefinitionConnection</a></td></tr></tbody></table>

Nested fields that support pagination:

<table><thead><tr><th width="168.79998779296875">Parent type</th><th width="148.800048828125">Field</th><th>Returns</th></tr></thead><tbody><tr><td>Organization</td><td><code>devices</code></td><td><a href="api-reference/objects.md#deviceconnection">DeviceConnection</a></td></tr><tr><td>Organization</td><td><code>assets</code></td><td><a href="api-reference/objects.md#assetconnection">AssetConnection</a></td></tr><tr><td>Organization</td><td><code>geoObjects</code></td><td><a href="api-reference/objects.md#geoobjectconnection">GeoObjectConnection</a></td></tr><tr><td>Organization</td><td><code>schedules</code></td><td><a href="api-reference/objects.md#scheduleconnection">ScheduleConnection</a></td></tr><tr><td>AssetGroup</td><td><code>history</code></td><td><a href="api-reference/objects.md#assetgroupitemconnection">AssetGroupItemConnection</a></td></tr><tr><td>Inventory</td><td><code>devices</code></td><td><a href="api-reference/objects.md#deviceconnection">DeviceConnection</a></td></tr></tbody></table>
