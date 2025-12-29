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

Your application must implement a specific auth endpoint and handle JWT tokens according to this contract.

## Required API Endpoint

### POST /api/auth/login

Your application **must** implement this endpoint to receive authentication requests from the middleware.

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
&#x20;The `email` field is critical for session validation. The middleware compares this email with the email from the user's session to detect if a different user is attempting to reuse a cached token.
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
### Implement Auth Endpoint

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
### Protect API Routes

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
### Use Database Connections

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
