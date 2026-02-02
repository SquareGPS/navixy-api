# Types

## Types

### GeoObjectConnection

A paginated list of GeoObject items.

**Implements:** [`Connection`](../core-api-reference/common-resources.md#connection)

| Field      | Type                                                             | Description                                                |
| ---------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| `edges`    | \[[GeoObjectEdge](types.md#geoobjectedge)!]!                     | A list of edges.                                           |
| `nodes`    | \[[GeoObject](types.md#geoobject)!]!                             | A list of nodes in the connection (without edge metadata). |
| `pageInfo` | [PageInfo](../core-api-reference/common-resources.md#pageinfo)!  | Information about the current page.                        |
| `total`    | [CountInfo](../core-api-reference/common-resources.md#countinfo) | The total count of items matching the filter.              |

### GeoObjectEdge

An edge in the GeoObject connection.

**Implements:** [`Edge`](../core-api-reference/common-resources.md#edge)

| Field    | Type                             | Description                            |
| -------- | -------------------------------- | -------------------------------------- |
| `cursor` | `String!`                        | An opaque cursor for this edge.        |
| `node`   | [GeoObject](types.md#geoobject)! | The geo object at the end of the edge. |

### GeoPoint

A geographic coordinate point.

| Field      | Type                             | Description                                  |
| ---------- | -------------------------------- | -------------------------------------------- |
| `lat`      | [Latitude](types.md#latitude)!   | The latitude coordinate in decimal degrees.  |
| `lng`      | [Longitude](types.md#longitude)! | The longitude coordinate in decimal degrees. |
| `altitude` | `Float`                          | The altitude in meters above sea level.      |
| `accuracy` | `Float`                          | The horizontal accuracy in meters.           |

### GeoObject

A geographic object such as a geofence, point of interest, or route.

**Implements:** [`Node`](../core-api-reference/common-resources.md#node), [`Titled`](../core-api-reference/common-resources.md#titled), [`Customizable`](../core-api-reference/common-resources.md#customizable), [`Versioned`](../core-api-reference/common-resources.md#versioned)

| Field            | Type                                                               | Description                                 |
| ---------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| `id`             | `ID!`                                                              |                                             |
| `version`        | `Int!`                                                             |                                             |
| `title`          | `String!`                                                          |                                             |
| `organization`   | [Organization](../core-api-reference/organizations/#organization)! | The organization that owns this geo object. |
| `type`           | [GeoObjectType](../catalogs/entity-types/types.md#geoobjecttype)!  | The geo object type classification.         |
| `geometry`       | [GeoJSON](types.md#geojson)!                                       |                                             |
| `customFields`   | [JSON](../core-api-reference/common-resources.md#json)!            |                                             |
| `containsPoints` | \[[PointContainmentResult](types.md#pointcontainmentresult)!]!     |                                             |

### PointContainmentResult

The result of checking whether a point is contained within a geometry.

| Field         | Type                           | Description                                          |
| ------------- | ------------------------------ | ---------------------------------------------------- |
| `index`       | `Int!`                         | The index of the point in the input array (0-based). |
| `point`       | [GeoPoint](types.md#geopoint)! | The point that was checked.                          |
| `isContained` | `Boolean!`                     | Whether the point is inside the geometry.            |

### GeoObjectPayload

The result of a geo object mutation.

| Field       | Type                             | Description                        |
| ----------- | -------------------------------- | ---------------------------------- |
| `geoObject` | [GeoObject](types.md#geoobject)! | The created or updated geo object. |

## Inputs

### GeoPointInput

Input for a geographic coordinate point.

| Field      | Type                             | Description                                     |
| ---------- | -------------------------------- | ----------------------------------------------- |
| `lat`      | [Latitude](types.md#latitude)!   | The latitude coordinate (-90 to 90 degrees).    |
| `lng`      | [Longitude](types.md#longitude)! | The longitude coordinate (-180 to 180 degrees). |
| `altitude` | `Float`                          | The altitude in meters above sea level.         |
| `accuracy` | `Float`                          | The horizontal accuracy in meters.              |

### GeoObjectFilter

Filtering options for geo objects.

| Field           | Type                                                           | Description                                         |
| --------------- | -------------------------------------------------------------- | --------------------------------------------------- |
| `typeIds`       | `[ID!]`                                                        | Filter by geo object types (OR within field).       |
| `titleContains` | `String`                                                       | Partial match on title (case-insensitive contains). |
| `customFields`  | \[[CustomFieldFilter](../custom-fields.md#customfieldfilter)!] | Filter by custom field values.                      |

### GeoObjectOrder

Ordering options for geo objects.

| Field             | Type                                                                        | Description                                                                |
| ----------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `field`           | [GeoObjectOrderField](types.md#geoobjectorderfield)                         | The standard field to order by. Mutually exclusive with `customFieldCode`. |
| `customFieldCode` | [Code](../core-api-reference/common-resources.md#code)                      | The custom field code to order by. Mutually exclusive with `field`.        |
| `direction`       | [OrderDirection](../core-api-reference/common-resources.md#orderdirection)! | The direction to order.                                                    |

### GeoObjectCreateInput

Input for creating a new geo object.

| Field            | Type                                                                 | Description                                    |
| ---------------- | -------------------------------------------------------------------- | ---------------------------------------------- |
| `organizationId` | `ID!`                                                                | The organization that will own the geo object. |
| `typeId`         | `ID!`                                                                | The geo object type ID.                        |
| `title`          | `String!`                                                            | The geo object display name.                   |
| `geometry`       | [GeoJSON](types.md#geojson)!                                         | The [GeoJSON](https://geojson.org/) geometry.  |
| `customFields`   | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field values.                       |

### GeoObjectUpdateInput

Input for updating an existing geo object.

| Field          | Type                                                                 | Description                                 |
| -------------- | -------------------------------------------------------------------- | ------------------------------------------- |
| `id`           | `ID!`                                                                | The geo object ID to update.                |
| `version`      | `Int!`                                                               | The current version for optimistic locking. |
| `title`        | `String`                                                             | The new display name.                       |
| `geometry`     | [GeoJSON](types.md#geojson)                                          | The new geometry.                           |
| `customFields` | [CustomFieldsPatchInput](../custom-fields.md#customfieldspatchinput) | The custom field changes.                   |

### GeoObjectDeleteInput

Input for deleting a geo object.

| Field     | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| `id`      | `ID!`  | The geo object ID to delete.                |
| `version` | `Int!` | The current version for optimistic locking. |

## Enums

### GeoJsonGeometryType

The type of [GeoJSON](https://geojson.org/) geometry.

| Value                 | Description                                     |
| --------------------- | ----------------------------------------------- |
| `POINT`               | A single geographic point.                      |
| `MULTI_POINT`         | A collection of points.                         |
| `LINE_STRING`         | A sequence of connected line segments.          |
| `MULTI_LINE_STRING`   | A collection of line strings.                   |
| `POLYGON`             | A closed shape defined by a linear ring.        |
| `MULTI_POLYGON`       | A collection of polygons.                       |
| `GEOMETRY_COLLECTION` | A heterogeneous collection of geometry objects. |

### GeoObjectOrderField

Fields available for ordering geo objects.

| Value   | Description     |
| ------- | --------------- |
| `TITLE` | Order by title. |

## Scalars

### GeoJSON

**Specification:** [https://www.rfc-editor.org/rfc/rfc7946](https://www.rfc-editor.org/rfc/rfc7946)

### Latitude

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/latitude](https://the-guild.dev/graphql/scalars/docs/scalars/latitude)

### Longitude

**Specification:** [https://the-guild.dev/graphql/scalars/docs/scalars/longitude](https://the-guild.dev/graphql/scalars/docs/scalars/longitude)
