
To interact with the Navixy API, you need an API key hash, which is essential for authenticating your requests. Follow these steps to obtain the hash.

## Steps to Obtain an API Key Hash

1. **Login to the Web Interface**:
    - Access the Navixy user interface via the web
    - Use your credentials to log in

2. **Navigate to the API Key Section**:
    - Once logged in, go to the `Settings` menu.
    - Find the `API Keys` section, typically located under `Account Settings` or `Security`.

3. **Generate a New API Key**:
    - Click on the `Generate New API Key` button.
    - Provide a name for the API key to easily identify it later.
    - Select the permissions and scope for the key based on your needs.
    - Click `Generate`.

4. **Copy the API Key Hash**:
    - Once the key is generated, you will see the API key hash.
    - Copy this hash and store it securely. You will use this hash in your API requests.

## Using the API Key Hash

### Including the API Key Hash in Requests

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

### Best Practices for API Key Security

- **Store securely**: Always store your API keys securely and do not expose them in your codebase or version control.
- **Restrict permissions**: Limit the permissions of the API key to only what is necessary for your application.
- **Rotate keys**: Regularly rotate your API keys and update your application accordingly.
