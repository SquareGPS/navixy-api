---
description: Cursor-based pagination in Navixy Repository API
---

# Pagination

When querying lists of entities (devices, assets, users, etc.), Navixy Repository API returns paginated results. This prevents overwhelming responses when you have thousands of records.

To control which results appear and in what order, see [Filtering and sorting](filtering-and-sorting.md).

## Where pagination applies

The API has two types of queries for fetching data:

* **Single-entity queries** return one item by ID. They use singular names: `device`, `asset`, `organization`.
* **List queries** return multiple items matching your criteria. They use plural names: `devices`, `assets`, `organizations`.

Pagination applies to all list queries. They return connection types following a consistent pattern: `devices` returns `DeviceConnection`, `assets` returns `AssetConnection`, `auditEvents` returns `AuditEventConnection`, and so on.

Many nested fields are also paginated — for example, `Organization.devices` or `AssetGroup.items`. You can identify paginated fields by their return type (anything ending in `Connection`) or by the presence of `first`, `after`, `last`, and `before` arguments.

See the [Queries ](operations-and-types/queries.md)reference for the complete list of available queries, or use [introspection ](graphql-basics.md#introspection)to explore them in your GraphQL client.

## The Connection pattern

Navixy Repository API uses [Relay Cursor Connections](https://relay.dev/graphql/connections.htm), a pagination standard from the GraphQL community. Instead of traditional page numbers, it uses opaque cursors that point to specific positions in the result set.

Using cursors instead of page numbers enables the following:

* Stable results: If new items are added while you're paginating, you won't see duplicates or miss items.
* Efficient: The database can resume from exact positions without re-scanning.
* Flexible: Works well with real-time data that changes frequently.

## Paginated query structure

Every paginated query returns a **Connection** type with this structure:

```graphql
type DeviceConnection {
  edges: [DeviceEdge!]!    # List of results with cursors
  nodes: [Device!]!        # Direct access to entities (shorthand)
  pageInfo: PageInfo!      # Pagination metadata
  total: CountInfo         # Total matching items (may be null)
}

type DeviceEdge {
  node: Device!            # The actual entity
  cursor: String!          # Position marker for this item
}

type PageInfo {
  hasNextPage: Boolean!    # More items after this page?
  hasPreviousPage: Boolean!# More items before this page?
  startCursor: String      # Cursor of first item in this page
  endCursor: String        # Cursor of last item in this page
}

type CountInfo {
  count: Int!              # The number of matching items
  precision: CountPrecision! # How the count was determined
}
```

## Reading results

You can access entities in two ways:

* `edges[].node`: includes cursor for each item (useful when you need cursors)
* `nodes[]`: direct array of entities (simpler when you only need the data)

Check `pageInfo.hasNextPage` to determine if more data is available.

## Pagination parameters

Pagination arguments are passed directly to the query:

| Parameter | Type   | Description                                                     |
| --------- | ------ | --------------------------------------------------------------- |
| `first`   | Int    | Number of items to fetch from the start (default: 20, max: 100) |
| `after`   | String | Cursor — fetch items after this position                        |
| `last`    | Int    | Number of items to fetch from the end                           |
| `before`  | String | Cursor — fetch items before this position                       |

Use `first`/`after` for forward pagination (most common). Use `last`/`before` for backward pagination.

## Forward pagination

Start by requesting the first page, then use `endCursor` to get subsequent pages.

#### First page

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    first: 20
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
    total {
      count
      precision
    }
  }
}
```

### Next page

To fetch the next page, pass `endCursor` from the previous response as the `after` argument:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    first: 20
    after: "cursor-from-previous-response"
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
    last: 20
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

To get the previous page, use `startCursor` as the `before` argument:

```graphql
query {
  auditEvents(
    organizationId: "your-organization-uuid"
    last: 20
    before: "cursor-from-previous-response"
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

## Understanding total count

The `total` field returns information about how many items match your query. Because counting can be expensive for large datasets, the API provides a `precision` field that indicates how the count was determined:

| Precision     | Meaning                                                   |
| ------------- | --------------------------------------------------------- |
| `EXACT`       | Precise count from a full database scan                   |
| `APPROXIMATE` | Estimate from table statistics (faster but less accurate) |
| `AT_LEAST`    | Counting stopped early; at least this many items exist    |

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    first: 50
  ) {
    nodes {
      id
      title
    }
    total {
      count      # e.g., 1523
      precision  # e.g., EXACT or APPROXIMATE
    }
  }
}
```

For large datasets, the API may return an approximate count or `null` for the entire `total` field to maintain performance. Design your UI to handle these cases gracefully — for example, display "About 10,000 results" or "1,000+ results" instead of requiring an exact number.

## Best practices

**Choose an appropriate page size.** Use 20–50 items for UI lists, up to 100 for background sync. The default is 20 if not specified, and the maximum is 100 per request.

**Keep sort parameters consistent.** Cursors encode the sort position, so changing `orderBy` between requests invalidates existing cursors. Always use the same `orderBy` value when paginating through a result set. If you need a different sort order, start pagination from the beginning.

**Don't store cursors long-term.** Cursors are meant for immediate pagination within a session. They may become invalid after data changes affecting sort order, server updates, or extended time periods.

**Handle empty results.** Always check for empty `nodes` or `edges` arrays before processing results.

**No random page access.** Cursor-based pagination doesn't support "jump to page 50" — you can only navigate sequentially through results. This is a deliberate trade-off for stability and performance. If you need random access to pages, consider limiting the result set with filters first.
