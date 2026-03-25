---
description: Create geofences, POIs, and routes in different shapes using GeoJSON geometry.
---

# Working with geo objects

{% include "../.gitbook/includes/navixy-repository-api-is-a-....md" %}

Geo objects in Navixy Repository API represent geographic features like geofences, points of interest, and routes. They store location data in GeoJSON format, making them useful for defining delivery zones, marking important locations, creating routes, and managing areas where your fleet operates.

This guide walks you through creating, updating, and managing geo objects with different geometry types.

## Before you start

To work with geo objects, you need your organization's ID. Use the [me](../actors/#me) query to find it through your membership:

```graphql
query GetMyOrganization {
  me {
    ... on User {
      memberships {
        nodes {
          organization {
            id
            title
          }
        }
      }
    }
  }
}
```

The response returns your organization's details:

```json
{
  "data": {
    "me": {
      "memberships": {
        "nodes": [
          {
            "organization": {
              "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
              "title": "TransLog GmbH"
            }
          }
        ]
      }
    }   
  }
}
```

Use the `id` of the organization you want to work with for all subsequent geo object operations.

### Check the available geo object types

Before creating a geo object, list the available types to see what options exist with this query:

```graphql
query ListGeoObjectTypes {
  geoObjectTypes(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
  ) {
    nodes {
      id
      code
      title
    }
  }
}
```

The response returns predefined types and any custom types your organization has created:

```json
{
  "data": {
    "geoObjectTypes": {
      "nodes": [
        {
          "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
          "code": "poi",
          "title": "Point of Interest"
        },
        {
          "id": "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22",
          "code": "geofence",
          "title": "Geofence"
        }
      ]
    }
  }
}
```

If the response returns an empty array, doesn't contain the type you need, or you want a type with a different code or title, create one:

```graphql
mutation CreateGeoObjectType {
  geoObjectTypeCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    code: "delivery_zone"
    title: "Delivery Zone"
  }) {
    geoObjectType {
      id
      code
      title
    }
  }
}
```

The response confirms the new type:

```json
{
  "data": {
    "geoObjectTypeCreate": {
      "geoObjectType": {
        "id": "c2ggde11-1e2d-6gh0-dd8f-8dd1df602c33",
        "code": "delivery_zone",
        "title": "Delivery Zone"
      }
    }
  }
}
```

Save the type ID — you'll need it when creating geo objects.

## Understanding GeoJSON geometry

Geo objects store their geographic shape in the `geometry` field, which uses GeoJSON format as defined in [RFC 7946](https://www.rfc-editor.org/rfc/rfc7946). This format represents geographic features with coordinate-based geometries.

{% hint style="info" %}
The `geometry` field is a convenience alias for the `geojson` system custom field. You can also access the same data through the `customFields` field.
{% endhint %}

A complete GeoJSON is always a `FeatureCollection` wrapping one or more `Feature` objects, each of which holds a geometry and optional properties:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [13.35, 52.48],
            [13.45, 52.48],
            [13.45, 52.56],
            [13.35, 52.56],
            [13.35, 52.48]
          ]
        ]
      },
      "properties": {}
    }
  ]
}
```

More examples of different geometry types wrapped in `FeatureCollection` can be found in the [Common GeoJSON patterns](working-with-geo-objects.md#common-geojson-patterns) section.

### Supported geometry types

<table><thead><tr><th width="143.4888916015625">Geometry type</th><th width="385.0889892578125">Use case</th><th>Example</th></tr></thead><tbody><tr><td>Point</td><td>A single coordinate marker. For GPS containment checks, use a Polygon centered on the point instead.</td><td>Warehouse pin on a map</td></tr><tr><td>Polygon</td><td>Area boundary. The only type that supports <code>containsPoints</code> checks.</td><td>Geofence</td></tr><tr><td>LineString</td><td>A straight or curved line passing through specific points. Useful for visual map overlays, but has no area and cannot be used for containment checks.</td><td>Road segment, boundary line</td></tr><tr><td>MultiPoint</td><td>Multiple separate coordinate markers</td><td>Distribution network</td></tr><tr><td>MultiLineString</td><td>Multiple line sequences</td><td>Multiple road segments</td></tr><tr><td>MultiPolygon</td><td>Multiple areas treated as a single geo object</td><td>Non-contiguous zones, city districts</td></tr></tbody></table>

**Modeling routes for deviation detection:** A GeoJSON `LineString` represents a line with no width. In fleet management, route monitoring works by detecting whether a vehicle leaves a defined corridor. This requires a zone with area — typically a `Polygon` shaped as a buffer around the intended path (sometimes called a "corridor" or "sausage" shape). Use `LineString` only for visual display purposes and `Polygon` for any containment or deviation logic.

**Points and GPS presence detection:** A `Point` geometry has no area, so `containsPoints` cannot be applied to it. If you need to detect whether a GPS device is near a specific location, create a `Polygon` centered on that location with an appropriate radius buffer instead of using a `Point`.

### Coordinate format

GeoJSON uses `[longitude, latitude]` order, which is opposite to how coordinates are often written in text.

```
Text format:     52.520008, 13.404954 (latitude, longitude)
GeoJSON format:  [13.404954, 52.520008] (longitude, latitude)
```

For example, Berlin's Brandenburg Gate is located at latitude 52.516275 and longitude 13.377704. In GeoJSON, this becomes `[13.377704, 52.516275]`.

{% hint style="warning" %}
Always double-check coordinate order when converting from other formats. Swapped coordinates will place your location in the wrong part of the world.
{% endhint %}

For details on geometry structure, winding order for polygons, and coordinate reference systems, see [RFC 7946 Section 3.1](https://www.rfc-editor.org/rfc/rfc7946#section-3.1).

### Custom fields

Geo objects support custom fields. You might want to add fields for:

* Access restrictions (delivery time windows, vehicle type requirements)
* Operational metadata (zone manager contact, capacity limits)
* Business attributes (pricing tier, priority level)

See [Implementing custom fields](implementing-custom-fields.md) for details on defining and using custom fields.

## Example scenario: Delivery service zones

A delivery company needs to define service areas and mark important locations. They start by creating an arrival zone around their main warehouse — a small polygon buffer that lets them detect when vehicles arrive or depart. Then they create a larger delivery zone, verify which addresses fall within it, and adjust boundaries as the business grows.

{% stepper %}
{% step %}
### **Create the arrival zone**

Rather than a `Point`, model the warehouse as a small `Polygon` buffer centered on the building. This lets you use `containsPoints` later to detect vehicle arrivals and departures.

```graphql
mutation CreateWarehouseZone {
  geoObjectCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Main Warehouse - Mitte"
    geometry: {
      type: "FeatureCollection"
      features: [{
        type: "Feature"
        geometry: {
          type: "Polygon"
          coordinates: [
            [
              [13.404754, 52.519808],
              [13.405154, 52.519808],
              [13.405154, 52.520208],
              [13.404754, 52.520208],
              [13.404754, 52.519808]
            ]
          ]
        }
        properties: {}
      }]
    }
  }) {
    geoObject {
      id
      version
      title
      geometry
    }
  }
}
```

The polygon is a small rectangle roughly 30 × 45 meters centered on coordinates `[13.404954, 52.520008]` in Berlin's Mitte district. Adjust the offsets to match your actual site boundary.

The response confirms creation:

```json
{
  "data": {
    "geoObjectCreate": {
      "geoObject": {
        "id": "019a6b2f-793e-807b-8001-555345529b44",
        "version": 1,
        "title": "Main Warehouse - Mitte",
        "geometry": {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [13.404754, 52.519808],
                    [13.405154, 52.519808],
                    [13.405154, 52.520208],
                    [13.404754, 52.520208],
                    [13.404754, 52.519808]
                  ]
                ]
              },
              "properties": {}
            }
          ]
        }
      }
    }
  }
}
```

Save the `id` and `version` — you'll need them for updates.
{% endstep %}

{% step %}
### **Verify the geo object**

Query the geo object to confirm it was created correctly:

```graphql
query GetWarehouseZone {
  geoObject(id: "019a6b2f-793e-807b-8001-555345529b44") {
    id
    version
    title
    type {
      code
      title
    }
    geometry
  }
}
```

The response returns the full geo object:

```json
{
  "data": {
    "geoObject": {
      "id": "019a6b2f-793e-807b-8001-555345529b44",
      "version": 1,
      "title": "Main Warehouse - Mitte",
      "type": {
        "code": "poi",
        "title": "Point of Interest"
      },
      "geometry": {
        "type": "FeatureCollection",
        "features": [
          {
            "type": "Feature",
            "geometry": {
              "type": "Polygon",
              "coordinates": [
                [
                  [13.404754, 52.519808],
                  [13.405154, 52.519808],
                  [13.405154, 52.520208],
                  [13.404754, 52.520208],
                  [13.404754, 52.519808]
                ]
              ]
            },
            "properties": {}
          }
        ]
      }
    }
  }
}
```

The `geometry` field contains the full GeoJSON structure you provided, which you can use to verify the configuration or display on a map in your application.
{% endstep %}

{% step %}
### **Create a polygon-shaped delivery zone**

Create a rectangular delivery zone covering central Berlin:

```graphql
mutation CreateDeliveryZone {
  geoObjectCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"
    title: "Central Berlin Zone"
    geometry: {
      type: "FeatureCollection"
      features: [{
        type: "Feature"
        geometry: {
          type: "Polygon"
          coordinates: [
            [
              [13.35, 52.48],
              [13.45, 52.48],
              [13.45, 52.56],
              [13.35, 52.56],
              [13.35, 52.48]
            ]
          ]
        }
        properties: {}
      }]
    }
  }) {
    geoObject {
      id
      version
      title
      geometry
    }
  }
}
```

Note the coordinate structure:

* The outer array contains one or more rings (here, just one exterior ring).
* Each ring is an array of `[longitude, latitude]` coordinate pairs.
* The first and last coordinates are identical, closing the ring.

The response returns:

```json
{
  "data": {
    "geoObjectCreate": {
      "geoObject": {
        "id": "019a6b30-8a4f-807b-8001-666456630c55",
        "version": 1,
        "title": "Central Berlin Zone",
        "geometry": {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [13.35, 52.48],
                    [13.45, 52.48],
                    [13.45, 52.56],
                    [13.35, 52.56],
                    [13.35, 52.48]
                  ]
                ]
              },
              "properties": {}
            }
          ]
        }
      }
    }
  }
}
```
{% endstep %}

{% step %}
### **Check test point containment**

Check if specific delivery addresses fall within your zone using the `containsPoints` field:

```graphql
query CheckDeliveryAddresses {
  geoObject(id: "019a6b30-8a4f-807b-8001-666456630c55") {
    title
    geometry
    containsPoints(points: [
      { lat: 52.520008, lng: 13.404954 }
      { lat: 52.500000, lng: 13.400000 }
      { lat: 52.600000, lng: 13.300000 }
    ]) {
      index
      point {
        lat
        lng
      }
      isContained
    }
  }
}
```

The response shows which points are inside the zone:

```json
{
  "data": {
    "geoObject": {
      "title": "Central Berlin Zone",
      "geometry": {
        "type": "FeatureCollection",
        "features": [
          {
            "type": "Feature",
            "geometry": {
              "type": "Polygon",
              "coordinates": [
                [
                  [13.35, 52.48],
                  [13.45, 52.48],
                  [13.45, 52.56],
                  [13.35, 52.56],
                  [13.35, 52.48]
                ]
              ]
            },
            "properties": {}
          }
        ]
      },
      "containsPoints": [
        {
          "index": 0,
          "point": { "lat": 52.520008, "lng": 13.404954 },
          "isContained": true
        },
        {
          "index": 1,
          "point": { "lat": 52.500000, "lng": 13.400000 },
          "isContained": true
        },
        {
          "index": 2,
          "point": { "lat": 52.600000, "lng": 13.300000 },
          "isContained": false
        }
      ]
    }
  }
}
```

The first two addresses fall within the zone, while the third is outside. This helps you validate which delivery requests you can accept.

{% hint style="warning" %}
The `containsPoints` method is only available for `Polygon` and `MultiPolygon` geometry types. It tests whether each point falls inside the polygon boundary.
{% endhint %}
{% endstep %}

{% step %}
### **Update the zone boundary**

As your delivery business expands, you need to cover a larger area. Update the zone geometry to extend the boundaries:

```graphql
mutation ExpandDeliveryZone {
  geoObjectUpdate(input: {
    id: "019a6b30-8a4f-807b-8001-666456630c55"
    version: 1
    geometry: {
      type: "FeatureCollection"
      features: [{
        type: "Feature"
        geometry: {
          type: "Polygon"
          coordinates: [
            [
              [13.30, 52.45],
              [13.50, 52.45],
              [13.50, 52.60],
              [13.30, 52.60],
              [13.30, 52.45]
            ]
          ]
        }
        properties: {}
      }]
    }
  }) {
    geoObject {
      id
      version
      geometry
    }
  }
}
```

The `version` parameter ensures you don't accidentally overwrite changes made by someone else. If the version doesn't match, you'll receive a [conflict error](../error-handling.md#version-conflict-409).

The response shows the incremented version:

```json
{
  "data": {
    "geoObjectUpdate": {
      "geoObject": {
        "id": "019a6b30-8a4f-807b-8001-666456630c55",
        "version": 2,
        "geometry": {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Polygon",
                "coordinates": [ "..." ]
              },
              "properties": {}
            }
          ]
        }
      }
    }
  }
}
```
{% endstep %}

{% step %}
### **Delete the geo object**

When you restructure your delivery zones and no longer need this geo object, you can delete it:

```graphql
mutation DeleteDeliveryZone {
  geoObjectDelete(input: {
    id: "019a6b30-8a4f-807b-8001-666456630c55"
    version: 2
  }) {
    deletedId
  }
}
```

The response confirms deletion:

```json
{
  "data": {
    "geoObjectDelete": {
      "deletedId": "019a6b30-8a4f-807b-8001-666456630c55"
    }
  }
}
```
{% endstep %}
{% endstepper %}

## Common GeoJSON patterns

All geometry values in the API are wrapped in a `FeatureCollection`. The examples below show the complete structure you pass in mutations and receive in responses.

### Single location marker (warehouse, customer address)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [13.404954, 52.520008]
      },
      "properties": {}
    }
  ]
}
```

### Rectangular area (simple geofence)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [13.35, 52.48],
            [13.45, 52.48],
            [13.45, 52.56],
            [13.35, 52.56],
            [13.35, 52.48]
          ]
        ]
      },
      "properties": {}
    }
  ]
}
```

### Polygon with exclusion zone (donut-shaped)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [13.30, 52.45],
            [13.50, 52.45],
            [13.50, 52.60],
            [13.30, 52.60],
            [13.30, 52.45]
          ],
          [
            [13.38, 52.50],
            [13.40, 52.50],
            [13.40, 52.52],
            [13.38, 52.52],
            [13.38, 52.50]
          ]
        ]
      },
      "properties": {}
    }
  ]
}
```

The first ring defines the exterior boundary. The second ring creates a hole — an area inside the outer boundary where the polygon doesn't apply. This is useful for delivery zones that exclude certain neighborhoods or restricted areas.

### Route corridor (for deviation detection)

In fleet management, routes are modeled as `Polygon` corridors rather than `LineString` geometries. A corridor is a buffer zone around the intended path: if a vehicle leaves this zone, it has deviated from the route. The example below shows a narrow corridor along a Berlin street segment:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [13.376, 52.515],
            [13.406, 52.519],
            [13.406, 52.521],
            [13.376, 52.517],
            [13.376, 52.515]
          ]
        ]
      },
      "properties": {}
    }
  ]
}
```

Use a wider corridor for highways where minor deviations are acceptable, and a narrower one for city routes requiring precise tracking.

#### Line overlay (visual display only)

Use `LineString` when you need to draw a line on a map for display purposes — for example, to show the planned path of a delivery or the boundary between two zones. A `LineString` has no area and cannot be used for containment checks.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [13.377704, 52.516275],
          [13.404954, 52.520008],
          [13.388175, 52.519444]
        ]
      },
      "properties": {}
    }
  ]
}
```

### Multiple warehouse locations

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "MultiPoint",
        "coordinates": [
          [13.404954, 52.520008],
          [13.410000, 52.515000],
          [13.395000, 52.525000]
        ]
      },
      "properties": {}
    }
  ]
}
```

## Listing geo objects

To retrieve all geo objects for an organization, use this query:

```graphql
query ListGeoObjects {
  geoObjects(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    first: 20
  ) {
    nodes {
      id
      title
      type {
        code
        title
      }
      geometry
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

The response returns a paginated list:

```json
{
  "data": {
    "geoObjects": {
      "nodes": [
        {
          "id": "019a6b2f-793e-807b-8001-555345529b44",
          "title": "Main Warehouse - Mitte",
          "type": {
            "code": "poi",
            "title": "Point of Interest"
          },
          "geometry": {
            "type": "FeatureCollection",
            "features": [
              {
                "type": "Feature",
                "geometry": {
                  "type": "Polygon",
                  "coordinates": [
                    [
                      [13.404754, 52.519808],
                      [13.405154, 52.519808],
                      [13.405154, 52.520208],
                      [13.404754, 52.520208],
                      [13.404754, 52.519808]
                    ]
                  ]
                },
                "properties": {}
              }
            ]
          }
        },
        {
          "id": "019a6b30-8a4f-807b-8001-666456630c55",
          "title": "Central Berlin Zone",
          "type": {
            "code": "geofence",
            "title": "Geofence"
          },
          "geometry": {
            "type": "FeatureCollection",
            "features": [
              {
                "type": "Feature",
                "geometry": {
                  "type": "Polygon",
                  "coordinates": [
                    [
                      [13.35, 52.48],
                      [13.45, 52.48],
                      [13.45, 52.56],
                      [13.35, 52.56],
                      [13.35, 52.48]
                    ]
                  ]
                },
                "properties": {}
              }
            ]
          }
        }
      ],
      "pageInfo": {
        "hasNextPage": false,
        "endCursor": "YXJyYXljb25uZWN0aW9uOjE="
      }
    }
  }
}
```

You can filter by type or search by title:

```graphql
query ListDeliveryZones {
  geoObjects(
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    filter: {
      typeIds: ["b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"]
      titleContains: "berlin"
    }
    first: 20
  ) {
    nodes {
      id
      title
    }
  }
}
```

The response returns only matching geo objects:

```json
{
  "data": {
    "geoObjects": {
      "nodes": [
        {
          "id": "019a6b30-8a4f-807b-8001-666456630c55",
          "title": "Central Berlin Zone"
        }
      ]
    }
  }
}
```

For more on filtering and pagination, see [Filtering and sorting](../filtering-and-sorting.md) and [Pagination](../pagination.md).

## Handling version conflicts

If you include `version` in your mutation and the entity has been modified since you last fetched it, the API returns a conflict error:

```json
{
  "errors": [
    {
      "message": "Entity has been modified by another request",
      "path": ["geoObjectUpdate"],
      "extensions": {
        "type": "https://api.navixy.com/errors/conflict",
        "title": "Conflict",
        "status": 409,
        "detail": "GeoObject 019a6b30-... was modified. Expected version 2, current version 3.",
        "code": "CONFLICT",
        "entityType": "GeoObject",
        "entityId": "019a6b30-8a4f-807b-8001-666456630c55",
        "expectedVersion": 2,
        "currentVersion": 3,
        "traceId": "0af7651916cd43dd8448eb211c80319c"
      }
    }
  ]
}
```

To resolve this:

1. Query the geo object to get the current version and geometry
2. Merge your changes with the current state
3. Retry the mutation with the correct version

For more details on version conflicts, see [Optimistic locking](../optimistic-locking.md).

### See also

* [Geo objects reference](../geo-objects/): A complete list of all operations and types related to geo objects
* [Filtering and sorting](../filtering-and-sorting.md): Full operator reference and value formats for custom field filters
* [Optimistic locking](../optimistic-locking.md): How `version` works in update and delete mutations
