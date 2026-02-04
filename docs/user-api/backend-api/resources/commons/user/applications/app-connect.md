---
description: Integrate custom applications with Navixy authentication
---

# App Connect

Navixy App Connect is an authentication gateway that enables you to build custom applications integrating with Navixy without implementing your own user management system. Users authenticate once through their Navixy account, and your application receives secure database access credentials automatically.

The middleware acts as an authentication proxy that:

1. Authenticates users via their `session_key`
2. Fetches database credentials from the master database
3. Calls your application's auth endpoint with user info and database URLs
4. Proxies all subsequent requests to your application

**Common use cases:**

* Custom dashboards for IoT data visualization
* Analytics tools processing telemetry data
* Business system integrations with Navixy data

{% hint style="info" %}
[Dashboard Studio](https://marketplace.navixy.com/shop/dashboard-studio/) uses this authentication approach. You can integrate any custom application the same way.
{% endhint %}

## Integration prerequisites

Your application must meet these technical requirements to integrate with Navixy App Connect:

* **API server**: Your application must have a publicly accessible API server that can receive HTTP POST requests from the middleware and respond with JSON authentication responses. The [Authentication endpoint](app-connect.md#authentication-endpoint) section describes the specific endpoint you must implement.\
  For testing, you can use cloud hosting platforms to quickly deploy a publicly accessible test server. Use production-grade hosting for live applications.
* **JWT token generation**: Your application must be able to generate JWT tokens with required fields (`userId`, `email`, `role`, `iat`, `exp`) using HS256 or RS256 algorithms. The [JWT Token Requirements](app-connect.md#jwt-token-requirements) section describes the token structure and validation rules.
* **Database connectivity**: Your application must include a PostgreSQL client library to connect to Navixy databases using connection strings provided during authentication. The [Using Database Connection Strings](app-connect.md#using-database-connection-strings) section provides connection examples and best practices.

## How application registration works

Navixy App Connect does not require separate application registration. Your application integrates directly with existing Navixy user accounts through the authentication middleware layer.

The connection between your application and Navixy is managed through the [User applications](https://app.gitbook.com/s/446mKak1zDrGv70ahuYZ/guide/account/user-applications) functionality. When a user accesses your application:

1. The middleware validates the user's session
2. The middleware retrieves database credentials for that user
3. The middleware calls your `/api/auth/login` endpoint with user information and database URLs
4. Your application responds with a JWT token
5. The user can now interact with your application

You do not need to register your application URL, provide callback endpoints, or configure webhook addresses. The middleware handles all communication between Navixy and your application automatically.

Watch this video to get a quick and visual walkthrough of authenticating a 3rd-party app with Navixy session using App Connect:&#x20;

{% embed url="https://youtu.be/y8Wwob-Uw3I?si=IwnECajenm7o7wtC" %}

## Development and testing workflow

### Local development

You can develop and test most of your application locally:

1. **Implement the auth endpoint** ([`POST /api/auth/login`](app-connect.md#post-api-auth-login)) on your local server
2. **Test token generation** by calling your endpoint directly with sample payloads
3. **Test database connectivity** using connection strings in the format provided by the middleware
4. **Test API routes** by generating tokens and making authenticated requests

See the [Complete Integration Example](app-connect.md#complete-integration-example) section for step-by-step implementation guidance with working code.

### Testing API connectivity

To test the complete authentication flow including middleware communication, deploy your API server to a publicly accessible endpoint. Hosting services provide free tiers suitable for testing:

1. Deploy your application to the selected platform
2. Configure your application through User applications functionality
3. Access your application through Navixy to trigger the authentication flow
4. Verify the middleware successfully calls your `/api/auth/login` endpoint
5. Test authenticated API requests with the returned JWT token

Once API connectivity is verified, you can continue development locally while using the deployed endpoint for integration testing.

{% hint style="info" %}
There is no dedicated test environment or sandbox. Test your integration using your development Navixy account and a test deployment of your application.
{% endhint %}

#### Configuration

Your application requires the following environment variables:

`JWT_SECRET` (Required)

* Purpose: Secret key for signing and verifying JWT tokens
* Format: String, minimum 32 characters recommended
* Example: `your-secret-key-at-least-32-characters-long`

`DASHBOARD_BASIC_AUTH` (Optional)

* Purpose: Credentials for Basic Authentication on static assets. Only needed if your application serves static assets (HTML, CSS, JS)
* Format: `username:password`
* Example: `admin:secure_password_here`

## Authentication endpoint

To complete the authentication flow, your application must implement the following endpoint that receives authentication requests from the middleware.

### POST /api/auth/login

Request

```http
POST /api/auth/login
Content-Type: application/json
```

Request Body:

```json
{
  "email": "user@example.com",
  "iotDbUrl": "postgresql://role_user:password@db.example.com:5432/iot_database",
  "userDbUrl": "postgresql://role_dashboard_studio:password@db.example.com:5432/user_database",
  "role": "admin"
}
```

| Field       | Type   | Description                                                                           |
| ----------- | ------ | ------------------------------------------------------------------------------------- |
| `email`     | string | User's email address from the session                                                 |
| `iotDbUrl`  | string | PostgreSQL connection string for IoT database (role ending with `user`)               |
| `userDbUrl` | string | PostgreSQL connection string for user database (role ending with `_dashboard_studio`) |
| `role`      | string | User role (default: `admin`, configurable via `DEFAULT_ROLE` env)                     |

Response

Success Response (200 OK):

```json
{
  "success": true,
  "user": {
    "id": "fd3ed43c-9b98-44e9-9ce5-f502a738ab97",
    "email": "user@example.com",
    "role": "admin"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

| Field        | Type    | Description                                  |
| ------------ | ------- | -------------------------------------------- |
| `success`    | boolean | Must be `true` for successful authentication |
| `user.id`    | string  | Unique user identifier (UUID recommended)    |
| `user.email` | string  | User's email address                         |
| `user.role`  | string  | User's role                                  |
| `token`      | string  | JWT token for subsequent API requests        |

Error Response (4xx/5xx):

```json
{
  "success": false,
  "error": "Error message describing the failure"
}
```

## JWT Token Requirements

### Token Creation

Your application must generate a JWT token with the following payload structure:

```json
{
  "userId": "fd3ed43c-9b98-44e9-9ce5-f502a738ab97",
  "email": "user@example.com",
  "role": "admin",
  "iat": 1764664049,
  "exp": 1764750449
}
```

| Field    | Type   | Required | Description                                        |
| -------- | ------ | -------- | -------------------------------------------------- |
| `userId` | string | Yes      | Unique user identifier                             |
| `email`  | string | Yes      | User's email address (used for session validation) |
| `role`   | string | Yes      | User's role                                        |
| `iat`    | number | Yes      | Issued at timestamp (Unix seconds)                 |
| `exp`    | number | Yes      | Expiration timestamp (Unix seconds)                |

{% hint style="danger" %}
The `email` field is critical for session validation. The middleware compares this email with the email from the user's session to detect if a different user is attempting to reuse a cached token.
{% endhint %}

### Token Signing

* Use HS256 (HMAC-SHA256) or RS256 (RSA-SHA256) algorithm
* Recommended expiration: 24 hours (`exp = iat + 86400`)
* The middleware does **not** verify the token signature; it only decodes and checks expiration

### Token Validation by Middleware

The middleware validates tokens by:

1. Expiration Check: Token `exp` must be in the future (with 30-second buffer)
2. Email Match: Token `email` must match the session user's email (case-insensitive)

## Token Storage (Client-Side)

The middleware stores the JWT token in the browser's `localStorage`:

```javascript
// After successful authentication
localStorage.setItem('auth_token', token)

// To retrieve the token
const token = localStorage.getItem('auth_token')

// To clear the token (logout)
localStorage.removeItem('auth_token')
```

Storage Key

| Key          | Value            |
| ------------ | ---------------- |
| `auth_token` | JWT token string |

## API Request Authorization

For /api/\* Routes

All requests to paths starting with `/api/` will include the JWT token as a Bearer token:

```http
GET /api/your-endpoint
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Your API endpoints should:

1. Extract the Bearer token from the `Authorization` header
2. Verify the token signature (using your secret key)
3. Check token expiration
4. Use the decoded payload for user identification

Example (Node.js/Express):

```javascript
import jwt from 'jsonwebtoken'

function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' })
  }

  const token = authHeader.slice(7)
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET)
    req.user = decoded
    next()
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' })
  }
}
```

For Static Assets and Other Routes

Non-API routes (HTML, CSS, JS, images) are proxied with Basic Authentication from the middleware's environment:

```http
GET /assets/app.js
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

This is configured via the `DASHBOARD_BASIC_AUTH` environment variable in the middleware.

## Using Database Connection Strings

### IoT Database URL (iotDbUrl)

The `iotDbUrl` provides a PostgreSQL connection string for the IoT database with a role that has read access to IoT data.

Format:

```
postgresql://[role_name]:[password]@[host]:[port]/[database]
```

Example usage (Node.js with pg):

```javascript
import { Pool } from 'pg'

// During authentication, store the connection URL
const iotDbUrl = requestBody.iotDbUrl

// Create a connection pool
const iotPool = new Pool({
  connectionString: iotDbUrl,
  ssl: { rejectUnauthorized: false }
})

// Execute queries
const result = await iotPool.query('SELECT * FROM telemetry WHERE device_id = $1', [deviceId])
```

### User Database URL (userDbUrl)

The `userDbUrl` provides a PostgreSQL connection string for user-specific data with Dashboard Studio role permissions.

Example usage:

```javascript
import { Pool } from 'pg'

const userPool = new Pool({
  connectionString: userDbUrl,
  ssl: { rejectUnauthorized: false }
})

// Store user preferences, dashboards, etc.
await userPool.query(
  'INSERT INTO user_dashboards (user_id, config) VALUES ($1, $2)',
  [userId, dashboardConfig]
)
```

Security Considerations

* Never expose database URLs to the client/browser
* Store connection URLs securely in server memory or encrypted storage
* Use connection pooling to manage database connections efficiently
* Consider setting connection timeouts to prevent resource exhaustion

## Complete Integration Example

{% stepper %}
{% step %}
#### Implement Auth Endpoint

```javascript
// /api/auth/login.js (Node.js/Express)
import jwt from 'jsonwebtoken'
import { v4 as uuidv4 } from 'uuid'

app.post('/api/auth/login', async (req, res) => {
  const { email, iotDbUrl, userDbUrl, role } = req.body

  // Validate required fields
  if (!email || !iotDbUrl || !userDbUrl) {
    return res.status(400).json({
      success: false,
      error: 'Missing required fields'
    })
  }

  // Create or find user in your system
  let user = await findUserByEmail(email)
  if (!user) {
    user = await createUser({
      id: uuidv4(),
      email,
      role: role || 'user'
    })
  }

  // Store database URLs for this user's session
  await storeUserDbCredentials(user.id, { iotDbUrl, userDbUrl })

  // Generate JWT token
  const token = jwt.sign(
    {
      userId: user.id,
      email: user.email,
      role: user.role
    },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  )

  res.json({
    success: true,
    user: {
      id: user.id,
      email: user.email,
      role: user.role
    },
    token
  })
})
```
{% endstep %}

{% step %}
#### Protect API Routes

```javascript
// Middleware to verify JWT on API routes
app.use('/api', (req, res, next) => {
  // Skip auth endpoint
  if (req.path === '/auth/login') return next()

  const authHeader = req.headers.authorization
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Unauthorized' })
  }

  try {
    const token = authHeader.slice(7)
    const decoded = jwt.verify(token, process.env.JWT_SECRET)
    req.user = decoded
    next()
  } catch {
    return res.status(401).json({ error: 'Invalid token' })
  }
})
```
{% endstep %}

{% step %}
#### Use Database Connections

```javascript
// API endpoint that queries IoT database
app.get('/api/devices/:deviceId/telemetry', async (req, res) => {
  const { deviceId } = req.params
  const userId = req.user.userId

  // Retrieve stored database credentials
  const { iotDbUrl } = await getUserDbCredentials(userId)
  
  const pool = new Pool({ connectionString: iotDbUrl })
  
  try {
    const result = await pool.query(
      'SELECT * FROM telemetry WHERE device_id = $1 ORDER BY timestamp DESC LIMIT 100',
      [deviceId]
    )
    res.json(result.rows)
  } finally {
    await pool.end()
  }
})
```
{% endstep %}
{% endstepper %}

## Checklist

Before integrating with App Connect, ensure your application:

* [ ] Implements `POST /api/auth/login` endpoint
* [ ] Accepts `email`, `iotDbUrl`, `userDbUrl`, and `role` in request body
* [ ] Returns `{ success: true, user: {...}, token: "..." }` on success
* [ ] Generates JWT with required fields (`userId`, `email`, `role`, `iat`, `exp`)
* [ ] Protects API routes with Bearer token authentication
* [ ] Securely stores and uses database connection strings
* [ ] Handles Basic Auth for static assets (if served from same origin)

## Troubleshooting

<details>

<summary>"Token does not match current session"</summary>

This error occurs when the `email` in the cached JWT token doesn't match the email of the current session user. This typically happens when:

* A different user logs in on the same browser
* The session expired and a new session was created

Solution: The middleware automatically handles this by removing the old token and requesting fresh authentication.

</details>

<details>

<summary>"Authentication failed"</summary>

The middleware received a non-success response from your `/api/auth/login` endpoint.

Check:

* Your endpoint returns `{ success: true, ... }` on success
* Your endpoint returns a valid JWT in the `token` field
* Your endpoint doesn't throw unhandled errors

</details>

<details>

<summary>API requests return 401</summary>

Check:

* The client is sending the `Authorization: Bearer <token>` header
* Your API middleware correctly extracts and verifies the token
* The token hasn't expired

</details>

## Version History

| Version | Date       | Changes                        |
| ------- | ---------- | ------------------------------ |
| 1.0     | 2025-12-23 | Initial contract documentation |
