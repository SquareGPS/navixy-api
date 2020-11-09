---
title: Vehicle
description: Vehicle  
---

# Vehicle

API path: `/vehicle`.

## Vehicle object

```json
{
    "id": 222,
    "tracker_id": 1,
    "label": "AGV",
    "max_speed": 90,
    "model": "Renault KERAX",
    "type": "truck",
    "subtype": "tractor",
    "garage_id": null,
    "trailer" : "trailer1",
    "manufacture_year" : 2001,
    "color" : "some color",
    "additional_info" : "additional info",
    "reg_number": "А001АА96",
    "vin": "TMBJF25LXC6080000",
    "chassis_number": "",
    "frame_number" : "",
    "payload_weight": 32000,
    "payload_height": 1.2,
    "payload_length": 1.0,
    "payload_width": 1.0,
    "passengers": 4,
    "gross_weight" : null,
    "fuel_type": "petrol",
    "fuel_grade": "А-80",
    "norm_avg_fuel_consumption": 9.0,
    "fuel_tank_volume": 50,
    "fuel_cost" : 100.3,
    "wheel_arrangement": "4x2",
    "tyre_size": "255/65 R16",
    "tyres_number": 4,
    "liability_insurance_policy_number": "12345",
    "liability_insurance_valid_till": "2020-10-15",
    "free_insurance_policy_number": "",
    "free_insurance_valid_till": null,
    "icon_id" : 55,
    "avatar_file_name": null,
    "tags": [1,2]
}
```

* `id` - int. An id of a vehicle.
* `tracker_id` - int. An id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.
* `label` - string. Vehicle's label.
* `max_speed` - int. Maximum speed of a vehicle.
* `model` - string. Vehicle's model.
* `type`  string enum. Vehicle's type. Can be "truck" | "car" | "bus" | "special".
* `subtype` - optional string enum. Depends on type, null means undefined. Possible subtypes listed below.
* `garage_id` - nullable int. An id of a garage.
* `trailer` - optional string. Information about a trailer.
* `manufacture_year` - optional int. Manufacture year of a vehicle.
* `color` - optional string. Not RGB. A color of a vehicle.
* `additional_info` - optional string. Additional info about a vehicle.
* `reg_number` - string. Reg number/ license plate of a vehicle.
* `vin` - string. VIN of a vehicle.
* `chassis_number` - string. Chassis number of a vehicle.
* `frame_number` - optional string. Frame number of a vehicle.
* `payload_weight` - int. Payload weight in kilograms.
* `payload_height` - decimal. Payload height in millimeters.
* `payload_length` - decimal. Payload length in millimeters.
* `payload_width` - decimal. Payload width in millimeters.
* `passengers` - int. A maximum count of passengers.
* `gross_weight` - optional int. Gross weight in kilograms.
* `fuel_type` - string enum. Can be "petrol" | "diesel" | "gas". 
* `fuel_grade` - string. Grade of fuel used in a vehicle.
* `norm_avg_fuel_consumption` - decimal. Normal average fuel consumption in liters per 100 km.
* `fuel_tank_volume` - int. Fuel tank capacity in liters.
* `fuel_cost` - optional decimal. Cost of fuel used in a vehicle per liter. 
* `wheel_arrangement` - string. Wheel arrangement of a vehicle.
* `tyre_size` - string. Tyre size.
* `tyres_number` - int. Number of tyres.
* `liability_insurance_policy_number` - string. Liability insurance policy number.
* `liability_insurance_valid_till` - string date. The date till liability insurance valid.
* `free_insurance_policy_number` -  string. Free insurance policy number.
* `free_insurance_valid_till` - string date. The date till free insurance valid.
* `icon_id` - nullable int. Can only be updated via [avatar/assign](../vehicle/avatar.md#assign).
* `avatar_file_name` - string. File name.
* `tags` - array of int. List of tag ids.

???+ example "Subtypes:"
    ```
        Type: "car"
        Subtypes: "sedan", "universal", "hatchback", "liftback", "limousine", "pickup", "minivan", "coupe", "coupe4d", "muscle", "convertible", "phaeton", "lando", "crossover", "roadster", "suv"
    ```
    ```
        Type: "truck"
        Subtypes: "tipper", "board", "covered", "awning", "mixer", "tanker", "refrigerator", "transporter", "container", "tractor"
    ```
    ```
        Type: "bus"
        Subtypes: "city", "shuttle", "platform", "school", "intercity", "sightseeing"
    ```
    ```
        Type: "special"
        Subtypes: "mobile_crane", "racing", "buggy", "ambulance", "firefighter", "hearse", "shop", "harvester", "snowplow", "tractor", "grader", "excavator", "bulldozer", "armored", "amphibian"
    ```

### create

Creates a new vehicle.

**required sub-user rights**: `vehicle_update`

##### parameters

| name | description | type |
| :------ | :------ | :----- |
| vehicle | A [vehicle object](#vehicle object) without `id` field. | JSON object |
| force_reassign | Optional. Default is `true`. Will reassign the device to created vehicle even if it was assign to another one. | boolean |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle": {"additional_info": null, "avatar_file_name": null, "chassis_number": "", "color": null, "frame_number": "", "free_insurance_policy_number": "", "free_insurance_valid_till": null, "fuel_cost": null, "fuel_grade": "", "fuel_tank_volume": null, "fuel_type": null, "garage_id": null, "gross_weight": null, "icon_color": "1E96DC", "icon_id": null, "label": "Vehicle", "liability_insurance_policy_number": "", "liability_insurance_valid_till": null, "manufacture_year": 2020, "max_speed": 160, "model": "", "norm_avg_fuel_consumption": null, "passengers": 1, "payload_height": 1868, "payload_length": 2820, "payload_weight": null, "payload_width": 1972, "reg_number": "AB234D", "subtype": "sedan", "tags": [], "tracker_id": null, "trailer": null, "type": "car", "tyre_size": "", "tyres_number": null, "vin": "45468743418579751", "wheel_arrangement": null}}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An id of the created vehicle.

#### errors

* 247 – Entity already exists, if tracker_id!=null and exists a vehicle that already bound to this tracker_id.

### delete

Deletes a vehicle with the specified id.

**required sub-user rights**: `vehicle_update`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| vehicle_id | Id of the vehicle to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle_id": 127722}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/delete?hash=a6aa75587e5c59c32d347da438505fc3&vehicle_id=127722
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no vehicle with such an id).

### list

Get all vehicles belonging to user.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "id": 222,
        "tracker_id": 1,
        "label": "AGV",
        "max_speed": 90,
        "model": "Renault KERAX",
        "type": "truck",
        "subtype": "tractor",
        "garage_id": null,
        "trailer" : "trailer1",
        "manufacture_year" : 2001,
        "color" : "some color",
        "additional_info" : "additional info",
        "reg_number": "А001АА96",
        "vin": "TMBJF25LXC6080000",
        "chassis_number": "",
        "frame_number" : "",
        "payload_weight": 32000,
        "payload_height": 1.2,
        "payload_length": 1.0,
        "payload_width": 1.0,
        "passengers": 4,
        "gross_weight" : null,
        "fuel_type": "petrol",
        "fuel_grade": "А-80",
        "norm_avg_fuel_consumption": 9.0,
        "fuel_tank_volume": 50,
        "fuel_cost" : 100.3,
        "wheel_arrangement": "4x2",
        "tyre_size": "255/65 R16",
        "tyres_number": 4,
        "liability_insurance_policy_number": "12345",
        "liability_insurance_valid_till": "2020-10-15",
        "free_insurance_policy_number": "",
        "free_insurance_valid_till": null,
        "icon_id" : 55,
        "avatar_file_name": null,
        "tags": [1,2]
    }]
}
```

#### errors

[General](../../../getting-started.md#error-codes) types only.

### read

Gets vehicle by specified id.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| vehicle_id | Id of a vehicle. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle_id": 127722}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/read?hash=a6aa75587e5c59c32d347da438505fc3&vehicle_id=127722
    ```

#### response

```json
{
    "success": true,
    "value": {
         "id": 222,
         "tracker_id": 1,
         "label": "AGV",
         "max_speed": 90,
         "model": "Renault KERAX",
         "type": "truck",
         "subtype": "tractor",
         "garage_id": null,
         "trailer" : "trailer1",
         "manufacture_year" : 2001,
         "color" : "some color",
         "additional_info" : "additional info",
         "reg_number": "А001АА96",
         "vin": "TMBJF25LXC6080000",
         "chassis_number": "",
         "frame_number" : "",
         "payload_weight": 32000,
         "payload_height": 1.2,
         "payload_length": 1.0,
         "payload_width": 1.0,
         "passengers": 4,
         "gross_weight" : null,
         "fuel_type": "petrol",
         "fuel_grade": "А-80",
         "norm_avg_fuel_consumption": 9.0,
         "fuel_tank_volume": 50,
         "fuel_cost" : 100.3,
         "wheel_arrangement": "4x2",
         "tyre_size": "255/65 R16",
         "tyres_number": 4,
         "liability_insurance_policy_number": "12345",
         "liability_insurance_valid_till": "2020-10-15",
         "free_insurance_policy_number": "",
         "free_insurance_valid_till": null,
         "icon_id" : 55,
         "avatar_file_name": null,
         "tags": [1,2]
    }
}
```

A [vehicle object](#vehicle object).

#### errors

* 201 – Not found in the database (if there is no vehicle with such an id).

### update

Updates existing vehicle.

**required sub-user rights**: `vehicle_update`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| vehicle | A [vehicle object](#vehicle object). | JSON object |
| force_reassign | Optional. Default is `true`. Will reassign the device to created vehicle even if it was assign to another one. | boolean |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle": {"additional_info": null, "avatar_file_name": null, "chassis_number": "", "color": null, "frame_number": "", "free_insurance_policy_number": "", "free_insurance_valid_till": null, "fuel_cost": null, "fuel_grade": "", "fuel_tank_volume": null, "fuel_type": null, "garage_id": null, "gross_weight": null, "icon_color": "1E96DC", "icon_id": null, "id": 223155, "label": "Vehicle", "liability_insurance_policy_number": "", "liability_insurance_valid_till": null, "manufacture_year": 2020, "max_speed": 160, "model": "", "norm_avg_fuel_consumption": null, "passengers": 1, "payload_height": 1868, "payload_length": 2820, "payload_weight": null, "payload_width": 1972, "reg_number": "AB234D", "subtype": "sedan", "tags": [], "tracker_id": null, "trailer": null, "type": "car", "tyre_size": "", "tyres_number": null, "vin": "45468743418579751", "wheel_arrangement": null}}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – (Not found in the database) If there is no vehicle with such an id.
* 247 – Entity already exists, if tracker_id!=null and exists a vehicle that already bound to this tracker_id.
* 261 – (Entity has external links) When `tracker_id` changes and there are some service tasks associated with this vehicle.

### batch_convert
Convert batch of tab-delimited vehicles and return list of checked vehicles with errors.

**Required subuser rights:** `vehicle_update`.

#### parameters
name | description | type
--- | --- | ---
batch | batch of tab-delimited vehicles. | String
file_id | preloaded file ID | String
fields | Optional, array of field names, default is `["label", "model", "reg_number", "fuel_grade"]` | array of strings
geocoder | geocoder type | String


If `file_id` is set – `batch` parameter will be ignored.

#### response

```json
{
    "success": true,
    "list": [ <checked_vehicle>, ... ],
    "limit_exceeded": false // true if given batch constrained by limit      
}
```

where `checked_vehicle` is:

```json
{
    ... // all fields from <vehicle>
    "errors": <array_of_objects> // optional
}
```

#### errors
* 234 (Invalid data format)