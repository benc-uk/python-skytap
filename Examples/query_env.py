#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap
from pprint import pprint
import credentials

api = Skytap.SkytapAPI(credentials.api_user, credentials.api_key)
status_code, json = api.getEnvironment(sys.argv[1])

print("Result: "+str(status_code))

if(status_code == 200):
    pprint(json)
else:
    print("!! Error !! Check template id and credentials")
