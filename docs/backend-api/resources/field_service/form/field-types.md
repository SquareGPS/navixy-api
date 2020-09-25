---
title: Form field types
description: Form field types
---

# Form fields and values

Every form (and form template) contains an ordered list of fields of various types. 
Field type defines how user input elements will look like, and how user input will be validated.

Every field has a set of common parameters, which are the same for all field types, and type-specific parameters, 
which define specific style and validation constraints. Both common and type-specific parameters are contained as fields in the JSON object.

Field values for submitted form are stored separately as JSON objects. The contents of value JSON objects are entirely 
field type-specific.

##### common field parameters:

```json
{
   "id": "111-aaa-whatever", //arbitrary alphanumeric string (1 to 19 characters), unique across current form’s fields, used to link with values and its "parent" in template form
   "label": "Name", //user-defined label, shown as field header, 1 to 100 printable characters
   "description": "Your full name", //field description, shown in smaller text under the header, 1 to 512 printable characters
   "required": true, //if true, form cannot be submitted without filling this field with valid value
   "type": "text", //determines field type
   //type-specific parameters go here...
}
```

### Text field

**type**: text

Multiline auto-expanding text field

**Note 1:** when value contains empty string, it’s considered empty, and thus valid when `required: false, min_length != 0`  
**Note 2:** combination `required: true, min_length: 0` is not allowed

##### type-specific parameters:

         "min_length": 5, //minimum allowed length, from 0 to 1024
         "max_length": 255 //maximum allowed length 1 to 1024
    

##### value object:

```json
{
    "type": "text",
    "value": "text field value" //What was entered in the text field
}
```

### Checkbox group

**type**: checkbox_group

Group of checkboxes.

**Note 1:** when zero checkboxes are selected, values is considered empty, and thus valid when `required: false, min_checked != 0`  
**Note 2:** combination `required: true, min_checked: 0` is not allowed

##### type-specific parameters:

        "min_checked": 0, //minimum allowed checked positions, 0 to "group".size - 1
        "max_checked": 3, //maximum allowed checled positions. 1 to "group".size - 1
        "group": [
            {
               "label" : "I agree to TOS"
            }
         ]
    

##### value object:

```json
{
    "type": "checkbox_group",
    "values": [true] //booleans in the same order as fields in "group"
}
```

### Dropdown field

**type**: dropdown

Dropdown menu for choosing one option.

##### type-specific parameters:

        "options": [
            {
               "label" : "John"
            },
            {
               "label" : "Alice"
            }
         ]
    

##### value object:

```json
{
    "type": "dropdown",
    "value_index": 1 //zero-based index of value from "options"
}
```

### Radio button group

**type**: radio_group

A group of radio buttons. Only one option is selectable.

##### type-specific parameters:

        "options": [
            {
               "label" : "John"
            },
            {
               "label" : "Alice"
            }
         ]
    

##### value object:

    {
        "type": "radio_group",
        "value_index": 1 //zero-based index of value from "options"
    }
    

### Date picker

**type**: date

A date picker

##### type-specific parameters:

        "disable_future": false,  //if true, date from the future cannot be selected
        "disable_past": true,  //if true, date from the past cannot be selected
    

##### value object:

    {
        "type": "date",
        "value": "2017-03-14"  //date string
    }
    

### Rating

**type**: rating

Rating with “stars”. Zero stars are not allowed.

##### type-specific parameters:

        "max_stars": 5  //max number of stars to select from
    

##### value object:

    {
        "type": "rating",
        "value": 3  //number of stars selected. Cannot be more than "max_stars"
    }
    

### File

**type**: file

File attachment, for example document or spreadsheet.

##### type-specific parameters:

        "max_file_size": 65536,  //max file size, bytes, no more than 16 mbytes
        "min_file_size": 128,  //minimum file size, bytes
        "allowed_extensions": ["xls", "doc"] //list of allowed file extensions, up to 16 items, cannot be empty, but can be null, which means "no extension limits"
    

##### value object:

    {
        "type": "file",
        "file_ids": [3345345]  //ids of the file which should be attahced to this form field as value. Files must be uploaded before form submission
    }
    

### Photo

**type**: photo

Photograph attachment.

##### type-specific parameters:

        "max_files": 2 //maxumum number of photos to attach, up to 6 
    

##### value object:

    {
        "type": "photo",
        "file_ids": [3345345, 534534534]  //ids of the files which should be attahced to this form field as value. Files must be uploaded befre form submission. Only image files are allowed.
    }
    

### Signature

**type**: signature

A small image of customer’s signature (usually obtained via writing on screen with stylus)

##### type-specific parameters:

        //none
    

##### value object:

    {
        "type": "file",
        "file_id": 3345345  //id of the file which should be attached to this form field as value. File must be uploaded befre form submission
    }
    

### Separator

**type**: separator

Cosmetic, just to show header. Doesn’t contain any actual value. Always filled and valid. Cannot be required.