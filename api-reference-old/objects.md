# Objects

Objects are the return types for queries and mutations. They represent the data structures in the Navixy API.

### Business entities

#### Device

Tracking device (GPS tracker, sensor, beacon, etc.). Devices are physical hardware that collect and transmit data.

**Implements:** Node, Timestamped, SoftDeletable, Customizable

<table><thead><tr><th width="153">Field</th><th width="185">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>UUID!</td><td>Globally unique identifier with embedded entity type discriminator</td></tr><tr><td><code>organization</code></td><td>Organization!</td><td>Organization that owns this device</td></tr><tr><td><code>type</code></td><td>DeviceType!</td><td>Device type classification</td></tr><tr><td><code>model</code></td><td>DeviceModel</td><td>Specific device model (optional)</td></tr><tr><td><code>status</code></td><td>DeviceStatus!</td><td>Current operational status</td></tr><tr><td><code>title</code></td><td>String!</td><td>Device display name</td></tr><tr><td><code>createdAt</code></td><td>DateTime!</td><td></td></tr><tr><td><code>updatedAt</code></td><td>DateTime!</td><td></td></tr><tr><td><code>deletedAt</code></td><td>DateTime</td><td></td></tr><tr><td><code>deletedBy</code></td><td>Actor</td><td></td></tr><tr><td><code>customFields</code></td><td>JSON!</td><td>Custom fields data</td></tr><tr><td><code>identifiers</code></td><td>[DeviceIdentifier!]!</td><td>Hardware identifiers (IMEI, serial, MAC, etc.)</td></tr><tr><td><code>inventory</code></td><td>Inventory</td><td>Inventory this device is assigned to</td></tr><tr><td><code>relationsFrom</code></td><td>[DeviceRelation!]!</td><td>Outgoing relationships to other devices</td></tr><tr><td><code>relationsTo</code></td><td>[DeviceRelation!]!</td><td>Incoming relationships from other devices</td></tr></tbody></table>

#### DeviceIdentifier

Device hardware identifier. Devices can have multiple identifiers of different types.

**Implements:** Node, Timestamped

| Field       | Type          | Description                                                                                                                                 |
| ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`        | UUID!         |                                                                                                                                             |
| `device`    | Device!       | Device this identifier belongs to                                                                                                           |
| `type`      | DeviceIdType! | Type of identifier                                                                                                                          |
| `value`     | String!       | Identifier value                                                                                                                            |
| `namespace` | String        | Namespace for identifier uniqueness. Allows same identifier value in different contexts. Example: factory\_a, factory\_b for serial numbers |
| `createdAt` | DateTime!     |                                                                                                                                             |
| `updatedAt` | DateTime!     |                                                                                                                                             |

#### DeviceRelation

Relationship between two devices. Defines how devices are connected or related.

**Implements:** Node

| Field          | Type                | Description                   |
| -------------- | ------------------- | ----------------------------- |
| `id`           | UUID!               |                               |
| `firstDevice`  | Device!             | First device in relationship  |
| `secondDevice` | Device!             | Second device in relationship |
| `type`         | DeviceRelationType! | Type of relationship          |

#### DeviceInventoryRelation

Device assignment to inventory record. Tracks which inventory a device belongs to.

**Implements:** Node, Timestamped, SoftDeletable

| Field        | Type       | Description              |
| ------------ | ---------- | ------------------------ |
| `id`         | UUID!      |                          |
| `device`     | Device!    | Device being assigned    |
| `inventory`  | Inventory! | Target inventory         |
| `assignedAt` | DateTime!  | When device was assigned |
| `assignedBy` | Actor      | Who assigned the device  |
| `deletedAt`  | DateTime   |                          |
| `deletedBy`  | Actor      |                          |
| `createdAt`  | DateTime!  |                          |
| `updatedAt`  | DateTime!  |                          |

#### Asset

Physical or logical asset. Assets are things being tracked (vehicles, trailers, people, etc.).

**Implements:** Node, Timestamped, SoftDeletable, Customizable

| Field          | Type            | Description                       |
| -------------- | --------------- | --------------------------------- |
| `id`           | UUID!           |                                   |
| `organization` | Organization!   | Organization that owns this asset |
| `type`         | AssetType!      | Asset type classification         |
| `title`        | String!         | Asset display name                |
| `createdAt`    | DateTime!       |                                   |
| `updatedAt`    | DateTime!       |                                   |
| `deletedAt`    | DateTime        |                                   |
| `deletedBy`    | Actor           |                                   |
| `customFields` | JSON!           | Custom fields data                |
| `groups`       | \[AssetGroup!]! | Groups this asset belongs to      |

#### AssetGroup

Group of assets. Used to organize assets into logical collections.

**Implements:** Node, Timestamped, SoftDeletable

| Field                                  | Type                      | Description                             |
| -------------------------------------- | ------------------------- | --------------------------------------- |
| `id`                                   | UUID!                     |                                         |
| `organization`                         | Organization!             | Organization that owns this group       |
| `type`                                 | AssetGroupType!           | Group type with constraints             |
| `title`                                | String!                   | Group display name                      |
| `color`                                | String                    | Color for UI display (hex format)       |
| `createdAt`                            | DateTime!                 |                                         |
| `updatedAt`                            | DateTime!                 |                                         |
| `deletedAt`                            | DateTime                  |                                         |
| `deletedBy`                            | Actor                     |                                         |
| `currentAssets`                        | \[Asset!]!                | Assets currently in this group          |
| `history(pagination: PaginationInput)` | AssetGroupItemConnection! | Full membership history with pagination |

#### AssetGroupItem

Asset group membership record. Tracks current and historical group membership.

**Implements:** Node, Timestamped

| Field        | Type        | Description                                                       |
| ------------ | ----------- | ----------------------------------------------------------------- |
| `id`         | UUID!       |                                                                   |
| `group`      | AssetGroup! | Group containing the asset                                        |
| `asset`      | Asset!      | Asset in the group                                                |
| `attachedAt` | DateTime!   | When asset was added to group                                     |
| `detachedAt` | DateTime    | When asset was removed from group. Null means currently attached. |
| `createdAt`  | DateTime!   |                                                                   |
| `updatedAt`  | DateTime!   |                                                                   |

#### GeoObject

Geographic object (geofence, POI, route). Geometry is stored in customFields as system field 'geojson'.

**Implements:** Node, Timestamped, SoftDeletable, Customizable

| Field          | Type           | Description                                                                                              |
| -------------- | -------------- | -------------------------------------------------------------------------------------------------------- |
| `id`           | UUID!          |                                                                                                          |
| `organization` | Organization!  | Organization that owns this geo object                                                                   |
| `type`         | GeoObjectType! | Geo object type classification                                                                           |
| `title`        | String!        | Geo object display name                                                                                  |
| `createdAt`    | DateTime!      |                                                                                                          |
| `updatedAt`    | DateTime!      |                                                                                                          |
| `deletedAt`    | DateTime       |                                                                                                          |
| `deletedBy`    | Actor          |                                                                                                          |
| `customFields` | JSON!          | Custom fields including 'geojson' system field. geojson contains GeoJSON geometry (Point, Polygon, etc.) |

#### Schedule

Schedule definition. Used for work hours, maintenance windows, holidays, etc. Schedule data is stored in customFields as system field 'schedule\_data'.

**Implements:** Node, Timestamped, SoftDeletable, Customizable

| Field          | Type          | Description                                         |
| -------------- | ------------- | --------------------------------------------------- |
| `id`           | UUID!         |                                                     |
| `organization` | Organization! | Organization that owns this schedule                |
| `type`         | ScheduleType! | Schedule type classification                        |
| `title`        | String!       | Schedule display name                               |
| `createdAt`    | DateTime!     |                                                     |
| `updatedAt`    | DateTime!     |                                                     |
| `deletedAt`    | DateTime      |                                                     |
| `deletedBy`    | Actor         |                                                     |
| `customFields` | JSON!         | Custom fields including schedule\_data system field |

#### Inventory

Inventory/warehouse record. Devices can be assigned to inventory for stock management.

**Implements:** Node, Timestamped, SoftDeletable

| Field                                                           | Type              | Description                               |
| --------------------------------------------------------------- | ----------------- | ----------------------------------------- |
| `id`                                                            | UUID!             |                                           |
| `organization`                                                  | Organization!     | Organization that owns this inventory     |
| `code`                                                          | String!           | Unique inventory code within organization |
| `createdAt`                                                     | DateTime!         |                                           |
| `updatedAt`                                                     | DateTime!         |                                           |
| `deletedAt`                                                     | DateTime          |                                           |
| `deletedBy`                                                     | Actor             |                                           |
| `devices(pagination: PaginationInput, includeDeleted: Boolean)` | DeviceConnection! | Devices assigned to this inventory        |

### Organizations

#### Organization

Organization in the hierarchy. Organizations contain users, devices, assets, and other business entities. Supports multi-tenancy with optional dealer hierarchy.

**Implements:** Node, Timestamped, SoftDeletable

| Field                                                              | Type                 | Description                                                                                                    |
| ------------------------------------------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------- |
| `id`                                                               | UUID!                |                                                                                                                |
| `code`                                                             | String!              | Unique organization code. Format: lowercase alphanumeric with underscores. Example: acme\_corp, dealer\_moscow |
| `title`                                                            | String!              | Organization display name                                                                                      |
| `externalId`                                                       | String               | External system identifier for integration                                                                     |
| `isActive`                                                         | Boolean!             | Whether organization is active                                                                                 |
| `isDealer`                                                         | Boolean!             | Whether organization can create child organizations. Dealer organizations can have sub-organizations.          |
| `createdAt`                                                        | DateTime!            |                                                                                                                |
| `updatedAt`                                                        | DateTime!            |                                                                                                                |
| `deletedAt`                                                        | DateTime             |                                                                                                                |
| `deletedBy`                                                        | Actor                |                                                                                                                |
| `parent`                                                           | Organization         | Parent organization (null for root)                                                                            |
| `children(includeDeleted: Boolean)`                                | \[Organization!]!    | Child organizations                                                                                            |
| `members(includeDeleted: Boolean)`                                 | \[Member!]!          | Members (users) of this organization                                                                           |
| `devices(filter: DeviceFilter, pagination: PaginationInput)`       | DeviceConnection!    | Devices owned by this organization                                                                             |
| `assets(filter: AssetFilter, pagination: PaginationInput)`         | AssetConnection!     | Assets owned by this organization                                                                              |
| `geoObjects(filter: GeoObjectFilter, pagination: PaginationInput)` | GeoObjectConnection! | Geographic objects owned by this organization                                                                  |
| `schedules(filter: ScheduleFilter, pagination: PaginationInput)`   | ScheduleConnection!  | Schedules owned by this organization                                                                           |

### Actors

#### Actor

Abstract actor entity. Actors are entities that can perform actions and have permissions. Resolved to concrete User or Integration type.

**Implements:** Node, Timestamped, SoftDeletable

| Field           | Type        | Description                                        |
| --------------- | ----------- | -------------------------------------------------- |
| `id`            | UUID!       |                                                    |
| `actorType`     | ActorType!  | Type discriminator                                 |
| `createdAt`     | DateTime!   |                                                    |
| `updatedAt`     | DateTime!   |                                                    |
| `deletedAt`     | DateTime    |                                                    |
| `deletedBy`     | Actor       |                                                    |
| `asUser`        | User        | Resolve to User if actorType is USER               |
| `asIntegration` | Integration | Resolve to Integration if actorType is INTEGRATION |

#### User

Human user account. Users authenticate via external identity providers and can be members of organizations.

**Implements:** Node, Timestamped, SoftDeletable

| Field                | Type       | Description                                                        |
| -------------------- | ---------- | ------------------------------------------------------------------ |
| `id`                 | UUID!      |                                                                    |
| `actorType`          | ActorType! | Always USER                                                        |
| `identityProvider`   | String!    | Identity provider name. Examples: keycloak, auth0, okta, azure\_ad |
| `identityProviderId` | UUID!      | User's unique ID in the identity provider                          |
| `fullName`           | String!    | User's display name                                                |
| `externalId`         | String     | External system identifier for integration                         |
| `isActive`           | Boolean!   | Whether user account is active                                     |
| `createdAt`          | DateTime!  |                                                                    |
| `updatedAt`          | DateTime!  |                                                                    |
| `deletedAt`          | DateTime   |                                                                    |
| `deletedBy`          | Actor      |                                                                    |

#### Member

User membership in an organization. Links users to organizations with membership-specific custom fields. A user can be a member of multiple organizations.

**Implements:** Node, Timestamped, SoftDeletable, Customizable

| Field          | Type          | Description                                                                                           |
| -------------- | ------------- | ----------------------------------------------------------------------------------------------------- |
| `id`           | UUID!         |                                                                                                       |
| `user`         | User!         | The user                                                                                              |
| `organization` | Organization! | Organization the user belongs to                                                                      |
| `isActive`     | Boolean!      | Whether membership is active                                                                          |
| `createdAt`    | DateTime!     |                                                                                                       |
| `updatedAt`    | DateTime!     |                                                                                                       |
| `assignedAt`   | DateTime!     | When user was assigned to organization                                                                |
| `deletedAt`    | DateTime      |                                                                                                       |
| `deletedBy`    | Actor         |                                                                                                       |
| `customFields` | JSON!         | Membership-specific custom fields. Examples: position, department, employee\_id, access\_card\_number |

#### Integration

External system integration. Integrations have API access and permissions like users. Credentials are stored in external secure vault.

**Implements:** Node, Timestamped, SoftDeletable

| Field           | Type       | Description                                                                                                                                                         |
| --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`            | UUID!      |                                                                                                                                                                     |
| `actorType`     | ActorType! | Always INTEGRATION                                                                                                                                                  |
| `name`          | String!    | Integration display name                                                                                                                                            |
| `credentialRef` | String     | Reference to credentials in secure vault. Actual credentials are never stored in database. Examples: vault:secret/integrations/erp, aws:secretsmanager:prod/api-key |
| `isActive`      | Boolean!   | Whether integration is active                                                                                                                                       |
| `createdAt`     | DateTime!  |                                                                                                                                                                     |
| `updatedAt`     | DateTime!  |                                                                                                                                                                     |
| `deletedAt`     | DateTime   |                                                                                                                                                                     |
| `deletedBy`     | Actor      |                                                                                                                                                                     |

### Access control

#### ActorRole

Role assignment to an actor. Links actors (users/integrations) to roles with optional expiration.

**Implements:** Node, Timestamped

| Field        | Type      | Description                                                 |
| ------------ | --------- | ----------------------------------------------------------- |
| `id`         | UUID!     |                                                             |
| `actor`      | Actor!    | Actor receiving the role                                    |
| `role`       | Role!     | Role being assigned                                         |
| `assignedAt` | DateTime! | When role was assigned                                      |
| `assignedBy` | Actor     | Who assigned the role                                       |
| `expireDate` | DateTime  | Role expiration timestamp. Null means permanent assignment. |
| `createdAt`  | DateTime! |                                                             |
| `updatedAt`  | DateTime! |                                                             |

#### RolePermission

Permission granted to a role. Defines what actions a role can perform on what entities.

**Implements:** Node, Timestamped

| Field             | Type                  | Description                                                                                                       |
| ----------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `id`              | UUID!                 |                                                                                                                   |
| `role`            | Role!                 | Role receiving the permission                                                                                     |
| `permissionScope` | PermissionScope!      | Permission scope being granted                                                                                    |
| `targetEntityId`  | UUID                  | Specific entity ID this permission applies to. Null means permission applies to all entities of the scope's type. |
| `actions`         | \[ActionPermission!]! | Actions allowed by this permission                                                                                |
| `grantedAt`       | DateTime!             | When permission was granted                                                                                       |
| `grantedBy`       | Actor                 | Who granted the permission                                                                                        |
| `createdAt`       | DateTime!             |                                                                                                                   |
| `updatedAt`       | DateTime!             |                                                                                                                   |

#### UserScope

Whitelist filter restricting actor's access to specific entities. When present, acts as an intersection with role permissions. Logic: - If user has NO UserScope entries: role permissions apply fully - If user has UserScope entries: effective\_permissions = role\_permissions ∩ user\_scope

**Implements:** Node

| Field             | Type                  | Description                             |
| ----------------- | --------------------- | --------------------------------------- |
| `id`              | UUID!                 |                                         |
| `actor`           | Actor!                | Actor being restricted                  |
| `permissionScope` | PermissionScope!      | Permission scope being filtered         |
| `targetEntityId`  | UUID!                 | Specific entity the actor can access    |
| `actions`         | \[ActionPermission!]! | Actions allowed on this specific entity |

### Custom fields

#### CustomFieldDefinition

Custom field definition (metadata). Defines structure and validation for custom fields on entities. Two-level architecture: 1. System fields - defined on EntityType (e.g., geojson for all geo\_objects) 2. Type fields - defined on specific type (e.g., vin for vehicle AssetType)

**Implements:** CatalogItem, Node, Timestamped, SoftDeletable

| Field              | Type             | Description                                                                                              |
| ------------------ | ---------------- | -------------------------------------------------------------------------------------------------------- |
| `id`               | UUID!            |                                                                                                          |
| `code`             | String!          |                                                                                                          |
| `title`            | String!          |                                                                                                          |
| `description`      | String           |                                                                                                          |
| `order`            | Int!             |                                                                                                          |
| `isSystem`         | Boolean!         |                                                                                                          |
| `extra`            | JSON!            |                                                                                                          |
| `createdAt`        | DateTime!        |                                                                                                          |
| `updatedAt`        | DateTime!        |                                                                                                          |
| `deletedAt`        | DateTime         |                                                                                                          |
| `deletedBy`        | Actor            |                                                                                                          |
| `parent`           | CatalogItem      |                                                                                                          |
| `children`         | \[CatalogItem!]! |                                                                                                          |
| `organization`     | Organization     | Organization that owns this definition                                                                   |
| `owner`            | CatalogItem!     | Owner catalog item. Either EntityType (for system fields) or specific type (AssetType, DeviceType, etc.) |
| `targetEntityType` | EntityType!      | Target entity type this field applies to                                                                 |
| `fieldType`        | FieldType!       | Data type determining validation and UI                                                                  |
| `params`           | FieldParams!     | Type-specific parameters (validation, options, references)                                               |

#### FieldParamsString

Parameters for STRING field type

**Implements:** FieldParams

| Field          | Type     | Description                             |
| -------------- | -------- | --------------------------------------- |
| `isRequired`   | Boolean! |                                         |
| `maxLength`    | Int      | Maximum character length (default: 255) |
| `defaultValue` | String   | Default value for new entities          |

#### FieldParamsText

Parameters for TEXT field type

**Implements:** FieldParams

| Field          | Type     | Description                                 |
| -------------- | -------- | ------------------------------------------- |
| `isRequired`   | Boolean! |                                             |
| `maxLength`    | Int      | Maximum character length (null = unlimited) |
| `defaultValue` | String   | Default value for new entities              |

#### FieldParamsNumber

Parameters for NUMBER field type

**Implements:** FieldParams

| Field          | Type     | Description                                    |
| -------------- | -------- | ---------------------------------------------- |
| `isRequired`   | Boolean! |                                                |
| `min`          | Float    | Minimum allowed value                          |
| `max`          | Float    | Maximum allowed value                          |
| `precision`    | Int      | Decimal precision (digits after decimal point) |
| `defaultValue` | Float    | Default value for new entities                 |

#### FieldParamsBoolean

Parameters for BOOLEAN field type

**Implements:** FieldParams

| Field          | Type     | Description                    |
| -------------- | -------- | ------------------------------ |
| `isRequired`   | Boolean! |                                |
| `defaultValue` | Boolean  | Default value for new entities |

#### FieldParamsDate

Parameters for DATE field type

**Implements:** FieldParams

| Field          | Type     | Description                    |
| -------------- | -------- | ------------------------------ |
| `isRequired`   | Boolean! |                                |
| `defaultValue` | Date     | Default value for new entities |

#### FieldParamsDatetime

Parameters for DATETIME field type

**Implements:** FieldParams

| Field          | Type     | Description                    |
| -------------- | -------- | ------------------------------ |
| `isRequired`   | Boolean! |                                |
| `defaultValue` | DateTime | Default value for new entities |

#### FieldParamsGeojson

Parameters for GEOJSON field type

**Implements:** FieldParams

| Field          | Type       | Description                                                                                                      |
| -------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| `isRequired`   | Boolean!   |                                                                                                                  |
| `allowedTypes` | \[String!] | Allowed GeoJSON geometry types. Examples: Point, Polygon, LineString, MultiPolygon Null means all types allowed. |

#### FieldParamsSchedule

Parameters for SCHEDULE field type

**Implements:** FieldParams

| Field        | Type     | Description |
| ------------ | -------- | ----------- |
| `isRequired` | Boolean! |             |

#### FieldParamsOptions

Parameters for OPTIONS field type

**Implements:** FieldParams

| Field          | Type             | Description                              |
| -------------- | ---------------- | ---------------------------------------- |
| `isRequired`   | Boolean!         |                                          |
| `isMulti`      | Boolean!         | Whether multiple options can be selected |
| `options`      | \[FieldOption!]! | Available options                        |
| `defaultValue` | String           | Default option code for new entities     |

#### FieldOption

Single option in OPTIONS field

| Field        | Type     | Description                                                              |
| ------------ | -------- | ------------------------------------------------------------------------ |
| `code`       | String!  | Unique option code within field                                          |
| `label`      | String!  | Display label (localizable)                                              |
| `isArchived` | Boolean! | Whether option is archived (hidden from selection but preserved in data) |

#### FieldParamsDevice

Parameters for DEVICE field type

**Implements:** FieldParams

| Field        | Type     | Description                              |
| ------------ | -------- | ---------------------------------------- |
| `isRequired` | Boolean! |                                          |
| `isMulti`    | Boolean! | Whether multiple devices can be selected |

#### FieldParamsReference

Parameters for REFERENCE field type

**Implements:** FieldParams

| Field               | Type     | Description                                 |
| ------------------- | -------- | ------------------------------------------- |
| `isRequired`        | Boolean! |                                             |
| `isMulti`           | Boolean! | Whether multiple references can be selected |
| `refEntityTypeCode` | String!  | Entity type code that can be referenced     |

#### FieldParamsCatalog

Parameters for CATALOG field type

**Implements:** FieldParams

| Field            | Type     | Description                                  |
| ---------------- | -------- | -------------------------------------------- |
| `isRequired`     | Boolean! |                                              |
| `isMulti`        | Boolean! | Whether multiple items can be selected       |
| `refCatalogCode` | String!  | Catalog code that items can be selected from |

#### FieldParamsTag

Parameters for TAG field type

**Implements:** FieldParams

| Field        | Type     | Description                           |
| ------------ | -------- | ------------------------------------- |
| `isRequired` | Boolean! |                                       |
| `isMulti`    | Boolean! | Whether multiple tags can be selected |

### Catalog items

#### Module

System module definition. Modules group related functionality and permission scopes. Examples: fleet\_management, maintenance, reports

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | UUID!            |             |
| `code`        | String!          |             |
| `title`       | String!          |             |
| `description` | String           |             |
| `order`       | Int!             |             |
| `isSystem`    | Boolean!         |             |
| `extra`       | JSON!            |             |
| `createdAt`   | DateTime!        |             |
| `updatedAt`   | DateTime!        |             |
| `parent`      | CatalogItem      |             |
| `children`    | \[CatalogItem!]! |             |

#### CatalogCategory

Category for grouping catalogs. Used to organize user-defined catalogs in UI. Examples: vehicles, equipment, locations

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | UUID!            |             |
| `code`        | String!          |             |
| `title`       | String!          |             |
| `description` | String           |             |
| `order`       | Int!             |             |
| `isSystem`    | Boolean!         |             |
| `extra`       | JSON!            |             |
| `createdAt`   | DateTime!        |             |
| `updatedAt`   | DateTime!        |             |
| `parent`      | CatalogItem      |             |
| `children`    | \[CatalogItem!]! |             |

#### EntityType

Entity type definition. Defines customizable entity types and their UUID discriminators. Examples: device, asset, geo\_object, schedule

**Implements:** CatalogItem, Node, Timestamped

| Field                    | Type                       | Description                                                                                                                                             |
| ------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                     | UUID!                      |                                                                                                                                                         |
| `code`                   | String!                    |                                                                                                                                                         |
| `title`                  | String!                    |                                                                                                                                                         |
| `description`            | String                     |                                                                                                                                                         |
| `order`                  | Int!                       |                                                                                                                                                         |
| `isSystem`               | Boolean!                   |                                                                                                                                                         |
| `extra`                  | JSON!                      |                                                                                                                                                         |
| `createdAt`              | DateTime!                  |                                                                                                                                                         |
| `updatedAt`              | DateTime!                  |                                                                                                                                                         |
| `parent`                 | CatalogItem                |                                                                                                                                                         |
| `children`               | \[CatalogItem!]!           |                                                                                                                                                         |
| `uuidDiscriminator`      | String!                    | 4-character code embedded in UUIDs for this entity type. Allows determining entity type from UUID alone. Example: 'DEVI' for devices, 'ASST' for assets |
| `isCustomizable`         | Boolean!                   | Whether entities of this type support custom fields                                                                                                     |
| `customFieldDefinitions` | \[CustomFieldDefinition!]! | Custom field definitions for this entity type. Includes both system-level and type-specific fields.                                                     |

#### DeviceVendor

Device vendor/manufacturer. Top level of device classification hierarchy. Examples: Teltonika, Queclink, CalAmp

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description                    |
| ------------- | ---------------- | ------------------------------ |
| `id`          | UUID!            |                                |
| `code`        | String!          |                                |
| `title`       | String!          |                                |
| `description` | String           |                                |
| `order`       | Int!             |                                |
| `isSystem`    | Boolean!         |                                |
| `extra`       | JSON!            |                                |
| `createdAt`   | DateTime!        |                                |
| `updatedAt`   | DateTime!        |                                |
| `parent`      | CatalogItem      |                                |
| `children`    | \[CatalogItem!]! |                                |
| `models`      | \[DeviceModel!]! | Device models from this vendor |

#### DeviceModel

Device model. Specific product model from a vendor. Examples: FMB920, GV300, LMU-2630

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description                         |
| ------------- | ---------------- | ----------------------------------- |
| `id`          | UUID!            |                                     |
| `code`        | String!          |                                     |
| `title`       | String!          |                                     |
| `description` | String           |                                     |
| `order`       | Int!             |                                     |
| `isSystem`    | Boolean!         |                                     |
| `extra`       | JSON!            |                                     |
| `createdAt`   | DateTime!        |                                     |
| `updatedAt`   | DateTime!        |                                     |
| `parent`      | CatalogItem      |                                     |
| `children`    | \[CatalogItem!]! |                                     |
| `vendor`      | DeviceVendor!    | Vendor that manufactures this model |

#### DeviceType

Device type classification. Logical grouping of devices by function. Examples: gps\_tracker, obd\_dongle, sensor, beacon

**Implements:** CatalogItem, Node, Timestamped

| Field                    | Type                       | Description                                           |
| ------------------------ | -------------------------- | ----------------------------------------------------- |
| `id`                     | UUID!                      |                                                       |
| `code`                   | String!                    |                                                       |
| `title`                  | String!                    |                                                       |
| `description`            | String                     |                                                       |
| `order`                  | Int!                       |                                                       |
| `isSystem`               | Boolean!                   |                                                       |
| `extra`                  | JSON!                      |                                                       |
| `createdAt`              | DateTime!                  |                                                       |
| `updatedAt`              | DateTime!                  |                                                       |
| `parent`                 | CatalogItem                |                                                       |
| `children`               | \[CatalogItem!]!           |                                                       |
| `customFieldDefinitions` | \[CustomFieldDefinition!]! | Custom field definitions specific to this device type |

#### DeviceStatus

Device operational status. Lifecycle state of a device. Examples: active, inactive, maintenance, decommissioned

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | UUID!            |             |
| `code`        | String!          |             |
| `title`       | String!          |             |
| `description` | String           |             |
| `order`       | Int!             |             |
| `isSystem`    | Boolean!         |             |
| `extra`       | JSON!            |             |
| `createdAt`   | DateTime!        |             |
| `updatedAt`   | DateTime!        |             |
| `parent`      | CatalogItem      |             |
| `children`    | \[CatalogItem!]! |             |

#### DeviceRelationType

Device-to-device relationship type. Defines how two devices relate to each other. Examples: master\_slave, backup, paired

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | UUID!            |             |
| `code`        | String!          |             |
| `title`       | String!          |             |
| `description` | String           |             |
| `order`       | Int!             |             |
| `isSystem`    | Boolean!         |             |
| `extra`       | JSON!            |             |
| `createdAt`   | DateTime!        |             |
| `updatedAt`   | DateTime!        |             |
| `parent`      | CatalogItem      |             |
| `children`    | \[CatalogItem!]! |             |

#### AssetType

Asset classification type. Defines categories of trackable assets. Examples: vehicle, trailer, container, employee, pet

**Implements:** CatalogItem, Node, Timestamped

| Field                    | Type                       | Description                                          |
| ------------------------ | -------------------------- | ---------------------------------------------------- |
| `id`                     | UUID!                      |                                                      |
| `code`                   | String!                    |                                                      |
| `title`                  | String!                    |                                                      |
| `description`            | String                     |                                                      |
| `order`                  | Int!                       |                                                      |
| `isSystem`               | Boolean!                   |                                                      |
| `extra`                  | JSON!                      |                                                      |
| `createdAt`              | DateTime!                  |                                                      |
| `updatedAt`              | DateTime!                  |                                                      |
| `parent`                 | CatalogItem                |                                                      |
| `children`               | \[CatalogItem!]!           |                                                      |
| `customFieldDefinitions` | \[CustomFieldDefinition!]! | Custom field definitions specific to this asset type |

#### AssetGroupType

Asset group type with membership constraints. Defines rules for what assets can be grouped together. Examples: fleet, department, route, project

**Implements:** CatalogItem, Node, Timestamped

| Field               | Type                          | Description                                                                                                        |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `id`                | UUID!                         |                                                                                                                    |
| `code`              | String!                       |                                                                                                                    |
| `title`             | String!                       |                                                                                                                    |
| `description`       | String                        |                                                                                                                    |
| `order`             | Int!                          |                                                                                                                    |
| `isSystem`          | Boolean!                      |                                                                                                                    |
| `extra`             | JSON!                         |                                                                                                                    |
| `createdAt`         | DateTime!                     |                                                                                                                    |
| `updatedAt`         | DateTime!                     |                                                                                                                    |
| `parent`            | CatalogItem                   |                                                                                                                    |
| `children`          | \[CatalogItem!]!              |                                                                                                                    |
| `allowedAssetTypes` | \[AssetGroupTypeConstraint!]! | Allowed asset types with optional per-type limits. Empty list means any asset type is allowed (polymorphic group). |

#### AssetGroupTypeConstraint

Constraint for asset types within a group type. Defines which asset types can be added and optional quantity limits.

| Field       | Type       | Description                                                               |
| ----------- | ---------- | ------------------------------------------------------------------------- |
| `assetType` | AssetType! | Allowed asset type                                                        |
| `maxItems`  | Int        | Maximum number of assets of this type in one group. Null means unlimited. |

#### GeoObjectType

Geographic object type. Defines categories of geofences and POIs. Examples: geofence, poi, route, zone, parking

**Implements:** CatalogItem, Node, Timestamped

| Field                    | Type                       | Description                                               |
| ------------------------ | -------------------------- | --------------------------------------------------------- |
| `id`                     | UUID!                      |                                                           |
| `code`                   | String!                    |                                                           |
| `title`                  | String!                    |                                                           |
| `description`            | String                     |                                                           |
| `order`                  | Int!                       |                                                           |
| `isSystem`               | Boolean!                   |                                                           |
| `extra`                  | JSON!                      |                                                           |
| `createdAt`              | DateTime!                  |                                                           |
| `updatedAt`              | DateTime!                  |                                                           |
| `parent`                 | CatalogItem                |                                                           |
| `children`               | \[CatalogItem!]!           |                                                           |
| `customFieldDefinitions` | \[CustomFieldDefinition!]! | Custom field definitions specific to this geo object type |

#### ScheduleType

Schedule type classification. Defines categories of schedules. Examples: work\_hours, maintenance\_window, holiday, shift

**Implements:** CatalogItem, Node, Timestamped

| Field                    | Type                       | Description                                             |
| ------------------------ | -------------------------- | ------------------------------------------------------- |
| `id`                     | UUID!                      |                                                         |
| `code`                   | String!                    |                                                         |
| `title`                  | String!                    |                                                         |
| `description`            | String                     |                                                         |
| `order`                  | Int!                       |                                                         |
| `isSystem`               | Boolean!                   |                                                         |
| `extra`                  | JSON!                      |                                                         |
| `createdAt`              | DateTime!                  |                                                         |
| `updatedAt`              | DateTime!                  |                                                         |
| `parent`                 | CatalogItem                |                                                         |
| `children`               | \[CatalogItem!]!           |                                                         |
| `customFieldDefinitions` | \[CustomFieldDefinition!]! | Custom field definitions specific to this schedule type |

#### Role

User role definition. Roles group permissions and can be assigned to actors. Can be system-wide or organization-specific.

**Implements:** CatalogItem, Node, Timestamped

| Field          | Type                | Description                                                                                   |
| -------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| `id`           | UUID!               |                                                                                               |
| `code`         | String!             |                                                                                               |
| `title`        | String!             |                                                                                               |
| `description`  | String              |                                                                                               |
| `order`        | Int!                |                                                                                               |
| `isSystem`     | Boolean!            |                                                                                               |
| `extra`        | JSON!               |                                                                                               |
| `createdAt`    | DateTime!           |                                                                                               |
| `updatedAt`    | DateTime!           |                                                                                               |
| `parent`       | CatalogItem         |                                                                                               |
| `children`     | \[CatalogItem!]!    |                                                                                               |
| `organization` | Organization        | Organization this role belongs to. Null for system-wide roles available to all organizations. |
| `permissions`  | \[RolePermission!]! | Permissions assigned to this role                                                             |

#### PermissionScope

Permission scope definition. Defines what actions can be controlled for a specific domain area. Examples: device.manage, asset.view, report.generate

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description                                                                   |
| ------------- | ---------------- | ----------------------------------------------------------------------------- |
| `id`          | UUID!            |                                                                               |
| `code`        | String!          |                                                                               |
| `title`       | String!          |                                                                               |
| `description` | String           |                                                                               |
| `order`       | Int!             |                                                                               |
| `isSystem`    | Boolean!         |                                                                               |
| `extra`       | JSON!            |                                                                               |
| `createdAt`   | DateTime!        |                                                                               |
| `updatedAt`   | DateTime!        |                                                                               |
| `parent`      | CatalogItem      |                                                                               |
| `children`    | \[CatalogItem!]! |                                                                               |
| `module`      | Module!          | Module this permission scope belongs to                                       |
| `entityType`  | EntityType!      | Entity type this permission applies to                                        |
| `category`    | String!          | Permission category for UI grouping. Examples: management, viewing, reporting |

#### Tag

Tag for labeling entities. Tags can be universal or restricted to specific entity types.

**Implements:** CatalogItem, Node, Timestamped

| Field          | Type             | Description                                                                                     |
| -------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| `id`           | UUID!            |                                                                                                 |
| `code`         | String!          |                                                                                                 |
| `title`        | String!          |                                                                                                 |
| `description`  | String           |                                                                                                 |
| `order`        | Int!             |                                                                                                 |
| `isSystem`     | Boolean!         |                                                                                                 |
| `extra`        | JSON!            |                                                                                                 |
| `createdAt`    | DateTime!        |                                                                                                 |
| `updatedAt`    | DateTime!        |                                                                                                 |
| `parent`       | CatalogItem      |                                                                                                 |
| `children`     | \[CatalogItem!]! |                                                                                                 |
| `entityType`   | EntityType       | Entity type this tag can be applied to. Null means tag is universal (applicable to any entity). |
| `organization` | Organization!    | Organization that owns this tag                                                                 |

#### Country

Country reference data. ISO 3166-1 country codes and names.

**Implements:** CatalogItem, Node, Timestamped

| Field         | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | UUID!            |             |
| `code`        | String!          |             |
| `title`       | String!          |             |
| `description` | String           |             |
| `order`       | Int!             |             |
| `isSystem`    | Boolean!         |             |
| `extra`       | JSON!            |             |
| `createdAt`   | DateTime!        |             |
| `updatedAt`   | DateTime!        |             |
| `parent`      | CatalogItem      |             |
| `children`    | \[CatalogItem!]! |             |

#### UserCatalogItem

User-defined catalog item. Custom dictionary entries created by organization users. Supports soft delete and hierarchy.

**Implements:** CatalogItem, Node, Timestamped

| Field          | Type             | Description                      |
| -------------- | ---------------- | -------------------------------- |
| `id`           | UUID!            |                                  |
| `code`         | String!          |                                  |
| `title`        | String!          |                                  |
| `description`  | String           |                                  |
| `order`        | Int!             |                                  |
| `isSystem`     | Boolean!         |                                  |
| `extra`        | JSON!            |                                  |
| `createdAt`    | DateTime!        |                                  |
| `updatedAt`    | DateTime!        |                                  |
| `deletedAt`    | DateTime         | Soft delete timestamp            |
| `parent`       | CatalogItem      |                                  |
| `children`     | \[CatalogItem!]! |                                  |
| `catalog`      | Catalog!         | Catalog this item belongs to     |
| `organization` | Organization!    | Organization that owns this item |

#### Catalog

Catalog definition (catalog of catalogs). Catalogs are themselves catalog items, enabling unified management.

**Implements:** CatalogItem, Node, Timestamped

| Field                            | Type             | Description                                                                                 |
| -------------------------------- | ---------------- | ------------------------------------------------------------------------------------------- |
| `id`                             | UUID!            |                                                                                             |
| `code`                           | String!          |                                                                                             |
| `title`                          | String!          |                                                                                             |
| `description`                    | String           |                                                                                             |
| `order`                          | Int!             |                                                                                             |
| `isSystem`                       | Boolean!         |                                                                                             |
| `extra`                          | JSON!            |                                                                                             |
| `createdAt`                      | DateTime!        |                                                                                             |
| `updatedAt`                      | DateTime!        |                                                                                             |
| `parent`                         | CatalogItem      |                                                                                             |
| `children`                       | \[CatalogItem!]! |                                                                                             |
| `organization`                   | Organization     | Organization that owns this catalog or null for system catalogs                             |
| `module`                         | Module!          | Module this catalog is associated with                                                      |
| `category`                       | CatalogCategory  | Optional category for grouping catalogs                                                     |
| `fieldsSchema`                   | JSON             | JSON Schema defining structure of item.extra fields. Used for validation and UI generation. |
| `items(includeDeleted: Boolean)` | \[CatalogItem!]! | Items in this catalog                                                                       |

### Pagination

#### PageInfo

Pagination info following Relay Cursor Connections specification. Cursors are opaque strings (Base64-encoded position identifiers).

| Field             | Type     | Description                                                                |
| ----------------- | -------- | -------------------------------------------------------------------------- |
| `hasNextPage`     | Boolean! | Whether more items exist after current page                                |
| `hasPreviousPage` | Boolean! | Whether more items exist before current page                               |
| `startCursor`     | String   | Cursor pointing to first item in current page                              |
| `endCursor`       | String   | Cursor pointing to last item in current page                               |
| `totalCount`      | Int      | Total count of items matching filter (may be expensive for large datasets) |

#### DeviceConnection

Paginated Device results

| Field      | Type            | Description          |
| ---------- | --------------- | -------------------- |
| `edges`    | \[DeviceEdge!]! | List of device edges |
| `pageInfo` | PageInfo!       | Pagination metadata  |

#### DeviceEdge

Edge wrapper for Device in connection

| Field    | Type    | Description              |
| -------- | ------- | ------------------------ |
| `node`   | Device! | The device entity        |
| `cursor` | String! | Cursor for this position |

#### AssetConnection

Paginated Asset results

| Field      | Type           | Description         |
| ---------- | -------------- | ------------------- |
| `edges`    | \[AssetEdge!]! | List of asset edges |
| `pageInfo` | PageInfo!      | Pagination metadata |

#### AssetEdge

Edge wrapper for Asset in connection

| Field    | Type    | Description              |
| -------- | ------- | ------------------------ |
| `node`   | Asset!  | The asset entity         |
| `cursor` | String! | Cursor for this position |

#### OrganizationConnection

Paginated Organization results

| Field      | Type                  | Description                |
| ---------- | --------------------- | -------------------------- |
| `edges`    | \[OrganizationEdge!]! | List of organization edges |
| `pageInfo` | PageInfo!             | Pagination metadata        |

#### OrganizationEdge

Edge wrapper for Organization in connection

| Field    | Type          | Description              |
| -------- | ------------- | ------------------------ |
| `node`   | Organization! | The organization entity  |
| `cursor` | String!       | Cursor for this position |

#### UserConnection

Paginated User results

| Field      | Type          | Description         |
| ---------- | ------------- | ------------------- |
| `edges`    | \[UserEdge!]! | List of user edges  |
| `pageInfo` | PageInfo!     | Pagination metadata |

#### UserEdge

Edge wrapper for User in connection

| Field    | Type    | Description              |
| -------- | ------- | ------------------------ |
| `node`   | User!   | The user entity          |
| `cursor` | String! | Cursor for this position |

#### GeoObjectConnection

Paginated GeoObject results

| Field      | Type               | Description              |
| ---------- | ------------------ | ------------------------ |
| `edges`    | \[GeoObjectEdge!]! | List of geo object edges |
| `pageInfo` | PageInfo!          | Pagination metadata      |

#### GeoObjectEdge

Edge wrapper for GeoObject in connection

| Field    | Type       | Description              |
| -------- | ---------- | ------------------------ |
| `node`   | GeoObject! | The geo object entity    |
| `cursor` | String!    | Cursor for this position |

#### ScheduleConnection

Paginated Schedule results

| Field      | Type              | Description            |
| ---------- | ----------------- | ---------------------- |
| `edges`    | \[ScheduleEdge!]! | List of schedule edges |
| `pageInfo` | PageInfo!         | Pagination metadata    |

#### ScheduleEdge

Edge wrapper for Schedule in connection

| Field    | Type      | Description              |
| -------- | --------- | ------------------------ |
| `node`   | Schedule! | The schedule entity      |
| `cursor` | String!   | Cursor for this position |

#### AuditEventConnection

Paginated AuditEvent results

| Field      | Type                | Description               |
| ---------- | ------------------- | ------------------------- |
| `edges`    | \[AuditEventEdge!]! | List of audit event edges |
| `pageInfo` | PageInfo!           | Pagination metadata       |

#### AuditEventEdge

Edge wrapper for AuditEvent in connection

| Field    | Type        | Description              |
| -------- | ----------- | ------------------------ |
| `node`   | AuditEvent! | The audit event entity   |
| `cursor` | String!     | Cursor for this position |

#### AssetGroupItemConnection

Paginated AssetGroupItem results

| Field      | Type                    | Description                    |
| ---------- | ----------------------- | ------------------------------ |
| `edges`    | \[AssetGroupItemEdge!]! | List of asset group item edges |
| `pageInfo` | PageInfo!               | Pagination metadata            |

#### AssetGroupItemEdge

Edge wrapper for AssetGroupItem in connection

| Field    | Type            | Description                 |
| -------- | --------------- | --------------------------- |
| `node`   | AssetGroupItem! | The asset group item entity |
| `cursor` | String!         | Cursor for this position    |

### Audit

#### AuditEvent

Audit log entry. Tracks all significant events in the system. Table is partitioned by occurred\_at (monthly).

**Implements:** Node

| Field           | Type            | Description                                                                            |
| --------------- | --------------- | -------------------------------------------------------------------------------------- |
| `id`            | UUID!           |                                                                                        |
| `organization`  | Organization    | Organization context (null for system events)                                          |
| `eventCategory` | String!         | Event category: auth or domain                                                         |
| `actor`         | Actor           | Actor who triggered the event (null for system events)                                 |
| `ipAddress`     | String          | Client IP address                                                                      |
| `userAgent`     | String          | Client User-Agent string                                                               |
| `sourceType`    | SourceType!     | Source type of the request                                                             |
| `sourceName`    | String          | Source application name                                                                |
| `traceId`       | UUID            | Distributed tracing ID. Used to correlate logs across services.                        |
| `aggregateType` | String          | Type of entity affected. Examples: device, asset, user, organization                   |
| `aggregateId`   | UUID            | ID of the affected entity                                                              |
| `eventType`     | AuditEventType! | Type of event that occurred                                                            |
| `eventData`     | JSON            | Event payload with details. For updates, includes changed\_fields with old/new values. |
| `occurredAt`    | DateTime!       | When event occurred                                                                    |

#### DomainEvent

Domain event for real-time updates. Unified format for all entity change notifications.

| Field            | Type            | Description                                      |
| ---------------- | --------------- | ------------------------------------------------ |
| `aggregateType`  | String!         | Entity type that changed                         |
| `aggregateId`    | UUID!           | ID of the changed entity                         |
| `eventType`      | AuditEventType! | Type of change                                   |
| `organizationId` | UUID            | Organization context                             |
| `payload`        | JSON            | Event details (changed fields, new values, etc.) |
| `occurredAt`     | DateTime!       | When the event occurred                          |

### Localization

#### I18nText

Localized text entry. Stores translations for entity fields.

| Field       | Type    | Description                                              |
| ----------- | ------- | -------------------------------------------------------- |
| `entityId`  | UUID!   | Entity this translation belongs to                       |
| `fieldCode` | String! | Field being translated (title, description, label, etc.) |
| `locale`    | String! | Locale code (en, ru, es, etc.)                           |
| `textValue` | String! | Translated text value                                    |

### Other

#### BulkDeleteResult

Result of bulk delete operation

| Field          | Type      | Description                                                    |
| -------------- | --------- | -------------------------------------------------------------- |
| `deletedCount` | Int!      | Number of successfully deleted entities                        |
| `failedIds`    | \[UUID!]! | IDs that failed to delete (permission denied, not found, etc.) |
