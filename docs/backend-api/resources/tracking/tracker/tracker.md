---
title: Tracker
description: Tracker information
---

Tracker is one of the key entities in our API. It represents tracking device registered in our GPS monitoring system. Lots of API calls are created for manipulation of tracker and/or its properties.

### Tracker object structure

```js
{
    "id": {int}, // tracker id aka object_id
    "label": {string}, // tracker label
    "clone": {boolean}, // true if this tracker is clone
    "group_id": {int}, // tracker group id, 0 if no group
    "avatar_file_name" : {string}, // optional. passed only if present
    "source": {
        "id": {int}, // source id
        "device_id": {string}, // device id aka source_imei
        "model": {string}, // tracker model name from "models" table
        "blocked": {boolean}, // true if tracker was blocked due to tariff end
        "tariff_id": {int}, // id of tracker's tariff from "main_tariffs" table
        "status_listing_id": {int}, // id of the status listing associated with this tracker, or null
        "creation_date": "2011-09-21", // date when the tracker registered
        "tariff_end_date": "2016-03-24", // date of next tariff prolongation or null
        "phone" : {string} // phone of the device. can be null or empty if device has no GSM module or uses bundled SIM which number is hidden from the user
    }
    "tag_bindings": [{tag_binding}, ...} // list of attached tags. appears only for “tracker/list“. 
}
```

where **tag_binding** is:

```js
{
  "tag_id": {int}, // id of tag. must be unique for tracker
  "ordinal": {int} // number that can be used as ordinal or kind of tag. must be unique for tracker. max value is 5
}
```

### change_phone

Changes tracker’s phone and setup new apn.

**required subuser rights:** tracker_configure

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999199 |
| phone | The phone number of the sim card inserted into device in international format without “+” sign | string| 6156680000 |
| apn_name | The name of GPRS APN of the sim card inserted into device | string | fast.tmobile.com |
| apn_ user | The user of GPRS APN of the sim card inserted into device | string | tmobile |
| apn_password | The password of GPRS APN of the sim card inserted into device | sting | tmobile |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/change_phone' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "265489", "phone": "6156680000", "apn_name": "fast.tmobile.com", "apn_user": "tmobile", "apn_password": "tmobile", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```json
{
    "success": true
}
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
* 219 – Not allowed for clones of the device (if specified tracker is a clone)
* 214 – Requested operation or parameters are not supported by the device (if device does not have GSM module)
* 223 – Phone number already in use (if specified phone number already used in another device)
* 241 – Cannot change phone to bundled sim. Contact tech support. (if specified phone number belongs tp sim card bundled with the device)

### corrupt

Marks tracker as deleted and corrupt its source, device_id and phone.

**required subuser rights**: tracker_register

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/corrupt' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```json
{
    "success": true
}
```

#### errors

* 13 – Operation not permitted – if tracker already connected to server, or if user has insufficient rights
* 243 – Device already connected
* 201 – Not found in database (if tracker was not found)
* 219 – Not allowed for clones of the device (if source tracker is clone itself)
* 252 – Device already corrupted
* 208 – Device blocked

### delete

Deletes tracker if it is “clone”. Will not work if specified id of the original tracker.

**required subuser rights**: admin (available only to master users)

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/delete' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 (Not found in database) – if tracker not found
* 249 (Operation available for clones only) – if tracker is not clone
* 203 (Delete entity associated with) – if there are some rules or vehicles associated with tracker

```js
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
```js
{
    "success": false,
    "status": {
        "code": 203,
        "description": "Delete entity associated with"
    },
    "vehicles": [11] // list of associated vehicle ids
}
```

### get_diagnostics

Gets last sensors and states values received from the device.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_diagnostics' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "user_time": "2014-07-09 07:50:58", // current time in user's timezone 
    "inputs": {list of last sensor values}, // list of last sensor values object (see below)
    "states": {"obd_vin": "123", "obd_mil_status":"false"}, // map of last state values or null (see below)
    "update_time": "2014-03-06 13:57:00" // date/time when the data was updated
}
```

Where **Sensor value object** is:
```js
{
  "label": {string}, // Sensor's label. E.g. "Sensor #1",
  "name": {string of enum}, // Name of sensor's raw input. E.g. "can_fuel" ( see below list of values)
  "type": {string of enum}, // Type of quantity, measured by sensor. E.g. "fuel",
  "value": {float}, // Reading's value, measured in units from eponymous field. E.g. 100.0
  "units_type": {string of enum}, // Unit of measurement of input to the sensor. E.g."litre"
  "units": {string}, // User's label for sensor's
  "converted_units_type": {string of enum} // Unit of measurement system prefered by current user (according to user/settings), suitable for this sensor. Can be null, if there is no need in conversion (unit of sensor's input (field `units_type`) belongs to user's measurement system).
  "converted_value": {float} // Reading's value in units from field `converted_units_type`. Can be null if there is no need in conversion.
}
```

List of available sensor's input names for field **inputs**:

* **composite**,
* **input_status**,
* **analog_x** (range for x: [1 – 8]),
* **freq_x** (range for x: [1 – 8]),
* **impulse\_counter\_x** (range for x: [1 – 8]),
* **fuel_level**,
* **fuel_frequency**,
* **fuel_temperature**,
* **lls\_temperature\_x** (range for x: [1 – 16]),
* **lls\_level\_x** (range for x: [1 – 16]),
* **fuel_consumption**,
* **obd_consumption**,
* **obd_rpm**,
* **obd_fuel**,
* **obd_coolant_t**,
* **obd_intake_air_t**,
* **obd_throttle**,
* **obd_speed**,
* **obd_engine_load**,
* **obd_absolute_load_value** (normalised value of air mass per intake stroke in percents),
* **obd_control_module_voltage** (in volts),
* **obd_time_since_engine_start** (run time since engine start in seconds),
* **obd_mil_run_time** (in minutes),
* **rs232_x** (range for x: [1 – 6]),
* **board_voltage**,
* **can_engine_temp**,
* **can_engine_hours**,
* **can_mileage**,
* **can_throttle**,
* **can_fuel** (fuel level in percents or in unknown units),
* **can_fuel_litres** (fuel level in litres),
* **can_fuel_economy** (fuel economy in km/litres),
* **can_consumption**,
* **can_rpm**,
* **can_speed**,
* **can_r_prefix**,
* **can_coolant_t**,
* **can_intake_air_t**,
* **can_engine_load**,
* **can_adblue_level**,
* **can_fuel_rate** (instant fuel consumption liter/hour),
* **raw_can_x** (range for x: [1 – 16]),
* **can_axle_load_x** (range for x: [1 – 15]),
* **temp_sensor**,
* **ext_temp_sensor_x** (range for x: [1 – 10]).

List of state names for field **states**:

* **obd_vin** (value type: string),
* **obd_mil_status** (value type: boolean),
* **obd_dtc_number** (DTC codes number; value type: integer),
* **obd_dtc_codes** (value type: string),
* **obd_dtc_cleared_distance** (distance traveled since codes cleared in km; value type: double),
* **obd_mil_activated_distance** (distance traveled with MIL on in km; value type: double),
* **hardware_key** (driver identification key; value type: string),
* **vibration_state** (value type: boolean),
* **idling_state** (value type: boolean),
* **external_power_state** (connected/disconnected; value type: boolean),
* **case_intrusion_state** (value type: boolean),
* **driver_ident_state** (identified/not identified; value type: boolean),
* **tacho_vin** (value type: string),
* **tacho_card1_sn** (value type: string),
* **tacho_card2_sn** (value type: string),
* **tacho_vin_last_download** (value type: string),
* **tacho_card1_last_download** (value type: string),
* **tacho_card2_last_download** (value type: string),
* **can_hand_brake_state** (value type: boolean),
* **can_hood_state** (value type: boolean, ‘true’ means ‘open’),
* **can_airbag_state** (value type: boolean, ‘true’ means ‘malfunction’),
* **can_trunk_state** (value type: boolean, ‘true’ means ‘open’),
* **can_seat_belt_driver_state** (value type: boolean, ‘true’ means ‘untied’),
* **can_seat_belt_passenger_state** (value type: boolean, ‘true’ means ‘untied’),
* **can_door_state** (value type: boolean),
* **can_door_driver_state** (value type: boolean, ‘true’ means ‘open’),
* **can_door_passenger_state** (value type: boolean, ‘true’ means ‘open’).

### get_fuel

Gets current fuel level (in liters) of tracker’s fuel tanks.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_fuel' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "user_time": "2014-07-09 07:50:58", // current time in user's timezone
    "inputs": [array] //array of last readings of fuel-related sensors. Items are objects of the same type as used in tracker/get_diagnostics,
    "update_time": "2014-03-06 13:57:00" // date/time when the data was updated
}
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

### get_inputs

Gets current state of tracker’s digital inputs and “semantic” inputs (ignition, buttons, car alarms, etc.) bound to them (if any).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_inputs' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "user_time": "2014-07-09 07:50:58", // current time in user's timezone
    "inputs": [true, true, false] means input 1 is on, input 2 is on, input 3 is off, //array[boolean] of states of all digital inputs
    "states": [
        {
            "type": {string}, // one of predefined semantic input types (see below)
            "name": {string}, // user-defined name for semantic input, or null if not specified
            "status": {boolean}, // true if input is active, false otherwise
            "input_number": {int} // number of the associated discrete input
        },
        ...
    ],
    "update_time": "2014-03-06 13:57:00" // date/time when the data was updated
}
```

List of **input types**:

* **ignition** - Car’s ignition. There can be only one sensor of this type,
* **engine** - Engine’s working status,
* **mass** - Car’s “ground”,
* **car_alarm** - Expected to be “on” when car alarm is triggered,
* **sos_button** - An emergency “red” button,
* **hood** - “on” if engine’s hood is open,
* **door** - “on” if car’s door is open,
* **car_lock** - “on” if car’s central lock is open,
* **custom** - user-defined type. In general, should have non empty “name” field.

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

### get_last_gps_point

Gets last point of the tracker located by GPS. Points located by GSM LBS are excluded from consideration.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_last_gps_point' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```json
{
    "success": true,
    "value": <see TrackPoint in tracker/track/read>
}
```

#### errors

* 201 (Not found in database) – if there is no tracker with such id belonging to authorized user
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason

### get_readings

Gets last sensor values for sensors that are:

- **metering**
- **not can- or obd-based**
- **not “fuel” sensors**

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_readings' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "user_time": "2014-07-09 07:50:58", // current time in user's timezone
    "inputs": {list of last sensor values} //list of last sensor values {name:"analog_1", type:"fuel", value:123, ...} (see tracker/get_diagnostics)
}
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

### get_state

Gets current tracker state (gps, gsm, outputs, etc.).

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_state' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999119", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "user_time":"2014-07-09 07:50:58", //current time in user's timezone
    "state": {
        "source_id": {int}, // tracker data source id (from table "sources")
        "gps": {
            "updated": "2013-02-19 10:48:08", // string date of last gps coordinates update in timezone of the user or null if there was no updates
            "signal_level": {int}, // gps signal level in percent, e.g. 25, or null if device cannot provide such info
            "location": {
                "lat": {float}, // latitude, e.g. 56.826068
                "lng": {float} // longitude, e.g. 60.594338
            },
            "heading": {int}, // heading in degrees, e.g. 3
            "speed": {int}, // speed in km/h, e.g. 20
            "alt": {int}, // altitude in meters, e.g. 10
            "precision": {int}, // precision in meters, optional
            "gsm_lbs": {boolean}, // true if location is detected by GSM LBS, optional
        },
        "connection_status": {enum}, // device connection status, possible values: "signal_lost", "just_registered", "offline", "idle", "active"
        "movement_status": {enum}, // movement status, possible values: "moving", "stopped", "parked"
        "gsm": {string} //can be null if device does not support transmission of gsm info
            "updated": "2013-02-19 10:48:08", //string date of last gsm status update in timezone of the user or null if there was no updates
            "signal_level": {int}, // gsm signal level in percent, e.g. 25, or null if device cannot provide such info
            "network_name": {string}, // gsm network name, e.g. "T-MOBILE", or null if device cannot provide such info
            "roaming": {boolean} // roaming state, or null if device cannot provide such info
        },
        "last_update": "2013-02-19 10:48:08", // date of last device state update in timezone of the user or null if there was no updates
        "battery_level": {int}, // battery level in percent, e.g. 25, or null if device cannot provide such info
        "battery_update": "2013-02-19 10:48:08", // date of last battery update in timezone of the user or null if there was no updates
        "inputs": [true, true, false], means input 1 is on, input 2 is on, input 3 is off // array of states of all digital inputs 
        "inputs_update": "2013-02-19 10:48:08", // date of last inputs update in timezone of the user or null if there was no updates
        "outputs": [true, true, false], means output 1 is on, output 2 is on, output 3 is off // array of states of all digital outputs
        "ouputs_update": "2013-02-19 10:48:08", // date of last outputs update in timezone of the user or null if there was no updates
        "additional": { //map of additional states, keys depends on tracker model
            "hardware_key": { // last scanned hardware key object
                "value": {int}, // hardware key
                "updated": "2013-02-19 10:48:08" // date of last hardware key update in timezone of the user or null if there was no updates
            }
        }
    }
}
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

### get_states

Gets current states (gps, gsm, outputs, etc.) for several trackers.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| trackers | id of trackers (aka “object_id”). Trackers must belong to authorized user and not be blocked | array of int | [999119, 999199, ...] |
| list_blocked | optional. If true call returns list of blocked tracker IDs instead of error 208. Default is false | boolean | true/false |
| allow_not_exist | optional. If true call returns list of nonexistent tracker IDs instead of error 217 or 201. Default is false | boolean | true/false |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/get_states' \
-H 'Content-Type: application/json' \ 
-d '{"trackers": "[999119, 999199, ...]", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "user_time":"2014-07-09 07:50:58", //current time in user's timezone
    "states": { //a map containing requested states
        <tracker_id, e.g. "1234"> : // state object from tracker/get_state response,
        ...
    },
    "blocked": [array of IDs] //returned only if list_blocked=true,
    "not_exist": [array of IDs] //returned only if allow_not_exist=true
}
```

#### errors

* 201 – Not found in database (if tracker was corrupted and allow_not_exist = false)
* 208 – Device blocked (if list_blocked = false and tracker exists but was blocked due to tariff restrictions or some other reason)
* 217 – List contains nonexistent entities (if allow_not_exist = false and there are nonexistent trackers belonging to an authorized user)

### list_models

Gets all integrated tracker models (from “models" table).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| compact_view | optional. True to compact view. Default is false | boolean | true/false |
| codes | optional. Array of model codes. If passed only given models will be returned | array of string | [model_1, model_2, ...] |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/list_models' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "list": [
        {
            "id": {int}, // model id
            "vendor": {string}, // vendor name
            "code": {string}, 
            "parent_code": {string} or null,
            "type": {string}, // <logger, portable, vehicle, or personal>
            "name": {string}, // model name
            "id_type": {string},
            "has_phone": {boolean},
            "has_apn_settings": {boolean},
            "register": {boolean},
            "check_bundle": {boolean},
            "has_auto_registration": {boolean}, // if true device may be registered by automatic commands from platform
            "port": {int},
            "battery": (see below), // internal device's battery. json object
            "altitude": {boolean},
            "satellites": {boolean},
            "gsm_level": {boolean},
            "gsm_network": {boolean},
            "gsm_roaming": {boolean},
            "has_detach_button": {boolean},
            "has_fuel_input": {boolean},
            "analog_inputs": {int}, // number of analog inputs
            "digital_inputs": {int}, // number of digital inputs
            "digital_outputs": {int}, // number of digital outputs
            "rs232_inputs": {int}, // number of RS232 inputs
            "track_control": {string},
            "output_control": {string},
            "special_control": {string},
            "inputs": [list of available inputs] // array of strings, 
            "rules": [list of available rules] // array of strings, ids of supported rules
            "state_fields": [],
            "has_led_control": {boolean}, // Does a switching LED supported by this tracker
            "has_location_request": {boolean}, // Does the tracker have an opportunity to request a location with a command by SMS
            "has_gprs_location_request": {boolean}, // Does the tracker have an opportunity to request a location with a command over a GPRS connection
            "has_gsm_lbs_location_request": {boolean}, // Does the tracker have an opportunity to request a location by LBS with a command over a GPRS connection
            "has_chat": {boolean}, // Does chat available for the device
            "has_odometer": {boolean}, // Does the tracker have an integrated odometer
            "has_lbs": {boolean}, // Does the tracker send information about cell info
            "has_motion_sensor": {boolean}, // Does the tracker have an integrated motion sensor
            "has_hardware_key": {boolean}, // Does the tracker have an opportunity for identification of a driver by a hardware key
            "additional_fields": [list of json object] // optional. list of descriptions of special fields using for control trackers that users fill on time of registration
        },
         ...
    ]
}
```

where **battery** is:

```js
{
    "min_charge": {float},
    "low_charge": {float}, // charge level for the "low battery" rule triggering 
    "max_charge": {float}
}
```
where **additional_fields** is:

```json
{
    "type": {string},
    "default_value": {string},
    "name": {string}
}
```

#### Id type:

Id type is used to determine the information needed to register device in our system (see [tracker/register](#register)).

Possible values are:

- **imei** – means device uses IMEI as its identifier, e. g. “356938035643809”. See [Wikipedia article](https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity). When needed, you should pass only digits of IMEI, no spaces, minus signs, etc.
- **meid** means device uses MEID consisting of 14 HEX digits as its identifier, e. g. “A10000009296F2”. See [Wikipedia article](https://en.wikipedia.org/wiki/Mobile_equipment_identifier).
- **id,n** – means device uses n-digit identifier (factory id with length n), for example, “id,7” means that you must pass 7-digit number, for example “1234567”
- **n,m** – n-digit generated id starting with m. This means that device has configurable ID and our platform generates and configures it automatically. You don’t need to pass any identifier during device registration in this case.

#### errors

general types only

#### example

```json
{
    "id": 166,
    "code": "tt1_wp",
    "type": "vehicle",
    "name": "WondeProud TT1",
    "id_type": "10,2",
    "has_phone": true,
    "has_apn_settings": true,
    "register": true,
    "battery": {
        "min_charge": 3.4,
        "low_charge": 3.7,
        "max_charge": 4.1
    },
    "altitude": true,
    "satellites": true,
    "gsm_level": true,
    "gsm_network": true,
    "gsm_roaming": true,
    "has_detach_button": false,
    "has_fuel_input": true,
    "analog_inputs": 2,
    "digital_inputs": 4,
    "rs232_inputs": 0,
    "digital_outputs": 4,
    "track_control": "tt1",
    "output_control": "default",
    "special_control": "none",
    "vendor": "WondeProud",
    "rules": [
        "offline",
        "input_change",
        "sos",
        "sensor_range",
        "speedup",
        "route",
        "track_change",
        "inoutzone",
        "battery_off"
    ],
    "inputs": ["analog_2", "analog_1"],
    "state_fields": [],
    "special_settings": ["none"],
    "sms_control": [],
    "has_led_control": false,
    "has_location_request": true,
    "has_gsm_lbs_location_request": true,
    "has_chat": false,
    "check_bundle": false,
    "has_odometer": true
}
```

### list

Gets user’s trackers with optional filtering by labels.

### parameters


| name | description | type | format |
| :------ | :------ | :----- | :----- |
| labels | optional. List of tracker label filters. If specified, only trackers that labels contains any of the given filter will be returned | array of string | ["aa", "b"] |

Constraints for labels:
* labels array size: minimum 1, maximum 1024
* no null items
* no duplicate items
* item length: minimum 1, maximum 60

For example, we have trackers with labels "aa1", "bb2", "cc3", if we pass `labels=["aa","b"]` only trackers containing "aa1" and "bb2" will be returned.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/list' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "list": [ ${tracker}, ... ] // list of JSON-objects
}
```
See tracker object structure description [here](#tracker-object-structure).

#### errors

general types only

### tags/set

Sets tags for tracker. Tags must be created.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 99119 |
| tag_bindings | list of **tag_binding** objects | array of Json objects | [{"tag_id" : 1, "ordinal" : 1}, {"tag_id" : 2, "ordinal" : 2}] |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/tags/set' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "99119"}'
```

#### response

```json
{
    "success": true
}
```

#### errors

general types only

### location_request

Execute this command to get current position of the device. The device must support requesting function. 

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 99119 |
| type | optional. Default type sms | string | sms |

Request types: 
**sms** – GNSS data via SMS. Will send an SMS to request location. SMS gateway must be installed for the panel
**gsm** – GSM LBS data via GPRS. Device must have `online` or `GPS not updated` status
**gprs** – GNSS data via GPRS. Device must have `online` or `GPS not updated` status

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/location_request' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "99119"}'
```

#### response

```json
{ "success": true }
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
* 213 – Cannot perform action: the device is offline
* 214 – Requested operation or parameters are not supported by the device
* 256 – Location already actual

### register_quick

Registers a new tracker using only IMEI. Automatic SMS commands will not be sent for register. The device must be preconfigured.

**required subuser rights:** tracker_register

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| label | User-defined label for this tracker. Must consist of prontable characters and have length between 1 and 60 | string | Courier |
| group_id | Tracker group id, 0 if tracker does not belong to any group. The specified group must exist. See [group/list](./group/group.md#list) | int | 0 |
| imei | tracker's IMEI | string | 35645587458999 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/register_quick' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "label": "Courier", "group_id": "0", "imei": "35645587458999"}'
```

#### response

```js
{
    "success": true,
    "value": <tracker> //a newly created tracker
}
```

For `tracker` object structure, see [tracker/](#tracker-object-structure).

#### errors

* 13 – Operation not permitted – if user has insufficient rights
* 201 – Not found in database (if there is no bundle with such IMEI)
* 204 – Entity not found (if specified group does not exist)
* 220 – Unknown device model (if specified device model does not exist)
* 221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)
* 222 – Plugin not found (if specified plugin is not found or is not supported by device model)
* 223 – Phone number already in use (if specified phone number already used in another device)
* 224 – Device ID already in use (if specified device ID already registered in the system)
* 225 – Not allowed for this legal type (if tariff of the new device is not compatible with user’s legal type)
* 226 – Wrong ICCID (if specified ICCID was not found)
* 227 – Wrong activation code (if specified activation code was not found or is already activated)

### register_retry

Resends registration commands to the device. The panel must have installed SMS gateway.

**required subuser rights:** tracker_register

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |
| device_id | Device ID that was used to register, e.g. IMEI. It can be used instead of **tracker_id** for models with a fixed ID | string | 4568005588562 |
| apn_name | The name of GPRS APN of this sim card inserted into device | string | fast.tmobile.com |
| apn_user | The user of GPRS APN of this sim card inserted into device | string | tmobile |
| apn_password | The password of GPRS APN of thes sim card inserted into device | string | tmobile |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/register_retry' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "999119", "apn_name": "fast.tmobile.com", "apn_user": "tmobile", "apn_password": "tmobile"}'
```

#### response

```js
{
    "success": true,
    "value": <tracker> // a newly created tracker
}
```
For `tracker` object structure, see [tracker/](#tracker-object-structure).

#### errors

* 13 – Operation not permitted – if user has insufficient rights
* 204 – Entity not found (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
* 219 – Not allowed for clones of the device (if specified tracker is a clone)
* 214 – Requested operation or parameters are not supported by the device (if device does not have GSM module)
* 242 – Device already connected. (if tracker was connected to the server)

### register

Registers a new tracker device. During registration, device is linked with current API user’s account and automatically configured to send data to our servers (if device model supports it). The panel must have installed SMS gateway.

**required subuser rights:** tracker_register

#### parameters

**IMPORTANT**
Because of the variety of tracker models and business applications, there are many different ways to register tracker in our system. They are called [Registration plugins](../../commons/plugin/plugin.md). Each of registration plugins has its own set of additional parameters.

In addition to parameters specified in this section, you **must** pass all parameters which are required by the plugin you have chosen. See example below.

Common parameters are:

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| label | User-defined label for this tracker. Must consist of printable characters and have length between 1 and 60 | string | Courier |
| group_id | Tracker group id, 0 if tracker does not belong to any group. The specified group must exist. See [group/list](./group/group.md#list) | int | 0 |
| model | A code of one of the supported models. See [tracker/list_models](#list_models) | string | pt10 |
| plugin_id | An id of a registration plugin which will be used to register the device. See [Registration plugins](../../commons/plugin/plugin.md) | int | 37 |
| device_id | **Must** be specified if device model uses fixed device id. See [tracker/list_models](#list_models) | string | 4568005588562 |
| send_register_commands | Indicates send or not to send activation commands to device (via SMS or GPRS channel). If parameter is not specified or equals  `null` will be used the platform settings. Default: `null` | boolean | true/false |

#### example

In this example we use plugin id = 37 (see [Plugin description](../../commons/plugin/plugin.md)) 
to register Queclink GV55Lite. We chose to include the device to default group, so group ID is 0. 
As this device is identified by IMEI, we include it as device ID (123451234512346).

Also we include **phone**, **apn_name**, **apn_user**, **apn_password** of the sim card installed in 
device and **activation_code** since this parameters are required by plugin.

You can try to “auto-detect” APN settings by phone number 
using [apn_settings/read](./apn_settings/apn_settings.md#read) API call.

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/register' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "label": "Courier", "group_id": "0", "plugin_id": "37", "model": "qlgv55lite", "phone": "79123122312", "activation_code": "123123123", "device_id": "123451234512346", "apn_name": "fast.tmobile.com", "apn_user": "tmobile", "apn_password": "tmobile"}'
```

#### response

```js
{
    "success": true,
    "value": <tracker> //a newly created tracker
}
```
For `tracker` object structure, see [tracker/](#tracker-object-structure).

#### errors

* 13 – Operation not permitted – if user has insufficient rights
* 204 – Entity not found (if specified group does not exist. See group/list )
* 220 – Unknown device model (if specified device model does not exist)
* 221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)
* 222 – Plugin not found (if specified plugin is not found or is not supported by device model)
* 223 – Phone number already in use (if specified phone number already used in another device)
* 224 – Device ID already in use (if specified device ID already registered in the system)
* 225 – Not allowed for this legal type (if tariff of the new device is not compatible with user’s legal type)
* 226 – Wrong ICCID (Plugin specific: if specified ICCID was not found)
* 227 – Wrong activation code (Plugin specific: if specified activation code was not found or is already activated)
* 258 – Bundle not found (Plugin specific: if bundle not found for specified device ID)

### send_command

Sends command to tracker for performing special control, determined with "special_control" field of tracker model.

**required subuser rights:** tracker_configure, tracker_set_output

common command format is:

```js
"command":{
  "name": "command name", // required field
  "some_parameter1": <parameter value>, // parameters depends on certain command
  "some_parameter2": <parameter value>,
  ...
  "special_settings": { // optional field. its structure is defined with "special_control" field of tracker model
    "type": "settings type",
    "some_field1": <value>,
    "some_field2": <value>
    ...
  }
}
```

Certain commands which can be used is defined with `special_control` field of **tracker model** and corresponds the table below:

| special control | available commands |
| :--- | :--- |
| jointech_lock_password | electronic_lock_command, set_special_settings_command |
| hhd_lock_password | electronic_lock_command, set_special_settings_command |
| vg_lock_password | electronic_lock_command, set_special_settings_command |
| any other special control | set_special_settings_command |

#### command types

**electronic_lock_command**

This command is used to seal/unseal electronic lock.

```js
command {
  name: "electronic_lock_command",
  command_code: "unseal", // "seal"/"unseal"
  special_settings: <special settings JSON object>
}
```

**set_special_settings_command**

This command is equivalent to API call [tracker/settings/special/update](./settings/special/special.md#update).

```json
command {
  name: "set_special_settings_command"
  special_settings: <special settings JSON object>
}
```
See [special settings JSON object](./settings/special/special.md#read)

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999119 |
| command | Command that will be sent to device. Not Null| JSON object | See format above |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/send_command' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "999119", "command": {name: "electronic_lock_command", command_code: "unseal", special_settings:{"type":"electronic_lock_password", "password": "345892", "remember_password": "true"}}}'
```

#### response

```js
{
    "success": true,
    "list": [ {tracker}, ... ] // list of JSON-objects
}
```
For `tracker` object structure, see [tracker/](#tracker-object-structure).

#### errors

general types only

