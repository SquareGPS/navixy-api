---
title: Tags usage
description: How to use tags and where they can help.
---

# Tags usage

“Tag” is a label for convenient and fast search of the desired information. In our system tags help you find desired
places, geofences, employees, tasks, trackers, and vehicles. You can create custom tags according to your needs. One 
object may have several tags. Tags are entities that could be assigned with objects.

***

## Case

I need to get easier searching by objects. For example, we have several places that are served by a certain team of 
employees, who in turn can only use the specified vehicles. We also want to easily find the tasks that we set for these teams.
To do this, we will assign a specific tag to all these objects.

***

## Creation

The first step is to [create](../resources/commons/tag/index.md#create) this tag. Let's name it "team1".

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag": {"name": "team1", "color": "#00BFFF"}}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/create?hash=a6aa75587e5c59c32d347da438505fc3&tag={"name": "team1", "color": "#00BFFF"}
    ```

The platform will reply with the created tag id. We can find this tag using the [tag/list](../resources/commons/tag/index.md#list)
call.

***

## Assigning

Now we need to assign this tag to our objects. We can do it using the update call for these objects. Also, we can assign
this tag to a new object while creating. It can be done with adding the "tags" parameter to objects in these calls:

* [place](../resources/field_service/place/index.md#place-object) object - [update](../resources/field_service/place/index.md#update)/[create](../resources/field_service/place/index.md#create). 
* [task](../resources/field_service/task/index.md#task-object) object - [update](../resources/field_service/task/index.md#update)/[create](../resources/field_service/task/index.md#create).
* [task_schedule](../resources/field_service/task/schedule/index.md#task-schedule-entry-object) object - [update](../resources/field_service/task/schedule/index.md#update)/[create](../resources/field_service/task/schedule/index.md#create).
* [employee](../resources/field_service/employee/index.md#employee-object) object - [update](../resources/field_service/employee/index.md#update)/[create](../resources/field_service/employee/index.md#create).
* [vehicle](../resources/fleet/vehicle/index.md#vehicle-object) object - [update](../resources/fleet/vehicle/index.md#update)/[create](../resources/fleet/vehicle/index.md#create).
* [zone](../resources/tracking/zone/index.md#entity-description) object - [update](../resources/tracking/zone/index.md#update)/[create](../resources/tracking/zone/index.md#create).
* [tracker](../resources/tracking/tracker/index.md#tracker-object-structure) object - There are no create and update calls for trackers. We should use [tags/set](../resources/tracking/tracker/index.md#tagsset) call for them.

***

## Searching objects with tag

Tags assigned with objects. To find all these objects with information we should use [tag/search](../resources/commons/tag/index.md#search)
call.

For example:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/search' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag_ids": [179227]}'
    ```

=== "HTTP GET"

    ```shell
    {{ extra.api_example_url }}/tag/search?hash=22eac1c27af4be7b9d04da2ce1af111b&tag_ids=[179227]
    ```

The platform will provide us with objects with assigned tag in the response:

???+ example "Response"

    ```json
    {
        "success": true,
        "result": {
            "place": [
                {
                    "id": 1446571,
                    "location": {
                        "lat": 56.82617746,
                        "lng": 60.59380531,
                        "address": "Ulitsa Kuybysheva, 24, Yekaterinburg, Sverdlovskaya oblast', Russia, 620144",
                        "radius": 100
                    },
                    "label": "New place",
                    "description": "",
                    "external_id": null,
                    "tags": [
                        179227
                    ]
                }
            ],
            "task": [
                {
                    "id": 8280866,
                    "user_id": 184541,
                    "tracker_id": 669673,
                    "status": "assigned",
                    "status_change_date": "2021-06-17 12:41:52",
                    "tags": [
                        179227
                    ],
                    "label": "New task ",
                    "description": "",
                    "external_id": null,
                    "creation_date": "2021-06-17 12:41:37",
                    "origin": "manual",
                    "location": {
                        "lat": 56.84437194,
                        "lng": 60.62976837,
                        "address": "Ulitsa Pervomayskaya, Д 59, Yekaterinburg, Sverdlovskaya oblast', Russia, 620075",
                        "radius": 152
                    },
                    "from": "2021-06-17 00:00:00",
                    "to": "2021-06-17 23:59:59",
                    "arrival_date": null,
                    "stay_duration": 0,
                    "min_stay_duration": 0,
                    "min_arrival_duration": 0,
                    "max_delay": 0,
                    "type": "task"
                }
            ],
            "employee": [
                {
                    "id": 55693,
                    "tracker_id": 669673,
                    "first_name": "Artem      ",
                    "middle_name": "",
                    "last_name": "",
                    "email": "",
                    "phone": "",
                    "driver_license_number": "",
                    "driver_license_cats": "",
                    "driver_license_issue_date": null,
                    "driver_license_valid_till": null,
                    "hardware_key": null,
                    "department_id": null,
                    "location": {
                        "lat": 56.86892633,
                        "lng": 60.53234832,
                        "address": "Prospekt Sedova, 33, Yekaterinburg, Sverdlovskaya oblast', Russia, 620050",
                        "radius": 150
                    },
                    "personnel_number": "1235341231",
                    "tags": [
                        179227
                    ]
                }
            ]
        }
    }
    ```
