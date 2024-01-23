---
title: How to work with geofences
description: How to create geofences of each type with examples
---

# How to work with geofences

Geofence is a virtual perimeter for a real geographic area. The system can control whether object crossed geofence border
(either "in" or "out"). All these events are logged, so user can obtain geofence reports and receive alerts.

Moreover, you can assign various rules for events to particular geofences. For example, if you need to get speeding alerts
only within a certain area (e.g. in city) or route.

***

## Geofence creation

To create a geofence we should use the [zone/create](../resources/tracking/zone/index.md) API call. We have several types
of them. So the call and process can be different between them.

### Circle geofence

It is the easiest geofence to create. There we should use only one point as a center and radius. The platform will automatically
calculate borders for it.

For example, we want to create a geofence with a radius 50 meters that will cover a business park to track employees.
We need this geofence to create a rule that will provide an alert when they will come to work and another one - when 
they go from it.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Circle geofence", "type": "circle", "center": {"lat": 61.49504550221769, "lng": 23.775476217269897}, "radius": 50, "tags": [179227], "color": "03A9F4", "address":"Address"}}'
    ```

The platform will respond with status and created geofence ID. We can use this ID to [create a rule](./use-rules.md).

***

### Polygon geofence

The second type we will create - the polygon geofence. It is more difficult than the circle geofence because we should 
specify special points for it where the geofence border will change direction. Maximum count of points is 100. This 
limitation is necessary because a geofence is not just a visual display of some area. The platform calculates the data 
for reports and alerts on the fly. When the number of points in a geofence is more than 100, computational costs begin 
to grow exponentially.

For example, we want to track maximum speed of our vehicles in Rome. To do that, we will need to create a geofence that 
covers the city.

!!! note "Geofence accuracy can be fairly low as long as it's border crosses all the main roads."

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Speed limit in Rome", "type": "polygon", "color": "27A9E3", "address": "Address"}, "points": [{"lat": 41.80970819375622, "lng": 12.576599121093752, "node": true}, {"lat": 41.79128073728445, "lng": 12.522354125976564, "node": true}, {"lat": 41.80970819375622, "lng": 12.38983154296875, "node": true}, {"lat": 41.86649282301996, "lng": 12.369232177734375, "node": true}, {"lat": 41.90943147946872, "lng": 12.38090515136719, "node": true}, {"lat": 41.956426414614235, "lng": 12.379531860351562, "node": true}, {"lat": 41.98501507352485, "lng": 12.435150146484375, "node": true}, {"lat": 41.98807738309159, "lng": 12.50724792480469, "node": true}, {"lat": 41.97531678812783, "lng": 12.54913330078125, "node": true}, {"lat": 41.95795827518022, "lng": 12.580718994140627, "node": true}, {"lat": 41.92322706102551, "lng": 12.61161804199219, "node": true}, {"lat": 41.902277040963696, "lng": 12.619171142578127, "node": true}, {"lat": 41.86904950322354, "lng": 12.607498168945312, "node": true}]}'
    ```

Don't forget that the rule isn't created yet. The platform will respond with geofence ID. Use [the next instruction](./use-rules.md) to create rules.

***

### Sausage geofence

We use sausage geofences for roads. They should be more accurate, and their calculated area is not so hard as for polygons.
That's why the maximum number of points is 1024. 

For example, we need to create special geofences for street cleaning cars, and we want to see - is this car cleaned the 
street, or it turned from it in the middle.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Clean street 1", "type": "sausage", "radius": 20, "color": "27A9E3", "address": "Address"}, "points": [{"lat":21.5337018035,"lng":-104.8700889945,"node":true},{"lat":21.5336107362,"lng":-104.8691622913,"node":true},{"lat":21.5336444186,"lng":-104.8674470186,"node":true},{"lat":21.5336494086,"lng":-104.8656499386,"node":true},{"lat":21.5341084873,"lng":-104.8656606674,"node":true},{"lat":21.5341434171,"lng":-104.8661112785,"node":true},{"lat":21.534742213,"lng":-104.8656713963,"node":true},{"lat":21.5350266402,"lng":-104.8659932613,"node":true},{"lat":21.5336593886,"lng":-104.8669320345,"node":true},{"lat":21.5336469136,"lng":-104.8691529036,"node":true},{"lat":21.5337367335,"lng":-104.8700594902,"node":true},{"lat":21.5338427707,"lng":-104.8705852032,"node":true},{"lat":21.5341184672,"lng":-104.8718833923,"node":true},{"lat":21.5344577853,"lng":-104.873329103,"node":true},{"lat":21.5346199591,"lng":-104.8735275865,"node":true},{"lat":21.532277154,"lng":-104.8760032654,"node":true},{"lat":21.5312941127,"lng":-104.8770868778,"node":true},{"lat":21.5301214405,"lng":-104.8784118891,"node":true},{"lat":21.5291383846,"lng":-104.8793131113,"node":true},{"lat":21.5287790935,"lng":-104.8795759678,"node":true},{"lat":21.5284647131,"lng":-104.8797154427,"node":true},{"lat":21.5280804693,"lng":-104.8797905445,"node":true},{"lat":21.5276413324,"lng":-104.879822731,"node":true},{"lat":21.5273668712,"lng":-104.8799729347,"node":true}]}'
    ```

The platform will provide the status, and geofence ID.

The sausage geofence also, could be used to create a special route for cars with valuable cargo, such as cash collectors.
Or for patrol cars. In this case, use the rule "deviation from the route".

***

### Getting geofence name by a tracker's location

It may be necessary to get the geofence name or ID where a device is located. In this case, 
use [zone/search_location](../resources/tracking/zone/index.md#search_location). For example, we want to get a geofence, 
where our device is located, or we want to count how many devices are in some zone.

To get this information we should request a device's [state and location](../resources/tracking/tracker/index.md#get_state) 
first. With received lat and lng parameters we can check geofences. 
