---
title: Getting Started
description: Getting started with Navixy API
---
# Navixy Developer Documentation

[Navixy](https://navixy.com) is a comprehensive GPS / Vehicle telematics platform developed by [SquareGPS](https://squaregps.com). This documentation provides detailed information on integrating third-party solutions with the Navixy platform, including API and technical documentation tailored for developers and partners.

## How to use this documentation

The documentation is organized into sections, each addressing a specific aspect of the Navixy platform:

* [**General**](../general/getting-started.md): Introduction, Navixy API Sandbox, No-code automation, and contribution guidelines.
* [**User Interface API**](../user-api/backend-api/getting-started/introduction.md): API calls for user interface functionalities like raw devices data, tracking, reports, tasks and much more.
* [**Admin Panel API**](../panel-api/getting-started.md): API calls for admin panel functionalities such as platform config and user management.

### Navigation

Navigate using the top menu. Access our GitHub via link on the right. The left-hand menu lists files for each section—click to view contents. Use the internal menu on the right for quick navigation within the file.

### Documentation structure

The documentation includes three types of files: Documents, Guides, and API calls. Documents and guides are divided into semantic parts, starting with an introduction that summarizes the content.

### API call descriptions

* **Introduction** - General information and purpose of the API call.
* **Object structure** - Describes the object structure used in the calls (optional).
* **API Actions** - Base API call and associated actions, including:
    * **Action description** - Purpose of the API action.
    * **Requirements** - Necessary permissions (optional).
    * **Parameters table** - Lists parameters for the API call with descriptions and data types.
    * **Examples** - API call examples with parameters. Includes a copy button for easy use.
    * **Response** - Example of a successful server response with field descriptions.
    * **Errors** - Specific errors related to the API action, plus a general error list.


## API Limits

To ensure system stability for all customers, the platform limits API requests to 50 requests per second per user and per IP address (for applications serving multiple users). These limits are applied based on user session hash and API keys.

## Navixy API Sandbox

Navixy provides a powerful Postman collection, the Navixy API Sandbox, for working with API documentation, exploring, and testing API queries using real or demo data. This collection offers a familiar environment for many developers and simplifies the process of building customized solutions. For detailed information on using Postman with Navixy, please refer to the [Postman Guide](./postman.md).

## Get involved

Help improve the [Navixy developer documentation](../general/contribute/dev-docs.md) or assist with [language translations](../general/contribute/translation.md). Your contributions make the Navixy platform even better for the community.