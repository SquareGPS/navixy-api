# Pagination

When querying lists of entities (devices, assets, users, etc.), the API returns paginated results. This prevents overwhelming responses when you have thousands of records.

### The Connection pattern

Navixy Repository API uses [Relay Cursor Connections](https://relay.dev/graphql/connections.htm), a pagination standard from the GraphQL community. Instead of traditional page numbers, it uses opaque cursors that point to specific positions in the result set.

Using cursors instead of page numbers enables the following:

* Stable results: If new items are added while you're paginating, you won't see duplicates or miss items.
* Efficient: The database can resume from exact positions without re-scanning.
* Flexible: Works well with real-time data that changes frequently.

#### Structure

Every paginated query returns a **Connection** type with this structure:

```graphql
type DeviceConnection {
  edges: [DeviceEdge!]!      # List of results with cursors
  pageInfo: PageInfo!         # Pagination metadata
}

type DeviceEdge {
  node: Device!               # The actual entity
  cursor: String!             # Position marker for this item
}

type PageInfo {
  hasNextPage: Boolean!       # More items after this page?
  hasPreviousPage: Boolean!   # More items before this page?
  startCursor: String         # Cursor of first item in this page
  endCursor: String           # Cursor of last item in this page
  totalCount: Int             # Total matching items (may be null for large datasets)
}
```

#### Reading results

To get the actual entities from a paginated response, access them through `edges[].node`. Check `pageInfo.hasNextPage` to determine if more data is available.

### Pagination parameters

Use `PaginationInput` to control which page of results you receive:

| Parameter | Type   | Description                               |
| --------- | ------ | ----------------------------------------- |
| `first`   | Int    | Number of items to fetch from the start   |
| `after`   | String | Cursor — fetch items after this position  |
| `last`    | Int    | Number of items to fetch from the end     |
| `before`  | String | Cursor — fetch items before this position |

Use `first`/`after` for forward pagination (most common). Use `last`/`before` for backward pagination.

### Forward pagination

Start by requesting the first page, then use `endCursor` to get subsequent pages.

#### First page

```graphql
query {
  devices(
    filter: { organizationId: "your-organization-uuid" }
    pagination: { first: 20 }
  ) {
    edges {
      node {
        id
        title
        status { code title }
      }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
      totalCount
    }
  }
}
```

#### Next page

To fetch the next page, pass `endCursor` from the previous response as the `after` parameter:

```graphql
query {
  devices(
    filter: { organizationId: "your-organization-uuid" }
    pagination: { 
      first: 20
      after: "cursor-from-previous-response"
    }
  ) {
    edges {
      node {
        id
        title
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Repeat this pattern — using each response's `endCursor` as the next request's `after` — until `hasNextPage` is `false`.

### Backward pagination

Use `last` and `before` to paginate from the end of the result set. This is useful for showing the most recent items first.

```graphql
query {
  auditEvents(
    filter: { organizationId: "your-organization-uuid" }
    pagination: { last: 20 }
  ) {
    edges {
      node {
        eventType
        occurredAt
      }
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
    filter: { organizationId: "your-organization-uuid" }
    pagination: { 
      last: 20
      before: "cursor-from-previous-response"
    }
  ) {
    edges {
      node {
        eventType
        occurredAt
      }
    }
    pageInfo {
      hasPreviousPage
      startCursor
    }
  }
}
```

### Combining with filters and sorting

Pagination works with filters and sorting. The `totalCount` reflects filtered results:

```graphql
query {
  devices(
    filter: { 
      organizationId: "your-organization-uuid"
      statusId: "active-status-uuid"
      title: "Truck"
    }
    pagination: { first: 50 }
    sort: ["title:ASC", "createdAt:DESC"]
  ) {
    edges {
      node {
        id
        title
        createdAt
      }
    }
    pageInfo {
      hasNextPage
      endCursor
      totalCount
    }
  }
}
```

### Best practices

#### Choose an appropriate page size

* **UI lists**: 20–50 items per page
* **Background sync**: 100–200 items per page
* **Maximum**: The API may limit page size; check error responses

#### Use totalCount carefully

`totalCount` requires counting all matching records, which can be expensive:

* **< 10K records**: Returns exact count
* **10K – 100K records**: Returns exact count but may be slow
* **> 100K records**: May return an approximate value or `null`

Only request `totalCount` when you need to display totals. For large datasets, consider UI patterns that don't require exact counts, such as "Showing 50 of 10,000+" infinite scroll with a "Load more" button, or "More than 1000 results found" without a specific number.

#### Keep sort parameters consistent

Cursors encode the sort position, so changing sort parameters between requests invalidates existing cursors. Always use the same `sort` value when paginating through a result set. If you need a different sort order, start pagination from the beginning.

#### Don't store cursors long-term

Cursors are meant for immediate pagination within a session. They may become invalid after:

* Data changes affecting sort order
* Server updates
* Extended time periods

#### Handle empty results

Always check for empty edge arrays before processing results.

#### No random page access

Cursor-based pagination doesn't support "jump to page 50" — you can only navigate sequentially through results. This is a deliberate trade-off for stability and performance. If you need random access to pages, consider limiting the result set with filters first.

### Paginated queries reference

These queries support pagination:

| Query           | Returns                |
| --------------- | ---------------------- |
| `devices`       | DeviceConnection       |
| `assets`        | AssetConnection        |
| `organizations` | OrganizationConnection |
| `users`         | UserConnection         |
| `geoObjects`    | GeoObjectConnection    |
| `schedules`     | ScheduleConnection     |
| `auditEvents`   | AuditEventConnection   |

Nested fields that support pagination:

| Parent type  | Field        | Returns                  |
| ------------ | ------------ | ------------------------ |
| Organization | `devices`    | DeviceConnection         |
| Organization | `assets`     | AssetConnection          |
| Organization | `geoObjects` | GeoObjectConnection      |
| Organization | `schedules`  | ScheduleConnection       |
| AssetGroup   | `history`    | AssetGroupItemConnection |
| Inventory    | `devices`    | DeviceConnection         |
