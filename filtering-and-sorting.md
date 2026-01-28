---
description: >-
  Use filter and orderBy on list queries, including custom-field conditions,
  text search, and sort rules that affect pagination cursors.
---

# Filtering and sorting

in Navixy Repository API, list queries (those returning multiple items, like `devices`, `assets`, or `organizations`) accept `filter` and `orderBy` arguments that let you control which results come back and in what order. Instead of fetching all devices and processing them client-side, you can request exactly what you need.

For navigating through large result sets, see [Pagination](pagination.md).

## Filtering

Pass a `filter` argument to any list query to narrow down results:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    filter: {
      statusIds: ["status-active-uuid"]
    }
  ) {
    nodes {
      id
      title
      status { title }
    }
  }
}
```

This returns only devices with the specified status.

Each entity type has its own filter input with different available fields. For example, `DeviceFilter` supports filtering by type, model, status, vendor, and inventory, while `OrganizationFilter` only supports filtering by parent and active status. Use [introspection ](operations-and-types/#introspection-and-schema)or the [API reference ](operations-and-types/)to see available filter fields for each entity.

### Filtering logic

Filters combine conditions using two types of logic:

| Location       | Logic | Meaning                 |
| -------------- | ----- | ----------------------- |
| Within a field | OR    | Match any of the values |
| Between fields | AND   | Match all conditions    |

Consider this filter:

```graphql
filter: {
  typeIds: ["type-truck-uuid", "type-van-uuid"]
  statusIds: ["status-active-uuid"]
}
```

This translates to:

```
(type = truck OR type = van) AND (status = active)
```

The result includes active trucks and active vans, but not inactive trucks or vehicles of other types.

### Empty values are ignored

If a filter field is `null` or an empty array, the API ignores it entirely:

```graphql
filter: {
  typeIds: []                        # Ignored — no filtering by type
  statusIds: ["status-active-uuid"]  # Applied
}
```

This is useful when building dynamic filters — you don't need to conditionally omit empty fields from your query.

### Text search

Most filters include a `titleContains` field for partial text matching:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    filter: {
      titleContains: "delivery"
    }
  ) {
    nodes {
      id
      title
    }
  }
}
```

This returns devices with "delivery" anywhere in their title, like "Delivery Van 1" or "North Delivery Truck". The search is case-insensitive.

Some filters have additional text search fields. For example, `DeviceFilter` includes `identifierContains` for searching hardware identifiers like IMEI numbers. Unlike `titleContains`, identifier search is case-sensitive.

### Limitations

The API does not support complex boolean expressions with nested AND/OR/NOT operators. If you need more complex filtering logic, apply the most restrictive server-side filter you can, then filter the results further in your application.

## Custom field filtering

Entities that support custom fields (devices, assets, geo objects, schedules) can be filtered by custom field values:

```graphql
query {
  assets(
    organizationId: "your-organization-uuid"
    filter: {
      customFields: [
        { code: "fuel_type", operator: EQ, value: "diesel" }
      ]
    }
  ) {
    nodes {
      id
      title
    }
  }
}
```

Each condition in the `customFields` array has three parts:

<table><thead><tr><th width="200.39996337890625">Field</th><th>Description</th></tr></thead><tbody><tr><td>code</td><td>The custom field's code, as defined in its CustomFieldDefinition</td></tr><tr><td>operator</td><td>How to compare the value</td></tr><tr><td>value</td><td>The value to compare against, formatted as JSON</td></tr></tbody></table>

### Operators

| Operator      | Description                             |
| ------------- | --------------------------------------- |
| EQ            | Equals                                  |
| NE            | Not equals                              |
| GT            | Greater than                            |
| GTE           | Greater than or equal                   |
| LT            | Less than                               |
| LTE           | Less than or equal                      |
| CONTAINS      | String contains (case-insensitive)      |
| IN            | Matches any value in the provided array |
| IS\_NULL      | Field has no value                      |
| IS\_NOT\_NULL | Field has a value                       |

### Value formats

The `value` field accepts JSON. Match the format to your field type:

| Field type        | JSON format          | Example                  |
| ----------------- | -------------------- | ------------------------ |
| STRING, TEXT      | string               | `"hello"`                |
| NUMBER            | number               | `42` or `3.14`           |
| BOOLEAN           | boolean              | `true`                   |
| DATE              | string (YYYY-MM-DD)  | `"2024-01-15"`           |
| DATETIME          | string (RFC 3339)    | `"2024-01-15T10:30:00Z"` |
| OPTIONS           | string (option code) | `"option_a"`             |
| DEVICE, REFERENCE | string (entity ID)   | `"019a6a3f-..."`         |
| CATALOG, TAG      | string (item code)   | `"ITEM_CODE"`            |

For IS\_NULL and IS\_NOT\_NULL operators, omit the `value` field or set it to `null`.

### Multiple conditions

Multiple custom field conditions are combined with AND logic:

```graphql
filter: {
  customFields: [
    { code: "fuel_type", operator: EQ, value: "diesel" },
    { code: "year", operator: GTE, value: 2020 }
  ]
}
```

This returns assets where fuel type is diesel AND year is 2020 or later.

### Multi-value fields

For custom fields configured to hold multiple values (`isMulti: true`), the filter matches if any stored value satisfies the condition:

```graphql
# Asset has colors: ["red", "blue", "white"]
filter: {
  customFields: [
    { code: "colors", operator: EQ, value: "red" }
  ]
}
# Matches — "red" is one of the values
```

### Combining standard and custom filters

You can use standard filter fields and custom field conditions together:

```graphql
query {
  devices(
    organizationId: "your-organization-uuid"
    filter: {
      typeIds: ["type-truck-uuid"]
      statusIds: ["status-active-uuid", "status-maintenance-uuid"]
      titleContains: "north"
      customFields: [
        { code: "region", operator: EQ, value: "northwest" }
      ]
    }
  ) {
    nodes {
      id
      title
    }
  }
}
```

This returns trucks that are active or in maintenance, have "north" in their title, and are assigned to the northwest region.

## Sorting

Use the `orderBy` argument to control the order of results:

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

The `direction` can be ASC (ascending: A→Z, 0→9, oldest→newest) or DESC (descending: Z→A, 9→0, newest→oldest).

Each entity type has its own set of sortable fields. For example, devices can be sorted by TITLE, while audit events can be sorted by OCCURRED\_AT. Use introspection or the API reference to see available sort fields.

### Sort behavior

Text fields use natural sorting with ICU collation:

* Case-insensitive: "apple" and "Apple" sort together
* Locale-aware: accented characters sort correctly (é sorts with e, not after z)
* Numeric-aware: "item2" comes before "item10"

NULL values appear last when sorting ASC, and first when sorting DESC.

### Sorting by custom fields

Some entity types (devices, assets, geo objects, schedules) support sorting by custom field values:

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

Use either `field` or `customFieldCode` in your orderBy input, not both — they are mutually exclusive.

### Sorting and pagination

Cursors encode the current sort position. If you change `orderBy` between pagination requests, your existing cursors become invalid. Always use the same `orderBy` value when paginating through a result set. If you need a different sort order, start from the beginning.
