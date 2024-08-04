# Getting List of GPS Trackers

This guide explains how to retrieve a list of GPS trackers associated with a user account using the Navixy API. This is essential for managing and monitoring multiple devices within the Navixy platform.
## Prerequisites

Before you begin, ensure you have an active Navixy account and an [API key for authentication](../../getting-started/authentication.md). 

## Make the API request

To get the list of trackers, you need to make a POST request to the [`/tracker/list`](../../resources/tracking/tracker/index.md) endpoint. Below are the details and examples of how to do this.  

### API endpoint

`https://api.navixy.com/v2/tracker/list`

### API request
##### cURL

```
curl -X POST 'https://api.navixy.com/v2/tracker/list' \
	-H 'Content-Type: application/json' \
	-d '{"hash": "your_api_key_hash"}'
```

##### HTTP GET

```
https://api.navixy.com/v2/tracker/list?hash=your_api_key_hash
```


##### Response

If the request is successful, the response will contain a list of trackers associated with your account.

```json
{
  "success": true,
  "list": [
    {
      "id": 123,
      "label": "Vehicle A",
      "imei": "123456789012345",
      "model": "Model X",
      "status": {
        "online": true,
        "last_update": "2023-05-01T12:00:00Z"
      }
    },
    {
      "id": 124,
      "label": "Vehicle B",
      "imei": "987654321098765",
      "model": "Model Y",
      "status": {
        "online": false,
        "last_update": "2023-04-30T08:30:00Z"
      }
    }
  ]
}
```  

If an account has a large number of trackers, and you only need specific ones, you can add an optional filter parameter to the request to return only matching records.

This parameter has the following constraints:

* Labels array size: minimum 1, maximum 1024.
* No null items.
* No duplicate items.
* Item length: minimum 1, maximum 60 characters.

To get a list of trackers with labels matching the filter, use this API call:

```
curl -X POST '{{ extra.api_example_url }}/tracker/list' \
   -H 'Content-Type: application/json' \
   -d '{"hash": "your_api_key_hash", "labels": ["aa", "b"]}'
```

**Usage notes**

- Ensure your API key hash is valid and has the necessary permissions.
- The list may include both online and offline trackers, along with their last known status.
- Use this method to manage and display multiple tracking devices on your application interface.