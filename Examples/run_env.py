#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap

api = Skytap.SkytapAPI('bcoleman_solo', '01ba4318b714bc11744f4c88b5c95c400f5d4c4c')

status_code, json = api.changeEnvironmentState(sys.argv[1], "running")

print("Result: "+str(status_code))