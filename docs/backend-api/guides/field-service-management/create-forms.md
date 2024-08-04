# Using Task Forms

Task forms are versatile tools that can be utilized across various business functions such as delivery, sales, inspections, customer surveys, and field reports. The data collected through these forms can be instrumental in enhancing different aspects of your business, focusing on specific areas, or conducting market analysis. Employees can fill out these forms using the X-GPS tracker application during task completion or check-ins.

## Creating Forms

To enable employees to fill out forms and for users to assign these forms to tasks, form templates must be [created](../../resources/field_service/form/template.md#create). Let's create a form for a delivery service, where employees deliver products like trackers and provide additional services if needed. Detailed form field types can be found [here](../../resources/field_service/form/field-types.md).

For instance, we need a form that is submitted only within the task zone to ensure task completion is recorded only after the employee has visited the task location. All fields are required except one.

- **Text Field 1**: Customer's and company's name.
- **Text Field 2**: Information about delivered products.
- **Checkbox Field**: Additional services provided (minimum 1, maximum 3 options, not required).
- **Signature Field**: Customer's signature to confirm receipt of the order.

#### API Request:
=== "cURL"
```shell
curl -X POST '{{ extra.api_example_url }}/form/template/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "template": {
            "label": "Trackers Delivery",
            "description": "Employee, fill this form with every delivery",
            "fields": [
                {
                    "id": "Text-1",
                    "type": "text",
                    "label": "Customer\'s name",
                    "required": true,
                    "description": "Specify here customer\'s and company\'s name",
                    "max_length": 1000,
                    "min_length": 1
                },
                {
                    "id": "Text-2",
                    "type": "text",
                    "label": "Delivered",
                    "required": true,
                    "description": "Specify here all delivered models and their amounts",
                    "max_length": 1000,
                    "min_length": 1
                },
                {
                    "id": "Checkbox",
                    "type": "checkbox_group",
                    "label": "Additional options",
                    "description": "Specify here all provided additional options",
                    "group": [
                        {"label": "Presentation and training"},
                        {"label": "Additional configuration"},
                        {"label": "Installation"}
                    ],
                    "max_checked": 3,
                    "min_checked": 1,
                    "required": false
                },
                {
                    "id": "Signature",
                    "type": "signature",
                    "label": "Customer\'s signature",
                    "description": "Let a customer add their signature to confirm receipt of the order",
                    "required": true
                }
            ],
            "submit_in_zone": true,
            "default": true
        }
    }'
```

#### Example Response:
```json
{
    "success": true,
    "id": 111
}
```

## Filling Forms

Forms can be filled in two ways:

- **Check-in**: An employee sends their location with a filled form. Any employee can choose a created form to send with check-ins without additional assignment.
- **Task Completion**: An employee completes a task and submits a form as a progress report. The form should be assigned to the task beforehand.

### Assigning Forms

A form can be assigned to an existing task with the [task update](../../resources/field_service/task/index.md#update) call or used during [task creation](../../resources/field_service/task/index.md#create).

!!! note "`create_form` parameter should be `false` to add an already created form."

## Retrieving Information from Submitted Forms

You can analyze the submitted forms in several ways:

### Specific Forms Submitted with Tasks

- Obtain a [list of templates](../../resources/field_service/form/template.md#list) to get the `template_id` of the desired form.
- Retrieve the [list of tasks](../../resources/field_service/task/form/index.md#list) with the specific `template_id` and time period.
- Use the `task_id` to [download](../../resources/field_service/task/form/index.md#download) or [read](../../resources/field_service/task/form/index.md#read) the form.

Alternatively:
- Get a [list of tasks](../../resources/field_service/task/index.md#list) to find a specific task and obtain the `form_id`.
- Use the `form_id` to [read](../../resources/field_service/form/index.md#read) and [download](../../resources/field_service/form/index.md#download) the forms.

### Specific Forms Submitted with Check-ins

- Obtain a list of [check-ins](../../resources/field_service/checkin.md#list) to get the `form_id`.
- Use the `form_id` to [read](../../resources/field_service/form/index.md#read) and [download](../../resources/field_service/form/index.md#download) the forms.

### Generating Reports

To get summarized information in a report format:
- [Generate](../../resources/commons/report/report_tracker.md#generate) a form completion report with [plugin_id 70](../../resources/commons/plugin/report_plugins.md#form-completion-statistics-report).
- [Download](../../resources/commons/report/report_tracker.md#download) the report.