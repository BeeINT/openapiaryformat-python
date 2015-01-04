#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This example covers a very basic example implementation on how to create
# a valid ouput in the openapiaryformat. 

# This is more or less basic python object and json handling and can 
# hopefully get beginner going.

import json



apiaries = []

apiary1 = {
	"name" : "My First Apiary",
	"type" : "apiary",
	"description": "This was the initial Apiary"
}
apiaries.append(apiary1)

apiary2 = {
	"name" : "The Second One",
	"type" : "apiary",
	"description" : "",
}
apiary2["location"] =  {
      "latitude": 50.0724825,
      "longitude": 8.2483534
    },
apiaries.append(apiary2)



output_string = json.dumps(apiaries,  encoding="utf-8", indent=2)
print "--------------Generated Data-----------------"
print output_string
print "---------------------------------------------\n"


apiaries_loaded = json.loads(output_string)
print "----------------Loaded Data------------------"
print apiaries_loaded
print "---------------------------------------------\n"


print "--------------Iterating Data-----------------"
for apiary in apiaries_loaded:
	print apiary["name"]
print "---------------------------------------------\n"




