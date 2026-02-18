---
description: Create geofences, POIs, and routes in different shapes using GeoJSON geometry.
---

# Working with geo objects

Geo objects in Navixy Repository API represent geographic features like geofences, points of interest, and routes. They store location data in GeoJSON format, making them useful for defining delivery zones, marking important locations, creating routes, and managing areas where your fleet operates.

This guide walks you through creating, updating, and managing geo objects with different geometry types.

## Before you start

To work with geo objects, you need your organization's ID. Use the [me](https://claude.ai/operations-and-types/queries.md#me) query to find it through your membership:

```graphql
query GetMyOrganization {
  me {
    memberships {
      organization {
        id
        title
      }
    }
  }
}
```

In most cases, you'll have one organization in the response. Use its `id` for geo object operations.

### Check the available geo object types

Before creating a geo object, list the available types to see what options exist:

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

This returns system types and any custom types your organization has created.

If you don't see a type you need, create one:

```graphql
mutation CreateGeoObjectType {
  geoObjectTypeCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    code: "delivery_zone_1"
    title: "Delivery Zone 1"
  }) {
    geoObjectType {
      id
      code
      title
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

### Supported geometry types

<table><thead><tr><th width="150.5999755859375">Geometry type</th><th width="336.2000732421875">Use case</th><th>Example</th></tr></thead><tbody><tr><td>Point</td><td>Single location (delivery stop, warehouse, customer address)</td><td>POI marker</td></tr><tr><td>Polygon</td><td>Area boundary (delivery zone, service area, restricted region)</td><td>Geofence</td></tr><tr><td>LineString</td><td>Route or path (delivery route, patrol path)</td><td>Navigation path</td></tr><tr><td>MultiPoint</td><td>Multiple separate locations</td><td>Distribution network</td></tr><tr><td>MultiLineString</td><td>Multiple routes</td><td>Alternative paths</td></tr><tr><td>MultiPolygon</td><td>Multiple areas</td><td>Non-contiguous zones</td></tr></tbody></table>

### Coordinate format

GeoJSON uses `[longitude, latitude]` order, which is opposite to how coordinates are often written in text.

```
Text format:     52.520008, 13.404954 (latitude, longitude)
GeoJSON format:  [13.404954, 52.520008] (longitude, latitude)
```

For example, Berlin's Brandenburg Gate is located at latitude 52.516275 and longitude 13.377704. In GeoJSON, this becomes `[13.377704, 52.516275]`.

{% hint style="danger" %}
Always double-check coordinate order when converting from other formats. Swapped coordinates will place your location in the wrong part of the world.
{% endhint %}

For details on geometry structure, winding order for polygons, and coordinate reference systems, see [RFC 7946 Section 3.1](https://www.rfc-editor.org/rfc/rfc7946#section-3.1).

### Custom fields

Like other entities in the API, geo objects support custom fields. You might add fields for:

* Access restrictions (delivery time windows, vehicle type requirements)
* Operational metadata (zone manager contact, capacity limits)
* Business attributes (pricing tier, priority level)

See [Working with custom fields](https://claude.ai/chat/working-with-custom-fields.md) for details on defining and using custom fields.

## Example scenario: Delivery service zones

A delivery company needs to define service areas and mark important locations. They start with a warehouse location, create a delivery zone around it, verify which addresses fall within the zone, and adjust boundaries as the business grows.

{% stepper %}
{% step %}
#### Create a Point location (warehouse)

Start by marking your main warehouse location with a `Point` type:

```graphql
mutation CreateWarehouseLocation {
  geoObjectCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    title: "Main Warehouse - Mitte"
    geometry: {
      type: "Point"
      coordinates: [13.404954, 52.520008]
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

The coordinates `[13.404954, 52.520008]` represent a location in Berlin's Mitte district (longitude 13.404954, latitude 52.520008).

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
          "type": "Point",
          "coordinates": [13.404954, 52.520008]
        }
      }
    }
  }
}
```

Save the `id` and `version` — you'll need them for updates.
{% endstep %}

{% step %}
#### Verify the geo object

Query the geo object to confirm it was created correctly:

```graphql
query GetWarehouseLocation {
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

The `geometry` field returns the full GeoJSON structure you provided, which you can use to verify the configuration or display on a map in your application.
{% endstep %}

{% step %}
#### Create a polygon-shaped delivery zone

Create a rectangular delivery zone covering central Berlin:

```graphql
mutation CreateDeliveryZone {
  geoObjectCreate(input: {
    organizationId: "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    typeId: "b1ffcd00-0d1c-5fg9-cc7e-7cc0ce491b22"
    title: "Central Berlin Zone"
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
  }) {
    geoObject {
      id
      version
      title
    }
  }
}
```

Note the coordinate structure:

* The outer array contains one or more rings (here, just one exterior ring)
* Each ring is an array of `[longitude, latitude]` coordinate pairs
* The first and last coordinates are identical, closing the ring

The response returns:

```json
{
  "data": {
    "geoObjectCreate": {
      "geoObject": {
        "id": "019a6b30-8a4f-807b-8001-666456630c55",
        "version": 1,
        "title": "Central Berlin Zone"
      }
    }
  }
}
```
{% endstep %}

{% step %}
#### Test point containment

Check if specific delivery addresses fall within your zone using the `containsPoints` method:

```graphql
query CheckDeliveryAddresses {
  geoObject(id: "019a6b30-8a4f-807b-8001-666456630c55") {
    title
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
**Update the zone boundary**

As your delivery business expands, you need to cover a larger area. Update the zone geometry to extend the boundaries:

```graphql
mutation ExpandDeliveryZone {
  geoObjectUpdate(input: {
    id: "019a6b30-8a4f-807b-8001-666456630c55"
    version: 1
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
          "type": "Polygon",
          "coordinates": [ ... ]
        }
      }
    }
  }
}
```
{% endstep %}

{% step %}
#### Delete the geo object

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

The `version` parameter ensures you don't accidentally delete a geo object that someone else has modified. If the version doesn't match, you'll receive a [conflict error](../error-handling.md#version-conflict-409).
{% endstep %}
{% endstepper %}

## Common GeoJSON patterns

### Single location (warehouse, customer address)

```json
{
  "type": "Point",
  "coordinates": [13.404954, 52.520008]
}
```

### Rectangular area (simple geofence)

```json
{
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
}
```

### Polygon with exclusion zone (donut-shaped)

```json
{
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
}
```

The first ring defines the exterior boundary. The second ring creates a hole — an area inside the outer boundary where the polygon doesn't apply. This is useful for delivery zones that exclude certain neighborhoods or restricted areas.

### Delivery route

```json
{
  "type": "LineString",
  "coordinates": [
    [13.377704, 52.516275],
    [13.404954, 52.520008],
    [13.388175, 52.519444]
  ]
}
```

### Multiple warehouse locations

```json
{
  "type": "MultiPoint",
  "coordinates": [
    [13.404954, 52.520008],
    [13.410000, 52.515000],
    [13.395000, 52.525000]
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

For more on filtering and pagination, see [Filtering and sorting](../filtering-and-sorting.md) and [Pagination](../pagination.md).

## Handling version conflicts

If someone else updates the geo object while you're working on it, your mutation will fail with a conflict error:

```json
{
  "errors": [
    {
      "message": "Entity has been modified by another request",
      "extensions": {
        "code": "CONFLICT",
        "status": 409,
        "expectedVersion": 2,
        "currentVersion": 3
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

### Next steps

* TBD
