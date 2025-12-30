# Objects

Objects are the return types for queries and mutations. They represent the data structures in the Navixy API.

## Devices

### Device

Tracking device (GPS tracker, sensor, beacon, etc.). Devices are physical hardware that collect and transmit data.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/), [Customizable](/api-reference/interfaces.md#customizable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this device |
| `type` | [DeviceType!](/api-reference/objects.md#devicetype/) | Device type classification |
| `model` | [DeviceModel](/api-reference/objects.md#devicemodel/) | Specific device model (optional) |
| `status` | [DeviceStatus!](/api-reference/objects.md#devicestatus/) | Current operational status |
| `title` | `String!` | Device display name |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Custom fields data |
| `identifiers` | [[DeviceIdentifier!]!](/api-reference/objects.md#deviceidentifier/) | Hardware identifiers (IMEI, serial, MAC, etc.) |
| `inventory` | [Inventory](/api-reference/objects.md#inventory/) | Inventory this device is assigned to |
| `relationsFrom` | [[DeviceRelation!]!](/api-reference/objects.md#devicerelation/) | Outgoing relationships to other devices |
| `relationsTo` | [[DeviceRelation!]!](/api-reference/objects.md#devicerelation/) | Incoming relationships from other devices |

### DeviceIdentifier

Device hardware identifier. Devices can have multiple identifiers of different types.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `device` | [Device!](/api-reference/objects.md#device/) | Device this identifier belongs to |
| `type` | [DeviceIdType!](/api-reference/scalars-and-enums.md#deviceidtype/) | Type of identifier |
| `value` | `String!` | Identifier value |
| `namespace` | `String` | Namespace for identifier uniqueness. Allows same identifier value in different contexts. Example: factory_a, factory_b for serial numbers |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |

### DeviceRelation

Relationship between two devices. Defines how devices are connected or related.

**Implements:** [Node](/api-reference/interfaces.md#node/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `firstDevice` | [Device!](/api-reference/objects.md#device/) | First device in relationship |
| `secondDevice` | [Device!](/api-reference/objects.md#device/) | Second device in relationship |
| `type` | [DeviceRelationType!](/api-reference/objects.md#devicerelationtype/) | Type of relationship |

### DeviceInventoryRelation

Device assignment to inventory record. Tracks which inventory a device belongs to.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `device` | [Device!](/api-reference/objects.md#device/) | Device being assigned |
| `inventory` | [Inventory!](/api-reference/objects.md#inventory/) | Target inventory |
| `assignedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When device was assigned |
| `assignedBy` | [Actor](/api-reference/objects.md#actor/) | Who assigned the device |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |

## Assets

### AssetGroupTypeConstraint

Constraint for asset types within a group type. Defines which asset types can be added and optional quantity limits.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `assetType` | [AssetType!](/api-reference/objects.md#assettype/) | Allowed asset type |
| `maxItems` | `Int` | Maximum number of assets of this type in one group. Null means unlimited. |

### Asset

Physical or logical asset. Assets are things being tracked (vehicles, trailers, people, etc.).

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/), [Customizable](/api-reference/interfaces.md#customizable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this asset |
| `type` | [AssetType!](/api-reference/objects.md#assettype/) | Asset type classification |
| `title` | `String!` | Asset display name |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Custom fields data |
| `groups` | [[AssetGroup!]!](/api-reference/objects.md#assetgroup/) | Groups this asset belongs to |

### AssetGroup

Group of assets. Used to organize assets into logical collections.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this group |
| `type` | [AssetGroupType!](/api-reference/objects.md#assetgrouptype/) | Group type with constraints |
| `title` | `String!` | Group display name |
| `color` | `String` | Color for UI display (hex format) |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `currentAssets` | [[Asset!]!](/api-reference/objects.md#asset/) | Assets currently in this group |
| `history` | [AssetGroupItemConnection!](/api-reference/objects.md#assetgroupitemconnection/) | Full membership history with pagination |

### AssetGroupItem

Asset group membership record. Tracks current and historical group membership.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `group` | [AssetGroup!](/api-reference/objects.md#assetgroup/) | Group containing the asset |
| `asset` | [Asset!](/api-reference/objects.md#asset/) | Asset in the group |
| `attachedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When asset was added to group |
| `detachedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) | When asset was removed from group. Null means currently attached. |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |

## Geo objects

### GeoObject

Geographic object (geofence, POI, route). Geometry is stored in customFields as system field 'geojson'.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/), [Customizable](/api-reference/interfaces.md#customizable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this geo object |
| `type` | [GeoObjectType!](/api-reference/objects.md#geoobjecttype/) | Geo object type classification |
| `title` | `String!` | Geo object display name |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Custom fields including 'geojson' system field. geojson contains [GeoJSON](https://geojson.org/) geometry (Point, Polygon, etc.) |

## Schedules

### Schedule

Schedule definition. Used for work hours, maintenance windows, holidays, etc. Schedule data is stored in customFields as system field 'schedule_data'.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/), [Customizable](/api-reference/interfaces.md#customizable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this schedule |
| `type` | [ScheduleType!](/api-reference/objects.md#scheduletype/) | Schedule type classification |
| `title` | `String!` | Schedule display name |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Custom fields including schedule_data system field |

## Inventory

### Inventory

Inventory/warehouse record. Devices can be assigned to inventory for stock management.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this inventory |
| `code` | `String!` | Unique inventory code within organization |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `devices` | [DeviceConnection!](/api-reference/objects.md#deviceconnection/) | Devices assigned to this inventory |

## Organizations

### Organization

Organization in the hierarchy. Organizations contain users, devices, assets, and other business entities. Supports multi-tenancy with optional dealer hierarchy.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` | Unique organization code. Format: lowercase alphanumeric with underscores. Example: acme_corp, dealer_moscow |
| `title` | `String!` | Organization display name |
| `externalId` | `String` | External system identifier for integration |
| `isActive` | `Boolean!` | Whether organization is active |
| `isDealer` | `Boolean!` | Whether organization can create child organizations. Dealer organizations can have sub-organizations. |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `parent` | [Organization](/api-reference/objects.md#organization/) | Parent organization (null for root) |
| `children` | [[Organization!]!](/api-reference/objects.md#organization/) | Child organizations |
| `members` | [[Member!]!](/api-reference/objects.md#member/) | Members (users) of this organization |
| `devices` | [DeviceConnection!](/api-reference/objects.md#deviceconnection/) | Devices owned by this organization |
| `assets` | [AssetConnection!](/api-reference/objects.md#assetconnection/) | Assets owned by this organization |
| `geoObjects` | [GeoObjectConnection!](/api-reference/objects.md#geoobjectconnection/) | Geographic objects owned by this organization |
| `schedules` | [ScheduleConnection!](/api-reference/objects.md#scheduleconnection/) | Schedules owned by this organization |

## Actors

### Actor

Abstract actor entity. Actors are entities that can perform actions and have permissions. Resolved to concrete User or Integration type.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `actorType` | [ActorType!](/api-reference/scalars-and-enums.md#actortype/) | Type discriminator |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `asUser` | [User](/api-reference/objects.md#user/) | Resolve to User if actorType is USER |
| `asIntegration` | [Integration](/api-reference/objects.md#integration/) | Resolve to Integration if actorType is INTEGRATION |

### User

Human user account. Users authenticate via external identity providers and can be members of organizations.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `actorType` | [ActorType!](/api-reference/scalars-and-enums.md#actortype/) | Always USER |
| `identityProvider` | `String!` | Identity provider name. Examples: keycloak, auth0, okta, azure_ad |
| `identityProviderId` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) | User's unique ID in the identity provider |
| `fullName` | `String!` | User's display name |
| `externalId` | `String` | External system identifier for integration |
| `isActive` | `Boolean!` | Whether user account is active |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |

### Member

User membership in an organization. Links users to organizations with membership-specific custom fields. A user can be a member of multiple organizations.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/), [Customizable](/api-reference/interfaces.md#customizable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `user` | [User!](/api-reference/objects.md#user/) | The user |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization the user belongs to |
| `isActive` | `Boolean!` | Whether membership is active |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `assignedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When user was assigned to organization |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Membership-specific custom fields. Examples: position, department, employee_id, access_card_number |

### Integration

External system integration. Integrations have API access and permissions like users. Credentials are stored in external secure vault.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `actorType` | [ActorType!](/api-reference/scalars-and-enums.md#actortype/) | Always INTEGRATION |
| `name` | `String!` | Integration display name |
| `credentialRef` | `String` | Reference to credentials in secure vault. Actual credentials are never stored in database. Examples: vault:secret/integrations/erp, aws:secretsmanager:prod/api-key |
| `isActive` | `Boolean!` | Whether integration is active |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |

## Access control

### ActorRole

Role assignment to an actor. Links actors (users/integrations) to roles with optional expiration.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `actor` | [Actor!](/api-reference/objects.md#actor/) | Actor receiving the role |
| `role` | [Role!](/api-reference/objects.md#role/) | Role being assigned |
| `assignedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When role was assigned |
| `assignedBy` | [Actor](/api-reference/objects.md#actor/) | Who assigned the role |
| `expireDate` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) | Role expiration timestamp. Null means permanent assignment. |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |

### RolePermission

Permission granted to a role. Defines what actions a role can perform on what entities.

**Implements:** [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `role` | [Role!](/api-reference/objects.md#role/) | Role receiving the permission |
| `permissionScope` | [PermissionScope!](/api-reference/objects.md#permissionscope/) | Permission scope being granted |
| `targetEntityId` | [UUID](/api-reference/scalars-and-enums.md#uuid/) | Specific entity ID this permission applies to. Null means permission applies to all entities of the scope's type. |
| `actions` | [[ActionPermission!]!](/api-reference/scalars-and-enums.md#actionpermission/) | Actions allowed by this permission |
| `grantedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When permission was granted |
| `grantedBy` | [Actor](/api-reference/objects.md#actor/) | Who granted the permission |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |

### UserScope

Whitelist filter restricting actor's access to specific entities. When present, acts as an intersection with role permissions. Logic: - If user has NO UserScope entries: role permissions apply fully - If user has UserScope entries: effective_permissions = role_permissions ∩ user_scope

**Implements:** [Node](/api-reference/interfaces.md#node/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `actor` | [Actor!](/api-reference/objects.md#actor/) | Actor being restricted |
| `permissionScope` | [PermissionScope!](/api-reference/objects.md#permissionscope/) | Permission scope being filtered |
| `targetEntityId` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) | Specific entity the actor can access |
| `actions` | [[ActionPermission!]!](/api-reference/scalars-and-enums.md#actionpermission/) | Actions allowed on this specific entity |

## Custom fields

### CustomFieldDefinition

Custom field definition (metadata). Defines structure and validation for custom fields on entities. Two-level architecture: 1. System fields - defined on EntityType (e.g., geojson for all geo_objects) 2. Type fields - defined on specific type (e.g., vin for vehicle AssetType)

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/), [SoftDeletable](/api-reference/interfaces.md#softdeletable/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `organization` | [Organization](/api-reference/objects.md#organization/) | Organization that owns this definition |
| `owner` | [CatalogItem!](/api-reference/interfaces.md#catalogitem/) | Owner catalog item. Either EntityType (for system fields) or specific type (AssetType, DeviceType, etc.) |
| `targetEntityType` | [EntityType!](/api-reference/objects.md#entitytype/) | Target entity type this field applies to |
| `fieldType` | [FieldType!](/api-reference/scalars-and-enums.md#fieldtype/) | Data type determining validation and UI |
| `params` | [FieldParams!](/api-reference/interfaces.md#fieldparams/) | Type-specific parameters (validation, options, references) |

### FieldParamsString

Parameters for STRING field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `maxLength` | `Int` | Maximum character length (default: 255) |
| `defaultValue` | `String` | Default value for new entities |

### FieldParamsText

Parameters for TEXT field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `maxLength` | `Int` | Maximum character length (null = unlimited) |
| `defaultValue` | `String` | Default value for new entities |

### FieldParamsNumber

Parameters for NUMBER field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `min` | `Float` | Minimum allowed value |
| `max` | `Float` | Maximum allowed value |
| `precision` | `Int` | Decimal precision (digits after decimal point) |
| `defaultValue` | `Float` | Default value for new entities |

### FieldParamsBoolean

Parameters for BOOLEAN field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `defaultValue` | `Boolean` | Default value for new entities |

### FieldParamsDate

Parameters for DATE field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `defaultValue` | [Date](/api-reference/scalars-and-enums.md#date/) | Default value for new entities |

### FieldParamsDatetime

Parameters for DATETIME field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `defaultValue` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) | Default value for new entities |

### FieldParamsGeojson

Parameters for GEOJSON field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `allowedTypes` | `[String!]` | Allowed [GeoJSON](https://geojson.org/) geometry types. Examples: Point, Polygon, LineString, MultiPolygon Null means all types allowed. |

### FieldParamsSchedule

Parameters for SCHEDULE field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |

### FieldParamsOptions

Parameters for OPTIONS field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `isMulti` | `Boolean!` | Whether multiple options can be selected |
| `options` | [[FieldOption!]!](/api-reference/objects.md#fieldoption/) | Available options |
| `defaultValue` | `String` | Default option code for new entities |

### FieldOption

Single option in OPTIONS field

| Field | Type | Description |
| ----- | ---- | ----------- |
| `code` | `String!` | Unique option code within field |
| `label` | `String!` | Display label (localizable) |
| `isArchived` | `Boolean!` | Whether option is archived (hidden from selection but preserved in data) |

### FieldParamsDevice

Parameters for DEVICE field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `isMulti` | `Boolean!` | Whether multiple devices can be selected |

### FieldParamsReference

Parameters for REFERENCE field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `isMulti` | `Boolean!` | Whether multiple references can be selected |
| `refEntityTypeCode` | `String!` | Entity type code that can be referenced |

### FieldParamsCatalog

Parameters for CATALOG field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `isMulti` | `Boolean!` | Whether multiple items can be selected |
| `refCatalogCode` | `String!` | Catalog code that items can be selected from |

### FieldParamsTag

Parameters for TAG field type

**Implements:** [FieldParams](/api-reference/interfaces.md#fieldparams/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` |  |
| `isMulti` | `Boolean!` | Whether multiple tags can be selected |

## Audit

### AuditEvent

Audit log entry. Tracks all significant events in the system.

**Implements:** [Node](/api-reference/interfaces.md#node/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `organization` | [Organization](/api-reference/objects.md#organization/) | Organization context (null for system events) |
| `eventCategory` | `String!` | Event category: auth or domain |
| `actor` | [Actor](/api-reference/objects.md#actor/) | Actor who triggered the event (null for system events) |
| `ipAddress` | `String` | Client IP address |
| `userAgent` | `String` | Client User-Agent string |
| `sourceType` | [SourceType!](/api-reference/scalars-and-enums.md#sourcetype/) | Source type of the request |
| `sourceName` | `String` | Source application name |
| `traceId` | [UUID](/api-reference/scalars-and-enums.md#uuid/) | Distributed tracing ID. Used to correlate logs across services. |
| `aggregateType` | `String` | Type of entity affected. Examples: device, asset, user, organization |
| `aggregateId` | [UUID](/api-reference/scalars-and-enums.md#uuid/) | ID of the affected entity |
| `eventType` | [AuditEventType!](/api-reference/scalars-and-enums.md#auditeventtype/) | Type of event that occurred |
| `eventData` | [JSON](/api-reference/scalars-and-enums.md#json/) | Event payload with details. For updates, includes changed_fields with old/new values. |
| `occurredAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When event occurred |

### DomainEvent

Domain event for real-time updates. Unified format for all entity change notifications.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `aggregateType` | `String!` | Entity type that changed |
| `aggregateId` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) | ID of the changed entity |
| `eventType` | [AuditEventType!](/api-reference/scalars-and-enums.md#auditeventtype/) | Type of change |
| `organizationId` | [UUID](/api-reference/scalars-and-enums.md#uuid/) | Organization context |
| `payload` | [JSON](/api-reference/scalars-and-enums.md#json/) | Event details (changed fields, new values, etc.) |
| `occurredAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When the event occurred |

## Localization

### I18nText

Localized text entry. Stores translations for entity fields.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `entityId` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) | Entity this translation belongs to |
| `fieldCode` | `String!` | Field being translated (title, description, label, etc.) |
| `locale` | `String!` | Locale code (en, ru, es, etc.) |
| `textValue` | `String!` | Translated text value |

## Pagination

### PageInfo

Pagination info following Relay Cursor Connections specification. Cursors are opaque strings (Base64-encoded position identifiers).

| Field | Type | Description |
| ----- | ---- | ----------- |
| `hasNextPage` | `Boolean!` | Whether more items exist after current page |
| `hasPreviousPage` | `Boolean!` | Whether more items exist before current page |
| `startCursor` | `String` | Cursor pointing to first item in current page |
| `endCursor` | `String` | Cursor pointing to last item in current page |
| `totalCount` | `Int` | Total count of items matching filter. Null if counting is too expensive. |
| `totalCountIsApproximate` | `Boolean` | True if totalCount is approximate (e.g., from pg_class.reltuples). Null or false means exact count. |

### DeviceConnection

Paginated Device results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[DeviceEdge!]!](/api-reference/objects.md#deviceedge/) | List of device edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### DeviceEdge

Edge wrapper for Device in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [Device!](/api-reference/objects.md#device/) | The device entity |
| `cursor` | `String!` | Cursor for this position |

### AssetConnection

Paginated Asset results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetEdge!]!](/api-reference/objects.md#assetedge/) | List of asset edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### AssetEdge

Edge wrapper for Asset in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [Asset!](/api-reference/objects.md#asset/) | The asset entity |
| `cursor` | `String!` | Cursor for this position |

### OrganizationConnection

Paginated Organization results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[OrganizationEdge!]!](/api-reference/objects.md#organizationedge/) | List of organization edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### OrganizationEdge

Edge wrapper for Organization in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [Organization!](/api-reference/objects.md#organization/) | The organization entity |
| `cursor` | `String!` | Cursor for this position |

### UserConnection

Paginated User results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[UserEdge!]!](/api-reference/objects.md#useredge/) | List of user edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### UserEdge

Edge wrapper for User in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [User!](/api-reference/objects.md#user/) | The user entity |
| `cursor` | `String!` | Cursor for this position |

### GeoObjectConnection

Paginated GeoObject results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectEdge!]!](/api-reference/objects.md#geoobjectedge/) | List of geo object edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### GeoObjectEdge

Edge wrapper for GeoObject in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [GeoObject!](/api-reference/objects.md#geoobject/) | The geo object entity |
| `cursor` | `String!` | Cursor for this position |

### ScheduleConnection

Paginated Schedule results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[ScheduleEdge!]!](/api-reference/objects.md#scheduleedge/) | List of schedule edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### ScheduleEdge

Edge wrapper for Schedule in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [Schedule!](/api-reference/objects.md#schedule/) | The schedule entity |
| `cursor` | `String!` | Cursor for this position |

### AuditEventConnection

Paginated AuditEvent results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AuditEventEdge!]!](/api-reference/objects.md#auditeventedge/) | List of audit event edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### AuditEventEdge

Edge wrapper for AuditEvent in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [AuditEvent!](/api-reference/objects.md#auditevent/) | The audit event entity |
| `cursor` | `String!` | Cursor for this position |

### AssetGroupItemConnection

Paginated AssetGroupItem results

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[AssetGroupItemEdge!]!](/api-reference/objects.md#assetgroupitemedge/) | List of asset group item edges |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Pagination metadata |

### AssetGroupItemEdge

Edge wrapper for AssetGroupItem in connection

| Field | Type | Description |
| ----- | ---- | ----------- |
| `node` | [AssetGroupItem!](/api-reference/objects.md#assetgroupitem/) | The asset group item entity |
| `cursor` | `String!` | Cursor for this position |

## Bulk operations

### BulkDeleteResult

Result of bulk delete operation

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedCount` | `Int!` | Number of successfully deleted entities |
| `failedIds` | [[UUID!]!](/api-reference/scalars-and-enums.md#uuid/) | IDs that failed to delete (permission denied, not found, etc.) |

## Catalog items

### Module

System module definition. Modules group related functionality and permission scopes. Examples: fleet_management, maintenance, reports

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |

### CatalogCategory

Category for grouping catalogs. Used to organize user-defined catalogs in UI. Examples: vehicles, equipment, locations

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |

### EntityType

Entity type definition. Defines customizable entity types and their UUID discriminators. Examples: device, asset, geo_object, schedule

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `uuidDiscriminator` | `String!` | 4-character code embedded in UUIDs for this entity type. Allows determining entity type from UUID alone. Example: 'DEVI' for devices, 'ASST' for assets |
| `isCustomizable` | `Boolean!` | Whether entities of this type support custom fields |
| `customFieldDefinitions` | [[CustomFieldDefinition!]!](/api-reference/objects.md#customfielddefinition/) | Custom field definitions for this entity type. Includes both system-level and type-specific fields. |

### DeviceVendor

Device vendor/manufacturer. Top level of device classification hierarchy. Examples: Teltonika, Queclink, CalAmp

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `models` | [[DeviceModel!]!](/api-reference/objects.md#devicemodel/) | Device models from this vendor |

### DeviceModel

Device model. Specific product model from a vendor. Examples: FMB920, GV300, LMU-2630

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `vendor` | [DeviceVendor!](/api-reference/objects.md#devicevendor/) | Vendor that manufactures this model |

### DeviceType

Device type classification. Logical grouping of devices by function. Examples: gps_tracker, obd_dongle, sensor, beacon

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `customFieldDefinitions` | [[CustomFieldDefinition!]!](/api-reference/objects.md#customfielddefinition/) | Custom field definitions specific to this device type |

### DeviceStatus

Device operational status. Lifecycle state of a device. Examples: active, inactive, maintenance, decommissioned

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |

### DeviceRelationType

Device-to-device relationship type. Defines how two devices relate to each other. Examples: master_slave, backup, paired

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |

### AssetType

Asset classification type. Defines categories of trackable assets. Examples: vehicle, trailer, container, employee, pet

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `customFieldDefinitions` | [[CustomFieldDefinition!]!](/api-reference/objects.md#customfielddefinition/) | Custom field definitions specific to this asset type |

### AssetGroupType

Asset group type with membership constraints. Defines rules for what assets can be grouped together. Examples: fleet, department, route, project

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `allowedAssetTypes` | [[AssetGroupTypeConstraint!]!](/api-reference/objects.md#assetgrouptypeconstraint/) | Allowed asset types with optional per-type limits. Empty list means any asset type is allowed (polymorphic group). |

### GeoObjectType

Geographic object type. Defines categories of geofences and POIs. Examples: geofence, poi, route, zone, parking

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `customFieldDefinitions` | [[CustomFieldDefinition!]!](/api-reference/objects.md#customfielddefinition/) | Custom field definitions specific to this geo object type |

### ScheduleType

Schedule type classification. Defines categories of schedules. Examples: work_hours, maintenance_window, holiday, shift

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `customFieldDefinitions` | [[CustomFieldDefinition!]!](/api-reference/objects.md#customfielddefinition/) | Custom field definitions specific to this schedule type |

### Role

User role definition. Roles group permissions and can be assigned to actors. Can be system-wide or organization-specific.

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `organization` | [Organization](/api-reference/objects.md#organization/) | Organization this role belongs to. Null for system-wide roles available to all organizations. |
| `permissions` | [[RolePermission!]!](/api-reference/objects.md#rolepermission/) | Permissions assigned to this role |

### PermissionScope

Permission scope definition. Defines what actions can be controlled for a specific domain area. Examples: device.manage, asset.view, report.generate

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `module` | [Module!](/api-reference/objects.md#module/) | Module this permission scope belongs to |
| `entityType` | [EntityType!](/api-reference/objects.md#entitytype/) | Entity type this permission applies to |
| `category` | `String!` | Permission category for UI grouping. Examples: management, viewing, reporting |

### Tag

Tag for labeling entities. Tags can be universal or restricted to specific entity types.

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `entityType` | [EntityType](/api-reference/objects.md#entitytype/) | Entity type this tag can be applied to. Null means tag is universal (applicable to any entity). |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this tag |

### Country

Country reference data. [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country codes and names.

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |

### UserCatalogItem

User-defined catalog item. Custom dictionary entries created by organization users. Supports soft delete and hierarchy.

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) | Soft delete timestamp |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `catalog` | [Catalog!](/api-reference/objects.md#catalog/) | Catalog this item belongs to |
| `organization` | [Organization!](/api-reference/objects.md#organization/) | Organization that owns this item |

### Catalog

Catalog definition (catalog of catalogs). Catalogs are themselves catalog items, enabling unified management.

**Implements:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Node](/api-reference/interfaces.md#node/), [Timestamped](/api-reference/interfaces.md#timestamped/)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` |  |
| `title` | `String!` |  |
| `description` | `String` |  |
| `order` | `Int!` |  |
| `isSystem` | `Boolean!` |  |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) |  |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) |  |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) |  |
| `organization` | [Organization](/api-reference/objects.md#organization/) | Organization that owns this catalog or null for system catalogs |
| `module` | [Module!](/api-reference/objects.md#module/) | Module this catalog is associated with |
| `category` | [CatalogCategory](/api-reference/objects.md#catalogcategory/) | Optional category for grouping catalogs |
| `fieldsSchema` | [JSON](/api-reference/scalars-and-enums.md#json/) | JSON Schema defining structure of item.extra fields. Used for validation and UI generation. |
| `items` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) | Items in this catalog |
