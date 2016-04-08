#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap
import credentials

api = Skytap.SkytapAPI(credentials.api_user, credentials.api_key)
status_code, json = api.getEnvironmentPubSets(sys.argv[1])

print("Result: "+str(status_code))
if(status_code == 200):
    for pubset in json:
        print("==========================================")
        print("Published set: '"+pubset['name']+"'")
        vms = pubset['vms']
        for vm in vms:
            print(vm['name'] + "\n  * " + vm['desktop_url'])
else:
    print("!! Error !! Check template id and credentials")
