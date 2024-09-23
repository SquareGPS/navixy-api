# Working with Check-ins

In Navixy, check-ins are a feature used to record and report the location and status of employees in the field. They allow employees to send real-time updates about their location, accompanied by additional data such as forms, photos, and comments. These check-ins can be used for various purposes, including verifying task completion, providing updates on job progress, and collecting field data. Check-ins are typically created using the X-GPS Tracker mobile app and can be integrated into workflows to ensure accurate and timely information from field employees.

!!! note "Check-ins are normally created using X-GPS Tracker mobile app. The description below is necessary only for non-standard use, such as creating your own Mobile Tracker app that works with the Navixy platform."

To create check-ins in the Navixy platform, follow these steps:

## Step 1: Create a Form from a Template
Use the [`checkin/form/create`](../../resources/field_service/checkin.md#formcreate) API call to create a form based on a template. In the X-GPS Tracker, the form is created when the template is selected by a user.

## Step 2: Create Files for Photos
Use the [`checkin/image/create`](../../resources/field_service/checkin.md#imagecreate) API call to create files for check-in photos and upload the photo data. In the X-GPS Tracker, check-in photos are created as each photo is added.

## Step 3: Create Form Files
Use the [`checkin/form/file/create`](../../resources/field_service/checkin.md#formfilecreate) API call to create form files and upload their data. In the X-GPS Tracker, form files are created when they are added while filling out the form.

## Step 4: Create the Check-in
Use the [`checkin/create`](../../resources/field_service/checkin.md#create) API call to create the check-in, attaching all the necessary data. If the form includes optional fields that should be left empty for your check-in, simply refrain from adding these fields to the form submission object.

## File Upload Process

Here's how to upload files to the platform. If you have multiple files to upload, add a brief delay between each upload to ensure a smooth process.

Using the API calls `checkin/image/create` and `checkin/form/file`, the app requests permission to upload a file. The platform responds with the location and token for the file upload.

### Internal Storage Example

The platform provides the location and token for the file upload:

```json
{
  "success": true,
  "value": {
    "file_id": 111,
    "url": "http://example.org/upload",
    "expires": "2020-02-03 03:04:00",
    "file_field_name": "example.png",
    "fields": {
      "token": "a43f43ed4340b86c808ac"
    }
  }
}
```

Upload the file using the provided URL and token:

```http
POST /upload HTTP/1.1
Host: example.org
Content-Length: 1325
Origin: http://example.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryePkpFF7tjBAqx29L

------WebKitFormBoundaryePkpFF7tjBAqx29L
Content-Disposition: form-data; name="token"

a43f43ed4340b86c808ac
------WebKitFormBoundaryePkpFF7tjBAqx29L
Content-Disposition: form-data; name="example.png"; filename="example.png"
Content-Type: image/png

... contents of file go here ...
------WebKitFormBoundaryePkpFF7tjBAqx29L--
```

### Amazon S3 Example

For the Cloud version of the platform using Amazon S3:

```json
{
  "success": true,
  "value": {
    "file_id": 111,
    "url": "https://example.s3.amazonaws.com/",
    "expires": "2020-02-03 03:04:00",
    "file_field_name": "file",
    "fields": {
      "policy": "<Base64-encoded policy string>",
      "key": "user/user1/${filename}",
      "success_action_status": "200",
      "x-amz-algorithm": "AWS4-HMAC-SHA256",
      "x-amz-credential": "AKIAIOSFODNN7EXAMPLE/20151229/us-east-1/s3/aws4_request",
      "x-amz-date": "20151229T000000Z",
      "x-amz-signature": "<signature-value>",
      "x-amz-server-side-encryption": "AES256",
      "content-type": "image/png"
    }
  }
}
```

Upload the file using the provided URL and fields:

```http
POST / HTTP/1.1
Host: example.s3.amazonaws.com
Content-Length: 1972
Origin: https://example.s3.amazonaws.com/
Content-Type: multipart/form-data; boundary=WebAppBoundary

--WebAppBoundary
Content-Disposition: form-data; name="policy"
Content-Type: text/plain

<Base64-encoded policy string>
--WebAppBoundary
Content-Disposition: form-data; name="key"
Content-Type: text/plain

user/user1/actual_file_name.png
--WebAppBoundary
Content-Disposition: form-data; name="success_action_status"
Content-Type: text/plain

200
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-algorithm"
Content-Type: text/plain

AWS4-HMAC-SHA256
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-credential"
Content-Type: text/plain

AKIAIOSFODNN7EXAMPLE/20151229/us-east-1/s3/aws4_request
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-date"
Content-Type: text/plain

20151229T000000Z
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-signature"
Content-Type: text/plain

<signature-value>
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-server-side-encryption"
Content-Type: text/plain

AES256
--WebAppBoundary
Content-Disposition: form-data; name="file"; filename="actual_file_name.png"
Content-Type: image/png

... contents of file go here ...
--WebAppBoundary--
```