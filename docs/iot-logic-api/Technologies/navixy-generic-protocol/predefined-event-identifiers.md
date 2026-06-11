---
description: >-
  Standard event_id values for NGP messages, covering power, security, safety,
  vehicle efficiency, track, I/O, and peripheral events.
---

# Predefined event identifiers

NGP includes pre-defined event identifiers (`event_id`) for the most common device events. Use these standard IDs wherever possible. For device-specific events not covered here, use custom IDs starting from **10,000**.

### Power

Range: 1–100.

| **Event ID** | **Description**                             |
| ------------ | ------------------------------------------- |
| 1            | Low battery                                 |
| 2            | Power lost or external power cut            |
| 3            | Power On button pressed                     |
| 4            | Power recovered or external power connected |
| 5            | OBD unplugged from the car's connector      |
| 6            | OBD plugged in                              |
| 7            | Device backup battery low                   |
| 8            | Device wakes up from sleep mode             |
| 9            | Sleep mode start                            |
| 10           | Timer wakeup                                |
| 11           | Motion wakeup                               |
| 12           | External power wakeup                       |
| 13           | Power Off button pressed                    |
| 14           | Device power off                            |
| 15           | Device power on                             |

### Security

Range: 101–200.

| **Event ID** | **Description**                                                      |
| ------------ | -------------------------------------------------------------------- |
| 101          | Unauthorized movement event determined by the device (tow detection) |
| 102          | Unauthorized movement end                                            |
| 103          | Device detached from the tracked object                              |
| 104          | Car alarm                                                            |
| 105          | Device case closed                                                   |
| 106          | Device case opened                                                   |
| 107          | Unplug from the tracked object                                       |
| 108          | Device attached to the tracked object                                |
| 109          | Door alarm                                                           |
| 110          | Device lock closed                                                   |
| 111          | Device lock opened                                                   |
| 112          | Vibration end                                                        |
| 113          | Vibration start                                                      |
| 114          | Strap bolt inserted                                                  |
| 115          | Strap bolt cut                                                       |
| 116          | GPS jamming detected                                                 |
| 117          | GSM signal jamming alarm                                             |
| 118          | Bracelet opened                                                      |
| 119          | Bracelet closed                                                      |
| 120          | G-sensor alert                                                       |
| 121          | GPS jamming end                                                      |

### Safety

Range: 201–300.

| **Event ID** | **Description**                                          |
| ------------ | -------------------------------------------------------- |
| 201          | Emergency contact number called                          |
| 202          | SOS button pressed                                       |
| 203          | Cruise control switched on                               |
| 204          | Cruise control switched off                              |
| 205          | DMS: driver not identified                               |
| 206          | DMS: driver identified                                   |
| 207          | ADAS: frequent lane change                               |
| 208          | DMS: device cannot detect human face                     |
| 209          | Seat belt unbuckled                                      |
| 210          | DMS: driver is drinking                                  |
| 211          | DMS: driver eyes closed                                  |
| 212          | DMS: new driver detection reported                       |
| 213          | DMS: driver enters cabin                                 |
| 214          | DMS: driver absence start                                |
| 215          | DMS: driver stopped smoking (driver distraction)         |
| 216          | DMS: driver started smoking (driver distraction)         |
| 217          | DMS: driver finished using phone (driver distraction)    |
| 218          | DMS: driver started using phone (driver distraction)     |
| 219          | DMS: yawning detected (fatigue driving)                  |
| 220          | DMS: driver stopped distraction                          |
| 221          | DMS: driver started distraction                          |
| 222          | DMS: driver stopped drowsiness (fatigue driving)         |
| 223          | DMS: driver started drowsiness (fatigue driving)         |
| 224          | Overspeeding                                             |
| 225          | Unexpected movement start                                |
| 226          | Unexpected movement end                                  |
| 227          | ADAS: pedestrian in danger zone                          |
| 228          | ADAS: traffic sign recognition                           |
| 229          | ADAS: pedestrian collision warning                       |
| 230          | Fatigue driving                                          |
| 231          | ADAS: headway warning                                    |
| 232          | ADAS: right lane departure                               |
| 233          | ADAS: left lane departure                                |
| 234          | ADAS: lane departure                                     |
| 235          | ADAS: forward collision warning                          |
| 236          | Harsh driving: quick lane change                         |
| 237          | Harsh driving: acceleration and turn                     |
| 238          | Harsh driving: braking and turn                          |
| 239          | Harsh driving: turn                                      |
| 240          | Harsh driving: acceleration                              |
| 241          | Harsh driving: braking                                   |
| 242          | Crash alarm                                              |
| 243          | Harsh driving                                            |
| 244          | Call button pressed                                      |
| 245          | Driver distraction: texting while driving                |
| 246          | Driver distraction: not watching the road ("lizard eye") |
| 247          | Lane drift detected                                      |
| 248          | Traffic STOP sign violation                              |
| 249          | Speed limit exceeded                                     |
| 250          | Traffic light violation                                  |
| 251          | Tailgating: unsafe following distance                    |
| 252          | Seat belt fastened                                       |

### Vehicle efficiency

Range: 301–400.

| **Event ID** | **Description**    |
| ------------ | ------------------ |
| 301          | Idle end           |
| 302          | Idle start         |
| 303          | Check engine light |

### Track information

Range: 401–500.

| **Event ID** | **Description**                     |
| ------------ | ----------------------------------- |
| 401          | Track point (no specific event)     |
| 402          | GSM LBS point report                |
| 403          | Track point by time interval        |
| 404          | Track point by distance             |
| 405          | Track point by heading angle change |
| 406          | Movement start                      |
| 407          | Movement end                        |
| 408          | Non-track message                   |
| 409          | Tracker entered auto geofence       |
| 410          | Tracker exited auto geofence        |

### Inputs

Range: 501–550.

| **Event ID** | **Description**       |
| ------------ | --------------------- |
| 501          | Input 1 state changed |
| 502          | Input 2 state changed |
| 503          | Input 3 state changed |
| 504          | Input 4 state changed |
| 505          | Input 5 state changed |
| 506          | Input 6 state changed |
| 507          | Input 7 state changed |
| 508          | Input 8 state changed |

### Outputs

Range: 551–600.

| **Event ID** | **Description**        |
| ------------ | ---------------------- |
| 551          | Output 1 state changed |
| 552          | Output 2 state changed |
| 553          | Output 3 state changed |
| 554          | Output 4 state changed |
| 555          | Output 5 state changed |
| 556          | Output 6 state changed |
| 557          | Output 7 state changed |
| 558          | Output 8 state changed |

### Peripherals and other

Range: 601–700.

| **Event ID** | **Description**                |
| ------------ | ------------------------------ |
| 601          | Antenna disconnected           |
| 602          | Accessory disconnected         |
| 603          | Accessory connected            |
| 604          | Ignition off                   |
| 605          | Ignition on                    |
| 606          | Light sensor determined dark   |
| 607          | Light sensor determined bright |
| 608          | GPS signal recovered           |
| 609          | GPS signal lost                |

### Custom event identifiers

For device-specific or application-specific events not covered by the ranges above, use identifiers starting from **10,000**. Values below 10,000 are reserved for future NGP standard events.
