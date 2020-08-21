---
title: Map layer
description: Map layer
---

# Map layer

API path: `/map_layer`.

`map_layer_object` is:
```json
{
    "id": <int>,      // map layer entity ID
    "label": <string> // map layer name, e.g. "test"
}
```

### read
Read the body of the specified layer.

#### parameters
name | description | type
--- | --- | ---
id | ID of the map layer | Int

#### response
Layer body with content-type: `application/vnd.google-earth.kml+xml; charset=utf-8`.

#### errors
* 201 (Not found in database) – if there is no map layer with such ID belonging to current user

### list
Returns metadata for all map layers for the user.

#### response
```json
{
    "success": true,
    "list": [<map_layer_object>, ... ]
}
```

#### errors
No specific errors.

### upload
Uploads new map layer.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a KML file upload (with the name “file”).

#### parameters
name | description | type
--- | --- | ---
label | Label for a new map layer | string
file | A KML file upload containing map_layer data | File upload
redirect_target | (optional) URL to redirect. If **redirect_target** passed return redirect to *&lt;redirect_target&gt;?response=&lt;urlencoded_response_json&gt;* | String


#### response
```json
{
    "success": true,
    "id": 163 // int. ID of the created layer
}
```

#### errors
* 233 (No data file – if file part is missing
* 234 (Invalid data format – if file has wrong mime type
* 242 (Validation error – if uploaded file is not valid KML
* 268 (Over quota – if the user's quota for map layers is exceeded

### update
Update metadata for the specified map layer.

#### parameters
name | description | type
--- | --- | ---
layer | &lt;map_layer_object&gt; | JSON object

#### response
```json
{ "success": true }
```

#### errors
* 201 (Not found in database) – if there is no map layer with such ID belonging to current user

### delete
Delete specified layer.

#### parameters
name | description | type
--- | --- | ---
id | ID of the map layer | Int

#### response
```json
{ "success": true }
```

#### errors
* 201 (Not found in database) – if there is no map layer with such ID belonging to current user
