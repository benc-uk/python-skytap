#!/usr/local/bin/python3

import sys
sys.path.append("..")
from Skytap import Skytap

api = Skytap.SkytapAPI('bcoleman_solo', '01ba4318b714bc11744f4c88b5c95c400f5d4c4c')

VM_TEMPLATE_ID = '771869'
ENV_ID = sys.argv[1]

new_vms_list = []

for server_loop in range(0, int(sys.argv[2])):
    status_code, json = api.addTemplateToEnv(ENV_ID, VM_TEMPLATE_ID)
    vms_count = len(json['vms'])
    vm = json['vms'][vms_count - 1]
    print("API result: "+str(status_code)+" - New VM '"+vm['id']+"' was deployed")
    new_vms_list.append(vm['id'])

status_code, json = api.changeVMStateMulti(ENV_ID, new_vms_list, 'running')
quit()
