---
title: Getting Started
description: Overview of Navixy Eco Fleet API
---

# Navixy Eco Fleet API

The structure of Eco Fleet API is close to the user API, so
we highly recommend reading [Backend API: getting started](../backend-api/getting-started/introduction.md).

The main differences are _request paths_, _authorization system_ and _request format_.


## Base URL

Eco Fleet API resides in `eco_fleet` subsection of API URL. So you can determine URL to API calls like this:

*  `https://api.eu.navixy.com/eco_fleet` for European Navixy ServerMate platform.
*  `https://api.us.navixy.com/eco_fleet` for American Navixy ServerMate platform.

For example, to make a sensor quality API call in European Navixy ServerMate, you should use the URL: 
```
{{ extra.eco_fleet_api_example_url }}/trackers/123/sensors/321/quality
```

## Auth


### Authentication

Authentication is handled by [Backend API](../backend-api/getting-started/authentication.md).


### Authorization

You should pass the session hash you obtained earlier as the `Authorization` HTTP header with `NVX` auth scheme.

Example:
```shell
$ curl -X GET '{{ extra.eco_fleet_api_example_url }}/trackers/123/sensors/321/quality' \
    -H 'Authorization: NVX 5dd33ef0ab37b6aaf2064ecdf50c4cdc'
```


## Response format

The responses are usually in `application/json` content type.
Consult the API call documentation in question for details.


### Errors

Errors are distinguished by HTTP status code (>= 400) and follow [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807).

Example:
```json
{
  "type": "errors/default/bad-request",
  "title": "Bad Request",
  "status": 400,
  "detail": "id: must be greater than or equal to 1"
}
```


#### Common error types

* `errors/default/bad-request` - Causes: missing or invalid parameter value.
* `errors/default/unauthorized` - Causes: missing `Authorization` header or credentials are insufficient or expired.


### Date/time formats

According to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

Example: `1999-12-31T23:59:59Z`.
