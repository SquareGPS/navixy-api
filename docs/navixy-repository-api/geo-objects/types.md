# Geo objects — Types

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

## Objects

<a id="type-geoobjecttype"></a>

### GeoObjectType

A classification type for geographic objects.

**Implements:** [CatalogItem](../catalogs/catalog-items.md#type-catalogitem), [Node](../common.md#type-node), [Versioned](../common.md#type-versioned), [Titled](../common.md#type-titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#type-catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations/README.md#type-organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs/catalog-items.md#type-catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#type-customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

---

<a id="type-geopoint"></a>

### GeoPoint

A geographic coordinate point.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `lat` | `Latitude!` | The latitude coordinate in decimal degrees. |
| `lng` | `Longitude!` | The longitude coordinate in decimal degrees. |
| `altitude` | `Float` | The altitude in meters above sea level. |
| `accuracy` | `Float` | The horizontal accuracy in meters. |

---

<a id="type-geoobject"></a>

### GeoObject

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#type-node), [Titled](../common.md#type-titled), [Customizable](../common.md#type-customizable), [Versioned](../common.md#type-versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking. Incremented on each update. Can be provided in update/delete mutations to prevent lost updates. If omitted, the update proceeds without stale-read protection. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations/README.md#type-organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](#type-geoobjecttype)! | The geo object type classification. |
| `geojsonData` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry. |
| `customFields` | `JSON!` | Custom field values as a key-value map. Keys are `CustomFieldDefinition` codes. System-reserved codes (`geojson_data`, `schedule_data`, `device`) are excluded from this map and exposed through dedicated typed fields on the entity instead. |
| `containsPoints` | [[PointContainmentResult](#type-pointcontainmentresult)!]! | Checks if the given points are contained within this geo object's geometry. Returns the containment status for each point. Only applicable to Polygon and MultiPolygon geometries. |

---

<a id="type-pointcontainmentresult"></a>

### PointContainmentResult

The result of checking whether a point is contained within a geometry.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `index` | `Int!` | The index of the point in the input array (0-based). |
| `point` | [GeoPoint](#type-geopoint)! | The point that was checked. |
| `isContained` | `Boolean!` | Whether the point is inside the geometry. |

---

<a id="type-geoobjectpayload"></a>

### GeoObjectPayload

The result of a geo object mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](#type-geoobject)! | The created or updated geo object. |

---

<a id="type-geoobjecttypepayload"></a>

### GeoObjectTypePayload

The result of a geo object type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](#type-geoobjecttype)! | The created or updated geo object type. |

---

## Inputs

<a id="type-geopointinput"></a>

### GeoPointInput

Input for a geographic coordinate point.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `lat` | `Latitude!` | The latitude coordinate (-90 to 90 degrees). |
| `lng` | `Longitude!` | The longitude coordinate (-180 to 180 degrees). |
| `altitude` | `Float` | The altitude in meters above sea level. |
| `accuracy` | `Float` | The horizontal accuracy in meters. |

---

<a id="type-geoobjectfilter"></a>

### GeoObjectFilter

Filtering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by geo object types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#type-customfieldfilter)!] | Filter by custom field values. |

---

<a id="type-geoobjectorder"></a>

### GeoObjectOrder

Ordering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [GeoObjectOrderField](#type-geoobjectorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#type-orderdirection)! | The direction to order. |

---

<a id="type-geoobjectcreateinput"></a>

### GeoObjectCreateInput

Input for creating a new geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geojsonData` | `GeoJSON!` | The GeoJSON geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#type-customfieldspatchinput) | The custom field values. |

---

<a id="type-geoobjectupdateinput"></a>

### GeoObjectUpdateInput

Input for updating an existing geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `geojsonData` | `GeoJSON` | The new geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#type-customfieldspatchinput) | The custom field changes. |

---

<a id="type-geoobjectdeleteinput"></a>

### GeoObjectDeleteInput

Input for deleting a geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |

---

<a id="type-geoobjecttypecreateinput"></a>

### GeoObjectTypeCreateInput

Input for creating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code` | The machine-readable code. Auto-generated from title if omitted. |
| `title` | `String!` | The display name. |
| `order` | `Int` | The display order. Auto-calculated as last position if omitted. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions for this geo object type. Only `create` is allowed when creating a new catalog item. |

---

<a id="type-geoobjecttypeupdateinput"></a>

### GeoObjectTypeUpdateInput

Input for updating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int` | The current version for optimistic locking. If omitted, auto-increments without conflict check. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#type-catalogitemmetainput) | The display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinitionInput](../custom-fields.md#type-customfielddefinitioninput)!] | Operations on custom field definitions belonging to this geo object type. |

---

## Enums

<a id="type-geojsongeometrytype"></a>

### GeoJsonGeometryType

The type of GeoJSON geometry.

| Value | Description |
| ----- | ----------- |
| `POINT` | A single geographic point. |
| `MULTI_POINT` | A collection of points. |
| `LINE_STRING` | A sequence of connected line segments. |
| `MULTI_LINE_STRING` | A collection of line strings. |
| `POLYGON` | A closed shape defined by a linear ring. |
| `MULTI_POLYGON` | A collection of polygons. |
| `GEOMETRY_COLLECTION` | A heterogeneous collection of geometry objects. |

---

<a id="type-geoobjectorderfield"></a>

### GeoObjectOrderField

Fields available for ordering geo objects.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

<a id="type-geoobjectconnection"></a>

### GeoObjectConnection

A paginated list of GeoObject items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectEdge](#type-geoobjectedge)!]! | A list of edges. |
| `nodes` | [[GeoObject](#type-geoobject)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-geoobjectedge"></a>

### GeoObjectEdge

An edge in the GeoObject connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [GeoObject](#type-geoobject)! | The geo object at the end of the edge. |

---

<a id="type-geoobjecttypeconnection"></a>

### GeoObjectTypeConnection

A paginated list of GeoObjectType items.

**Implements:** [Connection](../common.md#type-connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectTypeEdge](#type-geoobjecttypeedge)!]! | A list of edges. |
| `nodes` | [[GeoObjectType](#type-geoobjecttype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#type-pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#type-countinfo) | The total count of items matching the filter. |

---

<a id="type-geoobjecttypeedge"></a>

### GeoObjectTypeEdge

An edge in the GeoObjectType connection.

**Implements:** [Edge](../common.md#type-edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [GeoObjectType](#type-geoobjecttype)! | The geo object type at the end of the edge. |

---
