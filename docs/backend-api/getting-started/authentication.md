
To interact with the Navixy API, you need an API key hash, which is essential for authenticating your requests. Follow these steps to obtain the hash.

## Steps to Obtain an API Key Hash

### Obtaining an API Key from User Interface

1. **Login to the Web Interface**:
    - Access the Navixy user interface via the web
    - Use your credentials to log in

1. **Navigate to the API Key Section**:
    - Once logged in, go to the `Settings` menu.
    - Find the `API Keys` section, typically located under `Account Settings` or `Security`.

1. **Generate a New API Key**:
    - Click on the `Generate New API Key` button.
    - Provide a name for the API key to easily identify it later.
    - Select the permissions and scope for the key based on your needs.
    - Click `Generate`.

1. **Copy the API Key Hash**:
    - Once the key is generated, you will see the API key hash.
    - Copy this hash and store it securely. You will use this hash in your API requests.

### Obtaining User Key via Authentication Call

To authenticate and obtain a user key through the Navixy API, use the `user/auth` call. This section provides a detailed guide on how to make this API call, including example requests and expected responses.

#### Endpoint

```
POST /user/auth
```

#### Parameters

- `login` (string, required): The user's login name.
- `password` (string, required): The user's password.
- `app_key` (string, optional): The application key for additional security.

#### Request Example

HTTP POST Example with JSON

```sh
$ curl -X POST 'https://api.navixy.com/v2/user/auth' \
    -H 'Content-Type: application/json' \
    -d '{
          "login": "user@example.com",
          "password": "user_password"
        }'
```

HTTP POST Example with Form Data

```sh
$ curl -X POST 'https://api.navixy.com/v2/user/auth' \
    -d 'login=user@example.com' \
    -d 'password=user_password'
```

#### Response

Successful Response

```json
{
  "success": true,
  "hash": "a6aa75587e5c59c32d347da438505fc3",
  "user": {
    "id": 12345,
    "login": "user@example.com",
    "name": "John Doe"
  }
}
```

- `success` (boolean): Indicates if the authentication was successful
- `hash` (string): The API key hash to be used in subsequent API calls
- `user` (object): Contains user details
  - `id` (integer): The user ID
  - `login` (string): The user's login name
  - `name` (string): The user's full name

Error Response

```json
{
  "success": false,
  "status": {
    "code": 2,
    "description": "Service Auth error"
  }
}
```

- `success` (boolean): Indicates if the authentication failed
- `status` (object): Contains error details
  - `code` (integer): The error code
  - `description` (string): A description of the error


## Using the API Key Hash

### Including the API Key Hash in Requests

To authenticate your requests to the Navixy API, include the API key hash in one of the following ways:

1. **As a Query Parameter**: Append the hash to your API request URL
   ```sh
   https://api.navixy.com/v2/resource/action?hash=your_api_key_hash
   ```

1. **As a Request Header**: Include the hash in the `Authorization` header
   ```sh
   Authorization: NVX your_api_key_hash
   ```

1. **In the Request Body**: Include the hash in the JSON body of your request
   ```json
   {
     "hash": "your_api_key_hash",
     "param1": "value1"
   }
   ```

### Example Requests

#### HTTP GET Example

```sh
$ curl 'https://api.navixy.com/v2/resource/action?hash=your_api_key_hash'
```

#### HTTP POST Example with JSON

```sh
$ curl -X POST 'https://api.navixy.com/v2/resource/action' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "your_api_key_hash",
          "param1": "value1"
        }'
```

### Best Practices for API Key Security

- **Store securely**: Always store your API keys securely and do not expose them in your codebase or version control.
- **Restrict permissions**: Limit the permissions of the API key to only what is necessary for your application.
- **Rotate keys**: Regularly rotate your API keys and update your application accordingly.

