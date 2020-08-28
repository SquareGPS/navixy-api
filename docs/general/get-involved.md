---
title: Get involved
description: Get involved into improving documentation and translations of the Navixy Platform
---

# Get involved

If you notice an inaccuracy, mistake, typo or want to supplement the information in 
this documentation, then you can help us to improve it. All of this documentation is available in the 
public domain on [GitHub]({{ config.repo_url }}).

There are several ways:

1.  [Creating an issue]({{ config.repo_url }}issues/new) with a detailed description of the problem.
1.  [Editing a single page in a browser](#easy-way).
1.  [Manually creating a fork](#second-way) and doing multiply commits before creating a pull request.
1.  [Installing and editing](#hard-way) documentation locally on yours PC.

In each of these cases, a GitHub account required.
If you don't want to register on GitHub, you can just [contact us](contacts.md) with any convenient way.

### Easy way

On each page in the upper right corner of the text top there is a link with a picture of a pencil :material-pencil:.
After clicking on this link, you will be asked to create a fork of the repository (if you have
not done this before). 

![Create your fork](./assets/fork-proposal.png)

Creating a fork done with one green button. After that, the edit form with page source code will open.

!!! note "For correct edit of page, please read the [introduction into Mkdocs](#introduction-into-mkdocs)."

After editing the page, you must fill out a description of what you have done.

![Please fill the commit message](./assets/commit-message.png)

Submitting a change will write it to a new branch in your fork, so you can send a pull request. 
We will review your pull request and accept it in the main branch.

Thus, this method is only suitable for simple edits on one page.
There is [another way](#second-way) to create pull requests to fix multiple pages at once.

### Second way

This method allows you to make several edits on different pages before proposing them in a pull request.

1.  Create a fork [of the repository]({{ config.repo_url }}) if it has not been created yet.
    (Just click the "Fork" button in the upper right corner.)
1.  Go to the created fork and find the file you are interested in.
1.  Open the file and click the edit button.
1.  Make edits and commit with a clear description of the changes.
1.  Edit other files of interest to you in the same way.
1.  Go to the start page of the fork and click on the "Pull request" button.

After review and pull request will be merged, and you can drop a fork.

### Hard way

This method involves installing the Git, IDE, Python and 
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material) on yours PC.

1. Install [Python 3](https://www.python.org/downloads/).
1. Install [Git client](https://git-scm.com/downloads).
1. Install an IDE, for example [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community edition would be enough).
1. Create a fork [of the repository]({{ config.repo_url }}) and cloning it to local project. 
   In IDEA: `File` -> `New` -> `Project from version control`;
1. Install [mkdocs-material](https://squidfunk.github.io/mkdocs-material) and other dependencies. In console:
   ```sh
   cd /path/to/project
   mkdir venv
   python -m venv ./venv
   pip3 install -r requirements.txt
   ```
1. Start the documentation server locally. In console:
   ```sh
   cd /path/to/project
   mkdocs serve
   ```
1. To check that the server has started, open in a browser: http://localhost:8000
1. Create a local git branch in project.
1. Make changes in documentation and test it in browser. 
   Read the [introduction](#introduction-into-mkdocs).
1. Commit and push changes. Please, use English in commit message.
1. Create a Pull Request (PR) on Github from your fork. Please, use English in PR description.
1. After the PR has been reviewed and merged to upstream you can remove
   branch and rebase a fork to the upstream.

## Introduction into Mkdocs

This documentation built on [mkdocs engine](https://mkdocs.org) and [mkdocs-material theme](https://squidfunk.github.io/mkdocs-material).
Firstly, read [how to layout and write your Markdown source files](https://mkdocs.org/user-guide/writing-your-docs)
for an overview of how to write docs.

### Menu

The menu formed using the plugin [awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) automatically.
To set the desired page order in the menu, use the file `.pages.yml` in directory.
For example:

```yaml
title: Backend API
arrange:
    - getting-started.md
    - how-to
    - resources
    - websocket
```

`Title` sets name for menu section. `Arrange` sets the sub-items order.

### Meta information

Each page must have meta information section at the beginning. Required fields: `title` and `description`. 
For example:

```yaml
---
title: Get involved
description: Get involved into improving documentation and translations of the Navixy Platform
---
```

Title will be displayed in menu and in browser title.

### Headers

The information on each page should be structured. On pages of the same type, 
the structure should be uniform.

### Example

API resource page structure:

````markdown
# Resource name

Path: `/path/to/resource\`.

Resource description.

Resource specific actions:

* [/path/to/resource/method1](#method1)
* [/path/to/resource/method2](#method2)

## method1

Method description.

### Parameters

| name  | description | type  | restrictions |
| :---- | :----       | :---- | :----        |
|param1 | description | int   | [1..100], not null |

### Examples

=== "HTTP POST application/json

```abap
$ curl -X POST '{{ extra.api_example_url }}/resource/sub_resource/action' \
    -H 'Content-Type: application/json' \ 
    -d '{"param1": "value1", "param2": "value2", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

=== "HTTP POST application/x-www-form-urlencoded"

```abap
$ curl -X POST '{{ extra.api_example_url }}/resource/sub_resource/action' \
    -d 'param1=value1' \
    -d 'param2=value2' \
    -d 'hash=a6aa75587e5c59c32d347da438505fc3' 
```

=== "GET"

```abap
{{ extra.api_example_url }}/resource/sub_resource/action?param1=value1&hash=a6aa75587e5c59c32d347da438505fc3
```

### Response

```json
{ "success": true }
```

!!! warning "Please note"
    If the response or structure has comments it is necessary to write these comments separately in the form of a list below.

### Errors

Special error codes.

## method2

...

````

For real example see [/user](../backend-api/resources/commons/user/index.md) and
[:octicons-file-code-24: source](https://raw.githubusercontent.com/SquareGPS/navixy-api/master/docs/backend-api/resources/commons/user/index.md).
