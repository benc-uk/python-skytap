import requests
import json
import sys, traceback

# API endpoint for Skytap REST API
API_BASE = 'https://cloud.skytap.com/'

class SkytapAPI:
    def __init__(self, username, token):
        self.headers = {'accept': 'application/json', 'content-type': 'application/json'}
        self.auth = (username, token)

    #
    #  Fetch a list of all my templates
    #  GET https://cloud.skytap.com/v2/templates
    #
    def getTemplates(self):
        return self.__restCall('GET', '/v2/templates?scope=me')

    #
    #  Deploy new environment from a template
    #  POST https://cloud.skytap.com/v1/configurations
    #
    def createEnvironment(self, template_id, name=None):
        json_dict = {"template_id": template_id}
        if(name != None):
            json_dict['name'] = name
        return self.__restCall('POST', '/v1/configurations', data=json.dumps(json_dict))

    #
    #  Get environment details
    #  GET https://cloud.skytap.com/v2/configurations
    #
    def getEnvironment(self, env_id):
        return self.__restCall('GET', '/v2/configurations/'+str(env_id))

    #
    #  Get VM details
    #  GET https://cloud.skytap.com/v2/configurations/{id}/vms/{id}
    #
    def getVM(self, env_id, vm_id):
        return self.__restCall('GET', '/v2/configurations/'+str(env_id)+'/vms/'+vm_id)

    #
    #  Add server(s) to existing environment
    #  PUT https://cloud.skytap.com/v1/configurations
    #
    def addTemplateToEnv(self, env_id, template_id):
        json_dict = {"template_id": template_id}
        return self.__restCall('PUT', '/v1/configurations/'+str(env_id), data=json.dumps(json_dict))

    #
    #  Change environment run state; stop / start / suspend / resume
    #  PUT https://cloud.skytap.com/v2/configurations
    #
    def changeEnvironmentState(self, env_id, state):
        json_dict = {"runstate": state}
        return self.__restCall('PUT', '/v2/configurations/'+str(env_id), data=json.dumps(json_dict))

    #
    #  Change VM run state; stop / start / suspend / resume
    #  PUT https://cloud.skytap.com/v2/configurations/{id}/vms/{id}
    #
    def changeVMState(self, env_id, vm_id, state):
        json_dict = {"runstate": state}
        return self.__restCall('PUT', '/v2/configurations/'+str(env_id)+'/vms/'+str(vm_id), data=json.dumps(json_dict))

    #
    #  Change multiple VM run states; stop / start / suspend / resume
    #  PUT https://cloud.skytap.com/v2/configurations/{id}
    #
    def changeVMStateMulti(self, env_id, vm_id_list, state):
        json_dict = {"runstate": state, "multiselect": vm_id_list}
        return self.__restCall('PUT', '/v2/configurations/'+str(env_id), data=json.dumps(json_dict))

    #
    #  Create ICNR tunnel between two networks
    #  PUT https://cloud.skytap.com/v2/tunnels
    #
    def createICNR(self, source_net_id, target_net_id):
        json_dict = {"source_network_id": source_net_id, "target_network_id": target_net_id}
        return self.__restCall('POST', '/v2/tunnels/', data=json.dumps(json_dict))

    #
    #  Basic REST call to Skytap API
    #
    def __restCall(self, method, path, data=None):
        try:
            if(method == 'GET'):
                result = requests.get(API_BASE + path, headers=self.headers, auth=self.auth)
            if(method == 'POST'):
                result = requests.post(API_BASE + path, headers=self.headers, auth=self.auth, data=data)
            if(method == 'PUT'):
                result = requests.put(API_BASE + path, headers=self.headers, auth=self.auth, data=data)

            if result.status_code != requests.codes.ok:
                return result.status_code, None
            else:
                return result.status_code, result.json()
        except:
            traceback.print_exc()
            return -1, None
