---
title: Forms usage
description: How to create forms for tasks.
---

# Forms usage

Task forms can be used in many areas of business. Delivery, sales, inspections, customer surveys, field reports. The 
results can be used to improve certain areas of your business, concentration in an area, or market analysis. The forms 
can be filled out by employees using the X-GPS tracker application. Employees can fill out forms when completing tasks 
or sending check-ins.

***

## Forms creation

To make it possible for employees to fill out forms, and for users to assign these forms to tasks, the form templates must
be [created](../resources/field_service/form/template.md#create). Let's create a form for different needs. For example, we have a delivery service. Customers order certain products,
such as trackers, which are delivered and, if necessary, installed by our staff. Find form fields that will be used 
[here](../resources/field_service/form/field-types.md).

We expect to see results on every task that's why we create a form that should be submitted only in a zone of a task. 
It is necessary to avoid task completion after our employee visited and spent some time in a task point. All fields we 
create are required to submit except one.

* The first field will be a text field to get customer's and company's name. 
* The second text field will contain information about what was delivered to our customer. 
* The third we will use is a checkbox field where additional provided services will be checked. Minimum checked fields 1, 
  maximum 3 and this field will be not required because if our customer will not order additional options our employee 
  will be unavailable to send this form and complete a task.
*Also, we add a signature field. It will help us to confirm that the customer received the order.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/template/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "template": {"label": "Trackers delivery", "description": "Employee, fill this form with every delivery", "fields": [{"id": "Text-1", "type": "text", "label": "Customer's name", "required": true, "description": "Specify here customer's and company's name", "max_length": 1000, "min_length": 1}, {"id": "Text-2", "type": "text", "label": "Delivered", "required": true, "description": "Specify here all delivered models and its amount", "max_length": 1000, "min_length": 1}, {"id": "Checkbox", "type": "checkbox_group", "label": "Additional options", "description": "Specify here all provided additional options", "group": [{"label": "Presentation and training"}, {"label": "Additional configuration"}, {"label": "Installation"}], "max_checked": 3, "min_checked": 1, "required": false}, {"id": "Signature", "type": "signature", "label": "Customer's signature", "description": "Let a customer add his signature about receiving the order", "required": true}], "submit_in_zone": true, "default": true}}'
    ```

The platform will respond with:

```json
{
    "success": true,
    "id": 111
}
```

***

## Form filling

Forms can be filled in two ways:

* Check-in. An employee sends information about his location with a filled form. Every employee of a user can choose a 
  created form to send it with check-ins. Additional assigning is not necessary.
* Task completion. An employee performs a task and sends a form as progress report. A form should be assigned to a task 
  before an employee will have a possibility to fill it in a task completion zone. 

***

### Form assigning

A form can be assigned to an existing task with [task update call](../resources/field_service/task/index.md#update) or can be used in the process of [task creation](../resources/field_service/task/index.md#create).

!!! note "`create_form` parameter should be `false` to add an already created form."

***

## Obtaining information from submitted forms

We can get submitted forms to analyze all information our employees specified in several ways. 

### Specific forms as they sent in tasks

* Obtain a [list of templates](../resources/field_service/form/template.md#list) to get a template_id of a form we
  are interested in.
* Obtain the [list of tasks](../resources/field_service/task/form/index.md#list) with the necessary form template_id and per specific time period.
* With this task_id we can request [downloading](../resources/field_service/task/form/index.md#download) or
  [reading](../resources/field_service/task/form/index.md#read) the necessary form.

Or

* Get a [list of tasks](../resources/field_service/task/index.md#list) to find a specific task and obtain a form_id from it. 
* Use this form_id to [read](../resources/field_service/form/index.md#read) and [download](../resources/field_service/form/index.md#download) forms.


### Specific forms as they sent in check-ins

* Obtain a list of [check-ins](../resources/field_service/checkin.md#list) to get form_id we are interested in.
* Use this form_id to [read](../resources/field_service/form/index.md#read) and [download](../resources/field_service/form/index.md#download) forms.

#### To get counted information in the report format

* [Generate](../resources/commons/report/report_tracker.md#generate) a form completion report 
  with [plugin_id 70](../resources/commons/plugin/report_plugins.md#form-completion-statistics-report).   
* [Download](../resources/commons/report/report_tracker.md#download) this report.

