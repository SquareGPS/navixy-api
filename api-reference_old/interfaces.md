# Interfaces

Interfaces define common fields shared by multiple object types. When a type implements an interface, it guarantees those fields are present.

### Node

Base interface for all entities with a unique identifier. All domain entities implement this interface.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) | Globally unique identifier with embedded entity type discriminator |

**Implemented by:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Module](/api-reference/objects.md#module/), [CatalogCategory](/api-reference/objects.md#catalogcategory/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/), [Organization](/api-reference/objects.md#organization/), [Actor](/api-reference/objects.md#actor/), [User](/api-reference/objects.md#user/), [Member](/api-reference/objects.md#member/), [Integration](/api-reference/objects.md#integration/), [ActorRole](/api-reference/objects.md#actorrole/), [RolePermission](/api-reference/objects.md#rolepermission/), [UserScope](/api-reference/objects.md#userscope/), [Device](/api-reference/objects.md#device/), [DeviceIdentifier](/api-reference/objects.md#deviceidentifier/), [DeviceRelation](/api-reference/objects.md#devicerelation/), [DeviceInventoryRelation](/api-reference/objects.md#deviceinventoryrelation/), [Asset](/api-reference/objects.md#asset/), [AssetGroup](/api-reference/objects.md#assetgroup/), [AssetGroupItem](/api-reference/objects.md#assetgroupitem/), [Inventory](/api-reference/objects.md#inventory/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/), [AuditEvent](/api-reference/objects.md#auditevent/)

### Timestamped

Interface for entities that track creation and modification timestamps. Timestamps are automatically managed by the system.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When the entity was created (immutable) |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) | When the entity was last modified |

**Implemented by:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Module](/api-reference/objects.md#module/), [CatalogCategory](/api-reference/objects.md#catalogcategory/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/), [Organization](/api-reference/objects.md#organization/), [Actor](/api-reference/objects.md#actor/), [User](/api-reference/objects.md#user/), [Member](/api-reference/objects.md#member/), [Integration](/api-reference/objects.md#integration/), [ActorRole](/api-reference/objects.md#actorrole/), [RolePermission](/api-reference/objects.md#rolepermission/), [Device](/api-reference/objects.md#device/), [DeviceIdentifier](/api-reference/objects.md#deviceidentifier/), [DeviceInventoryRelation](/api-reference/objects.md#deviceinventoryrelation/), [Asset](/api-reference/objects.md#asset/), [AssetGroup](/api-reference/objects.md#assetgroup/), [AssetGroupItem](/api-reference/objects.md#assetgroupitem/), [Inventory](/api-reference/objects.md#inventory/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/)

### SoftDeletable

Interface for entities that support soft deletion. Soft-deleted entities are excluded from queries by default.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `deletedAt` | [DateTime](/api-reference/scalars-and-enums.md#datetime/) | When the entity was soft-deleted (null if active) |
| `deletedBy` | [Actor](/api-reference/objects.md#actor/) | Actor who performed the deletion |

**Implemented by:** [Organization](/api-reference/objects.md#organization/), [Actor](/api-reference/objects.md#actor/), [User](/api-reference/objects.md#user/), [Member](/api-reference/objects.md#member/), [Integration](/api-reference/objects.md#integration/), [Device](/api-reference/objects.md#device/), [DeviceInventoryRelation](/api-reference/objects.md#deviceinventoryrelation/), [Asset](/api-reference/objects.md#asset/), [AssetGroup](/api-reference/objects.md#assetgroup/), [Inventory](/api-reference/objects.md#inventory/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/)

### Customizable

Interface for entities that support custom fields. Custom fields are stored as JSON and validated against field definitions.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Custom fields as key-value map. Keys are field codes from CustomFieldDefinition. Values are typed according to field definitions. |

**Implemented by:** [Member](/api-reference/objects.md#member/), [Device](/api-reference/objects.md#device/), [Asset](/api-reference/objects.md#asset/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/)

### CatalogItem

Base interface for all catalog items (dictionaries/reference data). Catalog items use Hierarchy support: - parent/children fields are only meaningful when is_hierarchical=true - Hierarchical items use ltree for efficient tree queries

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | [UUID!](/api-reference/scalars-and-enums.md#uuid/) |  |
| `code` | `String!` | Machine-readable code, unique within discriminator scope. Format: lowercase letters, numbers, underscores. Must start with letter. Example: vehicle_car, status_active |
| `title` | `String!` | Human-readable localized title |
| `description` | `String` | Optional localized description |
| `order` | `Int!` | Display order within the same level/category |
| `isSystem` | `Boolean!` | Whether this is a system-managed item. System items cannot be deleted or moved between organizations. |
| `extra` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Additional flexible fields (icon, color, metadata). Schema may be defined by catalog.fieldsSchema. |
| `createdAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `updatedAt` | [DateTime!](/api-reference/scalars-and-enums.md#datetime/) |  |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) | Parent item in hierarchy (null for root items or non-hierarchical) |
| `children` | [[CatalogItem!]!](/api-reference/interfaces.md#catalogitem/) | Child items in hierarchy (empty for leaf items or non-hierarchical) |

**Implemented by:** [Module](/api-reference/objects.md#module/), [CatalogCategory](/api-reference/objects.md#catalogcategory/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/)

### FieldParams

Base interface for field parameters. All field param types share isRequired property.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether field value is required |

**Implemented by:** [FieldParamsString](/api-reference/objects.md#fieldparamsstring/), [FieldParamsText](/api-reference/objects.md#fieldparamstext/), [FieldParamsNumber](/api-reference/objects.md#fieldparamsnumber/), [FieldParamsBoolean](/api-reference/objects.md#fieldparamsboolean/), [FieldParamsDate](/api-reference/objects.md#fieldparamsdate/), [FieldParamsDatetime](/api-reference/objects.md#fieldparamsdatetime/), [FieldParamsGeojson](/api-reference/objects.md#fieldparamsgeojson/), [FieldParamsSchedule](/api-reference/objects.md#fieldparamsschedule/), [FieldParamsOptions](/api-reference/objects.md#fieldparamsoptions/), [FieldParamsDevice](/api-reference/objects.md#fieldparamsdevice/), [FieldParamsReference](/api-reference/objects.md#fieldparamsreference/), [FieldParamsCatalog](/api-reference/objects.md#fieldparamscatalog/), [FieldParamsTag](/api-reference/objects.md#fieldparamstag/)
