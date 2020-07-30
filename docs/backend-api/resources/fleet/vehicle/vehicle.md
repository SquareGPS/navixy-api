---
title: Vehicle
description: Vehicle  
---

# Vehicle

API path: `/vehicle`.

**vehicle** type is JSON object:

```js
{
    "id": 222,//int
    "tracker_id": 1, //int
    "label": "AGV",//string
    "max_speed": 90,// int
    "model": "Renault KERAX",//string
    "type": "truck",//string,  truck | car
    "subtype": "tractor",//optional, string depends on type, null means undefined
    "garage_id": null, // int
    "trailer" : "trailer1", // string, optional
    "manufacture_year" : 2001, // int, optional
    "color" : "some color", // string (not RGB!), optional
    "additional_info" : "additional info", // string, optional
    "reg_number": "А001АА96", //string
    "vin": "TMBJF25LXC6080000",//string
    "chassis_number": "",//string
    "frame_number" : "", // string, optional
    "payload_weight": 32000, //int, kilograms
    "payload_height": 1.2,//decimal
    "payload_length": 1.0,//decimal
    "payload_width": 1.0,//decimal
    "passengers": 4,//int
    "gross_weight" : null, // int, kilograms, optional
    "fuel_type": "petrol",//string petrol | diesel | gas
    "fuel_grade": "А-80",//string
    "norm_avg_fuel_consumption": 9.0,//decimal, liters
    "fuel_tank_volume": 50,//int
    "fuel_cost" : 100.3, decimal (per liter), optional
    "wheel_arrangement": "4x2", //string
    "tyre_size": "255/65 R16",//string
    "tyres_number": 4,//int
    "liability_insurance_policy_number": "12345",//string
    "liability_insurance_valid_till": "2015-03-01",//date
    "free_insurance_policy_number": "",//string
    "free_insurance_valid_till": null,//date
    "icon_id" : 55, // int, can be null, can only be updated via avatar/assign()
    "avatar_file_name": null,//<string>,
    "tags": [1,2] //array of tag ids
}
```

Subtypes:
null means undefined

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

## create()

Create new vehicle.

**required subuser rights**: vehicle_update

##### parameters

*   **vehicle** (JSON object) – object

#### return

    {
        "success": true,
        "id": 111 //id of the created vehicle
    }


#### errors

*   247 – Entity already exists, if tracker\_id!=null and exists vehicle that already binded to this tracker\_id


## delete()

Delete vehicle with the specified id.

**required subuser rights**: vehicle_update

#### parameters


*   **vehicle_id** (int) – Id of the vehicle to delete

#### return

```json
{ "success": true }
```


#### errors

*   201 – Not found in database (if there is no vehicle with such id)

## list()

Get all vehicles belonging to user.

#### return

```js
{
    "success": true,
    "list": [ ${vehicle}, ... ] // list of JSON objects
}
```


where **vehicle** described [here](#vehicle).

#### errors

general types only


## read()

Get vehicle by id.

#### parameters

*   **vehicle_id** (int) – Id of the vehicle

#### return

```
{
    "success": true,
    "value": <vehicle>
}
```

#### errors

*   201 – Not found in database (if there is no vehicle with such id)


## update()

Update existing vehicle.

**required subuser rights**: vehicle_update

#### parameters

*   **vehicle** – JSON object described [above](#vehicle).

#### return

```json
{ "success": true }
```


#### errors

*   201 – (Not found in database) If there is no vehicle with such id
*   247 – (Entity already exists) If **tracker_id** != **null** and exists vehicle that already binded to this **tracker_id**
*   261 – (Entity has external links) When **tracker_id** changes and there are some service tasks associated with this vehicle.
