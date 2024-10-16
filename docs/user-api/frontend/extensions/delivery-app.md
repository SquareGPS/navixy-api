---
title: Application 'Courier on the map'
description: Delivery is a special plugin which can be embedded to any other application or website and allows track user's task by external ID and bounded tracker in the real time.
---

# App: Courier on the map

**Delivery** is a special plugin which can be embedded to any other application or website and
 allows track user's task by external ID and bounded tracker in the real time.


##Usage

    https://saas.navixy.com/pro/applications/delivery/?key=GENERATED_KEY

where key – is a session key generated with API call `/user/session/delivery/create`.

### Parameters

The plugin can be easily customized with the following parameters provided as GET params:

*   `performer\_type` – You can use an employee or vehicle label as the tracker marker label. 
    Values: `employee`, `vehicle`, `tracker`.
*   `performer\_label` – You can set the custom tracker marker label.
*   `external\_id` – The task external ID, specified in task creation/edit form.
*   `hide\_task`(1,0) – Hides task. In this mode you can track only the tracker(courier).
*   `display\_fields` – You can show only important information in the task info panel. 
    Names of fields are listed through a comma. Fields: label, description, address, period.
*   `prompt\_placeholder`– The task external ID prompt placeholder e.g "Order ID"
* `panel\_align` – Specifies the task info panel align. Values: `tl` – Top-Left corner,
  `tr` – Top-Right corner, `bl` – Bottom-Left corner, `br` – Bottom-Right corner.
* `panel\_scale` – Specifies the task info panel size. Values: `small`, `medium`, `big` –
  `medium` is the default value.
* `color` – Specifies the task marker and tracker marker color. Values: `FF0000` (red), `FF9900` (orange), `339966` (
  green), `3366FF` (blue). `FF9900` (orange) by default.

Available colors: `000000, 993300, 333300, 003300, 003366, 000080, 
333399, 333333, 800000, FF6600, 808000, 008000, 008080, 0000FF, 
666699, 808080, FF0000, FF9900, 99CC00, 339966, 33CCCC, 3366FF, 
800080, 969696, FF00FF, FFCC00, FFFF00, 00FF00, 00FFFF, 00CCFF, 
993366, C0C0C0, FF99CC, FFCC99, FFFF99, CCFFCC, CCFFFF, 99CCFF, 
CC99FF, FFFFFF`.


### Autoscaling

Autoscaling means that the scale of the map, and the center of the area are automatically selected so that all displayed
objects are visible.

`autoscale`:

*   `0` – do not scale
*   `1` – scale (by default)


### Map scale

The zoom parameter allows specifying map scale by default. Parameter will be 
ignored with switched on autoscaling.

`map`:

*   `roadmap` – Google
*   `satellite` – Google satellite
*   `osm` – Open Street map
*   `doublegis` – 2Gis
*   `osmmapnik` – OSM mapnik
*   `wikimapia` – Wikimapia
*   `mailru` – Mail.ru
*   `yandexpublic` – Yandex Public map
*   `cdcom` – Progorod


## API for keys

### Authorisation on API

To use the calls described further you have to be authorized in system as it 
is described according to the link: [API authorization][1]

[1]: ../../backend-api/getting-started/introduction.md#authorization-and-access-levels


### Creating a key

Use the following API call to create a new key

    http://api.domain.com/user/session/delivery/create/?hash=USER\_HASH

answer example if the key is successfully generated:

```json
{
  "success": true,
  "value": "206831ba32ec9d2a6f7b91b033a48912"
}
```

!!! warning "Important"
    Previous key (if you already have got one), will be replaced with the new one. 
    All the links like http://ui.domain.com/pro/applications/locator/?key= <old key> 
    will not work anymore.


### Retrieving a key

To acquire the key you have created earlier, please use the method

    http://api.domain.com/user/session/delivery/read/?hash=USER_HASH

The reply will look like as follows:

```json
{
  "success": true,
  "value": "206831ba32ec9d2a6f7b91b033a48912"
}
```
