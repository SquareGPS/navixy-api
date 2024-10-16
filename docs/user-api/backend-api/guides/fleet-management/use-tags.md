# Using Tags

Tags in the Navixy system are labels that facilitate quick and convenient searches for places, geofences, employees, tasks, trackers, and vehicles. You can create custom tags according to your needs, and each object can have multiple tags assigned.

## Case

To streamline searching for objects, assign specific tags to related items. For example, if a team of employees services several places and uses specific vehicles, you can assign a unique tag to these objects. This way, you can easily find tasks assigned to these teams.

## Creation

First, create the tag using the `tag/create` method. Let's name it "team1."

API request:

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tag/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag": {"name": "team1", "color": "#00BFFF"}}'
```

=== "HTTP GET"

```shell
{{ extra.api_example_url }}/tag/create?hash=a6aa75587e5c59c32d347da438505fc3&tag={"name": "team1", "color": "#00BFFF"}
```

The platform will reply with the created tag ID. You can find this tag using the `tag/list` method.

## Assigning

Next, assign this tag to your objects. You can do this when updating or creating objects by adding the "tags" parameter:

* [Place](../../resources/field_service/place/index.md#place-object) - [update](../../resources/field_service/place/index.md#update)/[create](../../resources/field_service/place/index.md#create)
* [Task](../../resources/field_service/task/index.md#task-object) - [update](../../resources/field_service/task/index.md#update)/[create](../../resources/field_service/task/index.md#create)
* [Task schedule](../../resources/field_service/task/schedule/index.md#task-schedule-entry-object) - [update](../../resources/field_service/task/schedule/index.md#update)/[create](../../resources/field_service/task/schedule/index.md#create)
* [Employee](../../resources/field_service/employee/index.md#employee-object) - [update](../../resources/field_service/employee/index.md#update)/[create](../../resources/field_service/employee/index.md#create)
* [Vehicle](../../resources/fleet/vehicle/index.md#vehicle-object) - [update](../../resources/fleet/vehicle/index.md#update)/[create](../../resources/fleet/vehicle/index.md#create)
* [Zone](../../resources/tracking/zone/index.md#entity-description) - [update](../../resources/tracking/zone/index.md#update)/[create](../../resources/tracking/zone/index.md#create)
* [Tracker](../../resources/tracking/tracker/index.md#tracker-object-structure) - Use the `tags/set` method

## Searching Objects with Tags

To find all objects with a specific tag, use the `tag/search` method.

API request:

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

The platform will respond with objects that have the assigned tag:

???+ example "Response"

```json
{
    "success": true,
    "result": {
        "place": [
            {
                "id": 1446571,
                "location": {
                    "lat": 34.178868,
                    "lng": -118.599672,
                    "address": "21550 W Oxnard St, Woodland Hills, CA 91367, USA",
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
                    "lat": 33.492830,
                    "lng": -112.177673,
                    "address": "3836-3820 N 55th Ave, Phoenix, AZ 85031, USA",
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
                "first_name": "Andrew",
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
                    "lat": 39.801066,
                    "lng": -105.028685,
                    "address": "5735 Hooker St, Denver, CO 80221, United States",
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