# Scalars

Navixy Repository API defines these custom scalar types in addition to the standard GraphQL scalars. See [GraphQL basics](../graphql-basics.md#scalar-types) for the description of the predefined scalars (String, Int, Float, Boolean, ID).

## DateTime

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime string with timezone ([RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)). Example: `2024-01-15T10:30:00Z`.

| Property      | Value                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| Format        | `YYYY-MM-DDTHH:mm:ss.sssZ`                                                                                       |
| Example       | `2025-01-15T14:30:00.000Z`                                                                                       |
| Specification | [https://scalars.graphql.org/chillicream/date-time.html](https://scalars.graphql.org/chillicream/date-time.html) |

## Date

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date string without time component ([RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)). Example: `2024-01-15`.

| Property      | Value                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| Format        | `YYYY-MM-DD`                                                                                           |
| Example       | `2025-01-15`                                                                                           |
| Specification | [https://scalars.graphql.org/chillicream/date.html](https://scalars.graphql.org/chillicream/date.html) |

## JSON

An arbitrary JSON value. Can be an object, array, string, number, boolean, or null.

| Property      | Value                                                                            |
| ------------- | -------------------------------------------------------------------------------- |
| Format        | `Any valid JSON`                                                                 |
| Example       | `{"key": "value", "count": 42}`                                                  |
| Specification | [https://www.rfc-editor.org/rfc/rfc8259](https://www.rfc-editor.org/rfc/rfc8259) |

## GeoJSON

A [GeoJSON](https://geojson.org/) geometry object ([RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946)). Supports Point, LineString, Polygon, and other geometry types.

| Property      | Value                                                                            |
| ------------- | -------------------------------------------------------------------------------- |
| Format        | `GeoJSON geometry object`                                                        |
| Example       | `{"type": "Point", "coordinates": [125.6, 10.1]}`                                |
| Specification | [https://www.rfc-editor.org/rfc/rfc7946](https://www.rfc-editor.org/rfc/rfc7946) |

## Latitude

A geographic latitude coordinate in decimal degrees. Valid range: -90.0 to 90.0.

| Property | Value           |
| -------- | --------------- |
| Format   | `-90.0 to 90.0` |
| Example  | `37.7749`       |

## Longitude

A geographic longitude coordinate in decimal degrees. Valid range: -180.0 to 180.0.

| Property | Value             |
| -------- | ----------------- |
| Format   | `-180.0 to 180.0` |
| Example  | `-122.4194`       |

## Locale

A [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) language tag identifying a user locale. Example: `en-US`, `ru-RU`.

| Property      | Value                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Format        | `language-REGION`                                                                                                      |
| Example       | `en-US`                                                                                                                |
| Specification | [https://the-guild.dev/graphql/scalars/docs/scalars/locale](https://the-guild.dev/graphql/scalars/docs/scalars/locale) |

## EmailAddress

An email address conforming to [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322). Example: `user@example.com`.

| Property | Value              |
| -------- | ------------------ |
| Format   | `user@domain`      |
| Example  | `user@example.com` |

## HexColorCode

A hexadecimal color code. Supports 3-digit (`#RGB`) or 6-digit (`#RRGGBB`) format.

| Property | Value     |
| -------- | --------- |
| Format   | `#RRGGBB` |
| Example  | `#FF5733` |

## CountryCode

An [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code. Example: `US`, `GB`, `ES`.

| Property | Value                   |
| -------- | ----------------------- |
| Format   | `Two uppercase letters` |
| Example  | `US`                    |

## Code

A machine-readable identifier code.

Constraints:

* Allowed characters: ASCII letters (a-z, A-Z), digits (0-9), underscore (\_), dot (.), hyphen (-)
* Must start with a letter or digit
* Case-insensitive for uniqueness checks
* Maximum length: 64 characters

Naming conventions:

* System items: UPPER\_SNAKE\_CASE (e.g., DEVICE\_TYPE, ACTIVE)
* User items: any valid format (e.g., vehicle\_car, sensor-v2)

Examples: DEVICE\_TYPE, vehicle\_car, status.active, sensor-v2, ABC123

| Property      | Value                                                                                |
| ------------- | ------------------------------------------------------------------------------------ |
| Format        | `lowercase_snake_case`                                                               |
| Example       | `vehicle_type`                                                                       |
| Specification | [https://api.navixy.com/spec/scalars/code](https://api.navixy.com/spec/scalars/code) |

## ScheduleData

A schedule data structure containing time intervals and recurrence rules.

| Property      | Value                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| Format        | `iCalendar-compatible JSON`                                                                            |
| Specification | [https://api.navixy.com/spec/scalars/schedule-data](https://api.navixy.com/spec/scalars/schedule-data) |

JSON example:

```json
{
  "timezone": "Europe/Moscow",
  "events": [
    {
      "dtstart": "2025-01-06T06:00:00Z",
      "dtend": "2025-01-06T15:00:00Z",
      "rrule": {
        "freq": "WEEKLY",
        "byday": ["MO", "TU", "WE", "TH", "FR"]
      },
      "exdate": ["2025-01-06T10:00:00Z"]
    }
  ]
}
```
