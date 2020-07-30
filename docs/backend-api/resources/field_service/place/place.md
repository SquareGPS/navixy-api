---
title: Place
description: Place
---

# Place

API path: `/place`.

**place** is:
```js
{
    "id": 1, // int
    "icon_id" : 55, // int, optional, [1..255], can only be updated via avatar/assign()
    "avatar_file_name": null, // string, optional
    "location": {
        "lat": 52.366,
        "lng": 4.895,
        "address": "Halvemaansteeg, 3, Amsterdam, North Holland, Netherlands, 1017 CR",
        "radius": 500
    },
   "fields": { //Optional. A map, each key of which is a custom field id *as a string*. See entity/fields
        "131312" : {
             "type": "text",
             "value":  "I love text!"
        }
   }
    "label": "Baba",
    "description": "Best place at http://navixy.com",  // string, optional
    "tags": [ 1, 2 ],   // list of ints, optional, non-empty
    "external_id": "1"  // string, optional, max length 32
}
```

## read()
Get place by ID.

#### parameters
|name |description |type |
|:--- |:--- |:--- |
|place_id |ID of the place |int |

#### return
```js
{
    "success": true,
    "value": <place>
}
```
#### errors
* 201 (Not found in database) – if there is no place with such ID

## list()
Get places belonging to user.

#### parameters
name | description | type
--- | --- | ---
place_ids | optional, list of place IDs | array of ints
filter | optional, filter for all built-in and custom fields. If used with conditions, both filter and conditions must match for every returned place. | string
conditions | optional, search conditions to apply to list. | Array of search conditions, see [Search conditions](../../commons/entity/search_conditions.md)
order_by | built-in or custom field according to which output should be sorted | entity field name, e.g "label" (builtin) or "123" (field id as string, see [entity/](../../commons/entity/entity.md)
ascending | optional, if false – descending order | boolean
limit | optional, limit | int
offset | optional, offset, default is 0 | int

#### return
```js
{
    "success": true,
    "list": [ <place>, ... ],
    "count": 1 // found places count
}
```

#### errors
general types only

## create()
Create new place.

**required subuser rights:** place_update

#### parameters
name | description | type
--- | --- | ---
place | &lt;place&gt; | JSON object
ignore_missing_fields | Optional (default is false). If set to true, place can be created even without all required custom fields.| boolean 

#### return
```js
{
    "success": true,
    "id": 111 // ID of the created place
}
```

#### errors
* 268 (Over quota) – if the user's quota for places is exceeded

## update()
Update existing place.

**required subuser rights:** place_update

#### parameters
name | description | type
--- | --- | ---
place | &lt;place&gt; | JSON object

#### return
```json
{ "success": true }
```

#### errors
* 201 (Not found in database) – if there is no place with such ID

## delete()
Delete place with the specified ID.

**required subuser rights:** place_update

#### parameters
name | description | type
--- | --- | ---
place_id | ID of the place to delete | int

#### return
```json
{ "success": true }
```

#### errors
* 201 (Not found in database) – if there is no place with such ID

## batch_convert()
Convert batch of tab-delimited places and return list of checked places with errors.

**required subuser rights:** place_update

#### parameters
name | description | type
--- | --- | ---
batch | batch of tab-delimited places. | String
file_id | preloaded file ID | String
fields | Optional, array of field names, default is [“label”, “address”, “lat”, “lng”, “radius”, "description", "tags"] | array of strings
geocoder | geocoder type | String
default_radius | Optional, radius for point, meters, default is 100 | Integer

*If **file_id** is set – **batch** parameter will be ignored.*

return:

```js
{
    "success": true,
    "list": [ <checked_place>, ... ]
}
```

where `checked_place` is:

```js
{
    ... // all fields from <place>
    "errors": <array_of_objects>, // optional
    "tag_names": <array_of_strings> // optional
}
```

#### errors
* 234 (Invalid data format)

## upload()
Upload places.

**required subuser rights:** place_update

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV file upload (with the name “file”).

CSV column separator is ‘;’, columns order – `label;tags;address;lat;lng;radius;external_id;description`

#### parameters
name | description | type
--- | --- | ---
file | A CSV file upload containing places data | File upload
error_policy| | ignore&#124;fail (String)
duplicate_policy| | skip&#124;update&#124;fail (String)
default_radius | Optional, radius for point, meters, default is 100 | Int
geocoder | Geocoder type | String
redirect_target | (optional) URL to redirect. If **redirect_target** passed return redirect to *&lt;redirect_target&gt;?response=&lt;urlencoded_response_json&gt;* | String

#### return
```js
{
    "success": true,
    "total": 1,
    "errors": 0
}
```

#### errors
* 233 (No data file) – if file part is missing
* 234 (Invalid data format)
* 247 (Entity already exists) – if uploaded place contains external_id and place with this ID already exists and duplicate_policy=fail
* 268 (Over quota) – if the user's quota for places is exceeded
