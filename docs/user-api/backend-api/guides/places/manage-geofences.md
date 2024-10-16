# Managing Geofences

Geofences are virtual perimeters for real geographic areas. The Navixy platform can monitor whether an object equipped with a GPS tracker crosses a geofence border (either entering or exiting). All such events are logged, enabling users to obtain geofence reports and receive alerts. Furthermore, various rules can be assigned to events related to specific geofences. For instance, you might want to receive speeding alerts only within a certain area, such as a city or along a specific route.

## Geofence Creation

To create a geofence, use the [zone/create](../../resources/tracking/zone/index.md#create) API call. There are several types of geofences, and the creation process varies between them.

### Circle Geofence

The simplest geofence to create is the circle geofence, which requires only a center point and a radius. The platform will automatically calculate the borders.

For example, to create a geofence with a 50-meter radius around a business park to track employees, you can use the following API request. This geofence can trigger alerts when employees arrive at or leave work.

**API Request:**

=== "cURL"

    ```shell
    curl -X POST 'https://tracker.navixy.com/v2/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Circle Geofence", "type": "circle", "center": {"lat": 61.49504550221769, "lng": 23.775476217269897}, "radius": 50, "tags": [179227], "color": "03A9F4", "address":"Address"}}'
    ```

The platform will respond with the status and the created geofence ID. This ID can be used to [create a rule](../rules-notifications/use-rules.md).

### Polygon Geofence

A polygon geofence is more complex as it requires specifying multiple points where the geofence border changes direction. The maximum number of points is 100 to maintain computational efficiency. For example, to track the maximum speed of vehicles within Rome, you can create a geofence that covers the city.

**API Request:**

=== "cURL"

    ```shell
    curl -X POST 'https://tracker.navixy.com/v2/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Speed Limit in Rome", "type": "polygon", "color": "27A9E3", "address": "Address"}, "points": [{"lat": 41.80970819375622, "lng": 12.576599121093752, "node": true}, {"lat": 41.79128073728445, "lng": 12.522354125976564, "node": true}, {"lat": 41.80970819375622, "lng": 12.38983154296875, "node": true}, {"lat": 41.86649282301996, "lng": 12.369232177734375, "node": true}, {"lat": 41.90943147946872, "lng": 12.38090515136719, "node": true}, {"lat": 41.956426414614235, "lng": 12.379531860351562, "node": true}, {"lat": 41.98501507352485, "lng": 12.435150146484375, "node": true}, {"lat": 41.98807738309159, "lng": 12.50724792480469, "node": true}, {"lat": 41.97531678812783, "lng": 12.54913330078125, "node": true}, {"lat": 41.95795827518022, "lng": 12.580718994140627, "node": true}, {"lat": 41.92322706102551, "lng": 12.61161804199219, "node": true}, {"lat": 41.902277040963696, "lng": 12.619171142578127, "node": true}, {"lat": 41.86904950322354, "lng": 12.607498168945312, "node": true}]}'
    ```

The platform will respond with the geofence ID. Follow the [next instruction](../rules-notifications/use-rules.md) to create rules.

### Corridor Geofence

Corridor geofences are used for roads. They need to be accurate, and their calculated area is not as computationally intensive as polygons. Therefore, the maximum number of points is 1024.

For example, to create geofences for street cleaning vehicles to ensure they follow the correct route, you can use the following API request with the `sausage` parameter in it:

**API Request:**

=== "cURL"

    ```shell
    curl -X POST 'https://tracker.navixy.com/v2/zone/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone": {"label": "Clean Street 1", "type": "sausage", "radius": 20, "color": "27A9E3", "address": "Address"}, "points": [{"lat":21.5337018035,"lng":-104.8700889945,"node":true},{"lat":21.5336107362,"lng":-104.8691622913,"node":true},{"lat":21.5336444186,"lng":-104.8674470186,"node":true},{"lat":21.5336494086,"lng":-104.8656499386,"node":true},{"lat":21.5341084873,"lng":-104.8656606674,"node":true},{"lat":21.5341434171,"lng":-104.8661112785,"node":true},{"lat":21.534742213,"lng":-104.8656713963,"node":true},{"lat":21.5350266402,"lng":-104.8659932613,"node":true},{"lat":21.5336593886,"lng":-104.8669320345,"node":true},{"lat":21.5336469136,"lng":-104.8691529036,"node":true},{"lat":21.5337367335,"lng":-104.8700594902,"node":true},{"lat":21.5338427707,"lng":-104.8705852032,"node":true},{"lat":21.5341184672,"lng":-104.8718833923,"node":true},{"lat":21.5344577853,"lng":-104.873329103,"node":true},{"lat":21.5346199591,"lng":-104.8735275865,"node":true},{"lat":21.532277154,"lng":-104.8760032654,"node":true},{"lat":21.5312941127,"lng":-104.8770868778,"node":true},{"lat":21.5301214405,"lng":-104.8784118891,"node":true},{"lat":21.5291383846,"lng":-104.8793131113,"node":true},{"lat":21.5287790935,"lng":-104.8795759678,"node":true},{"lat":21.5284647131,"lng":-104.8797154427,"node":true},{"lat":21.5280804693,"lng":-104.8797905445,"node":true},{"lat":21.5276413324,"lng":-104.879822731,"node":true},{"lat":21.5273668712,"lng":-104.8799729347,"node":true}]}'
    ```

The platform will provide the status and geofence ID.

Corridor geofences can also be used to create special routes for vehicles carrying valuable cargo, such as cash collectors, or for patrol cars. In such cases, use the rule "deviation from the route."

### Getting Geofence Name by a Tracker's Location

To get the geofence name or ID where a device is located, use the [zone/search_location](../../resources/tracking/zone/index.md#search_location) API call. For example, to determine which geofence a device is in or to count how many devices are in a specific zone, first request the device's [state and location](../../resources/tracking/tracker/index.md#get_state). With the received latitude and longitude parameters, you can then check the geofences.