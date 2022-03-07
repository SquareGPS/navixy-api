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
We need this geofence to create a rule that will provide ann alert when they will come to work and another one - when 
they go from it.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Circle geofence", "type": "circle", "center": {"lat": 61.49504550221769, "lng": 23.775476217269897}, "radius": 50, "tags": [179227], "color": "03A9F4", "address":"Address"}}'
    ```

The platform will respond with status and created geofence id. We can use this id to [create a rule](./use-rules.md).

***

### Polygon geofence

The second type we will create - the polygon geofence. It is more difficult than the circle geofence because we should 
specify special points for it where the geofence border will change direction. Maximum count of points is 100. This 
limitation is necessary because a geofence is not just a visual display of some area. The platform calculates the data 
for reports and alerts on the fly. When the number of points in a geofence is more than 100, computational costs begin 
to grow exponentially.

For example, we want to track maximum speed of our vehicles in Rome. To do that, we will need to create a geofence that 
covers the city.

!!! note "Geofence's accuracy can be fairly low as long as it's border crosses all of the main roads."

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Speed limit in Rome", "type": "polygon", "color": "27A9E3", "address": "Address"}, points: [{"lat": 41.80970819375622, "lng": 12.576599121093752, "node": true}, {"lat": 41.79128073728445, "lng": 12.522354125976564, "node": true}, {"lat": 41.80970819375622, "lng": 12.38983154296875, "node": true}, {"lat": 41.86649282301996, "lng": 12.369232177734375, "node": true}, {"lat": 41.90943147946872, "lng": 12.38090515136719, "node": true}, {"lat": 41.956426414614235, "lng": 12.379531860351562, "node": true}, {"lat": 41.98501507352485, "lng": 12.435150146484375, "node": true}, {"lat": 41.98807738309159, "lng": 12.50724792480469, "node": true}, {"lat": 41.97531678812783, "lng": 12.54913330078125, "node": true}, {"lat": 41.95795827518022, "lng": 12.580718994140627, "node": true}, {"lat": 41.92322706102551, "lng": 12.61161804199219, "node": true}, {"lat": 41.902277040963696, "lng": 12.619171142578127, "node": true}, {"lat": 41.86904950322354, "lng": 12.607498168945312, "node": true}]}'
    ```

Don't forget that the rule isn't created yet. The platform will respond with geofence id. Use [the next instruction](./use-rules.md) to create rules.

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
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Clean street 1", "type": "sausage", "radius": 20, "color": "27A9E3", "address": "Address"}, points: [{"lat": 56.82530569999999, "lng": 60.5857809, "node": true}, {"lat": 56.82531, "lng": 60.58578, "node": false}, {"lat": 56.82531, "lng": 60.58588, "node": false}, {"lat": 56.82536, "lng": 60.58629, "node": false}, {"lat": 56.82541, "lng": 60.58669, "node": false}, {"lat": 56.82549, "lng": 60.58749, "node": false}, {"lat": 56.82553, "lng": 60.58789, "node": false}, {"lat": 56.82555, "lng": 60.58807, "node": false}, {"lat": 56.82557, "lng": 60.58821, "node": false}, {"lat": 56.82563, "lng": 60.58886, "node": false}, {"lat": 56.82585, "lng": 60.59086, "node": false}, {"lat":56.82598, "lng": 60.59208, "node": false}, {"lat": 56.82609, "lng": 60.59306, "node": false}, {"lat": 56.82613, "lng": 60.59353, "node": false}, {"lat": 56.82618, "lng": 60.59394, "node": false}, {"lat": 56.8263, "lng": 60.59513, "node": false}, {"lat": 56.82631, "lng": 60.59528, "node": false}, {"lat": 56.82632, "lng": 60.59537, "node": false}, {"lat": 56.82641, "lng": 60.59626, "node": false}, {"lat": 56.82642, "lng": 60.59634, "node": false}, {"lat": 56.82663, "lng": 60.59819, "node": false}, {"lat": 56.82686, "lng": 60.60027, "node": false}, {"lat": 56.82691, "lng": 60.60071, "node": false}, {"lat": 56.82697, "lng": 60.60118, "node": false}, {"lat": 56.82711, "lng": 60.60244, "node": false}, {"lat": 56.8271131, "lng": 60.6024369, "node": true}]}'
    ```

The platform will provide the status, and geofence id.

The sausage geofence also, could be used to create a special route for cars with valuable cargo, such as cash collectors.
Or for patrol cars. In this case, use the rule "deviation from the route".

***

### Getting geofence name by a tracker's location

It may be necessary to get the geofence name or ID where a device is located. In this case, 
use [zone/search_location](../resources/tracking/zone/index.md#search_location). For example, we want to get a geofence, 
where our device is located, or we want to count how many devices are in some zone.

To get this information we should request a device's [state and location](../resources/tracking/tracker/index.md#get_state) 
first. With received lat and lng parameters we can check geofences. 