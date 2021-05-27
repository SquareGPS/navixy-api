---
title: How to create and assign tasks
description: How to create and assign single and route tasks
---

# How to create and assign tasks

Tasks are a handy feature for the Field Service. This tool allowed planning and monitoring the work of field workers. The number of possible goals for tasks is truly great. You can use them for service, delivery, transportation,
merchandising, trade, and more. The employee will receive all the necessary information for the day and time, addresses,
task description, contact numbers, etc.

To start work with tasks, they must be created. It will be a task with one point or several? This will determine whether
we create a single task, or a route task.

<hr>

### Single task

Creation of a new single task.

The list of necessary parameters is next:

`task` - a JSON object that contains all necessary information about the [task](../resources/field_service/task/index.md#task-object).
`create_form` - a boolean parameter that responsible for a form creation for this task.  If `true` then check additional `form_template_id` field in `task` object and [create form template](../resources/field_service/form/template.md#create) if it is not null. Default value is `false` for backward compatibility.

For example, we want to create the next task:

George will deliver new devices to the office on 16th of March, from 12 to 2 PM. His car has a tracker with id 203190.
Today may be some traffic jams that's why he may be late on one hour. Also, I know that he needs 30 minutes to get to the 
office, put in new devices, and fill in documents.

In this case, the `task` object will have the next parameters:

* `tracker_id` - to which tracker this task should be assigned.
* `location` - where the task should be.
* `label` - the name of a new task.
* `description` - a note about the task.
* `from` and `to` - when the task should be completed.
* `max_delay` - the employee may be late with the execution for a maximum of this time in minutes.
* `min_stay_duration` - the task will not be considered completed if the employee spends less than this time in the task's zone.

[API request](../resources/field_service/task/index.md#create):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task": {"tracker_id": 203190, "location": {"lat": 56.826486, "lng": 60.594784, "radius": 150}, "label": "New devices to office", "description": "16 new devices", "from": "2021-03-16 12:00:00", "to": "2021-03-16 14:00:00", "max_delay": 60, "min_stay_duration": 30}, "create_form": false}'
    ```

The response will contain id of a new task.

```json
{
    "success": true,
    "id": 111
}
```

<hr>

### Route task

Creation of a new route task.

The list of necessary parameters is next:

* `route` - JSON object containing all necessary information about the [route](../resources/field_service/task/route/index.md#route-object) without *IGNORED* fields.
* `checkpoint` - array of [checkpoint objects](../resources/field_service/task/checkpoint.md#checkpoint-object) without *IGNORED* fields.
* `create_form` - boolean. If `true` then check additional `form_template_id` field in every **checkpoint** object and create form if it is not null. Default value is `false` for backward compatibility.

For example, we need to create the next route:

John needs to deliver our products to three customers on 18th of March, from 10 AM to 4 PM. His car has a tracker with
id 669673. He can't get late because our customers will wait for production at the exact time and if he is late - the checkpoint
will be considered failed. This is how we know about the quality of delivery. Also, I know that he needs a minimum of 10 minutes
to hand over the goods to the client and fill out the documents.

In this case, every `checkpoint` object will have the next parameters:

* `tracker_id` - an id of the tracker to which checkpoint should be assigned.
* `location` - location associated with this checkpoint. cannot be null.
* `label` - the name of the checkpoint.
* `description` - a note about the checkpoint.
* `from` and `to` - the time when this checkpoint should be completed.
* `external_id` - this is a delivery code. It is necessary for a checkpoint because I have the plugin "Courier on the map".
  Customers can specify this id to the plugin and see - where the driver at the moment.
* `max_delay` - the employee may be late with the execution for a maximum of this time in minutes. In our case, it is 0 minutes.
* `min_stay_duration` - the task will not be considered completed if the employee spends less than this time in the task's zone.
* `tags` - for every client, I created a tag. This allows me to keep statistics and facilitate the search for delivery to
  this particular client.
* `form_template_id` - when employees hand over the objects, they fill this form that contains information about the quality
  of delivery, photos of delivered products, bill, and customer's signature.
  
The route object will have its own parameters too:

* `tracker_id` - an id of the tracker to which a route should be assigned.
* `label` - route name.
* `description` - additional information about the whole route.
* `from` and `to` - the time when this route should be completed.

[API request](../resources/field_service/task/route/index.md#create):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"tracker_id": 669673, "label": "Products delivery", "description": "12 trackers of model 1 and 37 trackers of model 2", "from": "2020-03-18 10:00:00", "to": "2020-03-18 16:00:00"}, "checkpoints": [{"tracker_id": 669673,  "location": {"lat": 56.82425647897021, "lng": 60.596146783275664, "radius": 100}, "label": "Company1", "description": "5 trackers of model 1 and 15 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 12:00:00", "external_id": "10100", "max_delay": 0, "min_stay_duration": 10, "tags": [1, 4], "form_template_id": 132985}, {"tracker_id": 669673,  "location": {"lat": 56.82425647897021, "lng": 60.5731415901079, "radius": 100}, "label": "Company2", "description": "4 trackers of model 1 and 12 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 14:00:00", "external_id": "10101", "max_delay": 0, "min_stay_duration": 10, "tags": [2, 4], "form_template_id": 132985}, {"tracker_id": 669673,  "location": {"lat": 56.839578390716234, "lng": 60.61191376742048, "radius": 100}, "label": "Company3", "description": "3 trackers of model 1 and 10 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 16:00:00", "external_id": "10102", "max_delay": 0, "min_stay_duration": 10, "tags": [3, 4], "form_template_id": 132985}], "create_form": false}'
    ```

The response will be:

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

#### Route optimization

If we need to get the optimized route that will minimize transit time and costs, it may be beneficial to reorder route checkpoints
before route creation. Our platform provides a way to perform such optimization. Provide data required to optimize, and the 
algorithm returns order in which points should be visited. Specify checkpoint objects in this order when you will create
the route.

Necessary parameters:

* `start_point` - JSON object with the point and time from that our driver will start the move.
* `route_points` - an array of JSON objects with points and time that driver should visit.

[API request](../resources/field_service/task/route/optimize.md#optimize):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/points/optimize' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "start_point": {"lng": 56.80556254658192, "lat": 60.61020017514418, "departure":  "2021-03-18 10:00:00"}, "route_points": [{"location": {"lng": 56.8070005643385, "lat": 60.59535651773674}, "from":  "2021-03-18 10:00:00", "to": "2021-03-18 12:00:00"}, {"location": {"lng": 56.81842686951902, "lat": 60.55908602826782}, "from":  "2021-03-18 10:00:00", "to": "2021-03-18 14:00:00"}, {"location": {"lng": 56.833240263651874, "lat": 60.55538664239149}, "from":  "2021-03-18 10:00:00", "to": "2021-03-18 16:00:00"}]'
    ```

Response will consist the order in that checkpoint objects should be specified in `checkpoints` parameter of route creation:

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
