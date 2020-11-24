# Quick and dirty Python script to get a list of disks and if they are thin provisioned or not. Search for "replace" to find which values you need to replace.
# Use against the Prism/Prism Element 2.0 REST API
# Created by Bas Raayman - bas@nutanix.com

# Import modules
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import sys

pe_ip="replace_with_cluster_ip"
# Set values for the REST headers
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

# Create the REST request and pass parameters
auth=HTTPBasicAuth('replace_with_username_here', 'replace_with_password_here')
r = requests.get("https://{}:9440/PrismGateway/services/rest/v2.0/vms/?include_vm_disk_config=true".format(pe_ip),
           auth=auth,
           verify=False)

# Check if the REST call came back with an HTTP status code that indicates succes and load the result into a python dictionary, otherwise bubble up the error
if r.ok:
  # Load the request and create a Python dictionary using the json values. This leverages the json Python library
  result = json.loads(r.content)
	print("Succesful REST call returned status: {}".format(r.status_code))
else:
	print("Error in PUT /vms/{} - {}".format(vm_uuid, r.status_code))
  sys.exit()

# Print the disks filtered for thin provisioned
for i in range(len(result['entities'])):
        print("VM name              : ",result['entities'][i]['name'])
        print("thin provisioned disk: ",result['entities'][i]['vm_disk_info'][i]['is_thin_provisioned'])
        
