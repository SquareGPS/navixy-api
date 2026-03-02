# Objects

Objects are the return types for queries and mutations. They represent the data structures in the Navixy API.

## Devices

### Device

A tracking device such as a GPS tracker, sensor, or beacon.

**Implements:** [Node](interfaces.md#node), [Titled](interfaces.md#titled), [Customizable](interfaces.md#customizable), [Versioned](interfaces.md#versioned), [InventoryItem](interfaces.md#inventoryitem)

| Field              | Type                                                                               | Description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`               | `ID!`                                                                              |                                                                                    |
| `version`          | `Int!`                                                                             |                                                                                    |
| `title`            | `String!`                                                                          |                                                                                    |
| `organization`     | [Organization!](objects.md#organization)                                           | The organization that owns this device.                                            |
| `type`             | [DeviceType!](objects.md#devicetype)                                               | The device type classification.                                                    |
| `model`            | [DeviceModel!](objects.md#devicemodel)                                             | The specific device model.                                                         |
| `status`           | [DeviceStatus!](objects.md#devicestatus)                                           | The current operational status.                                                    |
| `customFields`     | [JSON!](scalars.md#json)                                                           |                                                                                    |
| `identifiers`      | [\[DeviceIdentifier!\]!](objects.md#deviceidentifier)                              | The hardware identifiers for this device (IMEI, serial number, MAC address, etc.). |
| `inventory`        | [Inventory](objects.md#inventory)                                                  | The inventory this device is currently assigned to.                                |
| `relationsFrom`    | [\[DeviceRelation!\]!](objects.md#devicerelation)                                  | The outgoing relationships from this device to other devices.                      |
| `relationsTo`      | [\[DeviceRelation!\]!](objects.md#devicerelation)                                  | The incoming relationships from other devices to this device.                      |
| `inventoryHistory` | [DeviceInventoryRelationConnection!](objects.md#deviceinventoryrelationconnection) | The history of inventory assignments for this device.                              |

### DeviceIdentifier

A hardware identifier for a device.

**Implements:** [Node](interfaces.md#node)

| Field       | Type                                   | Description                                                                       |
| ----------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| `id`        | `ID!`                                  |                                                                                   |
| `device`    | [Device!](objects.md#device)           | The device this identifier belongs to.                                            |
| `type`      | [DeviceIdType!](enums.md#deviceidtype) | The type of identifier.                                                           |
| `value`     | `String!`                              | The identifier value.                                                             |
| `namespace` | [Code](scalars.md#code)                | The namespace for uniqueness scope. Null means the identifier is globally unique. |

### DeviceRelation

A relationship between two devices.

**Implements:** [Node](interfaces.md#node)

| Field    | Type                                                 | Description                            |
| -------- | ---------------------------------------------------- | -------------------------------------- |
| `id`     | `ID!`                                                |                                        |
| `first`  | [Device!](objects.md#device)                         | The first device in the relationship.  |
| `second` | [Device!](objects.md#device)                         | The second device in the relationship. |
| `type`   | [DeviceRelationType!](objects.md#devicerelationtype) | The type of relationship.              |

### DeviceInventoryRelation

A record of a device's assignment to an inventory.

**Implements:** [Node](interfaces.md#node)

| Field        | Type                               | Description                                     |
| ------------ | ---------------------------------- | ----------------------------------------------- |
| `id`         | `ID!`                              |                                                 |
| `device`     | [Device!](objects.md#device)       | The device that was assigned.                   |
| `inventory`  | [Inventory!](objects.md#inventory) | The inventory the device was assigned to.       |
| `assignedAt` | [DateTime!](scalars.md#datetime)   | The date and time when the device was assigned. |
| `assignedBy` | [Actor](interfaces.md#actor)       | The actor who assigned the device.              |

## Assets

### AssetGroupTypeConstraint

A constraint defining which asset types can be included in an asset group type.

| Field       | Type                               | Description                                                                           |
| ----------- | ---------------------------------- | ------------------------------------------------------------------------------------- |
| `assetType` | [AssetType!](objects.md#assettype) | The asset type allowed in the group.                                                  |
| `maxItems`  | `Int`                              | The maximum number of assets of this type allowed in one group. Null means unlimited. |

### Asset

A physical or logical asset being tracked.

**Implements:** [Node](interfaces.md#node), [Titled](interfaces.md#titled), [Customizable](interfaces.md#customizable), [Versioned](interfaces.md#versioned)

| Field          | Type                                                     | Description                                                                                       |
| -------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`           | `ID!`                                                    |                                                                                                   |
| `version`      | `Int!`                                                   |                                                                                                   |
| `title`        | `String!`                                                |                                                                                                   |
| `organization` | [Organization!](objects.md#organization)                 | The organization that owns this asset.                                                            |
| `type`         | [AssetType!](objects.md#assettype)                       | The asset type classification.                                                                    |
| `customFields` | [JSON!](scalars.md#json)                                 |                                                                                                   |
| `device`       | [Device](objects.md#device)                              | The primary tracking device linked to this asset. This is an alias for the `device` custom field. |
| `groups`       | [AssetGroupConnection!](objects.md#assetgroupconnection) | The groups this asset belongs to.                                                                 |

### AssetGroup

A group of assets.

**Implements:** [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field           | Type                                                             | Description                                     |
| --------------- | ---------------------------------------------------------------- | ----------------------------------------------- |
| `id`            | `ID!`                                                            |                                                 |
| `version`       | `Int!`                                                           |                                                 |
| `title`         | `String!`                                                        |                                                 |
| `organization`  | [Organization!](objects.md#organization)                         | The organization that owns this group.          |
| `type`          | [AssetGroupType!](objects.md#assetgrouptype)                     | The group type with membership constraints.     |
| `color`         | [HexColorCode](scalars.md#hexcolorcode)                          | The color for UI display in hexadecimal format. |
| `currentAssets` | [AssetConnection!](objects.md#assetconnection)                   | The assets currently in this group.             |
| `history`       | [AssetGroupItemConnection!](objects.md#assetgroupitemconnection) | The full membership history for this group.     |

### AssetGroupItem

A record of an asset's membership in a group.

**Implements:** [Node](interfaces.md#node)

| Field        | Type                                 | Description                                                                                              |
| ------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| `id`         | `ID!`                                |                                                                                                          |
| `group`      | [AssetGroup!](objects.md#assetgroup) | The group containing the asset.                                                                          |
| `asset`      | [Asset!](objects.md#asset)           | The asset in the group.                                                                                  |
| `attachedAt` | [DateTime!](scalars.md#datetime)     | The date and time when the asset was added to the group.                                                 |
| `detachedAt` | [DateTime](scalars.md#datetime)      | The date and time when the asset was removed from the group. Null means the asset is currently attached. |

## Geo objects

### GeoObject

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](interfaces.md#node), [Titled](interfaces.md#titled), [Customizable](interfaces.md#customizable), [Versioned](interfaces.md#versioned)

| Field            | Type                                                              | Description                                                                                                                                                                        |
| ---------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`             | `ID!`                                                             |                                                                                                                                                                                    |
| `version`        | `Int!`                                                            |                                                                                                                                                                                    |
| `title`          | `String!`                                                         |                                                                                                                                                                                    |
| `organization`   | [Organization!](objects.md#organization)                          | The organization that owns this geo object.                                                                                                                                        |
| `type`           | [GeoObjectType!](objects.md#geoobjecttype)                        | The geo object type classification.                                                                                                                                                |
| `geometry`       | [GeoJSON!](scalars.md#geojson)                                    | The geographic shape of this object as [GeoJSON](https://geojson.org/) geometry. This is an alias for the `geojson` custom field.                                                  |
| `customFields`   | [JSON!](scalars.md#json)                                          |                                                                                                                                                                                    |
| `containsPoints` | [\[PointContainmentResult!\]!](objects.md#pointcontainmentresult) | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

## Schedules

### Schedule

A schedule definition for work hours, maintenance windows, or other time-based rules.

**Implements:** [Node](interfaces.md#node), [Titled](interfaces.md#titled), [Customizable](interfaces.md#customizable), [Versioned](interfaces.md#versioned)

| Field          | Type                                     | Description                                                                                                          |
| -------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `id`           | `ID!`                                    |                                                                                                                      |
| `version`      | `Int!`                                   |                                                                                                                      |
| `title`        | `String!`                                |                                                                                                                      |
| `organization` | [Organization!](objects.md#organization) | The organization that owns this schedule.                                                                            |
| `type`         | [ScheduleType!](objects.md#scheduletype) | The schedule type classification.                                                                                    |
| `scheduleData` | [ScheduleData!](scalars.md#scheduledata) | The calendar and time interval definitions for this schedule. This is an alias for the `schedule_data` custom field. |
| `customFields` | [JSON!](scalars.md#json)                 |                                                                                                                      |

## Inventory

### Inventory

An inventory or warehouse record for device stock management.

**Implements:** [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                             | Description                                |
| -------------- | ------------------------------------------------ | ------------------------------------------ |
| `id`           | `ID!`                                            |                                            |
| `version`      | `Int!`                                           |                                            |
| `title`        | `String!`                                        |                                            |
| `organization` | [Organization!](objects.md#organization)         | The organization that owns this inventory. |
| `devices`      | [DeviceConnection!](objects.md#deviceconnection) | The devices assigned to this inventory.    |

## Organizations

### Organization

An organization in the hierarchy that owns entities and users.

**Implements:** [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field        | Type                                                         | Description                                                            |
| ------------ | ------------------------------------------------------------ | ---------------------------------------------------------------------- |
| `id`         | `ID!`                                                        |                                                                        |
| `version`    | `Int!`                                                       |                                                                        |
| `title`      | `String!`                                                    |                                                                        |
| `externalId` | `String`                                                     | An external system identifier for integration purposes.                |
| `isActive`   | `Boolean!`                                                   | Whether this organization is active.                                   |
| `features`   | [\[OrganizationFeature!\]!](enums.md#organizationfeature)    | The feature flags enabled for this organization.                       |
| `parent`     | [Organization](objects.md#organization)                      | The parent organization in the hierarchy. Null for root organizations. |
| `children`   | [OrganizationConnection!](objects.md#organizationconnection) | The child organizations.                                               |
| `members`    | [MemberConnection!](objects.md#memberconnection)             | The members of this organization.                                      |
| `devices`    | [DeviceConnection!](objects.md#deviceconnection)             | The devices owned by this organization.                                |
| `assets`     | [AssetConnection!](objects.md#assetconnection)               | The assets owned by this organization.                                 |
| `geoObjects` | [GeoObjectConnection!](objects.md#geoobjectconnection)       | The geographic objects owned by this organization.                     |
| `schedules`  | [ScheduleConnection!](objects.md#scheduleconnection)         | The schedules owned by this organization.                              |

## Actors

### PersonName

Structured person name components following W3C Personal Names guidance. See: https://www.w3.org/International/questions/qa-personal-names Examples by culture: - US: givenNames="John", familyNames="Smith", middleName="Robert" - Russia: givenNames="Иван", familyNames="Иванов", middleName="Петрович" (patronymic) - Spain: givenNames="Juan Carlos", familyNames="García López" (paternal + maternal) - China: givenNames="明" (Ming), familyNames="王" (Wang) — note: family name first in native order - Iceland: givenNames="Björk", familyNames="Guðmundsdóttir" (patronymic as family name)

| Field         | Type      | Description                                                                                     |
| ------------- | --------- | ----------------------------------------------------------------------------------------------- |
| `givenNames`  | `String!` | The given name(s), also known as first name(s). May contain multiple names separated by spaces. |
| `familyNames` | `String!` | The family name(s), also known as surname(s) or last name(s). May contain multiple names.       |
| `middleName`  | `String`  | The middle name, patronymic, or additional name component.                                      |
| `fullName`    | `String!` | The full name formatted according to the user's locale preferences.                             |

### User

A human user account authenticated via an identity provider.

**Implements:** [Actor](interfaces.md#actor), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field                | Type                                             | Description                                                                       |
| -------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------- |
| `id`                 | `ID!`                                            |                                                                                   |
| `version`            | `Int!`                                           |                                                                                   |
| `title`              | `String!`                                        | The display name for the user. This is the user's full name for display purposes. |
| `name`               | [PersonName!](objects.md#personname)             | The structured name components from the identity provider.                        |
| `identityProvider`   | `String!`                                        | The identity provider name (keycloak, auth0, okta, etc.).                         |
| `identityProviderId` | `String!`                                        | The user's unique ID in the identity provider.                                    |
| `email`              | [EmailAddress!](scalars.md#emailaddress)         | The user's primary email address.                                                 |
| `locale`             | [Locale](scalars.md#locale)                      | The user's preferred locale.                                                      |
| `externalId`         | `String`                                         | An external system identifier for integration purposes.                           |
| `isActive`           | `Boolean!`                                       | Whether this user account is active.                                              |
| `memberships`        | [MemberConnection!](objects.md#memberconnection) | The organization memberships for this user.                                       |

### Member

A user's membership in an organization.

**Implements:** [Node](interfaces.md#node), [Customizable](interfaces.md#customizable), [Versioned](interfaces.md#versioned)

| Field          | Type                                     | Description                                                        |
| -------------- | ---------------------------------------- | ------------------------------------------------------------------ |
| `id`           | `ID!`                                    |                                                                    |
| `version`      | `Int!`                                   |                                                                    |
| `user`         | [User!](objects.md#user)                 | The user.                                                          |
| `organization` | [Organization!](objects.md#organization) | The organization the user belongs to.                              |
| `isActive`     | `Boolean!`                               | Whether this membership is active.                                 |
| `assignedAt`   | [DateTime!](scalars.md#datetime)         | The date and time when the user was assigned to this organization. |
| `customFields` | [JSON!](scalars.md#json)                 | Membership-specific custom fields such as position and department. |

### Integration

An external system integration with API access.

**Implements:** [Actor](interfaces.md#actor), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field           | Type                                     | Description                                          |
| --------------- | ---------------------------------------- | ---------------------------------------------------- |
| `id`            | `ID!`                                    |                                                      |
| `version`       | `Int!`                                   |                                                      |
| `title`         | `String!`                                |                                                      |
| `organization`  | [Organization!](objects.md#organization) | The organization this integration belongs to.        |
| `credentialRef` | `String`                                 | A reference to credentials stored in a secure vault. |
| `isActive`      | `Boolean!`                               | Whether this integration is active.                  |

## Access control

### ActorRole

An assignment of a role to an actor.

**Implements:** [Node](interfaces.md#node)

| Field        | Type                             | Description                                                                |
| ------------ | -------------------------------- | -------------------------------------------------------------------------- |
| `id`         | `ID!`                            |                                                                            |
| `actor`      | [Actor!](interfaces.md#actor)    | The actor receiving the role.                                              |
| `role`       | [Role!](objects.md#role)         | The role being assigned.                                                   |
| `assignedAt` | [DateTime!](scalars.md#datetime) | The date and time when the role was assigned.                              |
| `assignedBy` | [Actor](interfaces.md#actor)     | The actor who assigned the role.                                           |
| `expireDate` | [DateTime](scalars.md#datetime)  | The date and time when the role expires. Null means the role is permanent. |

### RolePermission

A permission granted to a role.

**Implements:** [Node](interfaces.md#node)

| Field             | Type                                                | Description                                                                             |
| ----------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`              | `ID!`                                               |                                                                                         |
| `role`            | [Role!](objects.md#role)                            | The role receiving the permission.                                                      |
| `permissionScope` | [PermissionScope!](objects.md#permissionscope)      | The permission scope being granted.                                                     |
| `targetEntityId`  | `ID`                                                | The specific entity ID this permission applies to. Null means all entities of the type. |
| `actions`         | [\[ActionPermission!\]!](enums.md#actionpermission) | The actions allowed by this permission.                                                 |
| `grantedAt`       | [DateTime!](scalars.md#datetime)                    | The date and time when the permission was granted.                                      |
| `grantedBy`       | [Actor!](interfaces.md#actor)                       | The actor who granted the permission.                                                   |

### UserScope

A whitelist filter that restricts an actor's access to specific entities. When present, effective permissions = role permissions ∩ user scope.

**Implements:** [Node](interfaces.md#node)

| Field             | Type                                                | Description                                  |
| ----------------- | --------------------------------------------------- | -------------------------------------------- |
| `id`              | `ID!`                                               |                                              |
| `actor`           | [Actor!](interfaces.md#actor)                       | The actor being restricted.                  |
| `permissionScope` | [PermissionScope!](objects.md#permissionscope)      | The permission scope being filtered.         |
| `targetEntityId`  | `ID!`                                               | The specific entity the actor can access.    |
| `actions`         | [\[ActionPermission!\]!](enums.md#actionpermission) | The actions allowed on this specific entity. |

## Custom fields

### CustomFieldDefinition

A custom field definition that specifies the metadata for a custom field. Note: The `fieldType` property is immutable after creation. To change the field type, delete the definition and create a new one.

**Implements:** [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field              | Type                                      | Description                                                                                                                   |
| ------------------ | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`               | `ID!`                                     |                                                                                                                               |
| `version`          | `Int!`                                    |                                                                                                                               |
| `title`            | `String!`                                 | The human-readable display name.                                                                                              |
| `code`             | [Code!](scalars.md#code)                  | The machine-readable code, unique per owner and organization.                                                                 |
| `description`      | `String`                                  | A description of the field for UI hints.                                                                                      |
| `order`            | `Int!`                                    | The display order within the owner context.                                                                                   |
| `organization`     | [Organization](objects.md#organization)   | The organization that owns this definition. Null for system-level fields.                                                     |
| `owner`            | [CatalogItem!](interfaces.md#catalogitem) | The owner catalog item: EntityType for system fields, or a specific type like AssetType for type-specific fields.             |
| `targetEntityType` | [EntityType!](objects.md#entitytype)      | The target entity type this field applies to.                                                                                 |
| `fieldType`        | [FieldType!](enums.md#fieldtype)          | The data type determining validation rules and UI rendering. This property is immutable and cannot be changed after creation. |
| `params`           | [FieldParams!](interfaces.md#fieldparams) | The type-specific parameters for validation, defaults, and options.                                                           |

### FieldParamsString

Parameters for STRING field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type       | Description                                      |
| -------------- | ---------- | ------------------------------------------------ |
| `isRequired`   | `Boolean!` |                                                  |
| `minLength`    | `Int`      | The minimum character length.                    |
| `maxLength`    | `Int`      | The maximum character length.                    |
| `defaultValue` | `String`   | The default value.                               |
| `trim`         | `Boolean!` | Whether to trim leading and trailing whitespace. |

### FieldParamsText

Parameters for TEXT field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type       | Description                                      |
| -------------- | ---------- | ------------------------------------------------ |
| `isRequired`   | `Boolean!` |                                                  |
| `maxLength`    | `Int`      | The maximum character length.                    |
| `defaultValue` | `String`   | The default value.                               |
| `trim`         | `Boolean!` | Whether to trim leading and trailing whitespace. |

### FieldParamsNumber

Parameters for NUMBER field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type       | Description                |
| -------------- | ---------- | -------------------------- |
| `isRequired`   | `Boolean!` |                            |
| `min`          | `Float`    | The minimum allowed value. |
| `max`          | `Float`    | The maximum allowed value. |
| `precision`    | `Int`      | The decimal precision.     |
| `defaultValue` | `Float`    | The default value.         |

### FieldParamsBoolean

Parameters for BOOLEAN field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type       | Description        |
| -------------- | ---------- | ------------------ |
| `isRequired`   | `Boolean!` |                    |
| `defaultValue` | `Boolean`  | The default value. |

### FieldParamsDate

Parameters for DATE field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type                    | Description        |
| -------------- | ----------------------- | ------------------ |
| `isRequired`   | `Boolean!`              |                    |
| `defaultValue` | [Date](scalars.md#date) | The default value. |

### FieldParamsDatetime

Parameters for DATETIME field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type                            | Description        |
| -------------- | ------------------------------- | ------------------ |
| `isRequired`   | `Boolean!`                      |                    |
| `defaultValue` | [DateTime](scalars.md#datetime) | The default value. |

### FieldParamsGeojson

Parameters for GEOJSON field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field          | Type                                                     | Description                                                   |
| -------------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| `isRequired`   | `Boolean!`                                               |                                                               |
| `allowedTypes` | [\[GeoJsonGeometryType!\]](enums.md#geojsongeometrytype) | The allowed geometry types. Null means all types are allowed. |

### FieldParamsSchedule

Parameters for SCHEDULE field type.

**Implements:** [FieldParams](interfaces.md#fieldparams)

| Field        | Type       | Description |
| ------------ | ---------- | ----------- |
| `isRequired` | `Boolean!` |             |

### FieldParamsOptions

Parameters for OPTIONS field type.

**Implements:** [FieldParams](interfaces.md#fieldparams), [MultiValue](interfaces.md#multivalue)

| Field          | Type                                        | Description                           |
| -------------- | ------------------------------------------- | ------------------------------------- |
| `isRequired`   | `Boolean!`                                  |                                       |
| `isMulti`      | `Boolean!`                                  |                                       |
| `options`      | [\[FieldOption!\]!](objects.md#fieldoption) | The available options to choose from. |
| `defaultValue` | [Code](scalars.md#code)                     | The default option code.              |

### FieldOption

A single option in an OPTIONS field.

| Field         | Type                     | Description                                                                 |
| ------------- | ------------------------ | --------------------------------------------------------------------------- |
| `code`        | [Code!](scalars.md#code) | The unique code for this option within the field.                           |
| `label`       | `String!`                | The display label.                                                          |
| `description` | `String`                 | A description of the option.                                                |
| `isArchived`  | `Boolean!`               | Whether this option is archived and should not be shown for new selections. |

### FieldParamsDevice

Parameters for DEVICE field type.

**Implements:** [FieldParams](interfaces.md#fieldparams), [MultiValue](interfaces.md#multivalue)

| Field        | Type       | Description |
| ------------ | ---------- | ----------- |
| `isRequired` | `Boolean!` |             |
| `isMulti`    | `Boolean!` |             |

### FieldParamsReference

Parameters for REFERENCE field type.

**Implements:** [FieldParams](interfaces.md#fieldparams), [MultiValue](interfaces.md#multivalue)

| Field               | Type                     | Description                                  |
| ------------------- | ------------------------ | -------------------------------------------- |
| `isRequired`        | `Boolean!`               |                                              |
| `isMulti`           | `Boolean!`               |                                              |
| `refEntityTypeCode` | [Code!](scalars.md#code) | The entity type code that can be referenced. |

### FieldParamsCatalog

Parameters for CATALOG field type.

**Implements:** [FieldParams](interfaces.md#fieldparams), [MultiValue](interfaces.md#multivalue)

| Field            | Type                     | Description                                       |
| ---------------- | ------------------------ | ------------------------------------------------- |
| `isRequired`     | `Boolean!`               |                                                   |
| `isMulti`        | `Boolean!`               |                                                   |
| `refCatalogCode` | [Code!](scalars.md#code) | The catalog code that items can be selected from. |
| `defaultValue`   | [Code](scalars.md#code)  | The default item code.                            |

### FieldParamsTag

Parameters for TAG field type.

**Implements:** [FieldParams](interfaces.md#fieldparams), [MultiValue](interfaces.md#multivalue)

| Field          | Type                    | Description           |
| -------------- | ----------------------- | --------------------- |
| `isRequired`   | `Boolean!`              |                       |
| `isMulti`      | `Boolean!`              |                       |
| `defaultValue` | [Code](scalars.md#code) | The default tag code. |

## Audit

### AuditEvent

An audit log entry recording an event that occurred in the system.

**Implements:** [Node](interfaces.md#node)

| Field           | Type                                       | Description                                                         |
| --------------- | ------------------------------------------ | ------------------------------------------------------------------- |
| `id`            | `ID!`                                      |                                                                     |
| `organization`  | [Organization](objects.md#organization)    | The organization context. Null for system events.                   |
| `actor`         | [Actor](interfaces.md#actor)               | The actor who triggered the event.                                  |
| `ipAddress`     | `String`                                   | The client IP address.                                              |
| `userAgent`     | `String`                                   | The client User-Agent string.                                       |
| `sourceType`    | [SourceType!](enums.md#sourcetype)         | The source type of the request.                                     |
| `traceId`       | `String`                                   | The distributed tracing ID (32 hex characters) for log correlation. |
| `aggregateType` | [Code](scalars.md#code)                    | The type of entity affected.                                        |
| `aggregateId`   | `ID`                                       | The ID of the affected entity.                                      |
| `eventType`     | [AuditEventType!](enums.md#auditeventtype) | The type of event that occurred.                                    |
| `eventData`     | [JSON](scalars.md#json)                    | The event payload with details such as changed fields.              |
| `occurredAt`    | [DateTime!](scalars.md#datetime)           | The date and time when the event occurred.                          |

## Pagination

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

| Field       | Type                                       | Description                             |
| ----------- | ------------------------------------------ | --------------------------------------- |
| `count`     | `Int!`                                     | The count of items matching the filter. |
| `precision` | [CountPrecision!](enums.md#countprecision) | The precision level of the count value. |

### CatalogItemConnection

A paginated list of CatalogItem items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                | Description                                                |
| ---------- | --------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[CatalogItemEdge!\]!](objects.md#catalogitemedge) | A list of edges.                                           |
| `nodes`    | [\[CatalogItem!\]!](interfaces.md#catalogitem)      | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                    | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                   | The total count of items matching the filter.              |

### CatalogItemEdge

An edge in the CatalogItem connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                      | Description                              |
| -------- | ----------------------------------------- | ---------------------------------------- |
| `cursor` | `String!`                                 | An opaque cursor for this edge.          |
| `node`   | [CatalogItem!](interfaces.md#catalogitem) | The catalog item at the end of the edge. |

### UserCatalogItemConnection

A paginated list of UserCatalogItem items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                        | Description                                                |
| ---------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[UserCatalogItemEdge!\]!](objects.md#usercatalogitemedge) | A list of edges.                                           |
| `nodes`    | [\[UserCatalogItem!\]!](objects.md#usercatalogitem)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                            | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                           | The total count of items matching the filter.              |

### UserCatalogItemEdge

An edge in the UserCatalogItem connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                           | Description                                   |
| -------- | ---------------------------------------------- | --------------------------------------------- |
| `cursor` | `String!`                                      | An opaque cursor for this edge.               |
| `node`   | [UserCatalogItem!](objects.md#usercatalogitem) | The user catalog item at the end of the edge. |

### OrganizationConnection

A paginated list of Organization items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                  | Description                                                |
| ---------- | ----------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[OrganizationEdge!\]!](objects.md#organizationedge) | A list of edges.                                           |
| `nodes`    | [\[Organization!\]!](objects.md#organization)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                      | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                     | The total count of items matching the filter.              |

### OrganizationEdge

An edge in the Organization connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                     | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `cursor` | `String!`                                | An opaque cursor for this edge.          |
| `node`   | [Organization!](objects.md#organization) | The organization at the end of the edge. |

### UserConnection

A paginated list of User items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                  | Description                                                |
| ---------- | ------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[UserEdge!\]!](objects.md#useredge) | A list of edges.                                           |
| `nodes`    | [\[User!\]!](objects.md#user)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)      | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)     | The total count of items matching the filter.              |

### UserEdge

An edge in the User connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                     | Description                      |
| -------- | ------------------------ | -------------------------------- |
| `cursor` | `String!`                | An opaque cursor for this edge.  |
| `node`   | [User!](objects.md#user) | The user at the end of the edge. |

### MemberConnection

A paginated list of Member items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                      | Description                                                |
| ---------- | ----------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[MemberEdge!\]!](objects.md#memberedge) | A list of edges.                                           |
| `nodes`    | [\[Member!\]!](objects.md#member)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)          | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)         | The total count of items matching the filter.              |

### MemberEdge

An edge in the Member connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `cursor` | `String!`                    | An opaque cursor for this edge.    |
| `node`   | [Member!](objects.md#member) | The member at the end of the edge. |

### IntegrationConnection

A paginated list of Integration items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                | Description                                                |
| ---------- | --------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[IntegrationEdge!\]!](objects.md#integrationedge) | A list of edges.                                           |
| `nodes`    | [\[Integration!\]!](objects.md#integration)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                    | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                   | The total count of items matching the filter.              |

### IntegrationEdge

An edge in the Integration connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                   | Description                             |
| -------- | -------------------------------------- | --------------------------------------- |
| `cursor` | `String!`                              | An opaque cursor for this edge.         |
| `node`   | [Integration!](objects.md#integration) | The integration at the end of the edge. |

### DeviceConnection

A paginated list of Device items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                      | Description                                                |
| ---------- | ----------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[DeviceEdge!\]!](objects.md#deviceedge) | A list of edges.                                           |
| `nodes`    | [\[Device!\]!](objects.md#device)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)          | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)         | The total count of items matching the filter.              |

### DeviceEdge

An edge in the Device connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `cursor` | `String!`                    | An opaque cursor for this edge.    |
| `node`   | [Device!](objects.md#device) | The device at the end of the edge. |

### AssetConnection

A paginated list of Asset items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                    | Description                                                |
| ---------- | --------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[AssetEdge!\]!](objects.md#assetedge) | A list of edges.                                           |
| `nodes`    | [\[Asset!\]!](objects.md#asset)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)        | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)       | The total count of items matching the filter.              |

### AssetEdge

An edge in the Asset connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                       | Description                       |
| -------- | -------------------------- | --------------------------------- |
| `cursor` | `String!`                  | An opaque cursor for this edge.   |
| `node`   | [Asset!](objects.md#asset) | The asset at the end of the edge. |

### AssetGroupConnection

A paginated list of AssetGroup items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                              | Description                                                |
| ---------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[AssetGroupEdge!\]!](objects.md#assetgroupedge) | A list of edges.                                           |
| `nodes`    | [\[AssetGroup!\]!](objects.md#assetgroup)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                  | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                 | The total count of items matching the filter.              |

### AssetGroupEdge

An edge in the AssetGroup connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                 | Description                             |
| -------- | ------------------------------------ | --------------------------------------- |
| `cursor` | `String!`                            | An opaque cursor for this edge.         |
| `node`   | [AssetGroup!](objects.md#assetgroup) | The asset group at the end of the edge. |

### AssetGroupItemConnection

A paginated list of AssetGroupItem items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                      | Description                                                |
| ---------- | --------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[AssetGroupItemEdge!\]!](objects.md#assetgroupitemedge) | A list of edges.                                           |
| `nodes`    | [\[AssetGroupItem!\]!](objects.md#assetgroupitem)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                          | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                         | The total count of items matching the filter.              |

### AssetGroupItemEdge

An edge in the AssetGroupItem connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                         | Description                                  |
| -------- | -------------------------------------------- | -------------------------------------------- |
| `cursor` | `String!`                                    | An opaque cursor for this edge.              |
| `node`   | [AssetGroupItem!](objects.md#assetgroupitem) | The asset group item at the end of the edge. |

### InventoryConnection

A paginated list of Inventory items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                            | Description                                                |
| ---------- | ----------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[InventoryEdge!\]!](objects.md#inventoryedge) | A list of edges.                                           |
| `nodes`    | [\[Inventory!\]!](objects.md#inventory)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)               | The total count of items matching the filter.              |

### InventoryEdge

An edge in the Inventory connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                               | Description                           |
| -------- | ---------------------------------- | ------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.       |
| `node`   | [Inventory!](objects.md#inventory) | The inventory at the end of the edge. |

### GeoObjectConnection

A paginated list of GeoObject items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                            | Description                                                |
| ---------- | ----------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[GeoObjectEdge!\]!](objects.md#geoobjectedge) | A list of edges.                                           |
| `nodes`    | [\[GeoObject!\]!](objects.md#geoobject)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)               | The total count of items matching the filter.              |

### GeoObjectEdge

An edge in the GeoObject connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                               | Description                            |
| -------- | ---------------------------------- | -------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.        |
| `node`   | [GeoObject!](objects.md#geoobject) | The geo object at the end of the edge. |

### ScheduleConnection

A paginated list of Schedule items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                          | Description                                                |
| ---------- | --------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[ScheduleEdge!\]!](objects.md#scheduleedge) | A list of edges.                                           |
| `nodes`    | [\[Schedule!\]!](objects.md#schedule)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)              | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)             | The total count of items matching the filter.              |

### ScheduleEdge

An edge in the Schedule connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                             | Description                          |
| -------- | -------------------------------- | ------------------------------------ |
| `cursor` | `String!`                        | An opaque cursor for this edge.      |
| `node`   | [Schedule!](objects.md#schedule) | The schedule at the end of the edge. |

### AuditEventConnection

A paginated list of AuditEvent items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                              | Description                                                |
| ---------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[AuditEventEdge!\]!](objects.md#auditeventedge) | A list of edges.                                           |
| `nodes`    | [\[AuditEvent!\]!](objects.md#auditevent)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                  | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                 | The total count of items matching the filter.              |

### AuditEventEdge

An edge in the AuditEvent connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                 | Description                             |
| -------- | ------------------------------------ | --------------------------------------- |
| `cursor` | `String!`                            | An opaque cursor for this edge.         |
| `node`   | [AuditEvent!](objects.md#auditevent) | The audit event at the end of the edge. |

### DeviceInventoryRelationConnection

A paginated list of DeviceInventoryRelation items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                                        | Description                                                |
| ---------- | --------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[DeviceInventoryRelationEdge!\]!](objects.md#deviceinventoryrelationedge) | A list of edges.                                           |
| `nodes`    | [\[DeviceInventoryRelation!\]!](objects.md#deviceinventoryrelation)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                                            | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                                           | The total count of items matching the filter.              |

### DeviceInventoryRelationEdge

An edge in the DeviceInventoryRelation connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                                           | Description                                           |
| -------- | -------------------------------------------------------------- | ----------------------------------------------------- |
| `cursor` | `String!`                                                      | An opaque cursor for this edge.                       |
| `node`   | [DeviceInventoryRelation!](objects.md#deviceinventoryrelation) | The device inventory relation at the end of the edge. |

### CatalogConnection

A paginated list of Catalog items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                        | Description                                                |
| ---------- | ------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[CatalogEdge!\]!](objects.md#catalogedge) | A list of edges.                                           |
| `nodes`    | [\[Catalog!\]!](objects.md#catalog)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)            | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)           | The total count of items matching the filter.              |

### CatalogEdge

An edge in the Catalog connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                           | Description                         |
| -------- | ------------------------------ | ----------------------------------- |
| `cursor` | `String!`                      | An opaque cursor for this edge.     |
| `node`   | [Catalog!](objects.md#catalog) | The catalog at the end of the edge. |

### DeviceTypeConnection

A paginated list of DeviceType items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                              | Description                                                |
| ---------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[DeviceTypeEdge!\]!](objects.md#devicetypeedge) | A list of edges.                                           |
| `nodes`    | [\[DeviceType!\]!](objects.md#devicetype)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                  | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                 | The total count of items matching the filter.              |

### DeviceTypeEdge

An edge in the DeviceType connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                 | Description                             |
| -------- | ------------------------------------ | --------------------------------------- |
| `cursor` | `String!`                            | An opaque cursor for this edge.         |
| `node`   | [DeviceType!](objects.md#devicetype) | The device type at the end of the edge. |

### DeviceStatusConnection

A paginated list of DeviceStatus items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                  | Description                                                |
| ---------- | ----------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[DeviceStatusEdge!\]!](objects.md#devicestatusedge) | A list of edges.                                           |
| `nodes`    | [\[DeviceStatus!\]!](objects.md#devicestatus)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                      | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                     | The total count of items matching the filter.              |

### DeviceStatusEdge

An edge in the DeviceStatus connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                     | Description                               |
| -------- | ---------------------------------------- | ----------------------------------------- |
| `cursor` | `String!`                                | An opaque cursor for this edge.           |
| `node`   | [DeviceStatus!](objects.md#devicestatus) | The device status at the end of the edge. |

### DeviceModelConnection

A paginated list of DeviceModel items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                | Description                                                |
| ---------- | --------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[DeviceModelEdge!\]!](objects.md#devicemodeledge) | A list of edges.                                           |
| `nodes`    | [\[DeviceModel!\]!](objects.md#devicemodel)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                    | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                   | The total count of items matching the filter.              |

### DeviceModelEdge

An edge in the DeviceModel connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                   | Description                              |
| -------- | -------------------------------------- | ---------------------------------------- |
| `cursor` | `String!`                              | An opaque cursor for this edge.          |
| `node`   | [DeviceModel!](objects.md#devicemodel) | The device model at the end of the edge. |

### AssetTypeConnection

A paginated list of AssetType items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                            | Description                                                |
| ---------- | ----------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[AssetTypeEdge!\]!](objects.md#assettypeedge) | A list of edges.                                           |
| `nodes`    | [\[AssetType!\]!](objects.md#assettype)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)               | The total count of items matching the filter.              |

### AssetTypeEdge

An edge in the AssetType connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                               | Description                            |
| -------- | ---------------------------------- | -------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.        |
| `node`   | [AssetType!](objects.md#assettype) | The asset type at the end of the edge. |

### AssetGroupTypeConnection

A paginated list of AssetGroupType items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                      | Description                                                |
| ---------- | --------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[AssetGroupTypeEdge!\]!](objects.md#assetgrouptypeedge) | A list of edges.                                           |
| `nodes`    | [\[AssetGroupType!\]!](objects.md#assetgrouptype)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                          | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                         | The total count of items matching the filter.              |

### AssetGroupTypeEdge

An edge in the AssetGroupType connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                         | Description                                  |
| -------- | -------------------------------------------- | -------------------------------------------- |
| `cursor` | `String!`                                    | An opaque cursor for this edge.              |
| `node`   | [AssetGroupType!](objects.md#assetgrouptype) | The asset group type at the end of the edge. |

### GeoObjectTypeConnection

A paginated list of GeoObjectType items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                    | Description                                                |
| ---------- | ------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[GeoObjectTypeEdge!\]!](objects.md#geoobjecttypeedge) | A list of edges.                                           |
| `nodes`    | [\[GeoObjectType!\]!](objects.md#geoobjecttype)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                        | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                       | The total count of items matching the filter.              |

### GeoObjectTypeEdge

An edge in the GeoObjectType connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                       | Description                                 |
| -------- | ------------------------------------------ | ------------------------------------------- |
| `cursor` | `String!`                                  | An opaque cursor for this edge.             |
| `node`   | [GeoObjectType!](objects.md#geoobjecttype) | The geo object type at the end of the edge. |

### ScheduleTypeConnection

A paginated list of ScheduleType items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                  | Description                                                |
| ---------- | ----------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[ScheduleTypeEdge!\]!](objects.md#scheduletypeedge) | A list of edges.                                           |
| `nodes`    | [\[ScheduleType!\]!](objects.md#scheduletype)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                      | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                     | The total count of items matching the filter.              |

### ScheduleTypeEdge

An edge in the ScheduleType connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                     | Description                               |
| -------- | ---------------------------------------- | ----------------------------------------- |
| `cursor` | `String!`                                | An opaque cursor for this edge.           |
| `node`   | [ScheduleType!](objects.md#scheduletype) | The schedule type at the end of the edge. |

### RoleConnection

A paginated list of Role items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                  | Description                                                |
| ---------- | ------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[RoleEdge!\]!](objects.md#roleedge) | A list of edges.                                           |
| `nodes`    | [\[Role!\]!](objects.md#role)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)      | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)     | The total count of items matching the filter.              |

### RoleEdge

An edge in the Role connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                     | Description                      |
| -------- | ------------------------ | -------------------------------- |
| `cursor` | `String!`                | An opaque cursor for this edge.  |
| `node`   | [Role!](objects.md#role) | The role at the end of the edge. |

### TagConnection

A paginated list of Tag items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                | Description                                                |
| ---------- | ----------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[TagEdge!\]!](objects.md#tagedge) | A list of edges.                                           |
| `nodes`    | [\[Tag!\]!](objects.md#tag)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)    | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)   | The total count of items matching the filter.              |

### TagEdge

An edge in the Tag connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                   | Description                     |
| -------- | ---------------------- | ------------------------------- |
| `cursor` | `String!`              | An opaque cursor for this edge. |
| `node`   | [Tag!](objects.md#tag) | The tag at the end of the edge. |

### ActorRoleConnection

A paginated list of ActorRole items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                            | Description                                                |
| ---------- | ----------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[ActorRoleEdge!\]!](objects.md#actorroleedge) | A list of edges.                                           |
| `nodes`    | [\[ActorRole!\]!](objects.md#actorrole)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)               | The total count of items matching the filter.              |

### ActorRoleEdge

An edge in the ActorRole connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                               | Description                            |
| -------- | ---------------------------------- | -------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.        |
| `node`   | [ActorRole!](objects.md#actorrole) | The actor role at the end of the edge. |

### RolePermissionConnection

A paginated list of RolePermission items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                                      | Description                                                |
| ---------- | --------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[RolePermissionEdge!\]!](objects.md#rolepermissionedge) | A list of edges.                                           |
| `nodes`    | [\[RolePermission!\]!](objects.md#rolepermission)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                          | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)                         | The total count of items matching the filter.              |

### RolePermissionEdge

An edge in the RolePermission connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                                         | Description                                 |
| -------- | -------------------------------------------- | ------------------------------------------- |
| `cursor` | `String!`                                    | An opaque cursor for this edge.             |
| `node`   | [RolePermission!](objects.md#rolepermission) | The role permission at the end of the edge. |

### UserScopeConnection

A paginated list of UserScope items.

**Implements:** [Connection](interfaces.md#connection)

| Field      | Type                                            | Description                                                |
| ---------- | ----------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | [\[UserScopeEdge!\]!](objects.md#userscopeedge) | A list of edges.                                           |
| `nodes`    | [\[UserScope!\]!](objects.md#userscope)         | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)                | Information about the current page.                        |
| `total`    | [CountInfo](objects.md#countinfo)               | The total count of items matching the filter.              |

### UserScopeEdge

An edge in the UserScope connection.

**Implements:** [Edge](interfaces.md#edge)

| Field    | Type                               | Description                            |
| -------- | ---------------------------------- | -------------------------------------- |
| `cursor` | `String!`                          | An opaque cursor for this edge.        |
| `node`   | [UserScope!](objects.md#userscope) | The user scope at the end of the edge. |

## Mutation payloads

### DeletePayload

The result of a delete mutation.

| Field       | Type  | Description                   |
| ----------- | ----- | ----------------------------- |
| `deletedId` | `ID!` | The ID of the deleted entity. |

### DevicePayload

The result of a device mutation.

| Field    | Type                         | Description                    |
| -------- | ---------------------------- | ------------------------------ |
| `device` | [Device!](objects.md#device) | The created or updated device. |

### AssetPayload

The result of an asset mutation.

| Field   | Type                       | Description                   |
| ------- | -------------------------- | ----------------------------- |
| `asset` | [Asset!](objects.md#asset) | The created or updated asset. |

### AssetGroupPayload

The result of an asset group mutation.

| Field        | Type                                 | Description                         |
| ------------ | ------------------------------------ | ----------------------------------- |
| `assetGroup` | [AssetGroup!](objects.md#assetgroup) | The created or updated asset group. |

### GeoObjectPayload

The result of a geo object mutation.

| Field       | Type                               | Description                        |
| ----------- | ---------------------------------- | ---------------------------------- |
| `geoObject` | [GeoObject!](objects.md#geoobject) | The created or updated geo object. |

### SchedulePayload

The result of a schedule mutation.

| Field      | Type                             | Description                      |
| ---------- | -------------------------------- | -------------------------------- |
| `schedule` | [Schedule!](objects.md#schedule) | The created or updated schedule. |

### InventoryPayload

The result of an inventory mutation.

| Field       | Type                               | Description                       |
| ----------- | ---------------------------------- | --------------------------------- |
| `inventory` | [Inventory!](objects.md#inventory) | The created or updated inventory. |

### OrganizationPayload

The result of an organization mutation.

| Field          | Type                                     | Description                          |
| -------------- | ---------------------------------------- | ------------------------------------ |
| `organization` | [Organization!](objects.md#organization) | The created or updated organization. |

### UserPayload

The result of a user profile mutation.

| Field  | Type                     | Description       |
| ------ | ------------------------ | ----------------- |
| `user` | [User!](objects.md#user) | The updated user. |

### MemberPayload

The result of a membership mutation.

| Field    | Type                         | Description                        |
| -------- | ---------------------------- | ---------------------------------- |
| `member` | [Member!](objects.md#member) | The created or updated membership. |

### IntegrationPayload

The result of an integration mutation.

| Field         | Type                                   | Description                         |
| ------------- | -------------------------------------- | ----------------------------------- |
| `integration` | [Integration!](objects.md#integration) | The created or updated integration. |

### CustomFieldDefinitionPayload

The result of a custom field definition mutation.

| Field                   | Type                                                       | Description                                     |
| ----------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| `customFieldDefinition` | [CustomFieldDefinition!](objects.md#customfielddefinition) | The created or updated custom field definition. |

### DeviceIdentifierPayload

The result of a device identifier mutation.

| Field              | Type                                             | Description                  |
| ------------------ | ------------------------------------------------ | ---------------------------- |
| `deviceIdentifier` | [DeviceIdentifier!](objects.md#deviceidentifier) | The added device identifier. |

### AssetGroupItemPayload

The result of an asset group item mutation.

| Field            | Type                                         | Description                          |
| ---------------- | -------------------------------------------- | ------------------------------------ |
| `assetGroupItem` | [AssetGroupItem!](objects.md#assetgroupitem) | The created group membership record. |

### DeviceInventoryRelationPayload

The result of a device inventory link mutation.

| Field                     | Type                                                           | Description                       |
| ------------------------- | -------------------------------------------------------------- | --------------------------------- |
| `deviceInventoryRelation` | [DeviceInventoryRelation!](objects.md#deviceinventoryrelation) | The created inventory assignment. |

### DeviceRelationPayload

The result of a device relation mutation.

| Field            | Type                                         | Description                      |
| ---------------- | -------------------------------------------- | -------------------------------- |
| `deviceRelation` | [DeviceRelation!](objects.md#devicerelation) | The created device relationship. |

### ActorRolePayload

The result of a role assignment mutation.

| Field       | Type                               | Description                  |
| ----------- | ---------------------------------- | ---------------------------- |
| `actorRole` | [ActorRole!](objects.md#actorrole) | The created role assignment. |

### RolePermissionPayload

The result of a permission grant mutation.

| Field            | Type                                         | Description             |
| ---------------- | -------------------------------------------- | ----------------------- |
| `rolePermission` | [RolePermission!](objects.md#rolepermission) | The created permission. |

### UserScopePayload

The result of a user scope mutation.

| Field       | Type                               | Description                         |
| ----------- | ---------------------------------- | ----------------------------------- |
| `userScope` | [UserScope!](objects.md#userscope) | The created user scope restriction. |

### DeviceTypePayload

The result of a device type mutation.

| Field        | Type                                 | Description                         |
| ------------ | ------------------------------------ | ----------------------------------- |
| `deviceType` | [DeviceType!](objects.md#devicetype) | The created or updated device type. |

### DeviceStatusPayload

The result of a device status mutation.

| Field          | Type                                     | Description                           |
| -------------- | ---------------------------------------- | ------------------------------------- |
| `deviceStatus` | [DeviceStatus!](objects.md#devicestatus) | The created or updated device status. |

### AssetTypePayload

The result of an asset type mutation.

| Field       | Type                               | Description                        |
| ----------- | ---------------------------------- | ---------------------------------- |
| `assetType` | [AssetType!](objects.md#assettype) | The created or updated asset type. |

### AssetGroupTypePayload

The result of an asset group type mutation.

| Field            | Type                                         | Description                              |
| ---------------- | -------------------------------------------- | ---------------------------------------- |
| `assetGroupType` | [AssetGroupType!](objects.md#assetgrouptype) | The created or updated asset group type. |

### GeoObjectTypePayload

The result of a geo object type mutation.

| Field           | Type                                       | Description                             |
| --------------- | ------------------------------------------ | --------------------------------------- |
| `geoObjectType` | [GeoObjectType!](objects.md#geoobjecttype) | The created or updated geo object type. |

### ScheduleTypePayload

The result of a schedule type mutation.

| Field          | Type                                     | Description                           |
| -------------- | ---------------------------------------- | ------------------------------------- |
| `scheduleType` | [ScheduleType!](objects.md#scheduletype) | The created or updated schedule type. |

### TagPayload

The result of a tag mutation.

| Field | Type                   | Description                 |
| ----- | ---------------------- | --------------------------- |
| `tag` | [Tag!](objects.md#tag) | The created or updated tag. |

### RolePayload

The result of a role mutation.

| Field  | Type                     | Description                  |
| ------ | ------------------------ | ---------------------------- |
| `role` | [Role!](objects.md#role) | The created or updated role. |

### UserCatalogItemPayload

The result of a user catalog item mutation.

| Field  | Type                                           | Description                               |
| ------ | ---------------------------------------------- | ----------------------------------------- |
| `item` | [UserCatalogItem!](objects.md#usercatalogitem) | The created or updated user catalog item. |

## Catalog items

### CatalogItemMeta

Metadata about a catalog item.

| Field             | Type                                             | Description                                                                                          |
| ----------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `description`     | `String`                                         | A description of the catalog item. Can be localized.                                                 |
| `origin`          | [CatalogItemOrigin!](enums.md#catalogitemorigin) | The origin indicating how this item was created.                                                     |
| `canBeDeleted`    | `Boolean!`                                       | Whether this item can be deleted. Returns `false` if the item has dependencies or is system-managed. |
| `hidden`          | `Boolean!`                                       | Whether this item is hidden from regular UI lists.                                                   |
| `textColor`       | [HexColorCode](scalars.md#hexcolorcode)          | The text color for UI display.                                                                       |
| `backgroundColor` | [HexColorCode](scalars.md#hexcolorcode)          | The background color for UI display.                                                                 |
| `icon`            | `String`                                         | A relative URL to the icon for this item.                                                            |

### Module

A system module that groups related functionality and permission scopes. Examples: repo (core), fleet\_management (FSM), iot (devices), reports, billing.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description |
| -------------- | ---------------------------------------------- | ----------- |
| `id`           | `ID!`                                          |             |
| `version`      | `Int!`                                         |             |
| `title`        | `String!`                                      |             |
| `code`         | [Code!](scalars.md#code)                       |             |
| `order`        | `Int!`                                         |             |
| `catalog`      | [Catalog!](objects.md#catalog)                 |             |
| `organization` | [Organization](objects.md#organization)        |             |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |             |

### EntityType

A definition of an entity type in the system.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field                    | Type                                                            | Description                                                                   |
| ------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                           |                                                                               |
| `version`                | `Int!`                                                          |                                                                               |
| `title`                  | `String!`                                                       |                                                                               |
| `code`                   | [Code!](scalars.md#code)                                        |                                                                               |
| `order`                  | `Int!`                                                          |                                                                               |
| `catalog`                | [Catalog!](objects.md#catalog)                                  |                                                                               |
| `organization`           | [Organization](objects.md#organization)                         |                                                                               |
| `meta`                   | [CatalogItemMeta!](objects.md#catalogitemmeta)                  |                                                                               |
| `uuidDiscriminator`      | `String!`                                                       | The 4-character code embedded in UUIDs for entities of this type.             |
| `isCustomizable`         | `Boolean!`                                                      | Whether entities of this type support custom fields.                          |
| `customFieldDefinitions` | [\[CustomFieldDefinition!\]!](objects.md#customfielddefinition) | Custom field definitions for entities of this type, ordered by display order. |

### DeviceVendor

A device manufacturer or vendor.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                                       | Description                            |
| -------------- | ---------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                      |                                        |
| `version`      | `Int!`                                                     |                                        |
| `title`        | `String!`                                                  |                                        |
| `code`         | [Code!](scalars.md#code)                                   |                                        |
| `order`        | `Int!`                                                     |                                        |
| `catalog`      | [Catalog!](objects.md#catalog)                             |                                        |
| `organization` | [Organization](objects.md#organization)                    |                                        |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta)             |                                        |
| `models`       | [DeviceModelConnection!](objects.md#devicemodelconnection) | Device models produced by this vendor. |

### DeviceModel

A specific device model produced by a vendor.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description                              |
| -------------- | ---------------------------------------------- | ---------------------------------------- |
| `id`           | `ID!`                                          |                                          |
| `version`      | `Int!`                                         |                                          |
| `title`        | `String!`                                      |                                          |
| `code`         | [Code!](scalars.md#code)                       |                                          |
| `order`        | `Int!`                                         |                                          |
| `catalog`      | [Catalog!](objects.md#catalog)                 |                                          |
| `organization` | [Organization](objects.md#organization)        |                                          |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |                                          |
| `vendor`       | [DeviceVendor!](objects.md#devicevendor)       | The vendor that manufactures this model. |

### DeviceType

A classification type for devices.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field                    | Type                                                            | Description                                                                      |
| ------------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                           |                                                                                  |
| `version`                | `Int!`                                                          |                                                                                  |
| `title`                  | `String!`                                                       |                                                                                  |
| `code`                   | [Code!](scalars.md#code)                                        |                                                                                  |
| `order`                  | `Int!`                                                          |                                                                                  |
| `catalog`                | [Catalog!](objects.md#catalog)                                  |                                                                                  |
| `organization`           | [Organization](objects.md#organization)                         |                                                                                  |
| `meta`                   | [CatalogItemMeta!](objects.md#catalogitemmeta)                  |                                                                                  |
| `customFieldDefinitions` | [\[CustomFieldDefinition!\]!](objects.md#customfielddefinition) | Custom field definitions specific to this device type, ordered by display order. |

### DeviceStatus

An operational status for devices.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description |
| -------------- | ---------------------------------------------- | ----------- |
| `id`           | `ID!`                                          |             |
| `version`      | `Int!`                                         |             |
| `title`        | `String!`                                      |             |
| `code`         | [Code!](scalars.md#code)                       |             |
| `order`        | `Int!`                                         |             |
| `catalog`      | [Catalog!](objects.md#catalog)                 |             |
| `organization` | [Organization](objects.md#organization)        |             |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |             |

### DeviceRelationType

A type of relationship between two devices.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description |
| -------------- | ---------------------------------------------- | ----------- |
| `id`           | `ID!`                                          |             |
| `version`      | `Int!`                                         |             |
| `title`        | `String!`                                      |             |
| `code`         | [Code!](scalars.md#code)                       |             |
| `order`        | `Int!`                                         |             |
| `catalog`      | [Catalog!](objects.md#catalog)                 |             |
| `organization` | [Organization](objects.md#organization)        |             |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |             |

### AssetType

A classification type for assets.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field                    | Type                                                            | Description                                                                     |
| ------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                           |                                                                                 |
| `version`                | `Int!`                                                          |                                                                                 |
| `title`                  | `String!`                                                       |                                                                                 |
| `code`                   | [Code!](scalars.md#code)                                        |                                                                                 |
| `order`                  | `Int!`                                                          |                                                                                 |
| `catalog`                | [Catalog!](objects.md#catalog)                                  |                                                                                 |
| `organization`           | [Organization](objects.md#organization)                         |                                                                                 |
| `meta`                   | [CatalogItemMeta!](objects.md#catalogitemmeta)                  |                                                                                 |
| `customFieldDefinitions` | [\[CustomFieldDefinition!\]!](objects.md#customfielddefinition) | Custom field definitions specific to this asset type, ordered by display order. |

### AssetGroupType

A type for asset groups with membership constraints.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field               | Type                                                                  | Description                                                                    |
| ------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `id`                | `ID!`                                                                 |                                                                                |
| `version`           | `Int!`                                                                |                                                                                |
| `title`             | `String!`                                                             |                                                                                |
| `code`              | [Code!](scalars.md#code)                                              |                                                                                |
| `order`             | `Int!`                                                                |                                                                                |
| `catalog`           | [Catalog!](objects.md#catalog)                                        |                                                                                |
| `organization`      | [Organization](objects.md#organization)                               |                                                                                |
| `meta`              | [CatalogItemMeta!](objects.md#catalogitemmeta)                        |                                                                                |
| `allowedAssetTypes` | [\[AssetGroupTypeConstraint!\]!](objects.md#assetgrouptypeconstraint) | The asset types allowed in groups of this type, with optional quantity limits. |

### GeoObjectType

A classification type for geographic objects.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field                    | Type                                                            | Description                                                                          |
| ------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `id`                     | `ID!`                                                           |                                                                                      |
| `version`                | `Int!`                                                          |                                                                                      |
| `title`                  | `String!`                                                       |                                                                                      |
| `code`                   | [Code!](scalars.md#code)                                        |                                                                                      |
| `order`                  | `Int!`                                                          |                                                                                      |
| `catalog`                | [Catalog!](objects.md#catalog)                                  |                                                                                      |
| `organization`           | [Organization](objects.md#organization)                         |                                                                                      |
| `meta`                   | [CatalogItemMeta!](objects.md#catalogitemmeta)                  |                                                                                      |
| `customFieldDefinitions` | [\[CustomFieldDefinition!\]!](objects.md#customfielddefinition) | Custom field definitions specific to this geo object type, ordered by display order. |

### ScheduleType

A classification type for schedules.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field                    | Type                                                            | Description                                                                        |
| ------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                     | `ID!`                                                           |                                                                                    |
| `version`                | `Int!`                                                          |                                                                                    |
| `title`                  | `String!`                                                       |                                                                                    |
| `code`                   | [Code!](scalars.md#code)                                        |                                                                                    |
| `order`                  | `Int!`                                                          |                                                                                    |
| `catalog`                | [Catalog!](objects.md#catalog)                                  |                                                                                    |
| `organization`           | [Organization](objects.md#organization)                         |                                                                                    |
| `meta`                   | [CatalogItemMeta!](objects.md#catalogitemmeta)                  |                                                                                    |
| `customFieldDefinitions` | [\[CustomFieldDefinition!\]!](objects.md#customfielddefinition) | Custom field definitions specific to this schedule type, ordered by display order. |

### Role

A role that can be assigned to actors to grant permissions.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                                             | Description                            |
| -------------- | ---------------------------------------------------------------- | -------------------------------------- |
| `id`           | `ID!`                                                            |                                        |
| `version`      | `Int!`                                                           |                                        |
| `title`        | `String!`                                                        |                                        |
| `code`         | [Code!](scalars.md#code)                                         |                                        |
| `order`        | `Int!`                                                           |                                        |
| `catalog`      | [Catalog!](objects.md#catalog)                                   |                                        |
| `organization` | [Organization](objects.md#organization)                          |                                        |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta)                   |                                        |
| `permissions`  | [RolePermissionConnection!](objects.md#rolepermissionconnection) | The permissions assigned to this role. |

### PermissionScope

A definition of a permission scope that can be granted to roles.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description                                  |
| -------------- | ---------------------------------------------- | -------------------------------------------- |
| `id`           | `ID!`                                          |                                              |
| `version`      | `Int!`                                         |                                              |
| `title`        | `String!`                                      |                                              |
| `code`         | [Code!](scalars.md#code)                       |                                              |
| `order`        | `Int!`                                         |                                              |
| `catalog`      | [Catalog!](objects.md#catalog)                 |                                              |
| `organization` | [Organization](objects.md#organization)        |                                              |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |                                              |
| `module`       | [Module!](objects.md#module)                   | The module this permission scope belongs to. |
| `entityType`   | [EntityType!](objects.md#entitytype)           | The entity type this permission applies to.  |

### Tag

A tag for labeling and categorizing entities.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description                                                                    |
| -------------- | ---------------------------------------------- | ------------------------------------------------------------------------------ |
| `id`           | `ID!`                                          |                                                                                |
| `version`      | `Int!`                                         |                                                                                |
| `title`        | `String!`                                      |                                                                                |
| `code`         | [Code!](scalars.md#code)                       |                                                                                |
| `order`        | `Int!`                                         |                                                                                |
| `catalog`      | [Catalog!](objects.md#catalog)                 |                                                                                |
| `organization` | [Organization](objects.md#organization)        |                                                                                |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |                                                                                |
| `entityTypes`  | [\[EntityType!\]!](objects.md#entitytype)      | The entity types this tag can be applied to. Empty means the tag is universal. |

### Country

A country reference data item.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                           | Description                                                                      |
| -------------- | ---------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`           | `ID!`                                          |                                                                                  |
| `version`      | `Int!`                                         |                                                                                  |
| `title`        | `String!`                                      |                                                                                  |
| `code`         | [Code!](scalars.md#code)                       |                                                                                  |
| `order`        | `Int!`                                         |                                                                                  |
| `catalog`      | [Catalog!](objects.md#catalog)                 |                                                                                  |
| `organization` | [Organization](objects.md#organization)        |                                                                                  |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) |                                                                                  |
| `alpha2Code`   | [CountryCode!](scalars.md#countrycode)         | The [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code. |

### UserCatalogItem

A user-defined catalog item that supports hierarchical organization.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [HierarchicalCatalogItem](interfaces.md#hierarchicalcatalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                                               | Description                                            |
| -------------- | ------------------------------------------------------------------ | ------------------------------------------------------ |
| `id`           | `ID!`                                                              |                                                        |
| `version`      | `Int!`                                                             |                                                        |
| `title`        | `String!`                                                          |                                                        |
| `code`         | [Code!](scalars.md#code)                                           |                                                        |
| `order`        | `Int!`                                                             |                                                        |
| `catalog`      | [Catalog!](objects.md#catalog)                                     |                                                        |
| `organization` | [Organization](objects.md#organization)                            |                                                        |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta)                     |                                                        |
| `parent`       | [UserCatalogItem](objects.md#usercatalogitem)                      | The parent item in the hierarchy. Null for root items. |
| `children`     | [UserCatalogItemConnection!](objects.md#usercatalogitemconnection) | The child items in the hierarchy.                      |

### Catalog

A catalog definition that contains catalog items. Catalogs are themselves catalog items.

**Implements:** [CatalogItem](interfaces.md#catalogitem), [Node](interfaces.md#node), [Versioned](interfaces.md#versioned), [Titled](interfaces.md#titled)

| Field          | Type                                                       | Description                                 |
| -------------- | ---------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                      |                                             |
| `version`      | `Int!`                                                     |                                             |
| `title`        | `String!`                                                  |                                             |
| `code`         | [Code!](scalars.md#code)                                   |                                             |
| `order`        | `Int!`                                                     |                                             |
| `catalog`      | [Catalog!](objects.md#catalog)                             | Self-reference for the meta-catalog.        |
| `organization` | [Organization](objects.md#organization)                    |                                             |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta)             |                                             |
| `module`       | [Module!](objects.md#module)                               | The module this catalog is associated with. |
| `items`        | [CatalogItemConnection!](objects.md#catalogitemconnection) | The items in this catalog.                  |

## Other

### SystemActor

The built-in system actor used for automated operations.

**Implements:** [Actor](interfaces.md#actor), [Node](interfaces.md#node), [Titled](interfaces.md#titled)

| Field   | Type      | Description |
| ------- | --------- | ----------- |
| `id`    | `ID!`     |             |
| `title` | `String!` |             |

### GeoPoint

A geographic coordinate point.

| Field      | Type                               | Description                                  |
| ---------- | ---------------------------------- | -------------------------------------------- |
| `lat`      | [Latitude!](scalars.md#latitude)   | The latitude coordinate in decimal degrees.  |
| `lng`      | [Longitude!](scalars.md#longitude) | The longitude coordinate in decimal degrees. |
| `altitude` | `Float`                            | The altitude in meters above sea level.      |
| `accuracy` | `Float`                            | The horizontal accuracy in meters.           |

### PointContainmentResult

The result of checking whether a point is contained within a geometry.

| Field         | Type                             | Description                                          |
| ------------- | -------------------------------- | ---------------------------------------------------- |
| `index`       | `Int!`                           | The index of the point in the input array (0-based). |
| `point`       | [GeoPoint!](objects.md#geopoint) | The point that was checked.                          |
| `isContained` | `Boolean!`                       | Whether the point is inside the geometry.            |
