# Catalog reference

This page provides a cross-reference of all catalog types organized by their parent entity.

## Device

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [DeviceType](../devices/types.md#devicetype) | A classification type for devices. |
| Object | [DeviceStatus](../devices/types.md#devicestatus) | An operational status for devices. |
| Object | [DeviceModel](../devices/types.md#devicemodel) | A specific device model produced by a vendor. |
| Object | [DeviceVendor](../devices/types.md#devicevendor) | A device manufacturer or vendor. |
| Object | [DeviceRelationType](../devices/types.md#devicerelationtype) | A type of relationship between two devices. |

**Related queries:**

- [deviceTypes](../devices/queries.md#devicetypes) — Lists device types for an organization.
- [deviceStatuses](../devices/queries.md#devicestatuses) — Lists device statuses for an organization.
- [deviceModels](../devices/queries.md#devicemodels) — Lists device models with optional vendor filter.
- [device](../devices/queries.md#device) — Retrieves a device by its ID.
- [devices](../devices/queries.md#devices) — Lists devices for an organization.

## Asset

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [AssetType](../assets/types.md#assettype) | A classification type for assets. |

**Related queries:**

- [assetTypes](../assets/queries.md#assettypes) — Lists asset types for an organization.
- [assetGroupTypes](../assets/groups/queries.md#assetgrouptypes) — Lists asset group types for an organization.
- [asset](../assets/queries.md#asset) — Retrieves an asset by its ID.
- [assets](../assets/queries.md#assets) — Lists assets for an organization.
- [assetGroup](../assets/groups/queries.md#assetgroup) — Retrieves an asset group by its ID.
- [assetGroups](../assets/groups/queries.md#assetgroups) — Lists asset groups for an organization.

## Asset group

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [AssetGroupType](../assets/groups/types.md#assetgrouptype) | A type for asset groups with membership constraints. |

**Related queries:**

- [assetGroupTypes](../assets/groups/queries.md#assetgrouptypes) — Lists asset group types for an organization.
- [assetGroup](../assets/groups/queries.md#assetgroup) — Retrieves an asset group by its ID.
- [assetGroups](../assets/groups/queries.md#assetgroups) — Lists asset groups for an organization.

## Geo object

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [GeoObjectType](../geo-objects/types.md#geoobjecttype) | A classification type for geographic objects. |

**Related queries:**

- [geoObjectTypes](../geo-objects/queries.md#geoobjecttypes) — Lists geo object types for an organization.
- [geoObject](../geo-objects/queries.md#geoobject) — Retrieves a geo object by its ID.
- [geoObjects](../geo-objects/queries.md#geoobjects) — Lists geo objects for an organization.

## Schedule

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [ScheduleType](../schedules/types.md#scheduletype) | A classification type for schedules. |

**Related queries:**

- [scheduleTypes](../schedules/queries.md#scheduletypes) — Lists schedule types for an organization.
- [schedule](../schedules/queries.md#schedule) — Retrieves a schedule by its ID.
- [schedules](../schedules/queries.md#schedules) — Lists schedules for an organization.

## Access

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [Role](../access-control/types.md#role) | A role that can be assigned to actors to grant permissions. |
| Object | [PermissionScope](../access-control/types.md#permissionscope) | A definition of a permission scope that can be granted to roles. |

**Related queries:**

- [roles](../access-control/queries.md#roles) — Lists roles for an organization.

## Other

| Kind | Name | Description |
| ---- | ---- | ----------- |
| Object | [Tag](tags.md#tag) | A tag for labeling and categorizing entities. |
| Object | [Module](system.md#module) | A system module that groups related functionality and permission scopes. |
| Object | [EntityType](system.md#entitytype) | A definition of an entity type in the system. |
| Object | [Country](system.md#country) | A country reference data item. |

**Related queries:**

- [tags](../catalogs/tags/queries.md#tags) — Lists tags for an organization.
