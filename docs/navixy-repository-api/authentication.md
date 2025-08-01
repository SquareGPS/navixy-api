# Authenticationx

Authentication is required for all API requests and is based on OAuth 2.0.

### Authentication environments

#### **Base URLs**

<table><thead><tr><th width="182.60003662109375">Region</th><th>Base URL</th><th>Data Location</th></tr></thead><tbody><tr><td>Europe</td><td><code>https://keycloak.navixy.com</code></td><td>European data centers</td></tr><tr><td>Americas</td><td><code>https://keycloak.us.navixy.com</code></td><td>US-based data centers</td></tr></tbody></table>

{% hint style="warning" %}
Note that in this and other articles about Navixy Repository API, {AUTH\_BASE\_URL} is a placeholder for the URL you'll be using.
{% endhint %}

### Organization-based access control

All API requests are automatically scoped to your organization. Your access token determines the organization context. You cannot access resources belonging to other organizations.

#### How organization scoping works

1. When you authenticate, your access token contains your organization identifier.
2. The API automatically extracts this identifier from your token.
3. All operations are restricted to your organization's resources.
4. No manual organization specification is required in API calls.

### Acquiring an access token

Navixy Repository API supports the OAuth2 Authorization Code Flow.

**Prerequisites**

Before you begin, ensure you have:

* Valid Navixy Repository API credentials (`client_id` and `client_secret`).
* A registered Callback URL (Redirect URI): The specific URL in your application where users will be redirected after granting consent.
* Authentication server URL ({AUTH\_BASE\_URL}), determined depending on your geographical location. For information about {AUTH\_BASE\_URL}, see [Authentication environments](authentication.md#authentication-urls).
* A secure method to generate and validate the `state` parameter for Cross-Site Request Forgery (CSRF) protection.

{% stepper %}
{% step %}
**Redirect the user to the authorization endpoint:**

```bash
curl -X GET "{AUTH_BASE_URL}/realms/users/protocol/openid-connect/auth" \
  --data-urlencode 'client_id=<YOUR_CLIENT_ID>' \
  --data-urlencode 'response_type=code' \
  --data-urlencode 'redirect_uri=https://<YOUR_APP_CALLBACK_URL>' \
  --data-urlencode 'scope=<REQUESTED_SCOPE_ONE> <REQUESTED_SCOPE_TWO>' \
  --data-urlencode 'state=<YOUR_SECURE_RANDOM>'
```
{% endstep %}

{% step %}
**Exchange authorization code for access token**

**Request:**

```bash
curl -X POST {AUTH_BASE_URL}/realms/users/protocol/openid-connect/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "client_id": "<YOUR_CLIENT_ID>",
    "client_secret": "<YOUR_CLIENT_SECRET>",
    "code": "<YOUR_AUTHORIZATION_CODE>",
    "redirect_uri": "https://<YOUR_APP_CALLBACK_URL>"
  }'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ...signature",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "8xLOxBtZp8",
  "scope": "<REQUESTED_SCOPE_ONE> <REQUESTED_SCOPE_TWO>",
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.e...signature"
}
```

**Error example:**

```json
{
  "error": "invalid_grant",
  "error_description": "Authorization code expired"
}
```
{% endstep %}
{% endstepper %}

### Transmitting the access token

Use `access_token` to authenticate API requests:

```bash
curl -X GET {BASE_URL}/resource \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### Refreshing an access token

Access tokens have a limited lifespan and typically expire after 900 seconds. In order to maintain access without requiring the user to re-authenticate, use the refresh token provided during the initial token exchange to obtain a new access token.

**Request:**

```bash
curl -X POST {AUTH_BASE_URL}/realms/users/protocol/openid-connect/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'grant_type=refresh_token' \
  -d 'client_id=<YOUR_CLIENT_ID>' \
  -d 'client_secret=<YOUR_CLIENT_SECRET>' \
  -d 'refresh_token=<YOUR_REFRESH_TOKEN>'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ...signature",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "8xLOxBtZp8",
  "scope": "<REQUESTED_SCOPE_ONE> <REQUESTED_SCOPE_TWO>"
}
```

**Notes:**

* The new `access_token` should replace the old one in all subsequent API requests.
* A new `refresh_token` may also be issued. If so, you should update your stored token accordingly.
* If the `refresh_token` has expired or is invalid, you must re-authenticate using the full authorization code flow.

This mechanism allows long-lived sessions while minimizing user effort and maintaining security best practices.

### Revoking tokens

If an access token or refresh token needs to be invalidated (for example, when a user logs out or client credentials are rotated), it can be revoked using the OAuth2 token revocation endpoint:

```bash
curl -X POST {AUTH_BASE_URL}/realms/users/protocol/openid-connect/revoke \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "<YOUR_CLIENT_ID>",
    "client_secret": "<YOUR_CLIENT_SECRET>",
    "token": "<TOKEN_TO_REVOKE>"
  }'
```

Revoked tokens become immediately invalid and cannot be used for accessing protected resources.

### Security recommendations

* Always send tokens over HTTPS. Any requests made over plain HTTP will be rejected.
* Never expose client secrets or tokens in frontend code or public repositories.
* Access tokens are short-lived and should be refreshed or re-requested as needed.

### Using a third-party library

To simplify integration, we recommend using ready-made OAuth 2.0 client libraries:

#### For browser-based applications

**Universal**

* [**oidc-client-ts**](https://github.com/authts/oidc-client-ts) – A popular and well-maintained library for managing OAuth2 and OIDC tokens in browser apps.
* [**AppAuth-JS**](https://github.com/openid/AppAuth-JS) – Official OpenID Connect client library for JavaScript.

**For React**

* [**react-oidc-context**](https://github.com/authts/react-oidc-context) – Wrapper around the oidc-client-ts, OIDC/OAuth2 support with React Context API, highly recommended for larger apps.
* [**react-oauth2-code-pkce**](https://github.com/soofstad/react-oauth2-pkce) – Lightweight React hook for OAuth2 Authorization Code Flow.

**For Vue.js**

* [**vuex-oidc**](https://github.com/perarnborg/vuex-oidc) – Wrapper around the oidc-client-ts, integration of OIDC authentication with Vuex.

**For Angular**

* [**angular-oauth2-oidc**](https://github.com/manfredsteyer/angular-oauth2-oidc) – Popular and mature OAuth2 and OIDC library for Angular.

#### For mobile applications

* [**AppAuth-Android**](https://github.com/openid/AppAuth-Android) – OpenID Certified library for Android apps.
* [**AppAuth-iOS**](https://github.com/openid/AppAuth-iOS) – OpenID Certified library for iOS apps (Objective-C/Swift).
* [**flutter\_appauth**](https://pub.dev/packages/flutter_appauth) – Wrapper around AppAuth for Flutter applications.
* [**react-native-app-auth**](https://github.com/FormidableLabs/react-native-app-auth) – An SDK for communicating with OAuth2 providers.

#### For server-side applications

**For Java**

* [**Spring Security OAuth2 Client**](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/index.html) – Spring Security component provides comprehensive OAuth 2.0 support.
* [**ScribeJava**](https://github.com/scribejava/scribejava) – Simple OAuth library for Java

**For Kotlin**

* [**Spring Security OAuth2 Client**](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/index.html) – Spring Security component provides comprehensive OAuth 2.0 support.
* [**ktor-auth-oauth**](https://ktor.io/docs/oauth.html) – A Ktor plugin that handles authentication and authorization.

**For Python**

* [**Authlib**](https://github.com/lepture/authlib) – Universal OAuth2 and OpenID Connect client for Python.
* [**requests-oauthlib**](https://github.com/requests/requests-oauthlib) – Provides OAuth library support for Requests.

**For Node.js**

* [**openid-client**](https://github.com/panva/node-openid-client) – OAuth 2 / OpenID Connect Client API for JavaScript Runtimes.
* [**Simple OAuth2**](https://github.com/lelylan/simple-oauth2) – A simple Node.js client library for OAuth2.

**For Go**

* [**golang.org/x/oauth2**](https://pkg.go.dev/golang.org/x/oauth2) – Client implementation for OAuth 2.0 spec.
* [**coreos/go-oidc**](https://github.com/coreos/go-oidc) – A Go OpenID Connect client.

**For ASP.NET Core**

* [**Microsoft.AspNetCore.Authentication.OpenIdConnect**](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.openidconnect) – ASP.NET Core middleware that enables an application to support the OpenID Connect authentication workflow.
* [**Duende.IdentityModel.OidcClient**](https://github.com/DuendeSoftware/IdentityModel.OidcClient) – a .NET library for claims-based identity, OAuth 2.0, and OpenID Connect.

**For PHP**

* [**Laravel Socialite**](https://laravel.com/docs/socialite) – Laravel wrapper around OAuth 1 & OAuth 2 libraries.
* [**league/oauth2-client**](https://github.com/thephpleague/oauth2-client) – Easy integration with OAuth 2.0 service providers
