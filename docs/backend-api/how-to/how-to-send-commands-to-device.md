---
title: How to send commands to devices via GPRS
description: How to send commands to devices via GPRS channel with user hash
---

# How to send commands to device via GPRS

Many devices can be reconfigured using GPRS commands. If we have commands in a protocol-dependent manner, 
and the device is online - we are able to change the device's configuration, or create an app for sending commands to 
devices from the UI by users. Also, that app can allow users to customize commands according to their needs.

Another way of usage is to bind commands sending to the rules, status changing, some parameters triggering. The count of
possible variations is great.

***

## Sending of a command

To send a command to a device we need only the next two parameters:

`tracker_id` - ID of the device to which we want to send the command.
`command` - Text or hexadecimal representation of the command in a protocol-dependent manner.

For example, we have a Teltonika FMB140 device with ID on the platform 231402. And I want to send a command to reconfigure
its IP address to a new one 52.57.1.136. According to the protocol the command should be the next:

`setparam 2004:52.57.1.136`

[API request](../resources/tracking/tracker/index.md#raw_commandsend):

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/raw_command/send' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 231402, "command": "setparam 2004:52.57.1.136"}'
    ```

The platform will notify you about success in reply.
