# Scalars & enums

This page documents scalar types, enumerations, and interfaces used throughout the API.

### Scalars

Navixy Repository API defines these custom scalar types in addition to the standard GraphQL scalars. See [GraphQL basics](../graphql-basics.md#scalar-types) for the description of the predefined scalars (String, Int, Float, Boolean, ID).

<table><thead><tr><th width="136.20001220703125">Type</th><th>Format</th><th>Description</th></tr></thead><tbody><tr><td><code>UUID</code></td><td><code>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</code></td><td>Unique identifier following RFC 9562</td></tr><tr><td><code>DateTime</code></td><td><code>YYYY-MM-DDTHH:mm:ss.sssZ</code></td><td>ISO 8601 datetime with timezone</td></tr><tr><td><code>Date</code></td><td><code>YYYY-MM-DD</code></td><td>ISO 8601 date without time</td></tr><tr><td><code>JSON</code></td><td>Any valid JSON</td><td>Arbitrary JSON object for custom fields and configurations</td></tr></tbody></table>

### Enums

Enums represent fixed sets of values. Use the exact value shown when passing as an argument.

#### ActionPermission

Permission action flags for access control. Combined as bitmask in database (READ=1, CREATE=2, UPDATE=4, DELETE=8).

| Value    | Description              |
| -------- | ------------------------ |
| `READ`   | View entity and its data |
| `CREATE` | Create new entities      |
| `UPDATE` | Modify existing entities |
| `DELETE` | Soft-delete entities     |

#### ActorType

Discriminator for actor types in the system. Actors are entities that can perform actions and have permissions.

| Value         | Description                                    |
| ------------- | ---------------------------------------------- |
| `USER`        | Human user authenticated via identity provider |
| `INTEGRATION` | External system integration with API access    |
| `SYSTEM`      | Internal system actor for automated operations |

#### AuditEventType

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

#### DeviceIdType

Hardware identifier types for devices. Used to uniquely identify physical devices across different systems.

<table><thead><tr><th width="170.79998779296875">Value</th><th>Description</th></tr></thead><tbody><tr><td><code>UUID</code></td><td>Globally unique identifier with embedded entity type discriminator</td></tr><tr><td><code>IMEI</code></td><td>International Mobile Equipment Identity (15 digits)</td></tr><tr><td><code>MEID_HEX</code></td><td>Mobile Equipment Identifier in hexadecimal format</td></tr><tr><td><code>MEID_DEC</code></td><td>Mobile Equipment Identifier in decimal format</td></tr><tr><td><code>MAC_ADDRESS</code></td><td>Media Access Control address (network interface)</td></tr><tr><td><code>SERIAL_NUMBER</code></td><td>Manufacturer serial number</td></tr><tr><td><code>CUSTOM</code></td><td>Custom identifier type defined by organization</td></tr></tbody></table>

#### FieldType

Data types for custom field definitions. Determines validation, storage, and UI rendering.

| Value       | Description                                         |
| ----------- | --------------------------------------------------- |
| `STRING`    | Single-line text, max 255 characters by default     |
| `TEXT`      | Multi-line text, unlimited length                   |
| `NUMBER`    | Numeric value (integer or decimal)                  |
| `BOOLEAN`   | True/false flag                                     |
| `DATE`      | Date without time (YYYY-MM-DD)                      |
| `DATETIME`  | Date with time and timezone                         |
| `GEOJSON`   | GeoJSON geometry (Point, Polygon, LineString, etc.) |
| `SCHEDULE`  | Schedule/calendar data in JSON format               |
| `OPTIONS`   | Selection from predefined options list              |
| `DEVICE`    | Reference to Device entity                          |
| `REFERENCE` | Reference to any entity by type                     |
| `CATALOG`   | Reference to catalog item                           |
| `TAG`       | Reference to Tag entity                             |

#### SortOrder

Sort direction for queries

| Value  | Description                               |
| ------ | ----------------------------------------- |
| `ASC`  | Ascending order (A-Z, 0-9, oldest first)  |
| `DESC` | Descending order (Z-A, 9-0, newest first) |

#### SourceType

Source type for audit events. Identifies the origin of the request that triggered the event.

| Value         | Description                      |
| ------------- | -------------------------------- |
| `WEB`         | Web browser application          |
| `MOBILE`      | Mobile application (iOS/Android) |
| `API`         | Direct API call                  |
| `INTERNAL`    | Internal system process          |
| `INTEGRATION` | External integration             |
