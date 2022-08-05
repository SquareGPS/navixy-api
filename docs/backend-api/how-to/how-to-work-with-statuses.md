---
title: How to work with statuses
description: How to create working status lists and working statuses and how to assign them to device
---

# How to work with statuses

Statuses are used to track current employee activity (in fact, of tracking devices owned by employees).
The simplest example is "busy" | "not busy". This is a status listing consisting of two elements (working statuses). Different
trackers can be assigned different status lists.

***

## Create

We need to create a working status list that we will assign to the device. Based on the working statuses that are created for the sheet
- we will have a choice - what working status can be assigned to the tracker.

To create the working status list we need only one parameter:
* `listing` - [status_listing](../resources/tracking/status/listing/index.md#status-listing-object-structure) object without "id" and "entries" fields.

For example, we will create a working status list for the delivery service to allow drivers and supervisors to change the working status.
Drivers can change their working status using the X-GPS app. Supervisors can change working status using the UI.

[API request](../resources/tracking/status/listing/index.md#create):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing": {"label": "Delivery_service", "employee_controlled": true, "supervisor_controlled": true}'
    ```

The response will contain id of a new working status list:

```json
{
    "success": true,
    "id": 1111
}
```

When we created a working status list, we need to fill it with working statuses, and we should use one request per one working status.

For example, we have 4 working statuses:
"Free", "Break", "Pick up the goods from storage", "Deliver goods".

[API request](../resources/tracking/status/index.md#create):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": 1111, "status": {"label": "Free", "color": "E57373"}}'
    ```

The response will contain id of a new working status:

```json
{
    "success": true,
    "id": 1
}
```

***

## Assign

To assign the working status list to some devices, we use the `tracker_id` and `listing_id.`

For example, we have 10 drivers. We should create 10 requests for assigning the working status list to them.

[API request](../resources/tracking/status/listing/tracker.md#assign):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/tracker/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 615487, "listing_id": 111}'
    ```

The platform will notify you about success in reply.

After that, our drivers and supervisors will have access to change working statuses. Where they could be used:
We can create a script that will assign a new task to a driver with the working status "Free". After assigning the task, this script
will change the working status itself to "Pick up the goods from storage".
Or when the task was completed, a script changes the working status to "Free" and gets fields from the ERP system, parses them to create
a new task assigns this task to a driver and so on.
