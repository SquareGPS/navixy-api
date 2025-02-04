---
title: Plugin
description: Contains plugin object description and API calls to interact with it. Plugins are special software modules which modify the behavior of various API calls.
---

# Plugin

Contains plugin object description and API calls to interact with it.<br>
Plugins are special software modules which modify the behavior of various API calls.


## Plugin object structure

```json
{
    "id": 1,
    "type":"tracker_register",
    "ui_module": "Registration.appPlugins.BundledSim",
    "module": "com.navixy.plugin.tracker.register.bundled_sim",
    "filter": {
        "exclusion": true,
        "values": ["navixymobile", "mobile_unknown.*"]
    },
    "parameters" : {<parameter1>}
```

* `id` - int. An ID of plugin.
* `type` - string. Plugin type.
* `ui_module` - string. Plugin UI module name.
* `module` - string. Plugin module name.
* `filter` - object. A model filter which describes to which device models this plugin is applicable.
    * `exclusion` - boolean. If `true`, "models" lists models NOT supported by this plugin, if `false`, "models" 
    contains all supported models.
    * `values` - string array. List of the regexes for models which are (not) supported by this plugin.
* `parameters` - plugin-specific parameters as JSON object. This field omitted if it's `null` (and it is `null` most of the time).

#### object example

```json
{
    "id": 4,
    "type": "tracker_report",
    "module": "com.navixy.plugin.tracker.report.trip",
    "ui_module": "Trip",
    "filter": {
        "exclusion": true,
        "values": []
    }
}
```


## API actions

API path: `/plugin`.

### `list`

Get all plugins available to the user. List of available plugins may vary from user to user depending on platform 
settings and purchased features. Only these plugins can be used to register trackers, generate reports, etc.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/plugin/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/plugin/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 4,
         "type": "tracker_report",
         "module": "com.navixy.plugin.tracker.report.trip",
         "ui_module": "Trip",
         "filter": {
             "exclusion": true,
             "values": []
         }
    }]
}
```

* `list` - array of objects. List of available plugins.

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.

#### Standalone-specific:

If no plugins enabled for user and his dealer then available plugins enabled by default 
(config options **plugin.tracker.register.defaultIds** and **plugin.tracker.report.defaultIds**).