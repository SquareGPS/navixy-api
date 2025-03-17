---
title: Get involved
description: Get involved into improving documentation and translations of the Navixy Platform
---
# Contributing to Developer documentation

Join us in enhancing Navixy developer documentation! Your contributions are highly valued and appreciated. Whether you’ve spotted an inaccuracy, found a typo, or have additional information to share, your help is appreciated. All our documentation is publicly available on [GitHub](https://github.com/SquareGPS/navixy-api), and you can get involved in several ways to make it better:

1. [Creating an issue with a detailed description of the problem.](https://github.com/SquareGPS/navixy-api/issues/new) 
2. [Editing a single page in a browser](#quick-edits-in-the-browser).
3. [Local editing and making multiple commits before creating a pull request.](#advanced-local-editing) 

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

## Local editing

For more comprehensive edits, or if you need to work on multiple pages, you can set up the documentation locally:

## Prerequisites

Before you start contributing to the Navixy API documentation in Stoplight, ensure you have the following tools installed:

- **Git** – Required for version control and managing your contributions
- **GitHub Account** – Needed for submitting your changes

Optional but recommended tools:

- **Stoplight Studio** – A visual editor for editing OpenAPI and Markdown files
- **Stoplight CLI** – Enables local previews of the documentation

### Getting started

Fork the repository, clone it to your local machine, and create a new branch for your changes. This keeps your contributions organized and makes the review process smoother.

### Editing documentation

#### Working with markdown files

The documentation consists primarily of Markdown files with Stoplight Flavored Markdown (SMD) extensions:

1. Navigate to the folder containing the documentation you want to edit
2. Open the relevant `.md` files in your preferred text editor or Stoplight Studio
3. Make your changes following the [Stoplight Flavored Markdown conventions](https://docs.stoplight.io/docs/platform/b591e6d161539-stoplight-flavored-markdown-smd)

#### Working with API specifications

If you're updating API endpoint documentation:

1. Locate the relevant OpenAPI specification files (`.yaml` or `.json`)
2. Edit them using Stoplight Studio for the best experience, or manually in a text editor
3. Ensure your changes maintain the correct OpenAPI syntax
4. Test your changes for validity if possible

### Previewing your changes

#### Using Stoplight Studio

For the best editing experience:

1. Open Stoplight Studio
2. Select "Open Existing Project" and navigate to your cloned repository
3. Make your edits and preview them in real-time within the Studio interface

#### Using Stoplight CLI

If you've installed the Stoplight CLI:

```sh
stoplight preview
```

This will start a local server where you can preview how your documentation changes will look.

### Submitting your changes

Commit your changes with clear, descriptive messages in English. Push to your fork on GitHub and create a pull request with a detailed description of your changes.

When creating your pull request, make sure to select `master` as the target branch. All contributions should be submitted against the master branch unless specifically instructed otherwise.

The repository maintainers will review your contribution and may request modifications or clarifications before merging.

### Documentation style guidelines

#### Documentation structure

The documentation includes three types of files:
* Documents (.md)
* API calls (.json or .yaml)

Documents are divided into semantic parts, starting with an introduction that summarizes the content.

#### API call descriptions

Each API call should include the following sections:

* **Introduction** - General information and purpose of the API call
* **Object structure** - Describes the object structure used in the calls (optional)
* **API Actions** - Base API call and associated actions, including:
    * **Action description** - Purpose of the API action
    * **Requirements** - Necessary permissions (optional)
    * **Parameters table** - Lists parameters for the API call with descriptions and data types
    * **Examples** - API call examples with parameters, including copy functionality
    * **Response** - Example of a successful server response with field descriptions
    * **Errors** - Specific errors related to the API action, plus a general error list

#### Example API documentation format

```markdown
# Resource name

Resource description.

## Object name

Object and its description.

## API actions

Path: `/path/to/resource/`.

### method_name

Method description.

#### Parameters

| name   | description  | type    | restrictions         |
|:-------|:-------------|:--------|:---------------------|
| param1 | description. | int     | `[1..100]`, not null |
| param2 | description. | boolean | not null             |

#### Examples

=== "cURL"
    ```shell
    curl -X POST 'https://api.navixy.com/v2/resource/sub_resource/action' \
    -H 'Content-Type: application/json' \
    -d '{"param1": "value1", "param2": "value2", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"
    ```http
    https://api.navixy.com/v2/resource/sub_resource/action?param1=value1&param2&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

    ```json
    {
      "success": true
    }
    ```

#### Errors

Special error codes.
```

Ensure your documentation is accurate and all examples work as described.

For actual examples, refer to [user](../../user-api/backend-api/resources/commons/user/index.md) and [source](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/master/docs/user-api/backend-api/resources/commons/user/index.md).
