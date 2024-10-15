
With Navixy APIs, you can use either the user session hash or API keys.

An API Key, also known as a "Hash" is a randomly generated string used to verify and authenticate actions. The hash of the API key must be included in most API calls.

### API Keys Advantages

Unlike a user's session hash, the API key has the following characteristics:

- It will not be deleted if the user logs out or changes their password.
- There is no need to [renew](../resources/commons/user/session/index.md#renew) the key periodically.
- It does not require the transfer or storage of the username and password.
- It can be deleted at any time if there is a suspicion of compromise.
- You can create a separate key for each individual integration.

Every user account may have up to 20 API keys. Sub-users don't have API keys functionality.

Follow these ways to obtain the API key.

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

## Using the API Key Hash

To authenticate your requests to the Navixy API, include the API key hash in one of the following ways:

1. **As a Request Header**: Include the hash in the `Authorization` header (preferable)
   ```sh
   Authorization: NVX your_api_key_hash
   ```

2. **In the Request Body**: Include the hash in the JSON body of your request
   ```json
   {
     "hash": "your_api_key_hash",
     "param1": "value1"
   }
   ```

3. **As a Query Parameter**: Append the hash to your API request URL.<br/>
   For testing purposes only, do **not** use this in production due to the security risk.
   ```sh
   https://api.navixy.com/v2/resource/action?hash=your_api_key_hash
   ```

### Example Requests

#### HTTP GET Example

```sh
$ curl 'https://api.navixy.com/v2/resource/action?hash=your_api_key_hash'
```

#### HTTP POST Example with JSON

```sh
$ curl -X POST 'https://api.navixy.com/v2/resource/action' \
    -H 'Authorization: NVX your_api_key_hash' \
    -H 'Content-Type: application/json' \
    -d '{
          "param1": "value1"
        }'
```

### Best Practices for Managing API Key

- **Store securely**: Always store your API keys securely and do not expose them in your codebase or version control. This helps prevent unauthorized access.
- **Don't mix keys and integrations**: Use one API key per integration. This practice helps in managing the usage of each key for integrations.
- **Use clear labels for API keys**: Use clear and descriptive labels for your API keys. This makes it easier to understand which key is used for which integration, improving overall organization and management.
- **Rotate keys**: Regularly rotate your API keys and update your application accordingly.
