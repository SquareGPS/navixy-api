---
title: /plugin
description: /plugin
---

# /plugin

Plugins are special software modules which modify the behavior of various API calls.

#### Plugin object structure

```js
{
    "id": <plugin id, e.g. 1>, //int
    "type": <plugin type, e.g. "tracker_register">, //String
    "ui_module": <plugin ui module name, e.g. "Registration.appPlugins.BundledSim">, //String
    "module": <plugin module name, e.g. "com.navixy.plugin.tracker.register.bundled_sim">, //String
    "filter": { //a model filter which describes to which device models this plugin is applicable
        "exclusion": true, //if true, "models" lists models NOT supported by this plugin, if false, "models" contains all supported models
        "values": <list of the regexes for models which are (not) supported by this plugin, e.g. ["navixymobile", "mobile_unknown.*"]> //string[]
    },
    "parameters" : { ... } //Plugin-specific parameters as JSON object. This field is omitted if it's null (and it is null most of the time)
}
```

#### Example

```js
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

## list(…)

Get all plugins available to the user. List of available plugins may vary from user to user depending on platform settings and purchased features. Only these plugins can be used to register trackers, generate reports, etc.

#### return:

```js
{
    "success": true,
    "list": [ <plugin>, … ]
}
```

For "plugin" object structure, see [plugin/](#plugin).

#### errors:

* general types only

#### Standalone-specific:

If no plugins enabled for user and his dealer then available plugins enabled by default (config options **plugin.tracker.register.defaultIds** and **plugin.tracker.report.defaultIds**).