---
title: How to create and work with points of interest. 
description: How to create and work with points of interest and using of custom fields with them. 
---

# How to create and work with points of interest.

Points of interest (POI) or places can be used for different purposes. They can help you organize your list of frequently
visited clients, simplify your work with tasks, and can be used to analyze your business with reports.

Custom fields have also been designed for them, which can be used to add additional necessary information about locations
and customers. ЕThey can be used for creation of your own CRM or ERP system, as well as for easy integration with third 
party systems. It is possible to add a phone number, e-mail, and other relevant customer data. To get to the next level,
it's possible to assign specific employees to a customer.

Here we will describe - how places with custom fields can be created and used.

<hr>

## Creation of fields and POIs

Before we start using fields and POIs we should create them. Our purpose is to create a new customer with necessary
information and assign an employee to him. This employee will be able to see the all information in his mobile app.

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

### Custom fields update

Some fields are default and can't be changed. They are Label, Address, Description and Tags. All other necessary fields 
should be created by ourselves. 

!!! note "Custom fields we change here will be added to all places we have and will create."

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": false, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7,"time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
    ```
