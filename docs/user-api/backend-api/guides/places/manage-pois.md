# Managing POIs

Points of Interest (POI), or places, can serve various purposes, such as organizing a list of frequently visited clients, simplifying task management, and analyzing business data through reports. Custom fields can be added to these places to store additional information about locations and customers, enabling the creation of custom CRM or ERP systems and easy integration with third-party systems. These fields can include phone numbers, emails, and other relevant customer data, as well as assign specific employees to customers for better management.

This guide will describe how to create and use places with custom fields using the Navixy API.

## Creating Custom Fields and POIs

Before using fields and POIs, we need to create them. Our goal is to create a new customer record with all necessary information and assign an employee to this customer. The employee will be able to view all information in their mobile app. The place object is described [here](../../resources/field_service/place/index.md#place-object).

### Example Fields for a CRM System

For our CRM system, we need the following fields:
* `Label`: The customer's name.
* `Address`: The full address of the customer.
* `Description`: Additional information about the customer, such as working hours or specific details.
* `Tags`: Useful for searching and task management in the UI.
* `E-mail`: The customer's email address.
* `Phone`: The customer's phone number.
* `The last visit date`: To track the last visit date and notify employees if the customer hasn't been visited in a while.
* `The last order №`: To easily find the last order ID of the customer.
* `The last visit result`: A text field for employees to specify the results of their last visit.
* `Responsible employee`: To assign a place to a responsible employee who can see and update necessary information using their mobile app.

### Creating Custom Fields

Some fields are default and cannot be changed (Label, Address, Description, and Tags). All other necessary fields should be created manually.

!!!note "Custom fields added here will be available for all places."

First, get the entity ID to identify which entity to update and where to add fields.

**API Request:**

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

The response will provide the necessary entity ID with existing fields. Add new fields to this entity. Only add fields that do not already exist.

**API Request:**

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/fields/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "delete_missing": true, "entity_id": 520, "fields": [{"label": "E-mail", "required": false, "type": "email", "description": "Customer\'s email"}, {"label": "Phone", "required": false, "type": "phone", "description": "Customer\'s phone"}, {"label": "The last visit date", "required": false, "type": "text", "description": null}, {"label": "The last order №", "required": false, "type": "text", "description": null}, {"label": "The last visit result", "required": false, "type": "text", "description": null}, {"label": "Responsible employee", "params": {"responsible": true}, "required": false, "type": "employee", "description": null}]}'
    ```

The platform will confirm the update with:

```json
{
    "success": true,
    "list": [
        {
            "id": 2327,
            "label": "E-mail",
            "required": false,
            "description": "Customer's email",
            "type": "email"
        },
        {
            "id": 2328,
            "label": "Phone",
            "required": false,
            "description": "Customer's phone",
            "type": "phone"
        },
        {
            "id": 2329,
            "label": "The last visit date",
            "required": false,
            "description": null,
            "type": "text"
        },
        {
            "id": 2330,
            "label": "The last order №",
            "required": false,
            "description": null,
            "type": "text"
        },
        {
            "id": 2331,
            "label": "The last visit result",
            "required": false,
            "description": null,
            "type": "text"
        },
        {
            "id": 2332,
            "label": "Responsible employee",
            "required": false,
            "description": null,
            "params": {
                "responsible": true
            },
            "type": "employee"
        }
    ]
}
```

Once we have the field IDs, we can change their order in the entity. Update the entity accordingly.

**API Request:**

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entity": {"allowed": true, "id": 520, "type": "place", "settings": {"layout": {"sections": [{"label": "Places", "field_order": ["label", "location", "description", "tags", "2327", "2328", "2329", "2330", "2331", "2332"]}]}}}}'
    ```

### Creating POIs

With the fields set up, we can now create a location. The field names indicate the information we want to capture for each place. Fill in the parameters based on the client's data.

**API Request:**

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/create' \
        -H 'Content-Type: application/json' \
        {% raw %}-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "place": {"label": "Company1", "description": "Accepted one more deal for 7 devices next week", "files": [], "fields": {"2327": {"value": "shop1@email.com", "type": "email"}, "2328": {"value": "555231415221", "type": "phone"}, "2329": {"value": "10/10/2021", "type": "text"}, "2330": {"value": "87292", "type": "text"}, "2331": {"value": "Sold 10 devices", "type": "text"}, "2332": {"value": 71247, "type": "employee"}}, "location": {"address": "Lovell House, 6 Archway, Hulme, Manchester M15 5RN, UK", "lat": 53.46583133200717, "lng": -2.2464680671691895, "radius": 50}, "tags": [218916]}}{% endraw %}
    ```

The platform will confirm creation with:

```json
{
  "success": true,
  "id": 1521307
}
```

* `id`: The ID of the created place. It can be used for obtaining and updating the place object.

## Obtaining and Updating Information about Places

* To retrieve information about place objects (e.g., to sync this data with your CRM), use the [`place/list`](../../resources/field_service/place/index.md#list) API call.
* To get a count of visits to places, [`generate`](../../resources/commons/report/report_tracker.md#generate) a report with [ID 85](../../resources/commons/plugin/report_plugins.md#poi-visits-report).
* To update information about a place, use the [`place/update`](../../resources/field_service/place/index.md#update) API call.

### Getting POI Name by a Tracker's Location

To get the POI name or ID where a device is located, use the [`place/search_location`](../../resources/field_service/place/index.md#search_location) API call. For example, you may want to determine which place a device is located in or count how many devices are in a particular place.

To get this information, first request the device's [`state and location`](../../resources/tracking/tracker/index.md#get_state). Using the received latitude and longitude parameters, you can check the relevant places.