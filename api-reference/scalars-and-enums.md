# Scalars & enums

This page documents scalar and enum types used in Navixy Repository API.

## Scalars

Navixy Repository API defines these custom scalar types in addition to the standard GraphQL scalars. See [GraphQL basics](../graphql-basics.md#scalar-types/) for the description of the predefined scalars (String, Int, Float, Boolean, ID).

### DateTime

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with timezone ([RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)).

| Property | Value |
| -------- | ----- |
| Format | `YYYY-MM-DDTHH:mm:ss.sssZ` |
| Example | `2025-01-15T14:30:00.000Z` |

### Date

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date without time component ([RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)).

| Property | Value |
| -------- | ----- |
| Format | `YYYY-MM-DD` |
| Example | `2025-01-15` |

### JSON

Arbitrary JSON object. Used for custom fields data, extra fields, and flexible configurations.

| Property | Value |
| -------- | ----- |
| Format | `Any valid JSON` |
| Example | `{"key": "value", "count": 42}` |

### GeoJSON

[GeoJSON](https://geojson.org/) geometry object (Point, Polygon, LineString, etc.).

| Property | Value |
| -------- | ----- |
| Format | `GeoJSON geometry object` |
| Example | `{"type": "Point", "coordinates": [125.6, 10.1]}` |

### Latitude

A geographic latitude coordinate in decimal degrees. Valid range: -90.0 to 90.0.

### Longitude

A geographic longitude coordinate in decimal degrees. Valid range: -180.0 to 180.0.

### Locale

A BCP 47 language tag identifying a user locale. Example: `en-US`, `ru-RU`.

### EmailAddress

An email address conforming to RFC 5322. Example: `user@example.com`.

### HexColorCode

CSS hex color code for UI display.

| Property | Value |
| -------- | ----- |
| Format | `#RRGGBB` |
| Example | `#FF5733` |

### CountryCode

An [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code. Example: `US`, `GB`, `ES`.

### Code

Machine-readable string identifier. Must match pattern `^[a-z][a-z0-9_]*$` (lowercase letters, numbers, underscores, starting with a letter).

| Property | Value |
| -------- | ----- |
| Format | `lowercase_snake_case` |
| Example | `vehicle_type` |

### ScheduleData

Schedule/calendar data with time intervals and recurrence rules following [iCalendar](https://datatracker.ietf.org/doc/html/rfc5545) format.

| Property | Value |
| -------- | ----- |
| Format | `iCalendar-compatible JSON` |
| Example | `{"intervals": [...], "rrule": "FREQ=WEEKLY;BYDAY=MO,WE,FR"}` |

## Enums

Enums represent fixed sets of values. Use the exact value shown when passing as an argument.

### OrderDirection

The direction for sorting query results.

| Value | Description |
| ----- | ----------- |
| `ASC` | Sort in ascending order (A→Z, 0→9, oldest→newest). |
| `DESC` | Sort in descending order (Z→A, 9→0, newest→oldest). |

### CatalogItemOrigin

The origin of a catalog item, indicating how it was created.

| Value | Description |
| ----- | ----------- |
| `SYSTEM` | Predefined by platform. Immutable and available to all organizations. |
| `ORGANIZATION` | Created by the current organization. |
| `PARENT_ORGANIZATION` | Inherited from a parent organization in the dealer hierarchy. |

### CountPrecision

The precision level of a total count value.

| Value | Description |
| ----- | ----------- |
| `EXACT` | The count is exact, calculated using `COUNT(*)`. |
| `APPROXIMATE` | The count is approximate, derived from table statistics. |
| `AT_LEAST` | At least this many items exist. Counting stopped early for performance reasons. |

### OrganizationFeature

Feature flags that can be enabled for an organization.

| Value | Description |
| ----- | ----------- |
| `DEALER` | The organization can create and manage child organizations (dealer/reseller model). |
| `WHITELABEL` | The organization has custom branding including domain, logo, and color scheme. |

### FieldType

The data type of a custom field, determining validation rules and UI rendering.

| Value | Description |
| ----- | ----------- |
| `STRING` | Single-line text input. Maximum 255 characters. |
| `TEXT` | Multi-line text input. Maximum 65,535 characters. |
| `NUMBER` | Numeric value, supporting both integers and decimals. |
| `BOOLEAN` | Boolean true/false value. |
| `DATE` | Calendar date without time component (YYYY-MM-DD). |
| `DATETIME` | Date and time with timezone information. |
| `GEOJSON` | [GeoJSON](https://geojson.org/) geometry object (Point, Polygon, LineString, etc.). |
| `SCHEDULE` | Schedule or calendar data with time intervals and recurrence rules. |
| `OPTIONS` | Selection from a predefined list of options. |
| `DEVICE` | Reference to a Device entity. |
| `REFERENCE` | Reference to any entity by its type and ID. |
| `CATALOG` | Reference to a catalog item. |
| `TAG` | Reference to a Tag entity. |

### DeviceIdType

The type of hardware identifier used to identify a device.

| Value | Description |
| ----- | ----------- |
| `GUID` | A GUID/UUID identifier. |
| `IMEI` | International Mobile Equipment Identity. A 15-digit number. |
| `MEID_HEX` | Mobile Equipment Identifier in hexadecimal format. |
| `MEID_DEC` | Mobile Equipment Identifier in decimal format. |
| `MAC_ADDRESS` | Media Access Control address of a network interface. |
| `SERIAL_NUMBER` | Manufacturer-assigned serial number. |
| `CUSTOM` | A custom identifier type defined by the organization. |

### ActionPermission

Permission actions that can be granted to actors for entity operations.

| Value | Description |
| ----- | ----------- |
| `READ` | Permission to view entities and their data. |
| `CREATE` | Permission to create new entities. |
| `UPDATE` | Permission to modify existing entities. |
| `DELETE` | Permission to delete entities. |

### SourceType

The source type identifying the origin of an API request.

| Value | Description |
| ----- | ----------- |
| `WEB` | Request originated from a web browser application. |
| `MOBILE` | Request originated from a mobile application (iOS/Android). |
| `API` | Request made directly via the API. |
| `INTERNAL` | Request generated by an internal system process. |
| `INTEGRATION` | Request made by an external integration. |

### AuditEventType

The type of event recorded in the audit log.

| Value | Description |
| ----- | ----------- |
| `LOGIN` | A user successfully authenticated. |
| `LOGOUT` | A user ended their session. |
| `FAILED_LOGIN` | An authentication attempt failed. |
| `PASSWORD_RESET` | A password reset was initiated. |
| `SESSION_EXPIRED` | A session was terminated due to inactivity. |
| `CREATED` | A new entity was created. |
| `UPDATED` | An existing entity was modified. |
| `DELETED` | An entity was deleted. |
| `RESTORED` | A soft-deleted entity was restored. |
| `ROLE_ASSIGNED` | A role was assigned to an actor. |
| `ROLE_REVOKED` | A role was removed from an actor. |
| `PERMISSION_GRANTED` | A permission was granted to a role. |
| `PERMISSION_REVOKED` | A permission was removed from a role. |
| `LINKED` | Two entities were linked together. |
| `UNLINKED` | A link between entities was removed. |
| `ATTACHED` | An entity was added to a group. |
| `DETACHED` | An entity was removed from a group. |

### FieldOperator

Comparison operators for filtering by custom field values.

| Value | Description |
| ----- | ----------- |
| `EQ` | Value equals the specified value. |
| `NE` | Value does not equal the specified value. |
| `GT` | Value is greater than the specified value. |
| `GTE` | Value is greater than or equal to the specified value. |
| `LT` | Value is less than the specified value. |
| `LTE` | Value is less than or equal to the specified value. |
| `CONTAINS` | String value contains the specified substring (case-insensitive). |
| `IN` | Value is one of the specified values in the array. |
| `IS_NULL` | Value is null. |
| `IS_NOT_NULL` | Value is not null. |

### GeoJsonGeometryType

The type of [GeoJSON](https://geojson.org/) geometry.

| Value | Description |
| ----- | ----------- |
| `POINT` | A single geographic point. |
| `MULTI_POINT` | A collection of points. |
| `LINE_STRING` | A sequence of connected line segments. |
| `MULTI_LINE_STRING` | A collection of line strings. |
| `POLYGON` | A closed shape defined by a linear ring. |
| `MULTI_POLYGON` | A collection of polygons. |
| `GEOMETRY_COLLECTION` | A heterogeneous collection of geometry objects. |

### CatalogItemOrderField

Fields available for ordering catalog items.

| Value | Description |
| ----- | ----------- |
| `ORDER` | Order by display order. |
| `CODE` | Order by code. |
| `TITLE` | Order by title. |

### OrganizationOrderField

Fields available for ordering organizations.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### MemberOrderField

Fields available for ordering members.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

### IntegrationOrderField

Fields available for ordering integrations.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### DeviceOrderField

Fields available for ordering devices.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### DeviceInventoryRelationOrderField

Fields available for ordering device inventory relations.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

### AssetOrderField

Fields available for ordering assets.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### AssetGroupOrderField

Fields available for ordering asset groups.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### AssetGroupItemOrderField

Fields available for ordering asset group items.

| Value | Description |
| ----- | ----------- |
| `ATTACHED_AT` | Order by attachment date. |

### InventoryOrderField

Fields available for ordering inventories.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### GeoObjectOrderField

Fields available for ordering geo objects.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### ScheduleOrderField

Fields available for ordering schedules.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

### AuditEventOrderField

Fields available for ordering audit events.

| Value | Description |
| ----- | ----------- |
| `OCCURRED_AT` | Order by occurrence date. |

### ActorRoleOrderField

Fields available for ordering actor roles.

| Value | Description |
| ----- | ----------- |
| `ASSIGNED_AT` | Order by assignment date. |

### RolePermissionOrderField

Fields available for ordering role permissions.

| Value | Description |
| ----- | ----------- |
| `GRANTED_AT` | Order by grant date. |

### UserScopeOrderField

Fields available for ordering user scopes.

| Value | Description |
| ----- | ----------- |
| `ID` | Order by ID. |
