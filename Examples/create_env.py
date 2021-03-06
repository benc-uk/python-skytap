#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap
import credentials

api = Skytap.SkytapAPI(credentials.api_user, credentials.api_key)
status_code, json = api.createEnvironment(sys.argv[1], sys.argv[2])

print("Result: "+str(status_code))

if(status_code == 200):
    print(json['description']+"' has been created: "+json['id'])
else:
    print("!! Error !! Check template id and credentials")
