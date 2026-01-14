# Interfaces

Interfaces define common fields shared by multiple object types. When a type implements an interface, it guarantees those fields are present.

## Node

An object with a globally unique identifier.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

**Implemented by:** [InventoryItem](/api-reference/interfaces.md#inventoryitem/), [Actor](/api-reference/interfaces.md#actor/), [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Module](/api-reference/objects.md#module/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/), [Organization](/api-reference/objects.md#organization/), [SystemActor](/api-reference/objects.md#systemactor/), [User](/api-reference/objects.md#user/), [Member](/api-reference/objects.md#member/), [Integration](/api-reference/objects.md#integration/), [ActorRole](/api-reference/objects.md#actorrole/), [RolePermission](/api-reference/objects.md#rolepermission/), [UserScope](/api-reference/objects.md#userscope/), [Device](/api-reference/objects.md#device/), [DeviceIdentifier](/api-reference/objects.md#deviceidentifier/), [DeviceRelation](/api-reference/objects.md#devicerelation/), [DeviceInventoryRelation](/api-reference/objects.md#deviceinventoryrelation/), [Asset](/api-reference/objects.md#asset/), [AssetGroup](/api-reference/objects.md#assetgroup/), [AssetGroupItem](/api-reference/objects.md#assetgroupitem/), [Inventory](/api-reference/objects.md#inventory/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/), [AuditEvent](/api-reference/objects.md#auditevent/)

## Titled

An object with a human-readable display name.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `title` | `String!` | The human-readable display name. |

**Implemented by:** [Actor](/api-reference/interfaces.md#actor/), [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Module](/api-reference/objects.md#module/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/), [Organization](/api-reference/objects.md#organization/), [SystemActor](/api-reference/objects.md#systemactor/), [User](/api-reference/objects.md#user/), [Integration](/api-reference/objects.md#integration/), [Device](/api-reference/objects.md#device/), [Asset](/api-reference/objects.md#asset/), [AssetGroup](/api-reference/objects.md#assetgroup/), [Inventory](/api-reference/objects.md#inventory/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/)

## Customizable

An object that supports custom field values.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `customFields` | [JSON!](/api-reference/scalars-and-enums.md#json/) | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |

**Implemented by:** [Member](/api-reference/objects.md#member/), [Device](/api-reference/objects.md#device/), [Asset](/api-reference/objects.md#asset/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/)

## Versioned

An object that supports optimistic locking for concurrency control.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |

**Implemented by:** [CatalogItem](/api-reference/interfaces.md#catalogitem/), [Module](/api-reference/objects.md#module/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/), [Organization](/api-reference/objects.md#organization/), [User](/api-reference/objects.md#user/), [Member](/api-reference/objects.md#member/), [Integration](/api-reference/objects.md#integration/), [Device](/api-reference/objects.md#device/), [Asset](/api-reference/objects.md#asset/), [AssetGroup](/api-reference/objects.md#assetgroup/), [Inventory](/api-reference/objects.md#inventory/), [GeoObject](/api-reference/objects.md#geoobject/), [Schedule](/api-reference/objects.md#schedule/), [CustomFieldDefinition](/api-reference/objects.md#customfielddefinition/)

## MultiValue

An interface for field parameters that support selecting multiple values.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |

**Implemented by:** [FieldParamsOptions](/api-reference/objects.md#fieldparamsoptions/), [FieldParamsDevice](/api-reference/objects.md#fieldparamsdevice/), [FieldParamsReference](/api-reference/objects.md#fieldparamsreference/), [FieldParamsCatalog](/api-reference/objects.md#fieldparamscatalog/), [FieldParamsTag](/api-reference/objects.md#fieldparamstag/)

## InventoryItem

An object that can be assigned to an inventory.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `inventory` | [Inventory](/api-reference/objects.md#inventory/) | The inventory this item is currently assigned to. |

**Implemented by:** [Device](/api-reference/objects.md#device/)

## Edge

An edge in a paginated connection.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge, used for pagination. |

**Implemented by:** [CatalogItemEdge](/api-reference/objects.md#catalogitemedge/), [UserCatalogItemEdge](/api-reference/objects.md#usercatalogitemedge/), [OrganizationEdge](/api-reference/objects.md#organizationedge/), [UserEdge](/api-reference/objects.md#useredge/), [MemberEdge](/api-reference/objects.md#memberedge/), [IntegrationEdge](/api-reference/objects.md#integrationedge/), [DeviceEdge](/api-reference/objects.md#deviceedge/), [AssetEdge](/api-reference/objects.md#assetedge/), [AssetGroupEdge](/api-reference/objects.md#assetgroupedge/), [AssetGroupItemEdge](/api-reference/objects.md#assetgroupitemedge/), [InventoryEdge](/api-reference/objects.md#inventoryedge/), [GeoObjectEdge](/api-reference/objects.md#geoobjectedge/), [ScheduleEdge](/api-reference/objects.md#scheduleedge/), [AuditEventEdge](/api-reference/objects.md#auditeventedge/), [DeviceInventoryRelationEdge](/api-reference/objects.md#deviceinventoryrelationedge/), [CatalogEdge](/api-reference/objects.md#catalogedge/), [DeviceTypeEdge](/api-reference/objects.md#devicetypeedge/), [DeviceStatusEdge](/api-reference/objects.md#devicestatusedge/), [DeviceModelEdge](/api-reference/objects.md#devicemodeledge/), [AssetTypeEdge](/api-reference/objects.md#assettypeedge/), [AssetGroupTypeEdge](/api-reference/objects.md#assetgrouptypeedge/), [GeoObjectTypeEdge](/api-reference/objects.md#geoobjecttypeedge/), [ScheduleTypeEdge](/api-reference/objects.md#scheduletypeedge/), [RoleEdge](/api-reference/objects.md#roleedge/), [TagEdge](/api-reference/objects.md#tagedge/), [ActorRoleEdge](/api-reference/objects.md#actorroleedge/), [RolePermissionEdge](/api-reference/objects.md#rolepermissionedge/), [UserScopeEdge](/api-reference/objects.md#userscopeedge/)

## Connection

A paginated connection following the Relay Cursor Connections specification.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `pageInfo` | [PageInfo!](/api-reference/objects.md#pageinfo/) | Information about the current page. |
| `total` | [CountInfo](/api-reference/objects.md#countinfo/) | The total count of items matching the filter. |

**Implemented by:** [CatalogItemConnection](/api-reference/objects.md#catalogitemconnection/), [UserCatalogItemConnection](/api-reference/objects.md#usercatalogitemconnection/), [OrganizationConnection](/api-reference/objects.md#organizationconnection/), [UserConnection](/api-reference/objects.md#userconnection/), [MemberConnection](/api-reference/objects.md#memberconnection/), [IntegrationConnection](/api-reference/objects.md#integrationconnection/), [DeviceConnection](/api-reference/objects.md#deviceconnection/), [AssetConnection](/api-reference/objects.md#assetconnection/), [AssetGroupConnection](/api-reference/objects.md#assetgroupconnection/), [AssetGroupItemConnection](/api-reference/objects.md#assetgroupitemconnection/), [InventoryConnection](/api-reference/objects.md#inventoryconnection/), [GeoObjectConnection](/api-reference/objects.md#geoobjectconnection/), [ScheduleConnection](/api-reference/objects.md#scheduleconnection/), [AuditEventConnection](/api-reference/objects.md#auditeventconnection/), [DeviceInventoryRelationConnection](/api-reference/objects.md#deviceinventoryrelationconnection/), [CatalogConnection](/api-reference/objects.md#catalogconnection/), [DeviceTypeConnection](/api-reference/objects.md#devicetypeconnection/), [DeviceStatusConnection](/api-reference/objects.md#devicestatusconnection/), [DeviceModelConnection](/api-reference/objects.md#devicemodelconnection/), [AssetTypeConnection](/api-reference/objects.md#assettypeconnection/), [AssetGroupTypeConnection](/api-reference/objects.md#assetgrouptypeconnection/), [GeoObjectTypeConnection](/api-reference/objects.md#geoobjecttypeconnection/), [ScheduleTypeConnection](/api-reference/objects.md#scheduletypeconnection/), [RoleConnection](/api-reference/objects.md#roleconnection/), [TagConnection](/api-reference/objects.md#tagconnection/), [ActorRoleConnection](/api-reference/objects.md#actorroleconnection/), [RolePermissionConnection](/api-reference/objects.md#rolepermissionconnection/), [UserScopeConnection](/api-reference/objects.md#userscopeconnection/)

## Actor

An entity that can perform actions and have permissions assigned.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `title` | `String!` | The display name of the actor. |

**Implemented by:** [SystemActor](/api-reference/objects.md#systemactor/), [User](/api-reference/objects.md#user/), [Integration](/api-reference/objects.md#integration/)

## CatalogItem

A dictionary item that provides reference data for the system.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | [Code!](/api-reference/scalars-and-enums.md#code/) | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog!](/api-reference/objects.md#catalog/) | The catalog this item belongs to. |
| `organization` | [Organization](/api-reference/objects.md#organization/) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta!](/api-reference/objects.md#catalogitemmeta/) | Metadata about this item including description, origin, and display properties. |

**Implemented by:** [Module](/api-reference/objects.md#module/), [EntityType](/api-reference/objects.md#entitytype/), [DeviceVendor](/api-reference/objects.md#devicevendor/), [DeviceModel](/api-reference/objects.md#devicemodel/), [DeviceType](/api-reference/objects.md#devicetype/), [DeviceStatus](/api-reference/objects.md#devicestatus/), [DeviceRelationType](/api-reference/objects.md#devicerelationtype/), [AssetType](/api-reference/objects.md#assettype/), [AssetGroupType](/api-reference/objects.md#assetgrouptype/), [GeoObjectType](/api-reference/objects.md#geoobjecttype/), [ScheduleType](/api-reference/objects.md#scheduletype/), [Role](/api-reference/objects.md#role/), [PermissionScope](/api-reference/objects.md#permissionscope/), [Tag](/api-reference/objects.md#tag/), [Country](/api-reference/objects.md#country/), [UserCatalogItem](/api-reference/objects.md#usercatalogitem/), [Catalog](/api-reference/objects.md#catalog/)

## HierarchicalCatalogItem

A catalog item that supports parent-child hierarchy.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `parent` | [CatalogItem](/api-reference/interfaces.md#catalogitem/) | The parent item in the hierarchy. Null for root items. |

**Implemented by:** [UserCatalogItem](/api-reference/objects.md#usercatalogitem/)

## FieldParams

The base interface for field parameters.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

**Implemented by:** [FieldParamsString](/api-reference/objects.md#fieldparamsstring/), [FieldParamsText](/api-reference/objects.md#fieldparamstext/), [FieldParamsNumber](/api-reference/objects.md#fieldparamsnumber/), [FieldParamsBoolean](/api-reference/objects.md#fieldparamsboolean/), [FieldParamsDate](/api-reference/objects.md#fieldparamsdate/), [FieldParamsDatetime](/api-reference/objects.md#fieldparamsdatetime/), [FieldParamsGeojson](/api-reference/objects.md#fieldparamsgeojson/), [FieldParamsSchedule](/api-reference/objects.md#fieldparamsschedule/), [FieldParamsOptions](/api-reference/objects.md#fieldparamsoptions/), [FieldParamsDevice](/api-reference/objects.md#fieldparamsdevice/), [FieldParamsReference](/api-reference/objects.md#fieldparamsreference/), [FieldParamsCatalog](/api-reference/objects.md#fieldparamscatalog/), [FieldParamsTag](/api-reference/objects.md#fieldparamstag/)
