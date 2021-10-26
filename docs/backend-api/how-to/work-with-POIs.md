---
title: How to create and work with points of interest. 
description: How to create and work with points of interest and using of custom fields with them. 
---

# How to create and work with points of interest.

Points of interest (POI) or places can be used for different purposes. They can help you organize your list of frequently
visited clients, simplify your work with tasks, and can be used to analyze your business with reports.

Custom fields have also been designed for them, which can be used to add additional necessary information about locations
and customers. They can be used for creation of your own CRM or ERP system, as well as for easy integration with third 
party systems. It is possible to add a phone number, e-mail, and other relevant customer data. To get to the next level,
it's possible to assign specific employees to a customer.

Here we will describe - how places with custom fields can be created and used.

<hr>

## Creation of fields and POIs

Before we start using fields and POIs we should create them. Our purpose is to create a new customer with necessary
information and assign an employee to him. This employee will be able to see the all information in his mobile app.
The place object described [here](../resources/field_service/place/index.md#place-object).

Example:
For our own CRM system we need to have the next fields:
* Label - there will be our customer's name.
* Address - full address where our customer located.
* Description - additional description about the customer. Like the working hours or something specific.
* Tags - here we will add tags. They will be useful to ease up searching and using for tasks in UI.
* E-mail - customer's email.
* Phone - customer's phone number.
* The last visit date - we are interested to see the last visit of customer. If the last visit will be more than X days 
  we will notify our employee about that.
* The last order № - to ease up the searching of the last customer's order_id.
* The last visit result - a text field where our employee can specify information about results of his last visit.
* Responsible employee - this field is necessary to assign a place to our responsible employee for this address. He will 
be able to see and change necessary information using his mobile app.

<hr>

### Custom fields

Some fields are default and can't be changed. They are Label, Address, Description and Tags. All other necessary fields 
should be created by ourselves. 

!!! note "Custom fields we change here will be added to all places we have and will create."

First we should get the entity ID to know - what entity we should update and where to add fields. 

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

In a reply we will receive a necessary entity ID with already existing fields in it. We should add new fields in this 
entity. We add only not existing fields that's why we will not list them in our request.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/fields/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "delete_missing": true, "entity_id": 520, "fields": [{"label": "E-mail", "required": false, "type": "email", "description": "Customer's email"}, {"label": "Phone", "required": false, "type": "phone", "description": "Customer's phone"}, {"label": "The last visit date", "required": false, "type": "text", "description": null}, {"label": "The last order №", "required": false, "type": "text", "description": null}, {"label": "The last visit result", "required": false, "type": "text", "description": null}, {"label": "Responsible employee", "params": {"responsible": true}, "required": false, "type": "employee", "description": null}]}'
    ```

The platform will confirm our update with:

```json
{
    "success": true,
    "list": [
      {"id":2327,
       "label":"E-mail",
       "required":false,
       "description":"Customer's email",
       "type":"email"
      },
      {"id":2328,
       "label":"Phone",
       "required":false,
       "description":"Customer's phone",
       "type":"phone" 
      },
      {
        "id": 2329,
        "label": "The last visit date",
        "required": false,
        "description": null,
        "type": "text"
      },
      {"id":2330, 
       "label":"The last order №",
       "required":false,
       "description":null,
       "type":"text"
      },
      {"id":2331,
       "label":"The last visit result", 
       "required":false,
       "description":null,
       "type":"text"
      },
      {"id":2332,
       "label":"Responsible employee",
       "required":false,
       "description":null,
       "params":{"responsible":true},
       "type":"employee"
      }
    ]
}
```

When the reply received we know what ids our fields have, and we can change their order in the entity. Now we should update 
our entity.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/entity/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entity": {"allowed": true, "id": 520, "type": "place", "settings": {"layout": {"sections": [{"label": "Places", "field_order": ["label", "location", "description", "tags", "2327", "2328", "2329", "2330", "2331", "2332"]}}}}'
    ```

<hr>

### POIs creation

We have successfully set the fields for all locations, and now we need to create a location. The names of the fields already
contain - what information we would like to see for each place. So we just need to fill in the parameters of these fields
according to the client's data.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "place": {"label": "Company1", "description": "accepted one more deal for 7 devices on the next week", "files": [], "fields": {{"2327": {"value": "shop1@email.com", "type": "email"}}, {"2328": {"value": "555231415221", "type": "phone"}}, {"2329": {"value": "10/10/2021", "type": "text"}}, {"2330": {"value": "87292", "type": "text"}}, {2331: {value: "Sold 10 devices", type: "text"}}, {"2332": {"value": 71247, "type": "employee"}}}, "location": {"address": "Lovell House, 6 Archway, Hulme, Manchester M15 5RN, UK", "lat": 53.46583133200717, "lng": -2.2464680671691895, "radius": 50}, "tags": [218916]}'
    ```

The platform will confirm creation with:

```json
{
  "success":true,
  "id":1521307
}
```

* `id` - int. An ID of the created place. It can be used for obtaining and updating the place object.

<hr>

## Obtaining and updating information about places

* To get information about place objects (for example, to pull this data to your CRM) use the 
[place/list](../resources/field_service/place/index.md#list) API call.

* To get a count of visits for places [generate](../resources/commons/report/report_tracker.md#generate) a report with
  [ID 85](../resources/commons/plugin/report_plugins.md#poi-visits-report).
  
* To update information about place use [place/update](../resources/field_service/place/index.md#update) API call.
