---
title: Working with geofences
description: This document contains zone object description and CRUD actions for geofences.
---

# Working with geofences

Geofences used in rules to limit rule area of activity. Also, geofence names shown in reports after the address, if 
an event happened inside the geofence.

This document describes CRUD actions for geofences. Note that geofence points handled separately because they are 
represented by big arrays of data.

Find instructions on working with geofences of different types [here](../../../guides/places/manage-geofences.md).


## Entity description

**zone** is JSON object with one of types: `sausage`, `circle` or `polygon`.

#### circle:

```json
{
  "id": 985472,
  "type": "circle",
  "label": "Zone name",
  "address": "Karlsplatz, 2",
  "color": "27A9E3",
  "radius": 150,
  "center": {
    "lat": 48.200940,
    "lng": 16.369856
  },
  "bounds": {
    "nw": {
      "lat": 48.202289,
      "lng": 16.367832
    },
    "se": {
      "lat": 48.199591,
      "lng": 16.371880
    }
  },
  "tags": [127, 15]
}
```

* `id` - int. Geofence ID.
* `label` - string. Geofence label.
* `address` - string. Geofence address.
* `color` - string. Geofence color in 3-byte RGB hex format.
* `radius` - int. Circle radius in meters.
* `center` - location object. Location of circle center.
* `bounds` - object. North-west and south-east coordinates of the axis-aligned minimum bounding box.
* `tags` - int array. Array of tag IDs.


#### polygon:

```json
{
  "id": 124597,
  "type": "polygon",
  "label": "Geofence name",
  "address": "Karlsplatz, 2",
  "color": "27A9E3",
  "points": [<point>, ...],
  "bounds": {
    "nw": {
      "lat": 48.202289,
      "lng": 16.367832
    },
    "se": {
      "lat": 48.199591,
      "lng": 16.371880
    }
  },
  "tags": [1, 236]
}
```

* `id` - int. Geofence ID.
* `label` - string. Geofence label.
* `address` - string. Geofence address.
* `color` - string. Geofence color in 3-byte RGB hex format.
* `points` - optional array of objects. [Geofence points](zone_point.md)
* `bounds` - object. North-west and south-east coordinates of the axis-aligned minimum bounding box that contains all points.
* `tags` - int array. Array of tag IDs.


#### sausage:

Represents all points within certain distance to the specified polyline.

```json
{
  "id": 12345,
  "type": "sausage",
  "label": "Geofence name",
  "address": "Karlsplatz, 2",
  "color": "27A9E3",
  "radius": 150,
  "points": [<point>, ...],
  "bounds": {
    "nw": {
      "lat": 48.202289,
      "lng": 16.367832
    },
    "se": {
      "lat": 48.199591,
      "lng": 16.371880
    }
  },
  "tags": [289]
}
```

* `id` - int. Geofence ID.
* `label` - string. Geofence label.
* `address` - string. Geofence address.
* `color` - string. Geofence color in 3-byte RGB hex format.
* `radius` - int. Polyline radius in meters.
* `points` - optional array of objects. [Geofence points](zone_point.md)
* `bounds` - object. North-west and south-east coordinates of the axis-aligned minimum bounding box that contains all points with a radius.
* `tags` - int array. Array of tag IDs.


## API actions

API base path: `/zone`.

### batch_convert

Convert batch of tab-delimited circle geofences and return list of checked geofences with errors.

**required sub-user rights**: `zone_update`.

#### Parameters

| name           | description                                                                                             | type                                                 |
|:---------------|:--------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|
| batch          | Batch of tab-delimited places.                                                                          | string                                               |
| file_id        | ID of file preloaded with [/data/spreadsheet/parse](../../commons/data.md#dataspreadsheetparse) method. | string                                               |
| fields         | Optional, array of field names, default is `["label", "address", "lat", "lng", "radius", "tags"]`.      | [enum](../../../getting-started/introduction.md#data-types) array |
| geocoder       | Optional. Geocoder type.                                                                                | [enum](../../../getting-started/introduction.md#data-types)       |
| default_radius | Optional. Radius for point, default is 100.                                                             | int                                                  |

If 'file_id' is set – 'batch' parameter will be ignored.

For `batch` parameter:
* address - required if `coordinates` are not specified.
* lat - required if `address` is not specified.
* lng - required if `address` is not specified.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/batch_convert' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "batch": "Geofence for test Karlsplatz, 2"}'
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": null,
      "type": "circle",
      "label": "Geofence name",
      "address": "Karlsplatz, 2",
      "color": "27A9E3",
      "radius": 100,
      "center": {
        "lat": 48.2009935,
        "lng": 16.3699642
      },
      "bounds": {
        "nw": {
          "lat": 48.202289,
          "lng": 16.367832
        },
        "se": {
          "lat": 48.199591,
          "lng": 16.371880
        }
      },
      "tags": []
    }
  ],
  "limit_exceeded": false
}
```

* `id` - int. Geofence ID.
* `label` - string. Geofence label.
* `address` - string. Geofence address.
* `color` - string. Geofence color in 3-byte RGB hex format.
* `radius` - int. Circle radius in meters.
* `center` - location object. Location of the circle center.
* `bounds` - object. North-west and south-east coordinates of the axis-aligned minimum bounding box.
* `tags` - int array. Array of tag IDs.
* `limit_exceeded` - boolean. `true` if given batch constrained by limit.

#### Response with errors object

```json
{
  "success": true,
  "list": [
    {
      "id": null,
      "label": "Geofence name",
      "address": "incorrect address",
      "color": "27A9E3",
      "radius": 100,
      "center": {
        "lat": 0.0,
        "lng": 0.0
      },
      "errors": [
        {
          "parameter": "zone.center",
          "error": "Location should be correct with 'lat' and 'lng' not null"
        }
      ],
      "tags": []
    }
  ],
  "limit_exceeded": false
}
```

* `errors` - optional object. It appears if parameters are incorrect.
    * `parameter` - string. Parameter name.
    * `error` - string. Error description.

#### Errors

* 234 - Invalid data format.


### `create`

Creates a new geofence.

**required sub-user rights**: `zone_update`.

#### Parameters

| name       | description                                                                                                                                                                               | type                          |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| zone       | zone JSON-object without `id` and `color` fields.                                                                                                                                         | JSON object                   |
| points     | Array of new [points](zone_point.md) for this geofence. Must contain at least 3 elements. MUST be omitted if zone does not support points (e.g. circle). | array of `zone point` objects |
| zone.color | Optional. Geofence color in 3-byte RGB hex format. Default is "27A9E3".                                                                                                                   | string                        |


#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Circle geofence", "type": "circle", "center": {"lat": 61.49504550221769, "lng": 23.775476217269897}, "radius": 50, "tags": [179227], "color": "03A9F4", "address":"Address"}}'
    ```

#### Response

```json
{
  "success": true,
  "id": 1234567
}
```

* `id` - int. An ID of the created geofence.

#### Errors

* 202 - Too many points in a geofence – max allowed count of points for a geofence is 500 for a polygon or 1024 for sausage.
* 230 - Not supported for this entity type – if "points" were specified, but geofence cannot have any points associated with
  it (e.g. if geofence is circle).
* 268 - Over quota –  if the user's quota for geofences exceeded.
* 284 - Not enough points for the zone. The minimum number of points for polygon: 3; the minimum for sausage: 2.


### `delete`

Deletes user's geofence by `zone_id` or array of `zone_ids`.

**required sub-user rights**: `zone_update`.

#### Parameters

| name     | description            | type      | format               |
|:---------|:-----------------------|:----------|:---------------------|
| zone_id  | ID of a geofence.      | int       | 1234567              |
| zone_ids | Array of geofence IDs. | int array | `[1234567, 2345678]` |

* Use only one parameter `zone_id` or `zone_ids`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone_id": 1234567}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/zone/delete?hash=a6aa75587e5c59c32d347da438505fc3&zone_id=1234567
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 - Not found in the database.
* 203 - Delete entity associated with.

```json
{
  "success": false,
  "status": {
    "code": 203,
    "description": "Delete entity associated with"
  },
  "entities": [
    {
      "type": "rules",
      "ids": [12345, 23456]
    }
  ]
}
```

* `ids` - int array. List IDs of the rules which uses the specified geofence.


### `list`

Gets all user geofences.

#### Parameters

| name        | description                                                                                           | type      | 
|:------------|:------------------------------------------------------------------------------------------------------|:----------|
| filter      | Optional. Filter for geofences label and description.                                                 | string    |
| tag_ids     | Optional. Tag IDs assigned to the geofences. The zones found must include all the tags from the list. | int array |
| offset      | Optional. Offset from start of the found geofences for pagination.                                    | int       |
| limit       | Optional. Limit of the found geofences for pagination.                                                | int       |
| with_points | Optional, default=`false`. If `true`, return geofence with its [points](zone_point.md)                | boolean   |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/zone/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 12345,
      "type": "sausage",
      "label": "Zone name",
      "address": "Karlsplatz, 2",
      "color": "27A9E3",
      "radius": 150,
      "points": [<point>, ...],
      "tags": [289]
    }
  ]
}
```

* `list` - array of objects. Geofence objects with optional points field.


### `read`

Gets geofence by specified ID.

#### Parameters

| name        | description                                                                            | type    | 
|:------------|:---------------------------------------------------------------------------------------|:--------|
| zone_id     | ID of a geofence.                                                                      | int     |
| with_points | Optional, default=`false`. If `true`, return geofence with its [points](zone_point.md) | boolean |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone_id": 12345}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/zone/read?hash=a6aa75587e5c59c32d347da438505fc3&zone_id=12345
    ```

#### Response

```json
{
  "success": true,
  "value": {
    "id": 12345,
    "type": "sausage",
    "label": "Zone name",
    "address": "Karlsplatz, 2",
    "color": "27A9E3",
    "radius": 150,
    "points": [<point>, ...],
    "tags": [289]
  }
}
```

* `value` - Geofence object with optional points field.


### `search_location`

Gets all geofence IDs and names within which a specified coordinates are located inside.

#### Parameters

| name     | description                                                                                                   | type        |
|:---------|:--------------------------------------------------------------------------------------------------------------|:------------|
| location | Location coordinates (see: [data types description section](../../../getting-started/introduction.md#data-types) section). | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/search_location' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "location": {"lat": 34.178868, "lng": -118.599672}}'
    ```

#### Response

```json
{
  "list": [
    {
      "id": 18404,
      "label": "geofence 1"
    },
    {
      "id": 35284,
      "label": "geofence 2"
    }
  ],
  "success": true
}
```

* `id` - int. Geofence ID that containing a searched location. 
* `label` - string. Geofence name.


### `update`

Update geofence parameters for the specified geofence.

!!! note "Notes"

    - The geofence must exist, belong to the current user, and its type cannot be modified.
    For example, if you already have a geofence with ID=1 of type "circle",
    you cannot submit a geofence with the same ID but of type "polygon".
    - If the `zone` object is of type `sausage` or `polygon` and contains an array of points, these points will be updated.
    Alternatively, you can update the points using the [zone/point/update](zone_point.md#update) endpoint.

**required sub-user rights**: `zone_update`.

#### Parameters

| name       | description                                                             | type        |
|:-----------|:------------------------------------------------------------------------|:------------|
| zone       | Geofence JSON-object with `id` and `color` fields.                      | JSON object |
| zone.color | Optional. Geofence color in 3-byte RGB hex format. Default is "27A9E3". | string      |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"id": 231512 "label": "Circle geofence", "type": "circle", "center": {"lat": 61.49504550221769, "lng": 23.775476217269897}, "radius": 50, "tags": [179227], "color": "03A9F4", "address":"Address"}}'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 - Not found in the database: if the geofence with specified ID cannot be found or belongs to another user.
* 231 - Entity type mismatch: if the type of submitted geofence differs from the type of geofence currently stored in the 
  database.


### `upload`

Import geofences from a KML file.

**required sub-user rights**: `zone_update`.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a KML file upload 
(with the name "file").

#### Parameters

| name            | description                                                                                                                         | type        |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------|:------------|
| file            | A KML file upload containing geofences data.                                                                                        | file upload |
| default_radius  | Default radius for circle and route geofence in meters. Min 20, default 150.                                                        | int         |
| dry_run         | If `true` returns ready to create geofences or creates it and returns list of IDs otherwise. Default `true`.                        | boolean     |
| redirect_target | Optional. URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>` | string      |

#### Responses

if `dry_run=true`:
```json
{
  "success": true,
  "list": [
    {
      "id": null,
      "label": "Simple line 1",
      "address": "",
      "color": "27A9E3",
      "points": [
        {
          "lat": 37.818844,
          "lng": -122.366278,
          "node": true
        },
        {
          "lat": 37.819267,
          "lng": -122.365248,
          "node": false
        },
        {
          "lat": 37.819861,
          "lng": -122.36564,
          "node": false
        },
        {
          "lat": 37.819429,
          "lng": -122.366669,
          "node": true
        }
      ],
      "radius": 150,
      "type": "sausage"
    }
  ]
}
```

if `dry_run=false`:

```json
{
  "success": true,
  "list": [1, 2]
}
```

#### Errors

* 202 - Too many points in a geofence – max allowed count of points for a geofence is 500 for a polygon or 1024 for sausage.
* 233 - No data file – if file part is missing.
* 234 - Invalid data format.
* 268 - Over quota – if the user's quota for geofences exceeded.
* 284 - Not enough points for the zone. The minimum number of points for polygon: 3; the minimum for sausage: 2.


From `Placemark` with `Point` geometry will be created circle geofence using the radius from extended data or the default value if not specified.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Points</name>
        <ExtendedData>
            <Data name="radius">
                <value>300</value>
            </Data>
        </ExtendedData>
        <Placemark>
            <name>named point</name>
            <Point>
                <coordinates>
                    -122.366278,37.818844,30
                </coordinates>
            </Point>
        </Placemark>
    </Document>
</kml>
```


From `Placemark` with `LineString` geometry will be created route geofence using the radius from extended data or the default value if not specified.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Simple line</name>
        <ExtendedData>
            <Data name="radius">
                <value>300</value>
            </Data>
        </ExtendedData>
        <Placemark>
            <LineString>
                <coordinates>
                    -122.366278,37.818844,30
                    -122.365248,37.819267,30
                    -122.365640,37.819861,30
                    -122.366669,37.819429,30
                </coordinates>
            </LineString>
        </Placemark>
    </Document>
</kml>
```


From `Placemark` with `Polygon` geometry will be created polygon geofence.
Polygons with holes are not supported. In that case, only the outer boundary will be imported and the inner boundary, holes, 
ignored.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Simple polygon</name>
        <Placemark>
            <name>hollow box</name>
            <Polygon>
                <outerBoundaryIs>
                    <LinearRing>
                        <coordinates>
                            -122.366278,37.818844,30
                            -122.365248,37.819267,30
                            -122.365640,37.819861,30
                            -122.366669,37.819429,30
                            -122.366278,37.818844,30
                        </coordinates>
                    </LinearRing>
                </outerBoundaryIs>
            </Polygon>
        </Placemark>
    </Document>
</kml>
```


From `Placemark` with `MultiGeometry` geometry will be created several geofences.
If `Placemark.name` defined it will be used as geofence name with respect of hierarchy of `Folder` and `Document`.


### `download`

Download geofences as KML File.

#### Parameters

| name     | description                                                                           | type                                                        |
|:---------|:--------------------------------------------------------------------------------------|:------------------------------------------------------------|
| format   | Optional. File format, either "kml" or "kmz". Default is "kml".                       | [enum](../../../getting-started/introduction.md#data-types) |
| zone_ids | Optional. Array of geofence IDs. If null, all available geofences will be downloaded. | int array                                                   |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

#### Response

A KML/KMZ file with the points (standard file download).

!!! example "Example of a KML file with different geofences"

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<kml xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
    <Document>
        <name>zones</name>
        <Placemark>
            <name>polygon_zone</name>
            <visibility>1</visibility>
            <Polygon>
                <outerBoundaryIs>
                    <LinearRing>
                        <coordinates>44.7489290062,41.7201261755 44.7572878562,41.7208046390 44.7562364303,41.7190268459</coordinates>
                    </LinearRing>
                </outerBoundaryIs>
            </Polygon>
        </Placemark>
        <Placemark>
            <name>circle_zone</name>
            <visibility>1</visibility>
            <ExtendedData>
                <Data name="radius">
                    <value>300</value>
                </Data>
            </ExtendedData>
            <Point>
                <coordinates>44.7463912723,41.7096716534</coordinates>
            </Point>
        </Placemark>
        <Placemark>
            <name>sausage_zone</name>
            <visibility>1</visibility>
            <ExtendedData>
                <Data name="radius">
                    <value>300</value>
                </Data>
            </ExtendedData>
            <LineString>
                <coordinates>44.7288827746,41.7176609187 44.7340679137,41.7181063157 44.7384917427,41.7187820845</coordinates>
            </LineString>
        </Placemark>
    </Document>
</kml>
```
