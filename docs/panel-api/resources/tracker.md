---
title: Tracker
description: API calls to interact with trackers in the admin panel.
---

# Tracker

API calls to manage GPS tracking devices within the Admin Panel.


## Tracker object

```json
{
    "id": 111231,
    "avatar_file_name" : "avatar",
    "clone": true,
    "comment": "Need to change SIM till next month",
    "creation_date": "2020-02-02",
    "group_id": 0,
    "dealer_id": 20410,
    "deleted": false,
    "label": "Truck",
    "user_id": 183654,
    "model_name": "Teltonika FMB120",
    "last_connection": "2020-02-02 12:44",
    "source": {
        "id": 456751,
        "device_id": "8624369656654",
        "model": "telfmb120",
        "blocked": false,
        "tariff_id": 13457,
        "creation_date": "2020-02-02",
        "tariff_end_date": "2021-02-02",
        "connection_status": "idle",
        "phone": "79995693344",
        "corrupted": true
    }
}
```

* `id` - int. Tracker ID aka object_id.
* `avatar_file_name` - optional string. Passed only if present.
* `clone` - boolean. `true` if this tracker is clone.
* `comment` - string. Comment (description) related to the tracker.
* `creation_date` - [date/time](../../user-api/backend-api/getting-started/introduction.md#data-types). Tracker or clone creation date.
* `group_id` - int. Tracker group ID. `0` if no group.
* `dealer_id` - int. An ID of a dealer to which this tracker (or clone) belongs to.
* `deleted` - boolean. True if tracker or clone has been marked as deleted.
* `label` - string. Tracker label.
* `user_id` - int. An ID of the user to which this tracker (or clone) belongs to.
* `model_name` - string. Human-readable tracker model name.
* `last_connection` - [date/time](../../user-api/backend-api/getting-started/introduction.md#data-types). Time when this tracker last connected to the server (in UTC+0 timezone).
* `source` - source JSON object. 
    * `id` - int. Source ID.
    * `device_id` - string. Source_imei.
    * `model` - string. Tracker model name from "models" table.
    * `blocked` - boolean. `true` if tracker has been blocked due to tariff end, etc.
    * `tariff_id` - int. An ID of tracker's tariff from "main_tariffs" table.
    * `creation_date` - [date/time](../../user-api/backend-api/getting-started/introduction.md#data-types). Date when this tracker first registered in the system.
    * `tariff_end_date` - [date/time](../../user-api/backend-api/getting-started/introduction.md#data-types). Date of next tariff prolongation or null.
    * `connection_status` - [enum](../../user-api/backend-api/getting-started/introduction.md#data-types). 
      Device connection status, possible values: "signal_lost", "just_registered", "just_replaced", "offline", "idle", "active"
    * `phone` - string. Phone of the device. Can be null or empty if the device has no GSM module or uses bundled SIM which number hidden from the user.
    * `corrupted` - boolean. `true` when tracker has been corrupted using /tracker/corrupt, and not passed when it is not corrupted.


## API actions

API path: `panel/tracker`.

### `active/history/list`

Provides information about trackers which were considered "active" by our PaaS billing system, on a month-by-month basis.

*required permissions*: `trackers: "read"`.

#### Parameters

| name | description                                          | type              |
|:-----|:-----------------------------------------------------|:------------------|
| from | Start year and month for searching, e. g. "2021-02". | year-month string |
| to   | End year and month for searching. e. g. "2021-03".   | year-month string |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/active/history/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "from": "2021-02", "to": "2021-03"}'
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "month": "2021-02",
      "amount": 1,
      "trackers": [
        {
          "tracker_id": 14,
          "user_id": 3,
          "label": "test",
          "device_id": "123321"
        }
      ]
    }
  ]
}
```

* `month` - string. Year and month of stats entry.
* `amount` - int. overall number of active trackers during a month.
* `trackers` - A basic info about active trackers

#### Errors

* 211 – Requested time span is too big.


### `bundle/assign`

Assign bundle to specified ICCID.

*required permissions*: `tracker_bundles: "update"`.

#### Parameters

| name      | description                                                            | type   |
|:----------|:-----------------------------------------------------------------------|:-------|
| bundle_id | ID of the bundle.                                                      | int    |
| iccid     | Must consist of printable characters and have length between 3 and 20. | string |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/bundle/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "bundle_id": 1241, "iccid": "78974217758"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/bundle/assign?hash=fa7bf873fab9333144e171372a321b06&bundle_id=1241&iccid=78974217758
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if bundle not found.
* 208 – Device blocked - if SIM card blocked.
* 223 – Phone number already in use - if SIM card already in use.
* 226 – Wrong ICCID - if SIM card not found.
* 247 – Entity already exists - if ICCID is already exist.
* 250 – Not allowed for deleted devices - if SIM card deleted.


### `bundle/order/assign`

Assigns bundle to specified order ID.

*required permissions*: `tracker_bundles: "update"`.

#### Parameters

| name      | description               | type |
|:----------|:--------------------------|:-----|
| bundle_id | ID of a bundle.           | int  |
| order_id  | ID of a bundle. Nullable. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/bundle/order/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "bundle_id": 1241, "order_id": 78974217758}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/bundle/order/assign?hash=fa7bf873fab9333144e171372a321b06&bundle_id=1241&order_id=78974217758
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database if bundle not found.


### `bundle/import`

Adds multiple bundles at once.

*required permissions*: `tracker_bundles: "create"`.

#### Parameters

| name           | description                                              | type         |
|:---------------|:---------------------------------------------------------|:-------------|
| imeis          | Array of IMEI numbers.                                   | string array |
| equip_id       | ID of equipment to associate with all specified IMEIs.   | int          |
| factory_preset | Whether this device was preconfigured on factory or not. | boolean      |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/bundle/import' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "imeis": ["896654523569742", "754854"], "equip_id": 13785, "factory_preset": false}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/bundle/import?hash=fa7bf873fab9333144e171372a321b06&bundle_id=1241&order_id=78974217758&factory_preset=false
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if bundle not found.
* 247 – Entity already exists - if one of IMEIs is already exist.
* 204 – Entity not found - if there is no equipment with specified equip_id.


### `bundle/list`

Gets list of all bundles. If `filter` is used, entities will be returned only if filter string contained within one of the following fields: `id`, `imei`, `model_code`, `iccid`, `assign_time`.

*required permissions*: `tracker_bundles: "read"`.

#### Parameters

| name                                  | description                                                                                                                                                                 | type                                                                          |
|:--------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| clones_filter                         | Optional. Possible values: `exclude_clones` (filter out "cloned" trackers from results), `only_include_clones` (results shall contain only "cloned" trackers) or `not_set`. | [enum](../../user-api/backend-api/getting-started/introduction.md#data-types) |
| filter  Optional. Text filter string. | string                                                                                                                                                                      |
| order_by                              | Optional. Specify list ordering. Can be one of `id`, `label`, `status`, `model`, `device_id`, `phone`, `creation_date`, `user_id`, `comment`. Default order by `id`.        | [enum](../../user-api/backend-api/getting-started/introduction.md#data-types) |
| ascending                             | If `true`, ordering will be ascending, descending otherwise. Default is `true`.                                                                                             | boolean                                                                       |
| offset                                | Optional. Starting offset, used for pagination. Default is `0`.                                                                                                             | int                                                                           |
| limit                                 | Optional. Max number of records to return, used for pagination.                                                                                                             | int                                                                           |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/bundle/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/bundle/list?hash=fa7bf873fab9333144e171372a321b06
    ```

#### Response

```json
{
    "success": true,
    "list" : [<bundle>],
    "count" : 42
}
```

* `list` - array of bundle objects.
* `count` - int. Total number of records (ignoring offset and limit).

#### Errors

* 201 – Not found in the database - if `user_id` or `tariff_id` specified but was not found.


### `bundle/read`

Returns the bundle object with the specified imei.

*required permissions*: `tracker_bundles: "read"`.

#### Parameters

| name | description    | type   |
|:-----|:---------------|:-------|
| imei | Device's IMEI. | string |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/bundle/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "imei": "835664527777452"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/bundle/read?hash=fa7bf873fab9333144e171372a321b06&imei=835664527777452
    ```
    
#### Response

```json
{
    "success": true,
    "value" : <bundle>
}
```

#### Errors

* 201 – Not found in the database - if bundle not found.


### `bundle/update`

Assign specified equipment to bundle.

*required permissions*: `tracker_bundles: "update"`.

#### Parameters

| name      | description         | type |
|:----------|:--------------------|:-----|
| bundle_id | ID of the bundle.   | int  | 
| equip_id  | Valid equipment ID. | int  | 

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/bundle/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "bundle_id": 13457, "equip_id": 35468}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/bundle/update?hash=fa7bf873fab9333144e171372a321b06&bundle_id=13457&equip_id=35468
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if bundle not found.
* 204 – Entity not found - if there is no equipment with specified `equip_id`.


### `clone`

Creates a clone of the existing non-clone tracker.
The method allows cloning from and to a subpaas's user account that is in the admin account hierarchy.
Cloning from a user of one subpaas to another user of another subpaas in the same hierarchy is also possible.

*required permissions*: `trackers: "create"`.

#### Parameters

| name       | description                                                                                                          | type   |
|:-----------|:---------------------------------------------------------------------------------------------------------------------|:-------|
| tracker_id | ID of the tracker. Tracker must belong to authorized dealer.                                                         | int    |
| label      | User-defined label for clone, e.g. "Courier". Must consist of printable characters and have length between 1 and 60. | string |
| user_id    | ID of the user who will become the owner of the clone.                                                               | int    |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/clone' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 134537, "user_id": 354468, "label": "Courier"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/clone?hash=fa7bf873fab9333144e171372a321b06&tracker_id=134537&user_id=354468&label=Courier
    ```

#### Response

```json
{
    "success": true,
    "id": 3947
}
```

* `id` - int. An ID of the created clone.

#### Errors

* 219 - Not allowed for clones of the device – when source tracker is clone itself.
* 201 - Not found in the database – when specified `tracker_id` not found.
* 246 - Invalid user ID – when user ID is same as source tracker's owner id, or it does not exist/belong to authorized dealer.
* 247 - Entity already exists – if destination user already has a clone of this tracker.
* 252 - Device already corrupted – when tracker's source corrupted.


### `console/connect`

Returns auth token for connection to tracker command console.

*required permissions*: `trackers: "update"`.

#### Parameters

| name       | description                                                | type |
|:-----------|:-----------------------------------------------------------|:-----|
| tracker_id | ID of a tracker. Tracker must belong to authorized dealer. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/console/connect' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 134537}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/console/connect?hash=fa7bf873fab9333144e171372a321b06&tracker_id=134537
    ```

#### Response

```json
{
    "success": true,
    "key": "6ad7490d4ec7f600ef10d4db41584980cd3ac230",
    "timestamp": 1399957326
}
```

* `key` - string. A key which is used to connect to console.
* `timestamp` - int. A timestamp which is used to connect to console.

Establish WS connection with a URL:

`wss://ws.navixy.com/console?device=<device_id>&key=<key>&timestamp=<timestamp>&dealer_id=<dealer_id>`

JSON objects come in the next text frames:

```json
{
  "data":
  [
    ["Time","2020-06-09 10:02:37.0"],
    ["Location valid","yes"],
    ["Latitude","-33.4595716"],
    ["Longitude","-70.7805233"],
    ["Speed","0"],
    ["Heading","229"],
    ["Moving","false"],
    ["Satellites","7"],
    ["Hardware mileage","3707.85"],
    ["Mileage","3853.16"],
    ["Digital input status","8"],
    ["Analog input 1","0.004"],
    ["Analog input 2","0.02"],
    ["Digital output status","3"],
    ["board_voltage","11.619"],
    ["temp_sensor","23.0"],
    ["GSM Level","13"],
    ["GSM Operator code","73002"],
    ["Battery level","3.827"]
  ],
  "type": "status"
}
```

#### Errors

* 230 - Not supported for this entity type – when tracker deleted or blocked.
* 201 - Not found in the database – when tracker with such `device_id` not found.
* 252 - Device already corrupted – when tracker's source corrupted.


### `corrupt`

Mark tracker as deleted and corrupt its source `device_id` and `phone`. Rename tracking table.

*required permissions*: `trackers: "corrupt"`.

#### Parameters

| name           | description                                                               | type    |
|:---------------|:--------------------------------------------------------------------------|:--------|
| tracker_id     | ID of a tracker. Tracker must belong to authorized dealer.                | int     |
| corrupt_clones | Optional. Default is `true`. Remove clones of the tracker for other users | boolean |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/corrupt' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 134537}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/corrupt?hash=fa7bf873fab9333144e171372a321b06&tracker_id=134537
    ```
    
#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if tracker not found.
* 219 – Not allowed for clones of the device - if source tracker is clone itself.
* 252 – Device already corrupted.
* 253 – Device has clones and `corrupt_clones` is false.

```json
{
    "success": false,
    "status": {
        "code": 253,
        "description": "Device has clones"
    },
    "list": [234651]
}
```

* `list` - int array. Clones tracker_ids list.


### `batch_clone`

Creates clones from the specified set of existing non-clone trackers.
The following actions are allowed within the same admin account hierarchy:

* Cloning from and to a subpaas's user account
* Cloning from a user of one subpaas to another user of another subpaas
* Cloning in a single operation from users that belong to different subpaas accounts


The maximum number of trackers to clone per operation is 1000. Labels from the original trackers are preserved.

To clone trackers across the hierarchy, use the master admin panel's hash.

*required permissions*: `trackers: "create"`.

| name            | description                                                                                                                                                                                                                                                                                                                                                                                                                      | type      |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| tracker_ids     | Tracker ID list. Each of these trackers must not be a clone and must be accessible to the target user.                                                                                                                                                                                                                                                                                                                           | int array |
| user_id         | Target user ID that is accessible from the admin panel hierarchy.                                                                                                                                                                                                                                                                                                                                                                | int       |
| ignore_existing | Optional (default = `false`). If `true`, allows performing a non-transactional cloning operation by creating clones if no clone conflicts are encountered within the operation. All already existing clones in the target user's account will not stop the operation, but the conflicting trackers from the tracker_ids will not be used in the cloning action and will be displayed in the response as `ignored_trackers` list. | boolean   |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/batch_clone' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 998836, "tracker_ids": [134537, 458412, 99330], "ignore_existing": true}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/batch_clone?hash=fa7bf873fab9333144e171372a321b06&user_id=998836&tracker_ids=[134537,458412]&ignore_existing=true
    ```
#### Response

| name             | description                                                                                                                                         | type      |
|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| list             | Resulting list of created clone tracker IDs.                                                                                                        | int array |
| success          | Action's execution status.                                                                                                                          | boolean   |
| ignored_trackers | The trackers from the request that were ignored during the `batch_clone` operation due to the target user tracker conflicts (clones already exist). | int array |

Example:

```json
{
  "ignored_trackers" : [ 99330 ],
  "list": [
    587469,
    587470
  ],
  "success": true
}
```
#### Errors

If the operation is applied transactionally meaning the `ignore_existing` = `false` or is not specified: it completes only if `"success": true` is received for the whole batch, otherwise, the cloning process for all trackers is rolled back.

* [Standard errors](../../user-api/backend-api/getting-started/errors.md#error-codes).
* 7 - Invalid parameters. Size must be between 1 and 1000 - triggered when the clone request exceeds 1000 trackers.
* 217 – List contains nonexistent entities - if at least one tracker from the request is not found.
* 247 – Entity already exists - if at least one of the trackers already has its clone in the target user. The error provides the list of trackers in the target user that caused the error.

Example:

```json
{
  "status": {
    "code": 247,
    "description": "Entity already exists"
  },
  "list": [
    10191656,
    10191657
  ],
  "success": false
}
```


### `batch_delete_clones`

Deletes the specified set of trackers that are clones of other trackers. 
The action will be considered as completed successfully, even if some trackers could not be deleted. Then for the rest 
response will contain a description of the reasons why the deletion failed.
 
*required permissions*: `trackers: "delete"`.

| name     | description                                                                                 | type      |
|:---------|:--------------------------------------------------------------------------------------------|:----------|
| trackers | Tracker ID list. Each of these trackers must be a clone and be accessible for current user. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/batch_delete_clones' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "trackers": [134537, 458412]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/batch_delete_clones?hash=fa7bf873fab9333144e171372a321b06&trackers=[134537, 458412]
    ```

#### Response

| name                 | description                                                                              | type             |
|:---------------------|:-----------------------------------------------------------------------------------------|:-----------------|
| success              | Action's execution status.                                                               | boolean          |
| deleted_count        | Number of successfully deleted clones from `trackers`.                                   | int              |
| not_deleted_count    | Number of not deleted clones.                                                            | int              |
| not_deleted_trackers | Optional. Description of failed deletion operations. `{"id": integer, "error": string}`. | array of objects |

Example:

```json
{
  "success": true,
  "deleted_count": 2,
  "not_deleted_count": 3,
  "not_deleted_trackers": [
    {
      "id": 2,
      "error": "Not a clone"
    },
    {
      "id": 3,
      "error": "Entity not found"
    },
    {
      "id": 4,
      "error": "Already deleted"
    }
  ]
}
```

#### Errors

* [Standard errors](../../user-api/backend-api/getting-started/errors.md#error-codes).


### `delete_clone`

Deletes a clone of the existing tracker.

*required permissions*: `trackers: "delete"`.

#### Parameters

| name       | description                                                                    | type |
|:-----------|:-------------------------------------------------------------------------------|:-----|
| tracker_id | ID of a tracker. Tracker must belong to authorized dealer and must be a clone. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/delete_clone' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 134537}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/delete_clone?hash=fa7bf873fab9333144e171372a321b06&tracker_id=134537
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 - Not found in the database – if tracker not found.
* 249 - Operation available for clones only – if source tracker is not a clone.
* 203 - Delete entity associated with – if there are some rules or vehicles associated with tracker.

```json
{
    "success": false,
    "status": {
        "code": 203,
        "description": "Delete entity associated with"
    },
    "rules": [10]
}
```

* `rules` - int array. A list of associated rule IDs.

or

```json
{
    "success": false,
    "status": {
        "code": 203,
        "description": "Delete entity associated with"
    },
    "vehicles": [11]
}
```

* `vehicles` - int array. A list of associated vehicle IDs.

* 252 - Device already corrupted – when tracker's source corrupted.


### `list`

Returns list of all trackers belonging to dealer (with optional filtering by `filter` string, `user_id` and/or `tariff_id`).

If `filter` is used, entities will be returned only if filter string contain one of the following fields:
`id`, `label`, `source.id`, `source.device_id`, `source.model`, `source.phone`, `user_id`.

*required permissions*: `trackers: "read"`.

#### Parameters

| name      | description                                                                                                                        | type    |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------|:--------|
| user_id   | Optional. ID of the user. User must belong to authorized dealer.                                                                   | int     |
| tariff_id | Optional. ID of the tariff. Tariff must belong to authorized dealer.                                                               | int     |
| filter    | Optional. Text filter string.                                                                                                      | string  |
| order_by  | Optional. List ordering. Can be one of "id", "label", "status", "model", "device_id", "phone", "creation_date", "last_connection". | 	string |
| ascending | Optional. If `true`, ordering will be ascending, descending otherwise. Default is `true`.                                          | boolean |
| offset    | Optional. Starting offset, used for pagination. Default is `0`.                                                                    | int     |
| limit     | Optional. Max number of records to return, used for pagination.                                                                    | int     |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/list?hash=fa7bf873fab9333144e171372a321b06
    ```

#### Response

```json
{
    "success": true,
    "list" : [{
      "id": 111231,
      "avatar_file_name" : "avatar",
      "clone": true,
      "comment": "Need to change SIM till next month",
      "creation_date": "2020-02-02",
      "group_id": 0,
      "dealer_id": 20410,
      "deleted": false,
      "label": "Truck",
      "user_id": 183654,
      "model_name": "Teltonika FMB120",
      "last_connection": "2020-02-02 12:44",
      "source": {
          "id": 456751,
          "device_id": "8624369656654",
          "model": "telfmb120",
          "blocked": false,
          "tariff_id": 13457,
          "creation_date": "2020-02-02",
          "tariff_end_date": "2021-02-02",
          "connection_status": "idle",
          "phone": "79995693344",
          "corrupted": true
      }
    }],
    "count" : 42
}
```

* `list` - array of objects. Tracker object described [above](#tracker-object).
* `count` - int. Total number of records ignoring `offset` and `limit`.

#### Errors

* 201 – Not found in the database - if specified `user_id` or `tariff_id` not found.


### `move`

Moves the existing non-clone tracker to another user belonging to the same dealer.

**Tracker will be unbound from any rules associated with it.**

*required permissions*: `trackers: "create", "delete"`.

#### Parameters

| name       | description                                                  | type |
|:-----------|:-------------------------------------------------------------|:-----|
| tracker_id | ID of the tracker. Tracker must belong to authorized dealer. | int  |
| user_id    | ID of the user who will become the owner of the tracker.     | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/move' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 1245678, "user_id": 214034}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/move?hash=fa7bf873fab9333144e171372a321b06&tracker_id=1245678&user_id=214034
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 219 - Not allowed for clones of the device – when source tracker is clone.
* 201 - Not found in the database – when tracker not found.
* 246 - Invalid user ID – when `user_id` is the same as source tracker's owner id, or it does not exist/belong to authorized dealer.
* 247 - Entity already exists – when destination user already has a clone of this tracker.
* 252 - Device already corrupted – when tracker's source corrupted.


### `read`

Returns the tracker object with the specified ID.

*required permissions*: `trackers: "read"`.

#### Parameters

| name       | description                                                  | type |
|:-----------|:-------------------------------------------------------------|:-----|
| tracker_id | ID of the tracker. Tracker must belong to authorized dealer. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 1245678}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/read?hash=fa7bf873fab9333144e171372a321b06&tracker_id=1245678
    ```

#### Response

```json
{
    "success": true,
    "value" : {
        "id": 111231,
        "avatar_file_name" : "avatar",
        "clone": true,
        "comment": "Need to change SIM till next month",
        "creation_date": "2020-02-02",
        "group_id": 0,
        "dealer_id": 20410,
        "deleted": false,
        "label": "Truck",
        "user_id": 183654,
        "model_name": "Teltonika FMB120",
        "last_connection": "2020-02-02 12:44",
        "source": {
            "id": 456751,
            "device_id": "8624369656654",
            "model": "telfmb120",
            "blocked": false,
            "tariff_id": 13457,
            "creation_date": "2020-02-02",
            "tariff_end_date": "2021-02-02",
            "connection_status": "idle",
            "phone": "79995693344",
            "corrupted": true
        }
    }
}
```

* `value` - JSON object. Tracker object described [above](#tracker-object).

#### Errors

* 201 - Not found in the database – when tracker not found.
* 252 - Device already corrupted – when tracker's source corrupted.


### `register_retry`

Sends tracker registration commands and resets all tracking settings. Can be executed once in 120 seconds for every tracker.

Device models `navixymobile*`, `mobile_unknown*`, `iosnavixytracker*` are not supported.

*required permissions*: `trackers: "update"`.

#### Parameters

| name                   | description                                                                                                                                                                                | type    |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
| tracker_id             | ID of the tracker. Tracker must belong to authorized dealer.                                                                                                                               | int     |
| send_register_commands | Indicates send or not to send activation commands to device (via SMS or GPRS channel). If parameter is not specified or equals `null` will be used the platform settings. Default: `null`. | boolean |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/register_retry' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 1245678, "send_register_commands": true}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/register_retry?hash=fa7bf873fab9333144e171372a321b06&tracker_id=1245678&send_register_commands=true
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 - Not found in the database – when tracker not found.
* 252 - Device already corrupted – if tracker corrupted.
* 264 - Timeout not reached – if another register retry request for this tracker done in last 120 seconds.
* 208 - Device blocked – when tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 - Not allowed for clones of the device – when specified tracker is a clone.
* 214 - Requested operation or parameters are not supported by the device – when device does not have GSM module.
* 252 - Device already corrupted – when tracker's source corrupted.


### `settings/update`

Updates tracker settings.

*required permissions*: `trackers: "update"`.

#### Parameters

| name       | description                                                                                                                                                     | type    |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
| tracker_id | ID of the tracker. Tracker must belong to authorized dealer.                                                                                                    | int     |
| label      | User-defined label for this tracker, e.g. "Courier". Must consist of printable characters and have length between 1 and 60. Cannot contain `<` and `>` symbols. | string  |
| deleted    | If `true`, tracker will be marked as deleted and will not be shown in user's interface.                                                                         | boolean |
| comment    | Optional. A comment (description) related to the tracker. Up to 3000 symbols.                                                                                   | string  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/settings/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 1245678, "label": "Courier", "deleted": false}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/settings/update?hash=fa7bf873fab9333144e171372a321b06&tracker_id=1245678&label=Courier&deleted=false
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 - Not found in the database – when tracker not found.
* 252 - Device already corrupted – when tracker's source corrupted.


### `source/update`

Updates source settings. Can block and unblock a device.

*required permissions*: `trackers: "update"`.

#### Parameters

| name       | description                                                  | type    |
|:-----------|:-------------------------------------------------------------|:--------|
| tracker_id | ID of the tracker. Tracker must belong to authorized dealer. | int     | 
| blocked    | If `true`, tracker will be marked as blocked.                | boolean | 

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/source/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 1245678, "blocked": false}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/source/update?hash=fa7bf873fab9333144e171372a321b06&tracker_id=1245678&blocked=false
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 - Not found in the database – when tracker not found.
* 252 - Device already corrupted – when tracker's source corrupted.


### `tariff/change`

*required permissions*: `[trackers: "update", "transactions": "create", "tariffs": "read"]`.

#### Parameters

| name       | description                                               | type    |
| :--------- | :-------------------------------------------------------- | :------ |
| tracker_id | ID of tracker. Tracker must belong to authorized dealer.  | int     |
| tariff_id  | New plan ID.                                              | int     |
| repay      | Repay remainder of current plan payment.                  | boolean |
| charge     | Charge payment for new plan. For monthly and daily plans. | boolean |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/tariff/change' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker_id": 1245678, "tariff_id": 15843, "repay": false, "charge": true}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tracker/tariff/change?hash=fa7bf873fab9333144e171372a321b06&tracker_id=1245678&tariff_id=15843&repay=false&charge=true
    ```
    
#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database.
* 219 – Not allowed for clones of the device.
* 221 - Device limit exceeded – when new tariff device limit is less than count of user's trackers.
* 237 – Invalid tariff - if there are no tariff with tracker.tariff_id and belongs to dealer.
* 238 – Changing tariff not allowed.
* 239 – New tariff doesn't exist.
* 250 – Not allowed for deleted devices.
* 252 - Device already corrupted – when tracker's source corrupted.

**Conditions of the change**

The current dealer can change tracker tariff from `t1` to `t2`, if:

1. Tracker:
    * is not removed.
    * belongs to the dealer's user.
    * is not a clone.
2. `t1.tariff_id != t2.tariff_id`, i.e. it is impossible to change to the same tariff.
3. `t1.dealer_id = t2.dealer_id = dealer.effectiveDealerId`, i.e. both tariffs belong to the current dealer.
4. `t2.device = tracker`, i.e. only tracker tariffs are available.
5. depending on `t2.doc_type`:
    * doc_type=0 (for all) – without conditions.
    * doc_type=1 (for physical persons) – user.face=1 (physical person).
    * doc_type=2 (for legal entities) – user.face=2 (legal entity) or user.face=3 (SP).
    * doc_type=3 (paas) – without conditions.
6. `t2.device_limit >= count` of trackers in user's cabinet.

**Repayment**

Repayment will be carried out if the following conditions met:

1. The "repay" flag set (repay).
2. A current tariff – monthly: `t1.type = monthly`.
3. Tariff – paid: tariff.price > 0.
4. That the current tariff didn't end (`tariff_end != 1`)
5. The tariff expiration date defined: tariff_end_date != 0 (for monthly tariffs it has to be carried out always).
6. The free period expired: created_date + free_period <= current date
where free_period obtained from the hardcodes table or from default_model_settings.
7. There is still at least one paid day on a tariff: reminder > 0
The rest of days on a tariff: remainder = the number of whole days before the end of the current tariff.

amount to be repaid = `ceil(tariff.price * remainder / amt)`,
where `amt` – the number of days in the current month, a ceil – the operation of taking the integer part.

**Change**

```shell
tariff_id = next_tariff = new tariff ID
tariff_change = current date
if tariff is active (tariff_end = false) then
    tariff_end = false
    last_charged_date = current date
    if new tariff is monthly and the flag "to charge" is not set (charge) then
        tariff_end_date = the first day of the next month from the current date
    else
        tariff_end_date = tomorrow date
else (tariff is not active: tariff_end = true)
    last_charged_date = yesterday date
    if new tariff is monthly then
        if the flag "to charge" is set (charge) then
            tariff_end_date = current date
            tariff_end = true
        else
            tariff_end_date = the first day of the next month from the current date
            tariff_end = false
    if the new tariff is everyday then
        if the flag "to charge" is set(charge) then
            tariff_end_date = current date
            tariff_end = true
        else
            tariff_end_date = tomorrow date
            tariff_end = false
    if the new tariff is activeday then
        tariff_end_date = 0
        tariff_end = false
```

All dates according to UTC time.


### `raw_command/send`

Sends the GPRS command to the device, processing it in a protocol-dependent manner beforehand.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name      | description                                                                                                                                        | type    |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
| device_id | Fixed device ID, e.g. IMEI.                                                                                                                        | string  |
| command   | Text or hexadecimal representation of the command.                                                                                                 | string  |
| type      | Optional. Default is `text` . Can be "text" or "hex".                                                                                              | string  |
| reliable  | Optional. default is `true`. If `false` the command doesn't need to be resent when the device is disconnected or if no acknowledgment is received. | boolean |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tracker/raw_command/send' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "device_id": "889654248978", "command": "setparam 101:4"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 7 - Invalid parameters.
* 201 - Not found in the database – if there is no tracker with such device ID belonging to authorized user.
* 252 - Device already corrupted – if tracker's source corrupted.

##### Example response with an error:

```json
{
  "success": false,
  "status": {
    "code": 7,
    "description": "Invalid parameters"
  },
  "errors": [
    {
      "parameter": "command",
      "error": "Non-hex string"
    }
  ]
}
```
