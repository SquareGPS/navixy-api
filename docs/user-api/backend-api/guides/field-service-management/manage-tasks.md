# How to Create and Assign Tasks

Tasks in Navixy are a feature used to plan and monitor the activities of field workers. They help in organizing and managing various operations such as service, delivery, transportation, merchandising, and trade. Tasks provide employees with detailed information including date, time, addresses, task descriptions, and contact numbers.
### How Do Tasks Operate?
1. **Creation**: Tasks are created with specific details such as the location, time, and description. They can be single-point tasks or route tasks with multiple checkpoints.
2. **Assignment**: Tasks are assigned to employees, typically those equipped with tracking devices. The tasks appear on their X-GPS tracker app, providing all necessary details.
3. **Execution**: Employees perform the tasks, updating their status and providing real-time information through the app. This can include check-ins, status updates, and form submissions.
4. **Monitoring**: Supervisors can monitor the progress of tasks, track the location of employees, and ensure that tasks are completed within the specified parameters.
5. **Completion**: Once tasks are completed, the system logs the details, allowing for reporting and analysis of field operations.

Tasks can be either **single-point** tasks or **route** tasks with multiple checkpoints. This guide explains how to create and assign both types of tasks using the Navixy API.

## Single Task

To create a new single task, use the [`task/create`](../../resources/field_service/task/index.md#create) method. You need to provide a JSON object that contains all the necessary information about the task. Optionally, you can create a form for the task by setting the `create_form` parameter to `true`.

### Example

Let's create a task for George to deliver new devices to an office on March 16th, from 12 PM to 2 PM. George's car has a tracker with ID 203190. He may be late by up to one hour due to potential traffic jams, and he needs at least 30 minutes at the office to complete the delivery and paperwork.

**API request:**

```shell
curl -X POST '{{ extra.api_example_url }}/task/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "task": {
            "tracker_id": 203190,
            "location": {
                "lat": 34.178868,
                "lng": -118.599672,
                "radius": 150
            },
            "label": "New devices to office",
            "description": "16 new devices",
            "from": "2021-03-16 12:00:00",
            "to": "2021-03-16 14:00:00",
            "max_delay": 60,
            "min_stay_duration": 30
        },
        "create_form": false
    }'
```

### Example Response

```json
{
    "success": true,
    "id": 111
}
```

## Route Task

To create a new route task, use the [`task/route/create`](../../resources/field_service/task/route/index.md#create) method. You need to provide a JSON object that contains all the necessary information about the route and its checkpoints.

### Example

Let's create a route task for John to deliver products to three customers on March 18th, from 10 AM to 4 PM. John's car has a tracker with ID 669673. Each checkpoint should be completed on time, and John needs at least 10 minutes at each location to hand over the goods and complete the paperwork.

**API request:**

```shell
curl -X POST '{{ extra.api_example_url }}/task/route/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "route": {
            "tracker_id": 669673,
            "label": "Products delivery",
            "description": "12 trackers of model 1 and 37 trackers of model 2",
            "from": "2020-03-18 10:00:00",
            "to": "2020-03-18 16:00:00"
        },
        "checkpoints": [
            {
                "tracker_id": 669673,
                "location": {
                    "lat": 34.178868,
                    "lng": -118.599672,
                    "radius": 100
                },
                "label": "Company1",
                "description": "5 trackers of model 1 and 15 trackers of model 2",
                "from": "2021-03-18 10:00:00",
                "to": "2021-03-18 12:00:00",
                "external_id": "10100",
                "max_delay": 0,
                "min_stay_duration": 10,
                "tags": [1, 4],
                "form_template_id": 132985
            },
            {
                "tracker_id": 669673,
                "location": {
                    "lat": 33.492830,
                    "lng": -112.177673,
                    "radius": 100
                },
                "label": "Company2",
                "description": "4 trackers of model 1 and 12 trackers of model 2",
                "from": "2021-03-18 12:00:00",
                "to": "2021-03-18 14:00:00",
                "external_id": "10101",
                "max_delay": 0,
                "min_stay_duration": 10,
                "tags": [2, 4],
                "form_template_id": 132985
            },
            {
                "tracker_id": 669673,
                "location": {
                    "lat": 39.801066,
                    "lng": -105.028685,
                    "radius": 100
                },
                "label": "Company3",
                "description": "3 trackers of model 1 and 10 trackers of model 2",
                "from": "2021-03-18 14:00:00",
                "to": "2021-03-18 16:00:00",
                "external_id": "10102",
                "max_delay": 0,
                "min_stay_duration": 10,
                "tags": [3, 4],
                "form_template_id": 132985
            }
        ],
        "create_form": false
    }'
```

### Example Response

```json
{
    "success": true,
    "result": {
        "id": 7115375,
        "user_id": 184541,
        "tracker_id": 669673,
        "label": "Products delivery",
        "description": "12 trackers of model 1 and 37 trackers of model 2",
        "from": "2021-03-18 10:00:00",
        "to": "2021-03-18 16:00:00",
        "creation_date": "2021-03-17 14:45:49",
        "status": "assigned",
        "status_change_date": "2021-03-17 14:45:49",
        "origin": "manual",
        "checkpoint_ids": [
            7115376,
            7115377,
            7115378
        ],
        "external_id": null,
        "type": "route"
    }
}
```

## Route Optimization

To optimize a route for minimizing transit time and costs, reorder the checkpoints before creating the route. Use the [`task/route/points/optimize`](../../resources/field_service/task/route/optimize.md) method to perform this optimization.

### Example Request

```shell
curl -X POST '{{ extra.api_example_url }}/task/route/points/optimize' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "start_point": {
            "lat": 34.178868,
            "lng": -118.599672,
            "departure": "2021-03-18 10:00:00"
        },
        "route_points": [
            {
                "location": {
                    "lat": 33.492830,
                    "lng": -112.177673
                },
                "from": "2021-03-18 10:00:00",
                "to": "2021-03-18 12:00:00"
            },
            {
                "location": {
                    "lat": 39.801066,
                    "lng": -105.028685
                },
                "from": "2021-03-18 12:00:00",
                "to": "2021-03-18 14:00:00"
            },
            {
                "location": {
                    "lat": 35.365948,
                    "lng": -108.112104
                },
                "from": "2021-03-18 14:00:00",
                "to": "2021-03-18 16:00:00"
            }
        ]
    }'
```

### Example Response

```json
{
    "success": true,
    "result": [
        0,
        1,
        2
    ]
}
```

## Association with Address

To associate a task or checkpoint with an address, include the address in the location object. Use the [`geocoder/search_location`](../../resources/tracking/geocoder.md#search_location) method to obtain an address when you have a location.