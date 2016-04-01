#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap
import credentials

api = Skytap.SkytapAPI(credentials.api_user, credentials.api_key)

code, json = api.getTemplates()
if(json):
  for template in json:
    print(template['name'], template['region'], template['svms'])
