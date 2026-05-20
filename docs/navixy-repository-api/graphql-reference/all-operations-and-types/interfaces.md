# Interfaces

Interfaces define common fields shared by multiple object types. When a type implements an interface, it guarantees those fields are present.

## Node

An object with a globally unique identifier.

| Field | Type  | Description                                                                          |
| ----- | ----- | ------------------------------------------------------------------------------------ |
| `id`  | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |

**Implemented by:** [InventoryItem](interfaces.md#inventoryitem), [Actor](interfaces.md#actor), [CatalogItem](interfaces.md#catalogitem), [Module](objects.md#module), [EntityType](objects.md#entitytype), [DeviceVendor](objects.md#devicevendor), [DeviceModel](objects.md#devicemodel), [DeviceType](objects.md#devicetype), [DeviceStatus](objects.md#devicestatus), [DeviceRelationType](objects.md#devicerelationtype), [AssetType](objects.md#assettype), [AssetGroupType](objects.md#assetgrouptype), [GeoObjectType](objects.md#geoobjecttype), [ScheduleType](objects.md#scheduletype), [Role](objects.md#role), [PermissionScope](objects.md#permissionscope), [Tag](objects.md#tag), [Country](objects.md#country), [UserCatalogItem](objects.md#usercatalogitem), [Catalog](objects.md#catalog), [Organization](objects.md#organization), [SystemActor](objects.md#systemactor), [User](objects.md#user), [Member](objects.md#member), [Integration](objects.md#integration), [ActorRole](objects.md#actorrole), [RolePermission](objects.md#rolepermission), [UserScope](objects.md#userscope), [Device](objects.md#device), [DeviceIdentifier](objects.md#deviceidentifier), [DeviceRelation](objects.md#devicerelation), [DeviceInventoryRelation](objects.md#deviceinventoryrelation), [Asset](objects.md#asset), [AssetGroup](objects.md#assetgroup), [AssetGroupItem](objects.md#assetgroupitem), [Inventory](objects.md#inventory), [GeoObject](objects.md#geoobject), [Schedule](objects.md#schedule), [CustomFieldDefinition](objects.md#customfielddefinition), [AuditEvent](objects.md#auditevent)

## Titled

An object with a human-readable display name.

| Field   | Type      | Description                      |
| ------- | --------- | -------------------------------- |
| `title` | `String!` | The human-readable display name. |

**Implemented by:** [Actor](interfaces.md#actor), [CatalogItem](interfaces.md#catalogitem), [Module](objects.md#module), [EntityType](objects.md#entitytype), [DeviceVendor](objects.md#devicevendor), [DeviceModel](objects.md#devicemodel), [DeviceType](objects.md#devicetype), [DeviceStatus](objects.md#devicestatus), [DeviceRelationType](objects.md#devicerelationtype), [AssetType](objects.md#assettype), [AssetGroupType](objects.md#assetgrouptype), [GeoObjectType](objects.md#geoobjecttype), [ScheduleType](objects.md#scheduletype), [Role](objects.md#role), [PermissionScope](objects.md#permissionscope), [Tag](objects.md#tag), [Country](objects.md#country), [UserCatalogItem](objects.md#usercatalogitem), [Catalog](objects.md#catalog), [Organization](objects.md#organization), [SystemActor](objects.md#systemactor), [User](objects.md#user), [Integration](objects.md#integration), [Device](objects.md#device), [Asset](objects.md#asset), [AssetGroup](objects.md#assetgroup), [Inventory](objects.md#inventory), [GeoObject](objects.md#geoobject), [Schedule](objects.md#schedule), [CustomFieldDefinition](objects.md#customfielddefinition)

## Customizable

An object that supports custom field values.

| Field          | Type                     | Description                                                                     |
| -------------- | ------------------------ | ------------------------------------------------------------------------------- |
| `customFields` | [JSON!](scalars.md#json) | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. |

**Implemented by:** [Member](objects.md#member), [Device](objects.md#device), [Asset](objects.md#asset), [GeoObject](objects.md#geoobject), [Schedule](objects.md#schedule)

## Versioned

An object that supports optimistic locking for concurrency control.

| Field     | Type   | Description                                                                                                                                 |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |

**Implemented by:** [CatalogItem](interfaces.md#catalogitem), [Module](objects.md#module), [EntityType](objects.md#entitytype), [DeviceVendor](objects.md#devicevendor), [DeviceModel](objects.md#devicemodel), [DeviceType](objects.md#devicetype), [DeviceStatus](objects.md#devicestatus), [DeviceRelationType](objects.md#devicerelationtype), [AssetType](objects.md#assettype), [AssetGroupType](objects.md#assetgrouptype), [GeoObjectType](objects.md#geoobjecttype), [ScheduleType](objects.md#scheduletype), [Role](objects.md#role), [PermissionScope](objects.md#permissionscope), [Tag](objects.md#tag), [Country](objects.md#country), [UserCatalogItem](objects.md#usercatalogitem), [Catalog](objects.md#catalog), [Organization](objects.md#organization), [User](objects.md#user), [Member](objects.md#member), [Integration](objects.md#integration), [Device](objects.md#device), [Asset](objects.md#asset), [AssetGroup](objects.md#assetgroup), [Inventory](objects.md#inventory), [GeoObject](objects.md#geoobject), [Schedule](objects.md#schedule), [CustomFieldDefinition](objects.md#customfielddefinition)

## MultiValue

An interface for field parameters that support selecting multiple values.

| Field     | Type       | Description                                             |
| --------- | ---------- | ------------------------------------------------------- |
| `isMulti` | `Boolean!` | Whether multiple values can be selected for this field. |

**Implemented by:** [FieldParamsOptions](objects.md#fieldparamsoptions), [FieldParamsDevice](objects.md#fieldparamsdevice), [FieldParamsReference](objects.md#fieldparamsreference), [FieldParamsCatalog](objects.md#fieldparamscatalog), [FieldParamsTag](objects.md#fieldparamstag)

## InventoryItem

An object that can be assigned to an inventory.

| Field       | Type                              | Description                                       |
| ----------- | --------------------------------- | ------------------------------------------------- |
| `id`        | `ID!`                             | A globally unique identifier.                     |
| `inventory` | [Inventory](objects.md#inventory) | The inventory this item is currently assigned to. |

**Implemented by:** [Device](objects.md#device)

## Edge

An edge in a paginated connection.

| Field    | Type      | Description                                          |
| -------- | --------- | ---------------------------------------------------- |
| `cursor` | `String!` | An opaque cursor for this edge, used for pagination. |

**Implemented by:** [CatalogItemEdge](objects.md#catalogitemedge), [UserCatalogItemEdge](objects.md#usercatalogitemedge), [OrganizationEdge](objects.md#organizationedge), [UserEdge](objects.md#useredge), [MemberEdge](objects.md#memberedge), [IntegrationEdge](objects.md#integrationedge), [DeviceEdge](objects.md#deviceedge), [AssetEdge](objects.md#assetedge), [AssetGroupEdge](objects.md#assetgroupedge), [AssetGroupItemEdge](objects.md#assetgroupitemedge), [InventoryEdge](objects.md#inventoryedge), [GeoObjectEdge](objects.md#geoobjectedge), [ScheduleEdge](objects.md#scheduleedge), [AuditEventEdge](objects.md#auditeventedge), [DeviceInventoryRelationEdge](objects.md#deviceinventoryrelationedge), [CatalogEdge](objects.md#catalogedge), [DeviceTypeEdge](objects.md#devicetypeedge), [DeviceStatusEdge](objects.md#devicestatusedge), [DeviceModelEdge](objects.md#devicemodeledge), [AssetTypeEdge](objects.md#assettypeedge), [AssetGroupTypeEdge](objects.md#assetgrouptypeedge), [GeoObjectTypeEdge](objects.md#geoobjecttypeedge), [ScheduleTypeEdge](objects.md#scheduletypeedge), [RoleEdge](objects.md#roleedge), [TagEdge](objects.md#tagedge), [ActorRoleEdge](objects.md#actorroleedge), [RolePermissionEdge](objects.md#rolepermissionedge), [UserScopeEdge](objects.md#userscopeedge)

## Connection

A paginated connection following the Relay Cursor Connections specification.

| Field      | Type                              | Description                                   |
| ---------- | --------------------------------- | --------------------------------------------- |
| `pageInfo` | [PageInfo!](objects.md#pageinfo)  | Information about the current page.           |
| `total`    | [CountInfo](objects.md#countinfo) | The total count of items matching the filter. |

**Implemented by:** [CatalogItemConnection](objects.md#catalogitemconnection), [UserCatalogItemConnection](objects.md#usercatalogitemconnection), [OrganizationConnection](objects.md#organizationconnection), [UserConnection](objects.md#userconnection), [MemberConnection](objects.md#memberconnection), [IntegrationConnection](objects.md#integrationconnection), [DeviceConnection](objects.md#deviceconnection), [AssetConnection](objects.md#assetconnection), [AssetGroupConnection](objects.md#assetgroupconnection), [AssetGroupItemConnection](objects.md#assetgroupitemconnection), [InventoryConnection](objects.md#inventoryconnection), [GeoObjectConnection](objects.md#geoobjectconnection), [ScheduleConnection](objects.md#scheduleconnection), [AuditEventConnection](objects.md#auditeventconnection), [DeviceInventoryRelationConnection](objects.md#deviceinventoryrelationconnection), [CatalogConnection](objects.md#catalogconnection), [DeviceTypeConnection](objects.md#devicetypeconnection), [DeviceStatusConnection](objects.md#devicestatusconnection), [DeviceModelConnection](objects.md#devicemodelconnection), [AssetTypeConnection](objects.md#assettypeconnection), [AssetGroupTypeConnection](objects.md#assetgrouptypeconnection), [GeoObjectTypeConnection](objects.md#geoobjecttypeconnection), [ScheduleTypeConnection](objects.md#scheduletypeconnection), [RoleConnection](objects.md#roleconnection), [TagConnection](objects.md#tagconnection), [ActorRoleConnection](objects.md#actorroleconnection), [RolePermissionConnection](objects.md#rolepermissionconnection), [UserScopeConnection](objects.md#userscopeconnection)

## Actor

An entity that can perform actions and have permissions assigned.

| Field   | Type      | Description                    |
| ------- | --------- | ------------------------------ |
| `id`    | `ID!`     | A globally unique identifier.  |
| `title` | `String!` | The display name of the actor. |

**Implemented by:** [SystemActor](objects.md#systemactor), [User](objects.md#user), [Integration](objects.md#integration)

## CatalogItem

A dictionary item that provides reference data for the system.

| Field          | Type                                           | Description                                                                     |
| -------------- | ---------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`           | `ID!`                                          | A globally unique identifier.                                                   |
| `version`      | `Int!`                                         | The version number for optimistic locking.                                      |
| `title`        | `String!`                                      | The human-readable display name. Can be localized.                              |
| `code`         | [Code!](scalars.md#code)                       | A machine-readable code, unique within the catalog scope.                       |
| `order`        | `Int!`                                         | The display order within the same level or category.                            |
| `catalog`      | [Catalog!](objects.md#catalog)                 | The catalog this item belongs to.                                               |
| `organization` | [Organization](objects.md#organization)        | The organization that owns this item. Null for system items.                    |
| `meta`         | [CatalogItemMeta!](objects.md#catalogitemmeta) | Metadata about this item including description, origin, and display properties. |

**Implemented by:** [Module](objects.md#module), [EntityType](objects.md#entitytype), [DeviceVendor](objects.md#devicevendor), [DeviceModel](objects.md#devicemodel), [DeviceType](objects.md#devicetype), [DeviceStatus](objects.md#devicestatus), [DeviceRelationType](objects.md#devicerelationtype), [AssetType](objects.md#assettype), [AssetGroupType](objects.md#assetgrouptype), [GeoObjectType](objects.md#geoobjecttype), [ScheduleType](objects.md#scheduletype), [Role](objects.md#role), [PermissionScope](objects.md#permissionscope), [Tag](objects.md#tag), [Country](objects.md#country), [UserCatalogItem](objects.md#usercatalogitem), [Catalog](objects.md#catalog)

## HierarchicalCatalogItem

A catalog item that supports parent-child hierarchy.

| Field    | Type                                     | Description                                            |
| -------- | ---------------------------------------- | ------------------------------------------------------ |
| `parent` | [CatalogItem](interfaces.md#catalogitem) | The parent item in the hierarchy. Null for root items. |

**Implemented by:** [UserCatalogItem](objects.md#usercatalogitem)

## FieldParams

The base interface for field parameters.

| Field        | Type       | Description                                 |
| ------------ | ---------- | ------------------------------------------- |
| `isRequired` | `Boolean!` | Whether a value is required for this field. |

**Implemented by:** [FieldParamsString](objects.md#fieldparamsstring), [FieldParamsText](objects.md#fieldparamstext), [FieldParamsNumber](objects.md#fieldparamsnumber), [FieldParamsBoolean](objects.md#fieldparamsboolean), [FieldParamsDate](objects.md#fieldparamsdate), [FieldParamsDatetime](objects.md#fieldparamsdatetime), [FieldParamsGeojson](objects.md#fieldparamsgeojson), [FieldParamsSchedule](objects.md#fieldparamsschedule), [FieldParamsOptions](objects.md#fieldparamsoptions), [FieldParamsDevice](objects.md#fieldparamsdevice), [FieldParamsReference](objects.md#fieldparamsreference), [FieldParamsCatalog](objects.md#fieldparamscatalog), [FieldParamsTag](objects.md#fieldparamstag)
