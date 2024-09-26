With Navixy APIs, you can use either the user session hash or API keys. If your integration only uses user account APIs, we suggest using API keys.

An API Key, also known as a "Hash" is a randomly generated string used to verify and authenticate actions. The hash of the API key must be included in most API calls.

### Key Characteristics

Unlike a user's session hash, the API key has the following characteristics:

- It will not be deleted if the user logs out or changes their password.
- There is no need to [renew](./user/session/index.md#renew) the key periodically.
- It does not require the transfer or storage of the username and password.
- It can be deleted at any time if there is a suspicion of compromise.
- You can create a separate key for each individual integration.

Follow these steps to obtain the API key.

## Ways to Obtain an API Key Hash

### Creating an API Key from User Interface

1. **Login to the Web Interface**:
    - Access the Navixy user interface via the web.
    - Use your credentials to log in.

2. **Navigate to the API Key Section**:
    - Once logged in, click on your username.
    - Find and select the `API Keys` section.

3. **Generate a New API Key**:
    - Click on the plus button on the top left corner.
    - Provide a name for the API key to easily identify it later.
    - Click `Save`.

4. **Copy the API Key Hash**:
    - Once the key is generated, you will see it in the API keys table, including the label, creation date, and the API key hash.
    - Use this hash in your API requests.

### Creating an API Key Using the User Session Hash

For security reasons, you cannot access or create API keys without the user session hash. Therefore, the first step is to obtain this user hash from the platform.

To authenticate and obtain a user hash through the Navixy API, use the `user/auth` call. This section provides a detailed guide on how to use this API call, create an API key with it and get the list of API keys, including example requests and expected responses.

#### Get User Session Hash

```
POST /user/auth
```

#### Parameters

- `login` (string, required): The user's login email.
- `password` (string, required): The user's password.

#### Request Example

Example with JSON:

```sh
$ curl -X POST 'https://api.navixy.com/v2/user/auth' \
    -H 'Content-Type: application/json' \
    -d '{
          "login": "user@example.com",
          "password": "user_password"
        }'
```

Example with Form Data:

```sh
$ curl -X POST 'https://api.navixy.com/v2/user/auth' \
    -d 'login=user@example.com' \
    -d 'password=user_password'
```

#### Response

Successful Response:

```json
{
  "success": true,
  "hash": "a6aa75587e5c59c32d347da438505fc3"
}
```

- `success` (boolean): Indicates if the authentication was successful.
- `hash` (string): The user hash to be used in subsequent API calls and to create or get the API key.

Error Response:

```json
{
  "success": false,
  "status": {
    "code": 102,
    "description": "Wrong login or password"
  }
}
```

- `success` (boolean): Indicates if the authentication failed
- `status` (object): Contains error details
    
    * `code` (integer): The error code
    * `description` (string): A description of the error

To make a new API key, send a request to api/key/create with the user session hash.

#### Create a New API Key

```
POST /api/key/create
```

#### Parameters

- `hash` (string, required): The user's session hash.
- `title` (string, required): Name of an API key you create. It should contain only printable characters. The maximum length is 255 symbols.

#### Request Example

Example with JSON:

```sh
$ curl -X POST 'https://api.navixy.com/v2/api/key/create' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "12891jknsioahse10jk1n2103u12jkn2",
          "title": "API key label"
        }'
```

Example with Form Data:

```sh
$ curl -X POST 'https://api.navixy.com/v2/api/key/create' \
    -d 'hash=12891jknsioahse10jk1n2103u12jkn2' \
    -d 'title=API key label'
```

#### Response

Successful Response:

```json
{
  "success": true
  "create_date": "2024-09-27"
  "title": "API key label"
}
```

- `success` (boolean): Indicates if the authentication was successful.
- `create_date` (string): The date and time when the API key was created.
- `title` (string): The assigned label.

Error Response:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "User or API key not found or session ended"
  }
}
```

- `success` (boolean): Indicates if the authentication failed
- `status` (object): Contains error details
    
    * `code` (integer): The error code
    * `description` (string): A description of the error
 
### Getting a List of API Keys with User Session Hash

You can also get a list of already existing API keys to use one. To get this list, you need the user session hash.

#### Endpoint

```
POST /api/key/list
```

#### Parameters

- `hash` (string, required): The user's session hash.

#### Request Example

Example with JSON:

```sh
$ curl -X POST 'https://api.navixy.com/v2/api/key/list' \
    -H 'Content-Type: application/json' \
    -d '{
          "hash": "12891jknsioahse10jk1n2103u12jkn2",
        }'
```

Example with Form Data:

```sh
$ curl -X POST 'https://api.navixy.com/v2/api/key/list' \
    -d 'hash=12891jknsioahse10jk1n2103u12jkn2'
```

#### Response

Successful Response:

```json
{
  "success": true
  "list": [{
    "hash": "API key1 hash"
    "create_date": "2024-09-27"
    "title": "API key1 label"
   }, {
    "hash": "API key2 hash"
    "create_date": "2024-09-27"
    "title": "API key2 label"
   }]
}
```

- `success` (boolean): Indicates if the authentication was successful.
- `list` (array of objects): List of already created API keys. Will be empty if user doesn't have API keys.
  
  * `hash` (string): The API key hash.
  * `create_date` (string): The date and time when the API key was created.
  * `title` (string): The assigned label.

Error Response:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "User or API key not found or session ended"
  }
}
```

- `success` (boolean): Indicates if the authentication failed
- `status` (object): Contains error details
    
    * `code` (integer): The error code
    * `description` (string): A description of the error


## Using the API Key Hash

To authenticate your requests to the Navixy API, include the API key hash.

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

### Best Practices for Managing API Key

- **Store securely**: Always store your API keys securely and do not expose them in your codebase or version control. This helps prevent unauthorized access.
- **Don't mix keys and integrations**: Use one API key per integration. This practice helps in managing the usage of each key more effectively.
- **Use clear labels for API keys**: Use clear and descriptive labels for your API keys. This makes it easier to understand which key is used for which integration, improving overall organization and management.
