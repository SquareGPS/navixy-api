# Sending Commands to a GPS Tracker via IP protocol (OTA)

Most modern GPS tracking devices can be reconfigured remotely using IP commands sent over-the-air (OTA). With the Navixy API, you can easily change device configurations or develop applications that allow users to send commands directly from the UI. These commands can also be integrated into automation rules, status changes, or parameter triggers, offering extensive flexibility and customization for managing your telematics solutions.

## Sending a Command

To send a command to a device, you only need the following parameters:

- `tracker_id`: The ID of the device to which you want to send the command.
- `command`: The text or hexadecimal representation of the command in a protocol-dependent manner.

#### Example: Reconfiguring a Teltonika FMB140 Device

Suppose you have a Teltonika FMB140 device with an ID of `231402` on the platform, and you want to reconfigure its IP address to `52.57.1.136`. According to the protocol, the command should be:

`setparam 2004:52.57.1.136`

### API Request

To send this command, use the API request [`raw_command/send`](../../resources/tracking/tracker/index.md#raw_commandsend):

=== "cURL"

```shell
curl -X POST 'https://tracker.navixy.com/v2/tracker/raw_command/send' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "tracker_id": 231402,
        "command": "setparam 2004:52.57.1.136"
    }'
```

Upon successful execution, the platform will confirm that the command has been sent.

This method provides a reliable and efficient way to manage and control your GPS tracking devices via IP, ensuring seamless and real-time updates to device configurations.