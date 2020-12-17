# App: Web Locator

"Web Locator" is a special plugin which can be embedded to any other application or website 
and allow to track user's objects on the map in real-time.

## Example

The following HTML texts is used to show on the map the objects from
[demo account](https://b2field.com/signup/):
```html
<iframe src="https://saas.navixy.com/pro/applications/locator/?key=14084cd4a31f702341afb3fd6f81e475" 
        width="900" height="400">
</iframe>
```

## Usage

To start using the Weblocator user needs to acquire the GENERATED\_KEY value. 
He or she can copy this value from their private user area in the Web-interface 
or use [appropriate API call](../../backend-api/resources/commons/user/session/weblocator.md#create). 
Once user generates the key value, it won't expire and can be used till user generates the newer key.

Insert the following HTML text on any web-page you require using the GENERATED\_KEY value.
```html
<iframe src="https://saas.navixy.com/pro/applications/locator/?key=GENERATED_KEY" 
        width="900" height="400">
</iframe>
```

### Parameters

You can define window size, choose the background map layer, list the objects to show, 
use autoscaling to track multiple objects.

All parameters are transferred to the Web locator application by the GET method. For example:

    ?key=613e16fe56f14baa13c676eb9ddceb&width=600&height=400&map=1

Width and height of area are set in pixels.

### Objects list

You can limit the list of objects which will be displayed in the Web locator window. 
All user's account objects are displayed by default.

`names` - names of objects are listed through a comma

or

`objects` - numbers of objects are listed through a comma (tracker_id)

### Autoscaling

Autoscaling means that the scale of the map and the center of the area 
are automatically selected so that all displayed objects are visible.

`autoscale` - 0: do not scale, 1: scale (by default).

### Trace

Traces behind the assets will be shown on the map, as defined by the duration value 
(in seconds). Disabled by default.

`tail_size`: from 0 to 604800 (one week).

### Map scale

The `zoom` parameter allows to specify map scale by default. Parameter will be ignored 
with switched on autoscaling.

`zoom`: from 0 to 18

### Map choice

You can define a cartographical substrate

`map`:

*   `roadmap` – Google
*   `osm` – Open Street map
*   `doublegis` – 2Gis
*   `osmmapnik` – OSM mapnik
*   `wikimapia` – Wikimapia
*   `mailru` – Mail.ru
*   `yandexpublic` – Yandex Public map
*   `cdcom` – Progorod
*   `satellite` – satellite

## API for keys

### Authorization on API

To use the calls described further you have to be authorized in system as it is 
described according to the link: [API authorization][1]

  [1]: ./../../backend-api/getting-started.md#authorization-and-access-levels

### Keys Generation

Use the following API call to generate a new key 

    http://api.domain.com/user/session/weblocator/create/?hash=USER_HASH

Important notice: previous key (if you already have got one), will be replaced with the new one. 
All the links like `http://ui.domain.com/pro/applications/locator/?key=<old key>` will not work anymore.

Answer example if the key is successfully generated:
```json
{
  "success": true,
  "value": "206831ba32ec9d2a6f7b91b033a48912"
}
```

### Acquiring key

To acquire the key generated earlier use the call 

    http://api.domain.com/user/session/weblocator/read/?hash=USER_HASH

The reply will look like as follows:
```json
{
  "success": true,
  "value": "206831ba32ec9d2a6f7b91b033a48912"
}
```
