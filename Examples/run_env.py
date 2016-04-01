#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap
import credentials

api = Skytap.SkytapAPI(credentials.api_user, credentials.api_key)

status_code, json = api.changeEnvironmentState(sys.argv[1], "running")

print("Result: "+str(status_code))
