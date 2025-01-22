---
title: Get involved
description: Get involved into improving documentation and translations of the Navixy Platform
---
# Contributing to Developer Documentation

Join us in enhancing Navixy developer documentation! Your contributions are highly valued and appreciated. Whether you’ve spotted an inaccuracy, found a typo, or have additional information to share, your help is appreciated. All our documentation is publicly available on [GitHub]({{ config.repo_url }}), and you can get involved in several ways to make it better:

1. [Creating an issue]({{ config.repo_url }}issues/new) with a detailed description of the problem.
2. [Editing a single page in a browser](#quick-edits-in-the-browser).
3. [Installing and editing](#advanced-local-editing) and making multiple commits before creating a pull request.

In each case, a GitHub account is required. If you prefer not to register on GitHub, you can [contact us](../contacts.md) with any feedback or suggestions.

### Quick Edits in the Browser

For simple, quick edits, you can use the built-in GitHub editor:

1. On any documentation page, find the pencil icon in the upper right corner and click it.
2. You will be prompted to create a fork of the repository if you haven't already.
3. Click the green "Create fork" button. This will open the source code of the page in an editable format.
4. Make your edits directly in the browser.
5. Provide a brief description of your changes in the commit message box.
6. Click the "Propose changes" button to create a new branch in your fork.
7. Submit a pull request from your fork to the main repository. 

We will review your pull request and, once approved, merge it into the main branch. This method is best for minor, single-page edits.

### Advanced Local Editing

For more comprehensive edits, or if you need to work on multiple pages, you can set up the documentation locally:

1. **Install Python and Git:**
    - Download and install [Python 3.7.9](https://www.python.org/downloads/release/python-379/). Newer versions might not work correctly.
    - Download and install the [Git client](https://git-scm.com/downloads).

2. **Set Up Your Development Environment:**
    - Install an Integrated Development Environment (IDE), such as [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community edition is sufficient).
    - Fork the [Navixy documentation repository]({{ config.repo_url }}).
    - Clone your fork to your local machine using your IDE: `File` -> `New` -> `Project from version control`.

3. **Install Dependencies:**
    - Open a terminal or command prompt and navigate to your project directory.
    - Set up a virtual environment:
      ```sh
      cd /path/to/project/on/your/pc
      mkdir venv
      python -m venv ./venv
      ```
    - Activate the virtual environment:
        - On Windows:
        ```
        C:\path\to\project\venv\Scripts\activate.bat
        ```
        - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
    - Install MkDocs and dependencies:
      ```sh
      pip install -r requirements.txt
      ```

4. **Run the Documentation Locally:**
    - Start the local MkDocs server:
      ```sh
      mkdocs serve --dirtyreload
      ```
    - Open your browser and navigate to `http://localhost:8000` to see the documentation.

5. **Make Your Edits:**
    - Create a new branch in your local Git repository (avoid using the master branch).
    - Make your changes and preview them locally in the browser.
    - Commit your changes with clear commit messages in English.

6. **Submit Your Changes:**
    - Push your changes to your fork on GitHub.
    - Open a pull request from your fork to the main repository. Ensure your pull request description is in English.

After your pull request is reviewed and merged, you can delete your branch and rebase your fork to the upstream repository.

## Introduction to MkDocs

Our documentation is built using [MkDocs](https://mkdocs.org) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material) theme. To get started, read the [MkDocs user guide](https://mkdocs.org/user-guide/writing-your-docs) for an overview of how to layout and write Markdown source files.

### Menu

The menu structure is automatically generated using the [awesome-pages plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin). To set the desired page order, use a `.pages.yml` file in the directory. Example:

```yaml
title: Backend API
nav:
  - introduction.md
  - how-to
  - resources
  - websocket
```

### Meta Information

Each page should start with a meta-information section. Required fields are `title` and `description`. Example:

```yaml
---
title: Get involved
description: Contribute to improving Navixy documentation and translations.
---
```

### Headers

Structure your information with clear headers. Ensure consistency across pages of the same type.

### Example

API resource page structure:

```markdown
# Resource Name

Resource description.

## Object Name

Object and its description.

## API Actions

Path: `/path/to/resource/`.

### Method_1

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

### Method_2
...


```


If the response or structure has comments, please write these comments separately in a list format below.

For actual examples, refer to [user](../../user-api/backend-api/resources/commons/user/index.md) and [source](https://raw.githubusercontent.com/SquareGPS/navixy-api/refs/heads/master/docs/user-api/backend-api/resources/commons/user/index.md).