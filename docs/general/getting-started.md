---
title: Getting Started
description: Getting started with Navixy API
---

# Getting started

## How to read this documentation

The documentation is organized into several sections, each covering a specific aspect of the Navixy platform:

* `General` - provides an introduction to the documentation and Navixy API Sandbox, including how to use documentation and how to contribute to its improvement. It also includes information on translating the platform into different languages.
* `Backend API` - describes all API calls for working with information presented to users or sub-users in the user interface, such as tracking, reports, tasks, and more.
* `Panel API` - describes all API calls for working with information presented to administrators in the admin panel, including information about devices, tariff plans, users, and more.
* `Eco Fleet API`  - describes API calls for providing information for efficient fuel management.
* `Data Warehouse API` - describes API calls for obtaining raw telematics data.
* `Frontend` - provides information on customizing the welcome page, adding your own apps into Navixy UI, and how to work with Delivery plugin.

You can navigate between sections using the menu at the top of the page. On the right side of the menu, you can find a button for downloading a PDF version of the documentation and a link to our `github` page.

The files within each section are listed in the menu on the left. Clicking on a file will display its contents. An internal menu on the right side of the page allows for quick navigation between different parts of the file.

The documentation includes three types of files: documents, guides, and API calls. Documents and guides are divided into semantic parts, with the first part serving as an introduction that briefly describes the content of the document.

API calls follow this structure:

* `Introduction` - provides a description and general information about the purpose of the API call.
* `The structure of the object` - describes the structure of the object used in the calls (optional).
* `API-actions` - includes the base API call and associated actions. Each API action includes the following:
    * `Description of the API-actions` - explains the purpose of the API action.
    * `Requirements` - lists any necessary permissions to use the API action (optional).
    * `Parameters table` - provides a table of parameters for the selected API call, including their description and data type.
    * `Examples` - demonstrates a correct API call with necessary parameters included. Examples can be useful for troubleshooting and can be easily copied and modified with your own data. Each example includes a copy button in the upper right corner. If the parameters contain special characters, only POST examples are provided.
    * `Response` - shows an example of a successful server response, including a description of each field.
    * `Errors` - lists any specific errors associated with the API action. A general error list applies to all calls.

***

## Navixy API Sandbox

The [Navixy API Sandbox](https://www.postman.com/navixyapisandbox/workspace/navixy-api-sandbox/overview) – a new tool designed to assist with working with API documentation and exploring and testing API queries using real or demo data. Built in Postman, it is a familiar tool for many developers. For those new to the Postman, our ["How to"](https://www.postman.com/navixyapisandbox/workspace/navixy-api-sandbox/folder/8534541-b576926c-002f-42aa-8a4c-b67ee63096f9?action=share&source=copy-link&creator=8534541&ctx=documentation) guides in the API Sandbox provide clear instructions on getting started. We will continue to expand the sandbox with detailed descriptions of all API calls, as well as new methods and instructions for working with the platform's data, making it even easier to build customized solutions for your customers.

Additionally, you can find information on how to use Postman to test all API calls listed in this documentation version [here](./postman.md).

***

## Limits

To ensure system stability for all users, the platform has an implemented limit of 50 requests per second per user and per IP address (in the case of an application serving multiple users). These limits are applied separately based on user session hash and API keys.

***

## Get involved

You can play a valuable role in improving the [Navixy Platform documentation](./get-involved.md) or [localizations](./localizations/contributing.md).

If you notice that the user interface translation into your language is missing or contains errors, you can contribute to or correct the localization on the [CrowdIn platform](https://crowdin.com/). Refer to [this guide](./localizations/contributing.md) on how to do it.

Additionally, the current documentation may contain errors or omissions. As it is publicly available on [GitHub]({{ config.repo_url }}), you can independently contribute to its correction or expansion. Refer to [this guide](./get-involved.md) on how to do it.
