# Common resources

Foundational types, scalars, and interfaces used throughout the API.

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

<summary>Node</summary>

An object with a globally unique identifier.

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

</details>

***

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

<summary>Node</summary>

An object with a globally unique identifier.

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

</details>

***

## Objects

### PageInfo

Information about the current page in a paginated connection.

| Field             | Type       | Description                                                |
| ----------------- | ---------- | ---------------------------------------------------------- |
| `hasNextPage`     | `Boolean!` | Whether more items exist after the current page.           |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before the current page.          |
| `startCursor`     | `String`   | The cursor pointing to the first item in the current page. |
| `endCursor`       | `String`   | The cursor pointing to the last item in the current page.  |

***

### CountInfo

Information about the total count of items in a connection.

| Field       | Type                                        | Description                             |
| ----------- | ------------------------------------------- | --------------------------------------- |
| `count`     | `Int!`                                      | The count of items matching the filter. |
| `precision` | [CountPrecision](common.md#countprecision)! | The precision level of the count value. |

***

### DeletePayload

The result of a delete mutation.

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

***

## Enums

### OrderDirection

The direction for sorting query results.

| Value  | Description                                                                   |
| ------ | ----------------------------------------------------------------------------- |
| `ASC`  | Sort in ascending order (A→Z, 0→9, oldest→newest). NULL values appear last.   |
| `DESC` | Sort in descending order (Z→A, 9→0, newest→oldest). NULL values appear first. |

***

### CountPrecision

The precision level of a total count value.

| Value         | Description                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `EXACT`       | The count is exact, calculated using `COUNT(*)`.                                |
| `APPROXIMATE` | The count is approximate, derived from table statistics.                        |
| `AT_LEAST`    | At least this many items exist. Counting stopped early for performance reasons. |

***

## Interfaces

### Node

An object with a globally unique identifier.

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

***

### Titled

An object with a human-readable display name.

| Field   | Type      | Description                      |
| ------- | --------- | -------------------------------- |
| `title` | `String!` | The human-readable display name. |

***

### Customizable

An object that supports custom field values.

| Field          | Type    | Description                                                                     |
| -------------- | ------- | ------------------------------------------------------------------------------- |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |

***

### Versioned

An object that supports [optimistic locking](optimistic-locking.md) for concurrency control.

| Field     | Type   | Description                                                                                                                                 |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |

***

### MultiValue

An interface for field parameters that support selecting multiple values.

| Field     | Type       | Description                                             |
| --------- | ---------- | ------------------------------------------------------- |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |

***

### Edge

An edge in a paginated connection.

| Field    | Type      | Description                                          |
| -------- | --------- | ---------------------------------------------------- |
| `cursor` | `String!` | An opaque cursor for this edge, used for pagination. |

***

### Connection

A paginated connection following the Relay Cursor Connections specification.

| Field      | Type                             | Description                                   |
| ---------- | -------------------------------- | --------------------------------------------- |
| `pageInfo` | [PageInfo](common.md#pageinfo)!  | Information about the current page.           |
| `total`    | [CountInfo](common.md#countinfo) | The total count of items matching the filter. |

***

## Scalars

### DateTime

An [ISO 8601](https://www.iso.org/standard/8601.html) datetime string with timezone ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html)).

| Property      | Value                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| Format        | `YYYY-MM-DDTHH:mm:ss.sssZ`                                                                                       |
| Example       | `2025-01-15T14:30:00.000Z`                                                                                       |
| Specification | [https://scalars.graphql.org/chillicream/date-time.html](https://scalars.graphql.org/chillicream/date-time.html) |

***

### Date

An [ISO 8601](https://www.iso.org/standard/8601.html) date string without time component ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html)).

<table><thead><tr><th width="340.22216796875">Property</th><th>Value</th></tr></thead><tbody><tr><td>Format</td><td><code>YYYY-MM-DD</code></td></tr><tr><td>Example</td><td><code>2025-01-15</code></td></tr><tr><td>Specification</td><td><a href="https://scalars.graphql.org/chillicream/date.htm">https://scalars.graphql.org/chillicream/date.htm</a></td></tr></tbody></table>



***

### JSON

An arbitrary JSON value. Can be an object, array, string, number, boolean, or null.

| Property      | Value                                                                            |
| ------------- | -------------------------------------------------------------------------------- |
| Format        | `Any valid JSON`                                                                 |
| Example       | `{"key": "value", "count": 42}`                                                  |
| Specification | [https://www.rfc-editor.org/rfc/rfc8259](https://www.rfc-editor.org/rfc/rfc8259) |

***

### GeoJSON

A GeoJSON geometry object ([RFC 7946](https://www.rfc-editor.org/rfc/rfc7946.html)). Supports Point, LineString, Polygon, and other geometry types.

| Property      | Value                                                                            |
| ------------- | -------------------------------------------------------------------------------- |
| Format        | `GeoJSON geometry object`                                                        |
| Example       | `{"type": "Point", "coordinates": [125.6, 10.1]}`                                |
| Specification | [https://www.rfc-editor.org/rfc/rfc7946](https://www.rfc-editor.org/rfc/rfc7946) |

***

### Latitude

A geographic latitude coordinate in decimal degrees.

| Property | Value           |
| -------- | --------------- |
| Format   | `-90.0 to 90.0` |
| Example  | `37.7749`       |

***

### Longitude

A geographic longitude coordinate in decimal degrees.

| Property | Value             |
| -------- | ----------------- |
| Format   | `-180.0 to 180.0` |
| Example  | `-122.4194`       |

***

### Locale

A BCP 47 language tag identifying a user locale.

| Property      | Value                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Format        | `language-REGION`                                                                                                      |
| Example       | `en-US`, `fr-CA`                                                                                                       |
| Specification | [https://the-guild.dev/graphql/scalars/docs/scalars/locale](https://the-guild.dev/graphql/scalars/docs/scalars/locale) |

***

### EmailAddress

An email address conforming to [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322.html).

| Property | Value              |
| -------- | ------------------ |
| Format   | `user@domain`      |
| Example  | `user@example.com` |

***

### HexColorCode

A hexadecimal color code. Supports 3-digit (`#RGB`) or 6-digit (`#RRGGBB`) format.

| Property | Value     |
| -------- | --------- |
| Format   | `#RRGGBB` |
| Example  | `#FF5733` |

***

### CountryCode

An [ISO 3166](https://www.iso.org/standard/3166.html)-1 alpha-2 country code. Example: `US`, `GB`, `ES`.

| Property | Value                   |
| -------- | ----------------------- |
| Format   | `Two uppercase letters` |
| Example  | `US`                    |

***

### Code

A machine-readable identifier code.

Constraints:

* Allowed characters: ASCII letters (a-z, A-Z), digits (0-9), underscore (\_), dot (.), hyphen (-)
* Must start with a letter or digit
* Case-insensitive for uniqueness checks
* Maximum length: 64 characters

Naming conventions:

* System items: UPPER\_SNAKE\_CASE (e.g., DEVICE\_TYPE, ACTIVE)
* User items: any valid format (e.g., vehicle\_car, sensor-v2)

| Property | Value                                  |
| -------- | -------------------------------------- |
| Format   | `UPPER_SNAKE_CASE`, `lower_snake_case` |
| Example  | `DEVICE_TYPE`, `vehicle_type`          |

***
