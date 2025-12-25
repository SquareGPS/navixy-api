# Interfaces

Interfaces define common fields shared by multiple object types. When a type implements an interface, it guarantees those fields are present.

### Node

Base interface for all entities with a unique identifier. All domain entities implement this interface.

**Fields**

<table><thead><tr><th width="113.79998779296875">Field</th><th width="93">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>UUID!</td><td>Globally unique identifier with embedded entity type discriminator</td></tr></tbody></table>

**Implemented by:** ActorRole, Actor, AssetGroupItem, AssetGroupType, AssetGroup, AssetType, Asset, AuditEvent, CatalogCategory, Catalog, Country, CustomFieldDefinition, DeviceIdentifier, DeviceInventoryRelation, DeviceModel, DeviceRelationType, DeviceRelation, DeviceStatus, DeviceType, DeviceVendor, Device, EntityType, GeoObjectType, GeoObject, Integration, Inventory, Member, Module, Organization, PermissionScope, RolePermission, Role, ScheduleType, Schedule, Tag, UserCatalogItem, UserScope, User

### Timestamped

Interface for entities that track creation and modification timestamps. Timestamps are automatically managed by the system.

**Fields**

| Field       | Type      | Description                             |
| ----------- | --------- | --------------------------------------- |
| `createdAt` | DateTime! | When the entity was created (immutable) |
| `updatedAt` | DateTime! | When the entity was last modified       |

**Implemented by:** ActorRole, Actor, AssetGroupItem, AssetGroupType, AssetGroup, AssetType, Asset, CatalogCategory, Catalog, Country, CustomFieldDefinition, DeviceIdentifier, DeviceInventoryRelation, DeviceModel, DeviceRelationType, DeviceStatus, DeviceType, DeviceVendor, Device, EntityType, GeoObjectType, GeoObject, Integration, Inventory, Member, Module, Organization, PermissionScope, RolePermission, Role, ScheduleType, Schedule, Tag, UserCatalogItem, User

### SoftDeletable

Interface for entities that support soft deletion. Soft-deleted entities are excluded from queries by default.

**Fields**

| Field       | Type     | Description                                       |
| ----------- | -------- | ------------------------------------------------- |
| `deletedAt` | DateTime | When the entity was soft-deleted (null if active) |
| `deletedBy` | Actor    | Actor who performed the deletion                  |

**Implemented by:** Actor, AssetGroup, Asset, CustomFieldDefinition, DeviceInventoryRelation, Device, GeoObject, Integration, Inventory, Member, Organization, Schedule, User

### Customizable

Interface for entities that support custom fields. Custom fields are stored as JSON and validated against field definitions.

**Fields**

| Field          | Type  | Description                                                                                                                       |
| -------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------- |
| `customFields` | JSON! | Custom fields as key-value map. Keys are field codes from CustomFieldDefinition. Values are typed according to field definitions. |

**Implemented by:** Asset, Device, GeoObject, Member, Schedule

### CatalogItem

Base interface for all catalog items (dictionaries/reference data). Catalog items use Single Table Inheritance pattern with a discriminator. Hierarchy support: - parent/children fields are only meaningful when is\_hierarchical=true - Hierarchical items use ltree for efficient tree queries

**Extends:** Node, Timestamped

**Fields**

| Field         | Type             | Description                                                                                                                                                              |
| ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`          | UUID!            | Globally unique identifier with embedded entity type discriminator&#xD;                                                                                                  |
| `code`        | String!          | Machine-readable code, unique within discriminator scope. Format: lowercase letters, numbers, underscores. Must start with letter. Example: vehicle\_car, status\_active |
| `title`       | String!          | Human-readable localized title                                                                                                                                           |
| `description` | String           | Optional localized description                                                                                                                                           |
| `order`       | Int!             | Display order within the same level/category                                                                                                                             |
| `isSystem`    | Boolean!         | Whether this is a system-managed item. System items cannot be deleted or moved between organizations.                                                                    |
| `extra`       | JSON!            | Additional flexible fields (icon, color, metadata). Schema may be defined by catalog.fieldsSchema.                                                                       |
| `createdAt`   | DateTime!        | When the entity was created                                                                                                                                              |
| `updatedAt`   | DateTime!        | When the entity was updated                                                                                                                                              |
| `parent`      | CatalogItem      | Parent item in hierarchy (null for root items or non-hierarchical)                                                                                                       |
| `children`    | \[CatalogItem!]! | Child items in hierarchy (empty for leaf items or non-hierarchical)                                                                                                      |

**Implemented by:** AssetGroupType, AssetType, CatalogCategory, Catalog, Country, CustomFieldDefinition, DeviceModel, DeviceRelationType, DeviceStatus, DeviceType, DeviceVendor, EntityType, GeoObjectType, Module, PermissionScope, Role, ScheduleType, Tag, UserCatalogItem

### FieldParams

Base interface for field parameters. All field param types share the `isRequired` property.

**Fields**

| Field        | Type     | Description                     |
| ------------ | -------- | ------------------------------- |
| `isRequired` | Boolean! | Whether field value is required |

**Implemented by:** FieldParamsBoolean, FieldParamsCatalog, FieldParamsDate, FieldParamsDatetime, FieldParamsDevice, FieldParamsGeojson, FieldParamsNumber, FieldParamsOptions, FieldParamsReference, FieldParamsSchedule, FieldParamsString, FieldParamsTag, FieldParamsText
