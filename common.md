# Common types

Foundational types, scalars, and interfaces used throughout the API.

## Queries

### node

Retrieves any entity by its globally unique identifier.

```graphql
node(id: ID!): Node
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `ID!` | The ID of the entity to retrieve. |

**Output types:**

<details>

<summary>Node</summary>

An object with a globally unique identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

</details>

---

### nodes

Retrieves multiple entities by their globally unique identifiers. Returns items in the same order as the input IDs.

```graphql
nodes(ids: [ID!]!): [Node]!
```

**Arguments**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `ids` | `[ID!]!` | The IDs of the entities to retrieve. |

**Output types:**

<details>

<summary>Node</summary>

An object with a globally unique identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

</details>

---

## Objects

### PageInfo

Information about the current page in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after the current page. |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page. |
| `startCursor` | `String` | The cursor pointing to the first item in the current page. |
| `endCursor` | `String` | The cursor pointing to the last item in the current page. |

---

### CountInfo

Information about the total count of items in a connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `count` | `Int!` | The count of items matching the filter. |
| `precision` | [CountPrecision](common.md#countprecision)! | The precision level of the count value. |

---

### DeletePayload

The result of a delete mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

---

## Enums

### OrderDirection

| Value | Description |
| ----- | ----------- |
| `ASC` | Sort in ascending order (A→Z, 0→9, oldest→newest). NULL values appear last. |
| `DESC` | Sort in descending order (Z→A, 9→0, newest→oldest). NULL values appear first. |

---

### CountPrecision

The precision level of a total count value.

| Value | Description |
| ----- | ----------- |
| `EXACT` | The count is exact, calculated using `COUNT(*)`. |
| `APPROXIMATE` | The count is approximate, derived from table statistics. |
| `AT_LEAST` | At least this many items exist. Counting stopped early for performance reasons. |

---

## Interfaces

### Node

An object with a globally unique identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

---

### Titled

An object with a human-readable display name.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String!` | The human-readable display name. |

---

### Customizable

An object that supports custom field values.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |

---

### Versioned

An object that supports optimistic locking for concurrency control.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |

---

### MultiValue

An interface for field parameters that support selecting multiple values.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |

---

### Edge

An edge in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge, used for pagination. |

---

### Connection

A paginated connection following the Relay Cursor Connections specification.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `pageInfo` | [PageInfo](common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](common.md#countinfo) | The total count of items matching the filter. |

---

## Scalars

### DateTime

An [ISO 8601](https://www.iso.org/standard/8601.html) datetime string with timezone ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html)). Example: `2024-01-15T10:30:00Z`.

**Specification:** [https://scalars.graphql.org/chillicream/date-time.html](https://scalars.graphql.org/chillicream/date-time.html)

---

### Date

**Specification:** [https://scalars.graphql.org/chillicream/date.html](https://scalars.graphql.org/chillicream/date.html)

---

### JSON

**Specification:** [https://www.rfc-editor.org/rfc/rfc8259](https://www.rfc-editor.org/rfc/rfc8259)

---

### GeoJSON

**Specification:** [https://www.rfc-editor.org/rfc/rfc7946](https://www.rfc-editor.org/rfc/rfc7946)

---

### Latitude

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/latitude](https://the-guild.dev/graphql/scalars/docs/scalars/latitude)

---

### Longitude

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/longitude](https://the-guild.dev/graphql/scalars/docs/scalars/longitude)

---

### Locale

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/locale](https://the-guild.dev/graphql/scalars/docs/scalars/locale)

---

### EmailAddress

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/email-address](https://the-guild.dev/graphql/scalars/docs/scalars/email-address)

---

### HexColorCode

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/hex-color-code](https://the-guild.dev/graphql/scalars/docs/scalars/hex-color-code)

---

### CountryCode

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/country-code](https://the-guild.dev/graphql/scalars/docs/scalars/country-code)

---

### Code

**Specification:** [https://api.navixy.com/spec/scalars/code](https://api.navixy.com/spec/scalars/code)

---
