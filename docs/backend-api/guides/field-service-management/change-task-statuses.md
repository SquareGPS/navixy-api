# Changing Employee Statuses

Employee statuses track the current activity of employees via their tracking devices. Examples include "busy" and "not busy." Each tracker can have a different status list assigned.

## Create

To manage employee activities effectively, create working status lists and assign them to devices. For instance, a status list for a delivery service allows drivers and supervisors to change their working status using the X-GPS app or the UI.

To create a working status list, use the `status/listing/create` method. You need to provide the `listing` parameter, which is a [status_listing](../../resources/tracking/status/listing/index.md#status-listing-object-structure) object without the "id" and "entries" fields.

### Example Request to Create a Working Status List

```shell
curl -X POST '{{ extra.api_example_url }}/status/listing/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "listing": {
            "label": "Delivery_service",
            "employee_controlled": true,
            "supervisor_controlled": true
        }
    }'
```

### Example Response

```json
{
    "success": true,
    "id": 1111
}
```

Next, add individual working statuses to the list. For example, you might have the following statuses: "Free," "Break," "Pick up the goods from storage," and "Deliver goods."

### Example Request to Add a Working Status

```shell
curl -X POST '{{ extra.api_example_url }}/status/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "listing_id": 1111,
        "status": {
            "label": "Free",
            "color": "E57373"
        }
    }'
```

### Example Response

```json
{
    "success": true,
    "id": 1
}
```

Repeat the above request for each working status you need to add to the list.

## Assign

To assign the working status list to devices, use the `tracker_id` and `listing_id`.

### Example Request to Assign a Status List to a Tracker

```shell
curl -X POST '{{ extra.api_example_url }}/status/listing/tracker/assign' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "tracker_id": 615487,
        "listing_id": 111
    }'
```

### Example Response

```json
{
    "success": true
}
```

## Usage

Once assigned, drivers and supervisors can change working statuses. Here are some use cases:

1. **Automated Task Assignment:** Create a script to assign a new task to a driver with the working status "Free." After assigning the task, the script changes the working status to "Pick up the goods from storage."

2. **Task Completion:** When a task is completed, a script changes the working status to "Free" and retrieves fields from the ERP system to create a new task and assign it to the driver.

This flexible system allows for efficient management of employee activities and can be integrated with various business processes for automation.