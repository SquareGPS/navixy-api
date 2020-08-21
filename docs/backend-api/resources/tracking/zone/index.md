---
title: Working with zones
description: Working with zones
---

# Working with zones

Zones are used in rules to limit rule area of activity. Also zone names are shown in reports after the address, if 
an event happened inside the zone.

This document describes CRUD actions for zones. Note that zone points are handled separately because they are 
represented by big arrays of data.

## Entity description

**zone** is JSON object with one of types: **sausage**, **circle** or **polygon**.

#### circle:
```json5
{
    "id": 1,                    // (int) zone ID
    "type": "circle",
    "label": "Zone name",       // (string) zone label
    "address": "Karlsplatz, 2", // (string) zone address
    "color": "27A9E3",          // (string) zone color in 3-byte RGB hex format
    "radius": 150,              // (int) circle radius in meters
    "center": {                 // (location object) location of circle center
        "lat": 48.200940,
        "lng": 16.369856
    },
    "tags": [127, 15]           // ([int]) array of tag IDs
}
```

#### polygon:
```json5
{
    "id": 1,                    // (int) zone ID
    "type": "polygon",
    "label": "Zone name",       // (string) zone label
    "address": "Karlsplatz, 2", // (string) zone address
    "color": "27A9E3",          // (string) zone color in 3-byte RGB hex format
    "tags": []                  // ([int]) array of tag IDs
}
```

#### sausage:
represents all points within certain distance to the specified polyline
```json5
{
    "id": 1,                    // (int) zone ID
    "type": "sausage",
    "label": "Zone name",       // (string) zone label
    "address": "Karlsplatz, 2", // (string) zone address
    "color": "27A9E3",          // (string) zone color in 3-byte RGB hex format
    "radius": 150,              // (int) polyline radius in meters
    "tags": [289]               // ([int]) array of tag IDs
}
```                   

## API actions

API base path: `/zone`

### batch_convert
Convert batch of tab-delimited circle zones and return list of checked zones with errors.

**required subuser rights**: zone_update
```json5
<checked_task> =
   {
        ... //all fields from zones
        "errors": <array of objects> // optional
    }
```

#### parameters
*   **batch** (string) – batch of tab-delimited places.
*   **file_id** (string) – ID of file preloaded with [/data/spreadsheet/parse](../../commons/data.md#dataspreadsheetparse) method.
*   **fields** (array of String) – Optional, array of field names, default is `["label", "address", "lat", "lng", "radius", "tags"]`.
*   **geocoder** (string) – geocoder type
*   **default_radius** (Integer) – Optional, radius for point, default is 100

If ‘file_id’ is set – ‘batch’ parameter will be ignored.

#### response
```json5
{
    "success": true,
    "list": [ <checked_zone>, ... ]
}
```

#### errors
* 234 (Invalid data format)


### create
Create new zone.

**required subuser rights**: zone_update

#### parameters
* **zone** – zone JSON-object without “id” field
* **points** (point[]) – Array of new points for this zone. Must contain at least 3 elements. MUST be omitted if zone does not support points (e.g. circle)

**zone.color** is optional here.

#### response
```json5
{
    "success": true,
    "id": ${int} // ID of the created zone
}
```

#### errors
*   202 (Too many points in zone) – max allowed points count for zone is 100 for polygon or 1024 for sausage
*   230 (Not supported for this entity type) – if “points” were specified, but zone cannot have any points associated with it (e.g. if zone is circle)
*   268 (Over quota) –  if the user's quota for zones is exceeded

### delete
Delete user’s zone by **zone_id** or array of **zone_ids**.

**required subuser rights**: zone_update

#### parameters
*   zone_id – int

OR

*   zone_ids – array of int

#### response
```json5
{ "success": true }
```

#### errors
*   201 (Not found in database)
*   203 (Delete entity associated with)

#### response
```json5
{
    "success": false,
    "status": {
        "code": 203,
        "description": "Delete entity associated with"
    },
    "entities": [
        {
            "type": "rules",
            "ids": [<rule_id>, ...]
        }
    ]
}
```

where `<rule_id>` is ID of the rule which uses the specified zone.

### list
Get all user’s zones.

#### response
```json5
{
    "success": true,
    "list": [ <zone>, ... ]
}
```

with `<zone>` without points field.

### update
Update zone parameters for the specified zone. Note that zone must exist, must belong to the current user, and its type cannot be changed, e.g. if you already have zone with ID=1 which type is “circle”, you cannot submit a zone which type is “polygon”.

**required subuser rights**: zone_update

#### parameters
*   **zone** – [JSON-object](#zone)

**zone.color** is optional. If it not passed then color will not be changed.

#### response
```json5
{ "success": true }
```

#### errors
*   201 (Not found in database) – if zone with the specified ID cannot be found or belongs to another user
*   231 (Entity type mismatch) – if type of the submitted zone differs from type of the zone currently stored in database.


### upload
Import geofences from KML file.

**required subuser rights**: zone_update

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a KML file upload (with the name “file”).

#### parameters
*   **file** – (File upload) A KML file upload containing geofences data
*   **default_radius** – (Int) default radius for circle and route geofences, meters, min 20, default 150
*   **dry_run** – (Boolean) if true returns ready to create geofences or creates it and returns list of IDs otherwise, default true
*   **redirect_target** – (String, optional) URL to redirect. If **redirect_target** passed return redirect to *&lt;redirect_target&gt;?response=&lt;urlencoded_response_json&gt;*

#### response
if `dry_run=true`:
```json5
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
```json5
{
    "success": true,
    "list": [ 1, 2 ]
}
```

#### errors
*   202 (Too many points in zone) – max allowed points count for zone is 100 for polygon or 1024 for sausage.
*   233 (No data file) – if file part is missing
*   234 (Invalid data format)
*   268 (Over quota) – if the user's quota for zones is exceeded

From Placemark with Point geometry will be created circle geofence with radius=default_radius.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Points</name>
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

From Placemark with LineString geometry will be created route geofence with radius=default_radius.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Simple line</name>
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

From Placemark with Polygon geometry will be created polygon geofence.
Polygons with holes are not supported. In that case only the outer boundary will be imported and the inner boundary, holes, ignored.
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
