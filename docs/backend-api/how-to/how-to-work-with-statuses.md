---
title: How to work with statuses
description: How to create status listings and statuses and how to assign status to device
---

# How to work with statuses

Statuses are used to track current employee activity (in fact, of tracking devices owned by employees).
The simplest example is "busy" | "not busy". This is a status listing consisting of two elements (statuses). Different
trackers can be assigned different status lists.

## Create

We need to create a status listing that we will assign to the device. Based on the statuses that are created for the sheet
- we will have a choice - what status can be assigned to the tracker.

To create the listing we need only one parameter:
* `listing` - [status_listing](../resources/tracking/status/index.md#status-listing-object-structure) object without "id" and "entries" fields.

For example, we will create a listing for the delivery service to allow drivers and supervisors to change the status.
Drivers can change their status using the X-GPS app. Supervisors can change status using the UI.

[API request](../resources/tracking/status/listing/index.md#create):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing": {"label": "Delivery_service", "employee_controlled": true, "supervisor_controlled": true}'
    ```

The response will contain id of a new status listing:

```json
{
    "success": true,
    "id": 1111
}
```

When we created a listing, we need to fill it with statuses, and we should use one request per one status.

For example, we have 4 statuses:
"Free", "Break", "Pick up the goods from storage", "Deliver goods".

[API request](../resources/tracking/status/index.md#create):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": 1111, "status": {"label": "Free", "color": "E57373"}}'
    ```

The response will contain id of a new status:

```json
{
    "success": true,
    "id": 1
}
```

## Assign

To assign the listing to some devices, we use the `tracker_id` and `listing_id.`

For example, we have 10 drivers. We should create 10 requests for assigning the listing to them.

[API request](../resources/tracking/status/listing/tracker.md#assign):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/tracker/assign' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 615487, "listing_id": 111}'
    ```

The platform will notify you about success in reply.

After that, our drivers and supervisors will have access to change statuses. Where they could be used:
We can create a script that will assign a new task to a driver with the status "Free". After assigning the task, this script
will change the status itself to "Pick up the goods from storage".
Or when the task was completed, a script changes the status to "Free" and gets fields from the ERP system, parses them to create
a new task assigns this task to a driver and so on.
