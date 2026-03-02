# Common resources

Shared types, interfaces, and scalars used across the API including pagination, connections, and base interfaces.

## Queries

### node

Retrieves any entity by its globally unique identifier.

```graphql
node(id: ID!): Node
```

**Arguments**

| Name | Type  | Description                       |
| ---- | ----- | --------------------------------- |
| `id` | `ID!` | The ID of the entity to retrieve. |

**Output types:**

<details>

<summary><code>Node</code></summary>

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

</details>

### nodes

Retrieves multiple entities by their globally unique identifiers. Returns items in the same order as the input IDs.

```graphql
nodes(ids: [ID!]!): [Node]!
```

**Arguments**

| Name  | Type     | Description                          |
| ----- | -------- | ------------------------------------ |
| `ids` | `[ID!]!` | The IDs of the entities to retrieve. |

**Output types:**

<details>

<summary><code>Node</code></summary>

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

</details>

## Types

### PageInfo

Information about the current page in a paginated connection.

| Field             | Type       | Description                                                |
| ----------------- | ---------- | ---------------------------------------------------------- |
| `hasNextPage`     | `Boolean!` | Whether more items exist after the current page.           |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page.          |
| `startCursor`     | `String`   | The cursor pointing to the first item in the current page. |
| `endCursor`       | `String`   | The cursor pointing to the last item in the current page.  |

### CountInfo

Information about the total count of items in a connection.

| Field       | Type                                                  | Description                             |
| ----------- | ----------------------------------------------------- | --------------------------------------- |
| `count`     | `Int!`                                                | The count of items matching the filter. |
| `precision` | [CountPrecision](common-resources.md#countprecision)! | The precision level of the count value. |

### DeletePayload

The result of a delete mutation.

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

## Enums

### OrderDirection

| Value  | Description                                                                   |
| ------ | ----------------------------------------------------------------------------- |
| `ASC`  | Sort in ascending order (A→Z, 0→9, oldest→newest). NULL values appear last.   |
| `DESC` | Sort in descending order (Z→A, 9→0, newest→oldest). NULL values appear first. |

### CountPrecision

The precision level of a total count value.

| Value         | Description                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `EXACT`       | The count is exact, calculated using `COUNT(*)`.                                |
| `APPROXIMATE` | The count is approximate, derived from table statistics.                        |
| `AT_LEAST`    | At least this many items exist. Counting stopped early for performance reasons. |

## Interfaces

### Node

An object with a globally unique identifier.

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

### Titled

An object with a human-readable display name.

| Field   | Type      | Description                      |
| ------- | --------- | -------------------------------- |
| `title` | `String!` | The human-readable display name. |

### Customizable

An object that supports custom field values.

| Field          | Type                              | Description |
| -------------- | --------------------------------- | ----------- |
| `customFields` | [JSON](common-resources.md#json)! |             |

### Versioned

An object that supports optimistic locking for concurrency control.

| Field     | Type   | Description |
| --------- | ------ | ----------- |
| `version` | `Int!` |             |

### MultiValue

An interface for field parameters that support selecting multiple values.

| Field     | Type       | Description                                             |
| --------- | ---------- | ------------------------------------------------------- |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |

### Edge

An edge in a paginated connection.

| Field    | Type      | Description                                          |
| -------- | --------- | ---------------------------------------------------- |
| `cursor` | `String!` | An opaque cursor for this edge, used for pagination. |

### Connection

A paginated connection following the Relay Cursor Connections specification.

| Field      | Type                                       | Description                                   |
| ---------- | ------------------------------------------ | --------------------------------------------- |
| `pageInfo` | [PageInfo](common-resources.md#pageinfo)!  | Information about the current page.           |
| `total`    | [CountInfo](common-resources.md#countinfo) | The total count of items matching the filter. |

## Scalars

### DateTime

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime string with timezone ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)). Example: `2024-01-15T10:30:00Z`.

**Specification:** [https://scalars.graphql.org/chillicream/date-time.html](https://scalars.graphql.org/chillicream/date-time.html)

### Date

**Specification:** [https://scalars.graphql.org/chillicream/date.html](https://scalars.graphql.org/chillicream/date.html)

### JSON

**Specification:** [https://www.rfc-editor.org/rfc/rfc8259](https://www.rfc-editor.org/rfc/rfc8259)

### Locale

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/locale](https://the-guild.dev/graphql/scalars/docs/scalars/locale)

### EmailAddress

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/email-address](https://the-guild.dev/graphql/scalars/docs/scalars/email-address)

### HexColorCode

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/hex-color-code](https://the-guild.dev/graphql/scalars/docs/scalars/hex-color-code)

### CountryCode

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/country-code](https://the-guild.dev/graphql/scalars/docs/scalars/country-code)

### Code

A machine-readable identifier code. Constraints: - Allowed characters: ASCII letters (a-z, A-Z), digits (0-9), underscore (\_), dot (.), hyphen (-) - Must start with a letter or digit - Case-insensitive for uniqueness checks - Maximum length: 64 characters Naming conventions: - System items: UPPER\_SNAKE\_CASE (e.g., DEVICE\_TYPE, ACTIVE) - User items: any valid format (e.g., vehicle\_car, sensor-v2) Examples: DEVICE\_TYPE, vehicle\_car, status.active, sensor-v2, ABC123

**Specification:** [https://api.navixy.com/spec/scalars/code](https://api.navixy.com/spec/scalars/code)
