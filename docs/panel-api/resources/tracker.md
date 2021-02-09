---
title: Tracker
description: Tracker
---

# Tracker

## Tracker data structure

```json
{
    "id": ${int},                   // tracker id aka object_id
    "avatar_file_name" : ${string}, // optional. passed only if present
    "clone": ${boolean},            // true if this tracker is clone
    "comment": ${string},           // comment (description) related to the tracker
    "creation_date": "2013-02-02",  // tracker or clone creation date
    "group_id": ${int},             // tracker group id, 0 if no group
    "dealer_id": ${int},            // id of the dealer to which this tracker (or clone) belongs to
    "deleted": ${boolean},          // true if tracker or clone has been marked as deleted
    "label": ${string},             // tracker label
    "user_id": ${int},              // id of the user to which this tracker (or clone) belongs to
    "source": {
        "id": ${int},            // source id
        "device_id": ${string},  // aka source_imei
        "model": ${string},      // tracker model name from "models" table
        "blocked": ${boolean},   // true if tracker was blocked due to tariff end, etc.
        "tariff_id": ${int},     // id of tracker's tariff from "main_tariffs" table
        "creation_date": "2013-01-01",  // date when this tracker was first registered in the system
        "tariff_end_date": "2016-03-24",// date of next tariff prolongation or null
        "connection_status": "idle",    // current connection status
        "phone": ${string}       // phone of the device. can be null or empty if device has no GSM module
                                 // or uses bundled SIM which number is hidden from the user
        "corrupted": true        // true when tracker is corrupted using /tracker/corrupt,
                                 // and not passed when it is not corrupted
    }
}
```

## active/

### history/


#### list

Provides information about trackers which were considered "active" by our PaaS billing system, on a month-by-month basis.

**Required permissions**

* `trackers: "read"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `from` | start year and month for searching, e. g. "2016-02" | year-month string |
| `to`   | end year and month for searching. for example "2016-05" | year-month string |

**Return**

```json
{
  "success": true,
  "list": [
    {
      "month": "2016-07", //year and month of the stats entry
      "amount": 2, //overall number of active trackers during month
      "trackers": [
        { //basic info about active tracker
          "tracker_id": 14,
          "user_id": 3,
          "label": "test",
          "device_id": "123321"
        },
        ...
      ]
    },
    ...
  ]
}
```

**Errors**

* 211 – Requested time span is too big
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## bundle/


### assign

`assign(bundle_id, iccid)`

Assign bundle to specified ICCID

**Required permissions**

* `tracker_bundles: "update"`

**Parameters**

| Name | Description | Type |
| --- | --- | --- |
| `bundle_id` | Id of the bundle. | Int |
| `iccid` | Must consist of printable characters and have length between 3 and 20. | String |

**Return**

```json
{ "success": true }
```

**Errors**

* 201 – Not found in database (if bundle was not found)
* 208 – Device blocked (if SIM card was blocked)
* 223 – Phone number already in use (if SIM card already in use)
* 226 – Wrong ICCID (if SIM card was not found)
* 247 – Entity already exists (if ICCID is already exist)
* 250 – Not allowed for deleted devices (if SIM card was deleted)
* [Standard errors](../../backend-api/getting-started.md#error-codes)


### order/


#### assign

`order/assign(bundle_id, order_id)`

Assign bundle to specified order ID.

**Required permissions**

* `tracker_bundles: "update"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `bundle_id` |	Id of the bundle. |	Int |
| `order_id` |	Id of the bundle. | Nullable	Int |

**Return**

```json
{ "success": true }
```

**Errors**

* 201 – Not found in database (if bundle was not found)
* [Standard errors](../../backend-api/getting-started.md#error-codes)


### import

`import(imeis, equip_id, factory_preset)`

Add multiple bundles at once.

**Required permissions**

* `tracker_bundles: "create"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `imeis` |	array of IMEI numbers |	String[] |
| `equip_id` |	Id of equipment to associate with all specified IMEIs |	Int |
| `factory_preset` |	Whether this device was preconfigured on factory or not |	Boolean |

**Return**

```json
{ "success": true }
```

**Error**

* 201 – Not found in database (if bundle was not found)
* 247 – Entity already exists (if one of IMEIs is already exist)
* 204 – Entity not found (if there is no equipment with specified equip_id)
* [Standard errors](../../backend-api/getting-started.md#error-codes)

### list


If `filter` is used, entities will be returned only if filter string is contained within one of the following fields:
 `id`, `imei`, `model_code`, `iccid`, `assign_time`.

**Required permissions**

* `tracker_bundles: "read"`

**Parameters**

| Name | Description  | Type |
| :--- | :--- | :--- |
| clones_filter | Optional. Possible values: `exclude_clones` (filter out "cloned" trackers from results), `only_include_clones` (results shall contain only "cloned" trackers) or `not_set` | Enum |
| filter |	Optional. Text filter string. |	String |
| order_by | Optional. Specify list ordering. Can be one of `id`, `label`, `status`, `model`, `device_id`, `phone`, `creation_date`, `user_id`, `comment`. Default order by `id`. | Enum |
| ascending |	If true, ordering will be ascending, descending otherwise. Default is true. |	Boolean |
| offset |	Optional. Starting offset, used for pagination. Default is 0. |	Int |
| limit |	Optional. Max number of records to return, used for pagination. | Int |


**Return**

```json
{
    "success": true,
    "list" : [ <bundle> , ... ],
    "count" : <int> // total number of records (ignoring offset and limit), e.g. 42
}
```

**Errors**

* 201 – Not found in database (if user_id or tariff_id was specified but was not found)
* [Standard errors](../../backend-api/getting-started.md#error-codes)


### read

`read(imei)`

Returns the bundle object with the specified imei.

**Required permissions**

* `tracker_bundles: "read"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| imei | IMEI | Int |

**Return**

```json
{
    "success": true,
    "value" : <bundle>
}
```

**Errors**

* 201 – Not found in database (if bundle was not found)
* [Standard errors](../../backend-api/getting-started.md#error-codes)

### update

`update(bundle_id, equip_id)`

Assign specified equipment to bundle

**Required permissions**

* `tracker_bundles: "update"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `bundle_id` | 	Id of the bundle. | 	Int | 
| `equip_id` | 	Valid equipment id | 	Int | 

**Return**

```json
{ "success": true }
```

**Errors**

* 201 – Not found in database (if bundle was not found)
* 204 – Entity not found (if there is no equipment with specified equip_id)
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## clone

Creates a clone of the existing non-clone tracker.

**Required permissions**

* `trackers: "create"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| tracker_id | (int) Id of the tracker. Tracker must belong to authorized dealer. | int |
| label | User-defined label for clone, e.g. "Courier". Must consist of printable characters and have length between 1 and 60. | string |
| user_id | Id of the user who will become the owner of the clone. | int |

**Return**

```json
{
    "success": true,
    "id": 3947 // id of the created clone
}
```

**Errors**

* 219 (Not allowed for clones of the device) – when source tracker is clone itself
* 201 (Not found in database) – when tracker was not found
* 246 (Invalid user ID) – when user id is same as source tracker's owner id or it does not exist/belong to authorized dealer
* 247 (Entity already exists) – if destination user already has clone of this tracker
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## console/

### connect

Returns auth token to connect to tracker command console.

**Required permissions**

* `trackers: "update"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `tracker_id` | Id of the tracker. Tracker must belong to authorized dealer. | int |

**Return**

```json
{
    "success": true,
    "key": "6ad7490d4ec7f600ef10d4db41584980cd3ac230", // a key which is used to connect to console
    "timestamp": 1399957326 // a (int) timestamp which is used to connect to console
}
```

Establish WS connection with a URL:

`wss://ws.navixy.com/console?device=<tracker_id>&key=<key>&timestamp=<timestamp>&dealer_id=<dealer_id>`

JSON objects come in the next text frames:
```json
{
  "data":
  [
    ["Time","2017-11-16 10:02:37.0"],
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

**Errors**

* 230 (Not supported for this entity type) – when tracker is deleted or blocked
* 201 (Not found in database) – when tracker was not found
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## corrupt

`corrupt(tracker_id)`

Mark tracker as deleted and corrupt its source device_id and phone. Rename tracking table.

**Required permissions**

* `trackers: "corrupt"`

**Return**

```json
{ "success": true }
```

**Errors**

* 201 – Not found in database (if tracker was not found)
* 219 – Not allowed for clones of the device (if source tracker is clone itself)
* 252 – Device already corrupted
* 253 – Device has clones
```json
{
    "success": false,
    "status": {
        "code": 253,
        "description": "Device has clones"
    },
    "list": [<int>, ...] //clones tracker_ids list
}
```
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## batch_delete_clones

Deletes the specified set of trackers that are clones of other trackers. 
The action is considered completed successfully, even if some of the trackers could not be deleted. Then for the rest response will contain a description of the reasons why the deletion failed.
 
**Required permissions**

* `trackers: "delete"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `trackers` | Tracker ID list. Each of these trackers must be a clone and be accessible for current user. | int array |

**Return**

| Name | Description  | Type |
| --- | --- | --- |
| `success` | Action's execution status  | boolean |
| `deleted_count` | Number of successfully deleted clones from `trackers` | int |
| `not_deleted_count` | Number of not deleted clones | int |
| `not_deleted_trackers` (optional)| Description of failed deletion operations |array of objects `{"id":integer, "error":string}` |

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

**Errors**

[Standard errors](../../backend-api/getting-started.md#error-codes)

## delete_clone

Deletes a clone of the existing tracker.

**Required permissions**

* `trackers: "delete"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `tracker_id` | Id of the tracker. Tracker must belong to authorized dealer and must be a clone. | int |

**Return**

```json
{ "success": true }
```

**Errors**

* 201 (Not found in database) – if tracker was not found
* 249 (Operation available for clones only) – if source tracker is not a clone
* 203 (Delete entity associated with) – if there are some rules or vehicles associated with tracker
```json
{
    "success": false,
    "status": {
        "code": 203,
        "description": "Delete entity associated with"
    },
    "rules": [10] // list of associated rule ids
}
```
or
```json
{
    "success": false,
    "status": {
        "code": 203,
        "description": "Delete entity associated with"
    },
    "vehicles": [11] // list of associated vehicle ids
}
```
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## list

Returns list of all trackers belonging to dealer (with optional filtering by filter string, user id and/or tariff id).

If `filter` is used, entities will be returned only if filter string is contained within one of the following fields:
`id`, `label`, `source.id`, `source.device_id`, `source.model`, `source.phone`, `user_id`

**Required permissions**

* `trackers: "read"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `user_id` | Optional. Id of the user. User must belong to authorized dealer. |	Int |
| `tariff_id` | Optional. Id of the tariff. Tariff must belong to authorized dealer. |	Int |
| `filter` | 	Optional. Text filter string. |	String |
| `order_by` | 	Optional. Specify list ordering. Can be one of id, label, status, model, device_id, phone, creation_date |	String |
| `ascending` | 	If true, ordering will be ascending, descending otherwise. Default is true. |	Boolean |
| `offset` | 	Optional. Starting offset, used for pagination. Default is 0. |	Int |
| `limit` | 	Optional. Max number of records to return, used for pagination. |	Int |

**Return**

```json
{
    "success": true,
    "list" : [ <tracker> , ... ],
    "count" : <int> // total number of records (ignoring offset and limit), e.g. 42
}
```

**Errors**

* 201 – Not found in database (if user_id or tariff_id was specified but was not found)
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## move

Moves the existing non-clone tracker to another user belonging to same dealer.

**Tracker will be unbound from any rules associated with it.**

**Required permissions**

* `trackers: "create", "delete"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| tracker_id | Id of the tracker. Tracker must belong to authorized dealer. | int |
| user_id | Id of the user who will become the owner of the tracker | int |

**Return**

```json
{ "success": true }
```

**Errors**

* 219 (Not allowed for clones of the device) – when source tracker is clone
* 201 (Not found in database) – when tracker is not found
* 246 (Invalid user ID) – when user id is same as source tracker's owner id or it does not exist/belong to authorized dealer
* 247 (Entity already exists) – when destination user already has clone of this tracker
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## read

Returns the tracker object with the specified id.

**Required permissions**

* `trackers: "read"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| tracker_id | Id of the tracker. Tracker must belong to authorized dealer. | int |

**Return**

```json
{
    "success": true,
    "value" : ${tracker}
}
```

where `value` is JSON object tracker.

**Errors**

* 201 (Not found in database) – when tracker not found
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## register_entry

Sends tracker registration commands and resets all tracking settings. Can be executed once in 120 seconds for every tracker.

Device models `navixymobile*`, `mobile_unknown*`, `iosnavixytracker*` are not supported.

**Required permissions**

* `trackers: "update"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| `tracker_id` | Id of the tracker. Tracker must belong to authorized dealer. | int |

**Return**

```json
{ "success": true }
```

**Errors**

* 201 (Not found in database) – when tracker not found
* 252 (Device already corrupted) – if tracker was corrupted
* 264 (Timeout not reached) – if another register retry request for this tracker was done in last 120 seconds
* 208 (Device blocked) – when tracker exists but was blocked due to tariff restrictions or some other reason
* 219 (Not allowed for clones of the device) – when specified tracker is a clone
* 214 (Requested operation or parameters are not supported by the device) – when device does not have GSM module
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## settings/

### update

Updates tracker settings.

**Required permissions**

* `trackers: "update"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| tracker_id | Id of the tracker. Tracker must belong to authorized dealer. | int |
| label | User-defined label for this tracker, e.g. "Courier". Must consist of printable characters and have length between 1 and 60. Cannot contain '<' and '>' symbols. | string |
| deleted | If true, tracker is marked as deleted an will not be shown in user's interface. | boolean |
| comment | A comment (description) related to the tracker. Up to 3000 symbols. | string |

**Return**

```json
{ "success": true }
```

**Errors**

* 201 (Not found in database) – when tracker not found
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)


## source/

### update

Updates tracker settings.

**Required permissions**

* `trackers: "update"`

**Parameters**

| Name | Description  | Type |
| --- | --- | --- |
| tracker_id | Id of the tracker. Tracker must belong to authorized dealer. | int | 
| blocked | If true, tracker is marked as blocked. | boolean | 

**Return**

```json
{ "success": true }
```

**Errors**

* 201 (Not found in database) – when tracker is not found
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## tariff/

### change

**Required permissions**

```json
trackers: "update"
transactions: "create"
tariffs: "read"
```

**Params**

| Name | Description  | Type |
| --- | --- | --- |
| tracker_id | id of tracker | int |
| tariff_id | new tariff id | int |
| repay | repay remainder of current tariff payment? | boolean |
| charge | charge payment for new tariff? (for monthly and everyday tariffs) | boolean |

**Return**

```json
{ "success": true }
```

**Errors**

* 201 – Not found in database
* 219 – Not allowed for clones of the device
* 221 (Device limit exceeded) – when new tariff device limit is less then count of user's trackers.
* 237 – Invalid tariff (if there are no tariff with tracker.tariff_id and belongs to dealer)
* 238 – Changing tariff is not allowed
* 239 – New tariff doesn't exist
* 250 – Not allowed for deleted devices
* 252 (Device already corrupted) – when tracker's source is corrupted
* [Standard errors](../../backend-api/getting-started.md#error-codes)

**Conditions of the change**

The current dealer can change tracker tariff from `t1` to `t2`, if:

1. Tracker:
    1. is not removed
    1. belongs to the dealer's user
    1. is not a clone
1. `t1.tariff_id != t2.tariff_id`, i.e. it is impossible to change for the same tariff
1. `t1.dealer_id = t2.dealer_id = dealer.effectiveDealerId`, i.e. both tariffs belong to the current dealer
1. `t2.device = tracker`, i.e. only tracker tariffs are available
1. depending on `t2.doc_type`
    * doc_type=0 (for all) – without conditions
    * doc_type=1 (for the physical persons) – user.face=1 (physical person)
    * doc_type=2 (for legal entities) – user.face=2 (legal entity) or user.face=3 (SP)
    * doc_type=3 (paas) – without conditions
1. `t2.device_limit >= count` of trackers in user's cabinet.

**Repayment**

Repayment is carried out if the following conditions are met:

1. the "repay" flag is set (repay)
2. current tariff – monthly: t1.type = monthly
3. tariff – paid: tariff.price > 0
4. that the current tariff didn't end (tariff_end != 1)
5. the tariff expiration date is defined: tariff_end_date != 0 (for monthly tariffs it has to be carried out always)
6. the free period expired: created_date + free_period <= current date,
where free_period obtained from the hardcodes table or from default_model_settings
7. there is still at least one paid day on a tariff: reminder > 0
The rest of days on a tariff: remainder = the number of whole days before the end of the current tariff.

amount to be repaid = `ceil(tariff.price * remainder / amt)`,
where `amt` – the number of days in the current month, а ceil – the operation of taking the integer part

**Change**

```abap
tariff_id = next_tariff = new tariff id
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

## raw_command/

### send

Sends the GPRS command to the device, processing it in a protocol-dependent manner beforehand.

**required subuser rights:** tracker_update

#### parameters

name | description | type
--- | --- | ---
device_id | Fixed device ID, e.g. IMEI | String
command | Text or hexadecimal representation of the command | String
type | **text** or **hex**. Optional, default is **text** | String
reliable | **
false** if the command does not need to be resent when the device is disconnected or if no acknowledgment is received. Optional, default is **
true** | Boolean

#### response
```json
{ "success": true }
```

#### errors
*   7 (Invalid parameters)
*   201 (Not found in database) – if there is no tracker with such device ID belonging to authorized user
*   252 (Device already corrupted) – if tracker's source is corrupted

#### example response with an error:
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
