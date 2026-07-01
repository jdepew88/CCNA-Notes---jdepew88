JSON Notes

For machine to machine communication it important to have a standard that different applications can use to communicate with each others.

JSON data is written as name/value pairs:

* A name / value or “key/value” pair consists of a field name (in double quotes “”), followed by a colon : , followed by a value

Ex:

“Key: value”

Manufacturer: Tesla

JSON Data Types: Object

**Object**

* Unordered collection of key:value pairs
* Data surrounded by curly braces {}
* Key and value are separated by a colon, spaces don’t matter
* Each key/value pair is separated by a comma (not the last!). Trailing commas must not be used
* Use double quotes, not single quotes.
* Boolean values must be lowercase (different to Python)
* Boolean = a binary variable, having two possible values called “true” and “false.”.
* Object Example:

{“firstName”: “Joe”, “lastName”: “Depew”}

* Example2:

{

“firstName” : “Joe”,

“lastName” : “Depew”,

“domainName” : “jrtechconsult.com”

}

Note: be sure last key:value pair does not have a trailing comma0

**Array**

* Ordered list of values
* Uses Square Brackets []
* Can store multiple types
  + JSON array can store valid JSON data types, such string, number, Boolean, object, null or another array
* Values must be separated by comma.