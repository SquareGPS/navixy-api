---
title: Driver journals usage
description: How to work with driver journals and get mileage counter values at the start and the end of a trip.
---

# Driver journals usage

Driver Journal logs all the trips an employee made during a selected time period and groups them by their status: business,
private or other. Users can choose to show either the summary of all trips with highlighted trip statuses or to view the 
required status only. The displayed data is already a finished document exportable as a PDF/Excel file or printed out as
it is.

Driver Journal itemizes all the trips, providing exact mileage, accurate location, date and time, so clients can easily
report business miles versus personal miles and deduct the exact amount of business-related expenses (e.g., by percentage
of the actual expenses).

However, some situations are not that easy to identify. For those cases, use “other” trip status (specific comments
can be given in notes). Such trips can be reviewed individually and using valid metrics be later converted to business
or private as the case might be.

All the trip data will be safely and securely stored in one digital place. No need to keep the piles of paperwork. However,
Revenue Services require to keep supporting receipts (for gas/fuel) to prove the actual amount of expenses.

For example, you need to distribute all trips of the device for the last day and distribute them by type in order to
generate a bill for fuel payment. 
Also, they will contain important information about trips like driver, who was assigned to a tracker, start/end 
dates of the trip, start/end locations, length, start/end odometer values. You can operate with this information or use 
it in your CRM. 

***

## Work with driver journals

### Getting all possible trips per period for journal

In order to generate a driver journal, we first need to get a list of possible trips.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/proposal/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2021-10-26 00:00:00", "to": "2021-10-26 23:59:59", "tracker_id": 311852}'
    ```

The platform will reply with the information about all trips per period:

```json
{
  "success":true,
  "list":[{
    "tracker_id":311852,
    "employee_id":2183,
    "start_date":"2021-10-26 00:00:00",
    "end_date":"2021-10-26 01:39:22",
    "start_location":{
      "address":"Central'naya kol'cevaya avtomobil'naya doroga, gor. okrug Istra, Moscow Oblast, Russia, 143540",
      "lat":55.8906183,
      "lng":36.944505
    },
    "end_location": {
      "address":"Klin, Moscow Oblast, Russia, 141609",
      "lat":56.356175,
      "lng":36.8077733
    },
    "length":70.83,
    "start_odometer":620741.0,
    "end_odometer":620812.0
  }, 
  {
    "tracker_id":311852,
    "employee_id":2183,
    "start_date":"2021-10-26 01:47:22",
    "end_date":"2021-10-26 03:30:58",
    "start_location":{
      "address":"Klin, Moscow Oblast, Russia, 141609",
      "lat":56.3562966,
      "lng":36.8079016
    },
    "end_location":{
      "address":"S/kh Lesnye ozera, Pyatnickoe shosse, Novaya, Moscow Oblast, Russia, 141591",
      "lat":56.082615,
      "lng":36.9091333
    },
    "length":45.32,
    "start_odometer":620812.0,
    "end_odometer":620856.0
  }, 
  {
    "tracker_id":311852,
    "employee_id":2183,
    "start_date":"2021-10-26 03:37:58",
    "end_date":"2021-10-26 04:53:18",
    "start_location":{
      "address":"S/kh Lesnye ozera, Pyatnickoe shosse, Novaya, Moscow Oblast, Russia, 141591",
      "lat":56.082615,
      "lng":36.9091333
    },
    "end_location":{
      "address":"Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 108806",
      "lat":55.5309516,
      "lng":36.967255
    },
    "length":77.6,
    "start_odometer":620856.0,
    "end_odometer":620934.0
  }]
}
```

### Entries creation

Once we have a list of all trips, we need to create a driver journal entries. In addition to the received objects in the
previous call, we must specify the type of entry to be created, and we can add a comment to each of them.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/create' \
        -H 'Content-Type: application/json' \ 
        -d {% raw %}'{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "entries": [{{"tracker_id":311852, "employee_id":2183, "start_date":"2021-10-26 00:00:00", "end_date":"2021-10-26 01:39:22", "start_location":{"address":"Central'naya kol'cevaya avtomobil'naya doroga, gor. okrug Istra, Moscow Oblast, Russia, 143540", "lat":55.8906183, "lng":36.944505}, "end_location": {"address":"Klin, Moscow Oblast, Russia, 141609", "lat":56.356175, "lng":36.8077733}, "length":70.83, "start_odometer":620741.0, "end_odometer":620812.0, "type": "work", "comment": "order_ID=23415"},{"tracker_id":311852, "employee_id":2183, "start_date":"2021-10-26 01:47:22", "end_date":"2021-10-26 03:30:58", "start_location":{"address":"Klin, Moscow Oblast, Russia, 141609", "lat":56.3562966, "lng":36.8079016}, "end_location":{"address":"S/kh Lesnye ozera, Pyatnickoe shosse, Novaya, Moscow Oblast, Russia, 141591", "lat":56.082615, "lng":36.9091333}, "length":45.32, "start_odometer":620812.0, "end_odometer":620856.0, "type": "personal", "comment": "trip to a cafe"},{"tracker_id":311852, "employee_id":2183, "start_date":"2021-10-26 03:37:58", "end_date":"2021-10-26 04:53:18", "start_location":{"address":"S/kh Lesnye ozera, Pyatnickoe shosse, Novaya, Moscow Oblast, Russia, 141591", "lat":56.082615, "lng":36.9091333}, "end_location":{"address":"Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 108806", "lat":55.5309516, "lng":36.967255}, "length":77.6, "start_odometer":620856.0, "end_odometer":620934.0, "type": "work", "comment": "order_ID=31024"}]}'{% endraw %}
    ```

The platform will confirm creation with:

```json
{ 
  "success": true
}
```

### Driver journal obtaining

After all entries have been created, we can download the driver journal in the format we 
want by [download](../resources/fleet/driver_journal/entry.md#download) API call.

To simply display the driver journal in a specialized application, for example,
use the [list](../resources/fleet/driver_journal/entry.md#list) request.