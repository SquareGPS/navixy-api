# Errors

This section provides detailed information on error handling in the Navixy API, including example error responses and descriptions of error codes.

## Error Handling

If an error occurs, the API returns a special error response. You can detect an error by checking the HTTP response code. If it is not `200 OK`, you should parse and handle the response body as an error response.

### Example Error Response

When an error occurs, the response will be in the following format:

```json
{
  "success": false,
  "status": {
    "code": 1,
    "description": "Database error"
  }
}
```

- `success` (boolean): Indicates if the request was successful.
- `status` (object): Contains details about the error.

    * `code` (integer): The error code.
    * `description` (string): A description of the error.

## Error Codes

Default HTTP code is `400`. Common error codes (should be handled for all API calls) are `1-100`, and resource or action-specific errors are `101-300`.

### Common Error Codes

| Code | Description                                                          | HTTP Code |
|------|----------------------------------------------------------------------|-----------|
| 1    | Database error                                                       | 500       |
| 2    | Service Auth error                                                   | 403       |
| 3    | Wrong hash                                                           |           |
| 4    | User or API key not found or session ended                           |           |
| 5    | Wrong request format                                                 |           |
| 6    | Unexpected error                                                     | 500       |
| 7    | Invalid parameters                                                   |           |
| 8    | Queue service error, try again later                                 | 503       |
| 9    | Too large request                                                    | 412       |
| 11   | Access denied                                                        | 403       |
| 12   | Dealer not found                                                     |           |
| 13   | Operation not permitted                                              | 403       |
| 14   | Database unavailable                                                 | 503       |
| 15   | Too many requests (rate limit exceeded)                              | 429       |
| 101  | In demo mode this function is disabled                               | 403       |
| 102  | Wrong login or password                                              |           |
| 103  | User not activated                                                   |           |
| 111  | Wrong handler                                                        |           |
| 112  | Wrong method                                                         |           |
| 201  | Not found in database                                                |           |
| 202  | Too many points in zone                                              |           |
| 203  | Delete entity associated with                                        |           |
| 204  | Entity not found                                                     | 404       |
| 206  | Login already in use                                                 |           |
| 207  | Invalid captcha                                                      |           |
| 208  | Device blocked                                                       | 403       |
| 209  | Failed sending email                                                 |           |
| 210  | Geocoding failed                                                     |           |
| 211  | Requested time span is too big                                       |           |
| 212  | Requested limit is too big                                           |           |
| 213  | Cannot perform action: the device is offline                         |           |
| 214  | Requested operation or parameters are not supported by the device    |           |
| 215  | External service error                                               |           |
| 217  | List contains nonexistent entities                                   |           |
| 218  | Malformed external service parameters                                |           |
| 219  | Not allowed for clones of the device                                 | 403       |
| 220  | Unknown device model                                                 |           |
| 221  | Device limit exceeded                                                | 403       |
| 222  | Plugin not found                                                     |           |
| 223  | Phone number already in use                                          |           |
| 224  | Device ID already in use                                             |           |
| 225  | Not allowed for this legal type                                      | 403       |
| 226  | Wrong ICCID                                                          |           |
| 227  | Wrong activation code                                                |           |
| 228  | Not supported by sensor                                              |           |
| 229  | Requested data is not ready yet                                      | 404       |
| 230  | Not supported for this entity type                                   |           |
| 231  | Entity type mismatch                                                 | 409       |
| 232  | Input already in use                                                 |           |
| 233  | No data file                                                         |           |
| 234  | Invalid data format                                                  |           |
| 235  | Missing calibration data                                             |           |
| 236  | Feature unavailable due to tariff restrictions                       | 402       |
| 237  | Invalid tariff                                                       |           |
| 238  | Changing tariff is not allowed                                       | 403       |
| 239  | New tariff does not exist                                            | 404       |
| 240  | Not allowed to change tariff too frequently                          | 403       |
| 241  | Cannot change phone to bundled sim. Contact tech support.            |           |
| 242  | There were errors during content validation                          |           |
| 243  | Device already connected.                                            |           |
| 244  | Duplicate entity label.                                              |           |
| 245  | New password must be different                                       |           |
| 246  | Invalid user ID                                                      |           |
| 247  | Entity already exists                                                | 409       |
| 248  | Wrong password                                                       |           |
| 249  | Operation available for clones only                                  | 403       |
| 250  | Not allowed for deleted devices                                      | 403       |
| 251  | Insufficient funds                                                   | 403       |
| 252  | Device already corrupted                                             |           |
| 253  | Device has clones                                                    |           |
| 254  | Cannot save file                                                     | 500       |
| 255  | Invalid task state                                                   |           |
| 256  | Location already actual                                              |           |
| 257  | Registration forbidden                                               | 403       |
| 258  | Bundle not found                                                     | 404       |
| 259  | Payments count not comply with summary                               |           |
| 260  | Payments sum not comply with summary                                 |           |
| 261  | Entity has external links                                            | 403       |
| 262  | Entries list is missing some entries or contains nonexistent entries |           |
| 263  | No change needed, old and new values are the same                    |           |
| 264  | Timeout not reached                                                  | 403       |
| 265  | Already done                                                         | 403       |
| 266  | Cannot perform action for the device in current status               | 403       |
| 267  | Too many entities                                                    |           |
| 268  | Over quota                                                           | 402       |
| 269  | Invalid file state                                                   |           |
| 270  | Too many sensors of same type already exist                          |           |
| 271  | File over max size                                                   | 413       |
| 272  | Trackers must have same models                                       |           |
| 273  | Duplicate login                                                      |           |
| 274  | Empty data file                                                      |           |
| 275  | User is blocked                                                      | 403       |
| 276  | Action is forbidden for received session type                        | 403       |
| 277  | Security group has users in it                                       | 409       |
| 278  | Security group is a default one                                      | 409       |
| 279  | Invalid task period                                                  |           |
| 280  | Invalid import request state                                         |           |
| 281  | This resource is closed                                              |           |
| 284  | Not enough points for the specified zone type                        |           |

## Best Practices for Error Handling

- **Check HTTP Status Codes**: Always check the HTTP status code of the response to determine if the request was successful.
- **Parse the Error Response**: If the status code indicates an error, parse the response body to obtain the error details.
- **Handle Specific Error Codes**: Implement handling for common error codes and resource-specific error codes to provide meaningful feedback to the user.
- **Retry Logic**: For transient errors (e.g., service unavailable, rate limits), implement retry logic with exponential backoff.
- **Logging**: Log error responses for debugging and monitoring purposes.

By following these guidelines, you can effectively handle errors in your application and provide a better experience for your users.