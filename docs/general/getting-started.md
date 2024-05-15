---
title: Getting Started
description: Getting started with Navixy API
---

# Getting started

## How to read this documentation

The documentation presented in several sections that are responsible for its own part of the Navixy platform:

* `General` - introductory section. Explains how to work with the documentation and how you can help us improve it. It 
also has information regarding translation of the platform into different languages.
* `Backend API` - describes all calls for working with information presented to users or sub-users in the UI. Tracking, 
reports, tasks, and more.
* `Panel API` - describes all calls for working with information presented to administrators in the admin panel. 
Information about devices, tariff plans, users, and more.
* `Eco Fleet API` - describes calls that provide information for efficient fuel management.
* `Data Warehouse API` - describes calls for obtaining raw telematics data.
* `Frontend` - provides information on customizing the welcome page and additional Weblocator and Delivery plugins.

You can switch between sections using menu on the top of the page. On the right side of the menu, you can find a button 
for downloading a PDF version of documentation and a link to our `github` page. 

All files of the section are presented in menu on the left. Once you click on one of them - it will display file contents. 
On the right side of page you can find file's internal menu. Use it for quick navigation between parts of the file.

The documentation has three types of files: documents, guides and API calls.

Documents and guides are divided into semantic parts, the first of which is an introduction that briefly describes 
what the document is about.

API calls have the following structure:

* `Introduction` - API call description and general information about its purpose.
* `The structure of the object` - describes an object that is used in the calls. (optional)
* `API-actions` - the API base call and actions. All API-actions also divided into several points:
    * `Description of the API-actions` - describes purpose of the call.
    * `Requirements` - what rights are required to use the API-action. (optional)
    * `Parameters table` - contains list of parameters for selected API call, their description and data type.
    * `Examples` - example of a correct API call with all parameters listed. Examples can be useful for troubleshooting. 
    You can also copy them and simply substitute the data with your own. Each example has a copy button in the upper right 
    corner. If the parameters don't contain special characters, they are presented in two variants: POST and GET. If the 
    parameters include special characters, only POST examples given.
    * `Response` - an example of successful response from the server with description of every field.
    * `Errors` - specific errors for this API-action. General error list applies to all calls.

***

## Limits

To maintain the stability of the system for all users, the platform has a limit of 50 requests/second per user and per IP 
address (if your app works with multiple users).

***

## Get involved

You can really help to improve [this documentation](./get-involved.md) or
 [localizations](./localizations/index.md) of Navixy Platform.

If the translation of the user interface into your language is missing or contains errors, you can make or fix the
localization on the [CrowdIn platform](https://crowdin.com/) yourself. Read [here](./localizations/contributing.md) how
to do it.

Current documentation may also contain errors or white spots. All of it is available in the public domain on [GitHub]({{
config.repo_url }}), and you can independently contribute in its correction or addition. Read [here](./get-involved.md)
how to do it.

***

## Useful things

It is convenient to [use postman](./postman.md) for testing work with API.
