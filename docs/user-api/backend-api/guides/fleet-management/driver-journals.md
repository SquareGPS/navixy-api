# Using Driver Journals

Driver Journals log all trips made by an employee within a selected period, categorizing them by status: business, private, or other. Users can view a summary of all trips, highlighting their statuses, or filter to show only specific types. This data can be exported as PDF/Excel files or printed directly.

Driver Journals provide detailed trip information, including mileage, location, date, and time, enabling clients to differentiate between business and personal miles accurately. This helps in deducting business-related expenses. For ambiguous cases, trips can be marked as "other" and later reviewed for proper categorization.

All trip data is securely stored digitally, eliminating the need for physical paperwork. However, supporting receipts for expenses like fuel should be kept for verification.

For example, to generate a bill for fuel payment, you may need to categorize all trips of a device for the previous day. These records include important trip details such as driver, start/end dates, locations, trip length, and odometer readings, which can be used in your CRM.

## Working with Driver Journals

### Retrieving All Trips for a Period

To generate a driver journal, first retrieve a list of possible trips using the [`fleet/driver_journal/proposal/list`](../../resources/fleet/driver_journal/proposal.md#list) API call.

#### API Request

=== "cURL"
```shell
curl -X POST '{{ extra.api_example_url }}/driver/journal/proposal/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2021-10-26 00:00:00", "to": "2021-10-26 23:59:59", "tracker_id": 311852}'
```

#### Example Response
```json
{
  "success": true,
  "list": [
    {
      "tracker_id": 311852,
      "employee_id": 2183,
      "start_date": "2021-10-26 00:00:00",
      "end_date": "2021-10-26 01:39:22",
      "start_location": {
        "address": "123 Main St, Los Angeles, CA 90012",
        "lat": 34.052235,
        "lng": -118.243683
      },
      "end_location": {
        "address": "456 Elm St, Los Angeles, CA 90012",
        "lat": 34.052235,
        "lng": -118.243683
      },
      "length": 70.83,
      "start_odometer": 620741.0,
      "end_odometer": 620812.0
    },
    {
      "tracker_id": 311852,
      "employee_id": 2183,
      "start_date": "2021-10-26 01:47:22",
      "end_date": "2021-10-26 03:30:58",
      "start_location": {
        "address": "456 Elm St, Los Angeles, CA 90012",
        "lat": 34.052235,
        "lng": -118.243683
      },
      "end_location": {
        "address": "789 Oak St, Los Angeles, CA 90012",
        "lat": 34.052235,
        "lng": -118.243683
      },
      "length": 45.32,
      "start_odometer": 620812.0,
      "end_odometer": 620856.0
    },
    {
      "tracker_id": 311852,
      "employee_id": 2183,
      "start_date": "2021-10-26 03:37:58",
      "end_date": "2021-10-26 04:53:18",
      "start_location": {
        "address": "789 Oak St, Los Angeles, CA 90012",
        "lat": 34.052235,
        "lng": -118.243683
      },
      "end_location": {
        "address": "101 Pine St, Los Angeles, CA 90012",
        "lat": 34.052235,
        "lng": -118.243683
      },
      "length": 77.6,
      "start_odometer": 620856.0,
      "end_odometer": 620934.0
    }
  ]
}
```

### Creating Journal Entries

Once you have a list of all trips, create driver journal entries. Specify the type of entry and optionally add a comment for each trip.

#### API Request

=== "cURL"
```shell
curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "entries": [{"tracker_id": 311852, "employee_id": 2183, "start_date": "2021-10-26 00:00:00", "end_date": "2021-10-26 01:39:22", "start_location": {"address": "123 Main St, Los Angeles, CA 90012", "lat": 34.052235, "lng": -118.243683}, "end_location": {"address": "456 Elm St, Los Angeles, CA 90012", "lat": 34.052235, "lng": -118.243683}, "length": 70.83, "start_odometer": 620741.0, "end_odometer": 620812.0, "type": "work", "comment": "order_ID=23415"}, {"tracker_id": 311852, "employee_id": 2183, "start_date": "2021-10-26 01:47:22", "end_date": "2021-10-26 03:30:58", "start_location": {"address": "456 Elm St, Los Angeles, CA 90012", "lat": 34.052235, "lng": -118.243683}, "end_location": {"address": "789 Oak St, Los Angeles, CA 90012", "lat": 34.052235, "lng": -118.243683}, "length": 45.32, "start_odometer": 620812.0, "end_odometer": 620856.0, "type": "personal", "comment": "trip to a cafe"}, {"tracker_id": 311852, "employee_id": 2183, "start_date": "2021-10-26 03:37:58", "end_date": "2021-10-26 04:53:18", "start_location": {"address": "789 Oak St, Los Angeles, CA 90012", "lat": 34.052235, "lng": -118.243683}, "end_location": {"address": "101 Pine St, Los Angeles, CA 90012", "lat": 34.052235, "lng": -118.243683}, "length": 77.6, "start_odometer": 620856.0, "end_odometer": 620934.0, "type": "work", "comment": "order_ID=31024"}]}'
```

#### Example Response
```json
{
  "success": true
}
```

### Downloading the Driver Journal

After creating the entries, you can download the driver journal in the desired format using the `download` API call. To display the journal in an application, use the `list` request.

For detailed API documentation, refer to the [Navixy API reference](../../resources/fleet/driver_journal/entry.md).