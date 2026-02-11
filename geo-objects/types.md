# Geo objects — Types

## Objects

### GeoObjectType

A classification type for geographic objects.

**Implements:** [CatalogItem](../catalogs.md#catalogitem), [Node](../common.md#node), [Versioned](../common.md#versioned), [Titled](../common.md#titled)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. |
| `version` | `Int!` | The version number for optimistic locking. |
| `title` | `String!` | The human-readable display name. Can be localized. |
| `code` | `Code!` | A machine-readable code, unique within the catalog scope. |
| `order` | `Int!` | The display order within the same level or category. |
| `catalog` | [Catalog](../catalogs/catalog-items.md#catalog)! | The catalog this item belongs to. |
| `organization` | [Organization](../organizations.md#organization) | The organization that owns this item. Null for system items. |
| `meta` | [CatalogItemMeta](../catalogs.md#catalogitemmeta)! | Metadata about this item including description, origin, and display properties. |
| `customFieldDefinitions` | [[CustomFieldDefinition](../custom-fields.md#customfielddefinition)!]! | Custom field definitions specific to this geo object type, ordered by display order. |

---

### GeoPoint

A geographic coordinate point.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `lat` | `Latitude!` | The latitude coordinate in decimal degrees. |
| `lng` | `Longitude!` | The longitude coordinate in decimal degrees. |
| `altitude` | `Float` | The altitude in meters above sea level. |
| `accuracy` | `Float` | The horizontal accuracy in meters. |

---

### GeoObject

A geographic object such as a geofence, point of interest, or route.

**Implements:** [Node](../common.md#node), [Titled](../common.md#titled), [Customizable](../common.md#customizable), [Versioned](../common.md#versioned)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | A globally unique identifier. This ID is opaque and should not be parsed by clients. |
| `version` | `Int!` | The version number for optimistic locking.
  Incremented on each update. Must be provided in update/delete mutations to prevent lost updates. |
| `title` | `String!` | The human-readable display name. |
| `organization` | [Organization](../organizations.md#organization)! | The organization that owns this geo object. |
| `type` | [GeoObjectType](types.md#geoobjecttype)! | The geo object type classification. |
| `geometry` | `GeoJSON!` | The geographic shape of this object as GeoJSON geometry.
  This is an alias for the `geojson` custom field. |
| `codes` | `[Code!]` | Limit returned fields to these codes. Returns all fields if not specified. |
| `points` | [[GeoPointInput](types.md#geopointinput)!]! | The points to check for containment. |

---

### PointContainmentResult

The result of checking whether a point is contained within a geometry.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `index` | `Int!` | The index of the point in the input array (0-based). |
| `point` | [GeoPoint](types.md#geopoint)! | The point that was checked. |
| `isContained` | `Boolean!` | Whether the point is inside the geometry. |

---

### GeoObjectPayload

The result of a geo object mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObject` | [GeoObject](types.md#geoobject)! | The created or updated geo object. |

---

### GeoObjectTypePayload

The result of a geo object type mutation.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `geoObjectType` | [GeoObjectType](types.md#geoobjecttype)! | The created or updated geo object type. |

---

## Inputs

### GeoPointInput

Input for a geographic coordinate point.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `lat` | `Latitude!` | The latitude coordinate (-90 to 90 degrees). |
| `lng` | `Longitude!` | The longitude coordinate (-180 to 180 degrees). |
| `altitude` | `Float` | The altitude in meters above sea level. |
| `accuracy` | `Float` | The horizontal accuracy in meters. |

---

### GeoObjectFilter

Filtering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `typeIds` | `[ID!]` | Filter by geo object types (OR within field). |
| `titleContains` | `String` | Partial match on title (case-insensitive contains). |
| `customFields` | [[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values. |

---

### GeoObjectOrder

Ordering options for geo objects.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `field` | [GeoObjectOrderField](types.md#geoobjectorderfield) | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | `Code` | The custom field code to order by. Mutually exclusive with `field`. |
| `direction` | [OrderDirection](../common.md#orderdirection)! | The direction to order. |

---

### GeoObjectCreateInput

Input for creating a new geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the geo object. |
| `typeId` | `ID!` | The geo object type ID. |
| `title` | `String!` | The geo object display name. |
| `geometry` | `GeoJSON!` | The GeoJSON geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values. |

---

### GeoObjectUpdateInput

Input for updating an existing geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `geometry` | `GeoJSON` | The new geometry. |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes. |

---

### GeoObjectDeleteInput

Input for deleting a geo object.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The geo object ID to delete. |
| `version` | `Int!` | The current version for optimistic locking. |

---

### GeoObjectTypeCreateInput

Input for creating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `organizationId` | `ID!` | The organization that will own the item. |
| `code` | `Code!` | The machine-readable code. |
| `title` | `String!` | The display name. |
| `order` | `Int = 0` | The display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

### GeoObjectTypeUpdateInput

Input for updating a geo object type.

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | `ID!` | The item ID to update. |
| `version` | `Int!` | The current version for optimistic locking. |
| `title` | `String` | The new display name. |
| `order` | `Int` | The new display order. |
| `meta` | [CatalogItemMetaInput](../catalogs/catalog-items.md#catalogitemmetainput) | The display properties. |

---

## Enums

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

### GeoObjectOrderField

Fields available for ordering geo objects.

| Value | Description |
| ----- | ----------- |
| `TITLE` | Order by title. |

---

## Pagination types

### GeoObjectConnection

A paginated list of GeoObject items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectEdge](types.md#geoobjectedge)!]! | A list of edges. |
| `nodes` | [[GeoObject](types.md#geoobject)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### GeoObjectEdge

An edge in the GeoObject connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [GeoObject](types.md#geoobject)! | The geo object at the end of the edge. |

---

### GeoObjectTypeConnection

A paginated list of GeoObjectType items.

**Implements:** [Connection](../common.md#connection)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `edges` | [[GeoObjectTypeEdge](types.md#geoobjecttypeedge)!]! | A list of edges. |
| `nodes` | [[GeoObjectType](types.md#geoobjecttype)!]! | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../common.md#pageinfo)! | Information about the current page. |
| `total` | [CountInfo](../common.md#countinfo) | The total count of items matching the filter. |

---

### GeoObjectTypeEdge

An edge in the GeoObjectType connection.

**Implements:** [Edge](../common.md#edge)

| Field | Type | Description |
| ----- | ---- | ----------- |
| `cursor` | `String!` | An opaque cursor for this edge. |
| `node` | [GeoObjectType](types.md#geoobjecttype)! | The geo object type at the end of the edge. |

---
