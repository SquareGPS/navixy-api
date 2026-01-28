---
title: Get involved
description: >-
  Get involved into improving documentation and translations of the Navixy
  Platform
---

# Get involved

## Contributing to Developer documentation

Join us in enhancing Navixy developer documentation! Your contributions are highly valued and appreciated. Whether you’ve spotted an inaccuracy, found a typo, or have additional information to share, your help is appreciated. All our documentation is publicly available on [GitHub](https://github.com/SquareGPS/navixy-api), and you can get involved in several ways to make it better:

1. [Creating an issue with a detailed description of the problem.](https://github.com/SquareGPS/navixy-api/issues/new)
2. [Editing a single page in a browser](./#quick-edits-in-the-browser).
3. [Local editing and making multiple commits before creating a pull request.](./#advanced-local-editing)

In each case, a GitHub account is required. If you prefer not to register on GitHub, you can [contact us](../contacts.md) with any feedback or suggestions.

### Quick edits in the browser

For simple, quick edits, you can use the built-in GitHub editor:

1. On any documentation page, find the pencil icon in the upper right corner and click it.
2. You will be prompted to create a fork of the repository if you haven't already.
3. Click the green "Create fork" button. This will open the source code of the page in an editable format.
4. Make your edits directly in the browser.
5. Provide a brief description of your changes in the commit message box.
6. Click the "Propose changes" button to create a new branch in your fork.
7. Submit a pull request from your fork to the main repository.

We will review your pull request and, once approved, merge it into the main branch. This method is best for minor, single-page edits.

### Local editing

For more comprehensive edits, or if you need to work on multiple pages, you can set up the documentation locally:

#### Prerequisites

Before you start contributing to the Navixy API documentation in Stoplight, ensure you have the following tools installed:

* [**Git**](https://git-scm.com/downloads) – Required for version control and managing your contributions
* [**GitHub Account**](https://github.com/login) – Needed for submitting your changes

#### Editing documentation

{% stepper %}
{% step %}
**Getting started**

Fork the [repository](https://github.com/SquareGPS/navixy-api), clone it to your local machine, and create a new branch for your changes. This keeps your contributions organized and makes the review process smoother.
{% endstep %}

{% step %}
**Working with markdown files**

The documentation consists primarily of Markdown files with GFM (GitHub Flavored Markdown) extensions:

1. Navigate to the folder containing the documentation you want to edit
2. Open the relevant `.md` files in your preferred text editor
3. Make your changes following the [GitHub Flavored Markdown conventions](https://github.github.com/gfm/)
{% endstep %}

{% step %}
**Working with API specifications**

If you're updating API endpoint documentation:

1. Locate the relevant OpenAPI specification files `.yaml` or `.json`(if applicable)
2. Edit them in an IDE of choice
3. Ensure your changes maintain the correct OpenAPI syntax or follow Documentation style guidelines
4. Test your changes for validity if possible (**try out** requests)
{% endstep %}

{% step %}
**Submitting your changes**

Commit your changes with clear, descriptive messages in English. Push to your fork on GitHub and create a pull request with a detailed description of your changes.

When creating your pull request, make sure to select `master` as the target branch. All contributions should be submitted against the master branch unless specifically instructed otherwise.

The repository maintainers will review your contribution and may request modifications or clarifications before merging.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
When adding new pages to the documentation, you must update the [\`SUMMARY.md](../../SUMMARY.md)\` file in the repository to ensure your changes appear in the published documentation. The table of contents is generated from this file.
{% endhint %}

## Documentation style guidelines

### Documentation structure

The documentation includes two types of files:

* Documents (.md)
* API calls (.json or .yaml)

Documents are divided into semantic parts, starting with an introduction that summarizes the content.

### API call descriptions

Each API call documentation should include:

* **Introduction** - Resource overview and purpose
* **Hint block** - Warnings/limitations (optional, use `{% hint style="warning" %}`)
* **Object structure** - JSON objects with field descriptions (optional)
* **API Actions** section with base path, containing:
  * **Action name** - Method heading
  * **Description** - What the action does
  * **Required permissions** - If applicable (optional)
  * **Parameters** - Table with name, description, type, format
  * **Examples** - Tabbed cURL and HTTP GET examples (`{% tabs %}`)
  * **Response** - JSON example with field descriptions
  * **Errors** - Specific codes plus link to general errors

### Example API documentation format (MD reference)

{% code overflow="wrap" expandable="true" %}
````markdown
# Resource name

Brief description of the resource explaining its purpose and main functionality.

{% hint style="warning" %}
Use for important notices, limitations, or warnings. Optional - remove if not needed.
{% endhint %}

## Object structure

Describe what the object represents and when it's used in the API.
```json
{
  "id": 123456,
  "label": "object label",
  "parameter1": "value1",
  "nested_object": {
    "field1": "value",
    "field2": 100
  }
}
```

List each field with its type and description:

* `id` - int. Unique identifier.
* `label` - string. Human-readable name.
* `parameter1` - string. Description of parameter.
* `nested_object` - object. Description of nested object.
  * `field1` - string. Description.
  * `field2` - int. Description.

# API actions

API base path: `/path/to/resource`.

## method_name

Explain what this action does, its purpose, and expected outcome.

**required permissions:** `permission_name` (optional - include only if specific permissions needed).

### Parameters

List all parameters with descriptions, marking required vs optional.

| name    | description                                      | type    | format   |
| ------- | ------------------------------------------------ | ------- | -------- |
| param1  | Description. Required. Constraints if any.       | int     | 123456   |
| param2  | Description. Optional. Default value if any.     | boolean | true     |

### Examples

Provide working examples with realistic values in both formats.

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/resource/sub_resource/action' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "param1": 123456}'
```

{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/resource/sub_resource/action?hash=a6aa75587e5c59c32d347da438505fc3&param1=123456
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Response

Show example of successful response with all possible fields.
```json
{
  "success": true,
  "value": {
    "id": 123456,
    "label": "object label"
  }
}
```

Describe response structure and all returned fields:

* `success` - boolean. Always `true` for successful responses.
* `value` - object. The returned object. See [structure above](#object-structure).

### Errors

List specific error codes this action can return, then link to general errors.

* 201 - Not found in the database – if resource does not exist.
* 7 - Invalid parameters – if parameters don't meet validation requirements.

[General error codes](https://www.navixy.com/docs/navixy-api/user-api/backend-api/errors) 
````
{% endcode %}

Ensure your documentation is accurate and all examples work as described.

For actual examples, refer to [user](../../user-api/backend-api/resources/commons/user/index.md) and [tracker](../../panel-api/resources/tracker.md#list) sections.
