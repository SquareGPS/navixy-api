# Scalars & enums

This page documents scalar and enum types used in Navixy Repository API.

## Scalars

Navixy Repository API defines these custom scalar types in addition to the standard GraphQL scalars. See [GraphQL basics](../graphql-basics.md#scalar-types/) for the description of the predefined scalars (String, Int, Float, Boolean, ID).

### UUID

Universally unique identifier following [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562). Entity type codes are embedded in the last segment for easy debugging.

| Property | Value                                  |
| -------- | -------------------------------------- |
| Format   | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` |
| Example  | `550e8400-e29b-41d4-a716-446655440000` |

### DateTime

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with timezone.

| Property | Value                      |
| -------- | -------------------------- |
| Format   | `YYYY-MM-DDTHH:mm:ss.sssZ` |
| Example  | `2025-01-15T14:30:00.000Z` |

### Date

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date without time component.

| Property | Value        |
| -------- | ------------ |
| Format   | `YYYY-MM-DD` |
| Example  | `2025-01-15` |

### JSON

Arbitrary JSON object. Used for custom fields data, extra fields, and flexible configurations.

| Property | Value                           |
| -------- | ------------------------------- |
| Format   | `Any valid JSON`                |
| Example  | `{"key": "value", "count": 42}` |

## Enums

Enums represent fixed sets of values. Use the exact value shown when passing as an argument.

### ActorType

Discriminator for actor types in the system. Actors are entities that can perform actions and have permissions.

| Value         | Description                                    |
| ------------- | ---------------------------------------------- |
| `USER`        | Human user authenticated via identity provider |
| `INTEGRATION` | External system integration with API access    |
| `SYSTEM`      | Internal system actor for automated operations |

### FieldType

Data types for custom field definitions. Determines validation, storage, and UI rendering.

| Value       | Description                                                                 |
| ----------- | --------------------------------------------------------------------------- |
| `STRING`    | Single-line text, max 255 characters by default                             |
| `TEXT`      | Multi-line text, unlimited length                                           |
| `NUMBER`    | Numeric value (integer or decimal)                                          |
| `BOOLEAN`   | True/false flag                                                             |
| `DATE`      | Date without time (YYYY-MM-DD)                                              |
| `DATETIME`  | Date with time and timezone                                                 |
| `GEOJSON`   | [GeoJSON](https://geojson.org/) geometry (Point, Polygon, LineString, etc.) |
| `SCHEDULE`  | Schedule/calendar data in JSON format                                       |
| `OPTIONS`   | Selection from predefined options list                                      |
| `DEVICE`    | Reference to Device entity                                                  |
| `REFERENCE` | Reference to any entity by type                                             |
| `CATALOG`   | Reference to catalog item                                                   |
| `TAG`       | Reference to Tag entity                                                     |

### DeviceIdType

Hardware identifier types for devices. Used to uniquely identify physical devices across different systems.

| Value           | Description                                         |
| --------------- | --------------------------------------------------- |
| `UUID`          | System-generated UUID                               |
| `IMEI`          | International Mobile Equipment Identity (15 digits) |
| `MEID_HEX`      | Mobile Equipment Identifier in hexadecimal format   |
| `MEID_DEC`      | Mobile Equipment Identifier in decimal format       |
| `MAC_ADDRESS`   | Media Access Control address (network interface)    |
| `SERIAL_NUMBER` | Manufacturer serial number                          |
| `CUSTOM`        | Custom identifier type defined by organization      |

### SortOrder

Sort direction for queries

| Value  | Description                               |
| ------ | ----------------------------------------- |
| `ASC`  | Ascending order (A-Z, 0-9, oldest first)  |
| `DESC` | Descending order (Z-A, 9-0, newest first) |

### ActionPermission

Permission action flags for access control.

| Value    | Description              |
| -------- | ------------------------ |
| `READ`   | View entity and its data |
| `CREATE` | Create new entities      |
| `UPDATE` | Modify existing entities |
| `DELETE` | Soft-delete entities     |

### SourceType

Source type for audit events. Identifies the origin of the request that triggered the event.

| Value         | Description                      |
| ------------- | -------------------------------- |
| `WEB`         | Web browser application          |
| `MOBILE`      | Mobile application (iOS/Android) |
| `API`         | Direct API call                  |
| `INTERNAL`    | Internal system process          |
| `INTEGRATION` | External integration             |

### AuditEventType

Audit event types for tracking entity lifecycle and access changes.

| Value                | Description                      |
| -------------------- | -------------------------------- |
| `LOGIN`              | Successful user login            |
| `LOGOUT`             | User logout                      |
| `FAILED_LOGIN`       | Failed login attempt             |
| `PASSWORD_RESET`     | Password reset initiated         |
| `SESSION_EXPIRED`    | Session expired due to timeout   |
| `CREATED`            | Entity created                   |
| `UPDATED`            | Entity updated                   |
| `DELETED`            | Entity soft-deleted              |
| `RESTORED`           | Entity restored from soft-delete |
| `ROLE_ASSIGNED`      | Role assigned to actor           |
| `ROLE_REVOKED`       | Role revoked from actor          |
| `PERMISSION_GRANTED` | Permission granted to role       |
| `PERMISSION_REVOKED` | Permission revoked from role     |
| `LINKED`             | Entities linked together         |
| `UNLINKED`           | Entity link removed              |
| `ATTACHED`           | Entity attached to group         |
| `DETACHED`           | Entity detached from group       |
