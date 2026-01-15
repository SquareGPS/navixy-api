# Scalars

Navixy Repository API defines these custom scalar types in addition to the standard GraphQL scalars. See [GraphQL basics](../graphql-basics.md#scalar-types/) for the description of the predefined scalars (String, Int, Float, Boolean, ID).

## DateTime

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with timezone ([RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)).

| Property | Value |
| -------- | ----- |
| Format | `YYYY-MM-DDTHH:mm:ss.sssZ` |
| Example | `2025-01-15T14:30:00.000Z` |

## Date

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date without time component ([RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)).

| Property | Value |
| -------- | ----- |
| Format | `YYYY-MM-DD` |
| Example | `2025-01-15` |

## JSON

Arbitrary JSON object. Used for custom fields data, extra fields, and flexible configurations.

| Property | Value |
| -------- | ----- |
| Format | `Any valid JSON` |
| Example | `{"key": "value", "count": 42}` |

## GeoJSON

[GeoJSON](https://geojson.org/) geometry object (Point, Polygon, LineString, etc.).

| Property | Value |
| -------- | ----- |
| Format | `GeoJSON geometry object` |
| Example | `{"type": "Point", "coordinates": [125.6, 10.1]}` |

## Latitude

A geographic latitude coordinate in decimal degrees.

| Property | Value |
| -------- | ----- |
| Format | `-90.0 to 90.0` |
| Example | `37.7749` |

## Longitude

A geographic longitude coordinate in decimal degrees.

| Property | Value |
| -------- | ----- |
| Format | `-180.0 to 180.0` |
| Example | `-122.4194` |

## Locale

A [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) language tag identifying a user locale.

| Property | Value |
| -------- | ----- |
| Format | `language-REGION` |
| Example | `en-US` |

## EmailAddress

An email address conforming to [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322).

| Property | Value |
| -------- | ----- |
| Format | `user@domain` |
| Example | `user@example.com` |

## HexColorCode

CSS hex color code for UI display.

| Property | Value |
| -------- | ----- |
| Format | `#RRGGBB` |
| Example | `#FF5733` |

## CountryCode

An [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code.

| Property | Value |
| -------- | ----- |
| Format | `Two uppercase letters` |
| Example | `US` |

## Code

Machine-readable string identifier. Must match pattern `^[a-z][a-z0-9_]*$` (lowercase letters, numbers, underscores, starting with a letter).

| Property | Value |
| -------- | ----- |
| Format | `lowercase_snake_case` |
| Example | `vehicle_type` |

## ScheduleData

Schedule/calendar data with time intervals and recurrence rules following [iCalendar](https://datatracker.ietf.org/doc/html/rfc5545) format.

| Property | Value |
| -------- | ----- |
| Format | `iCalendar-compatible JSON` |
| Example | `{"intervals": [...], "rrule": "FREQ=WEEKLY;BYDAY=MO,WE,FR"}` |
