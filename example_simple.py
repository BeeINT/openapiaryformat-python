#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This example covers a very basic example implementation on how to create
# a valid ouput in the openapiaryformat. 

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
	"description" : ""
}
apiaries.append(apiary2)



print json.dumps(apiaries,  encoding="utf-8", indent=2)
