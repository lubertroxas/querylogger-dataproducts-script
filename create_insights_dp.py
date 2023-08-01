import json
import sys
import dp_openapi as dp
import argparse
import urllib3
from datetime import datetime


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config_file', required=True, help='Path to config file script will use')
parser.add_argument('-e', '--export_file', help='Path to export file', default = f"export_domains_{(datetime.now()).strftime('%m%d%Y_%H%M%S')}.json")

args = parser.parse_args()

c = open(args.config_file)
configs = json.load(c)
api_client = dp.create_api_client(configs)
domainId = None

### 1. Get Domain ID or Create based on configs### 

if configs.get("createDomain"):
    ### Run create domain
    print(f"Creating domain {configs.get('domain').get('domainName')}")
    domain = dp.create_domain(api_client, configs)
    domainId = domain.id
else:
    ### Get domain id based on domain name 
    print(f"Finding domain id for {configs.get('domain').get('domainName')}")

    domains = dp.get_domains(api_client)
    domainName = configs.get("domain").get("domainName")
    for i in domains: 
        if i.name == domainName:
            domainId = i.id 

if domainId is None:
    print("Script execution failed. Domain does not exist. Create the specified domain in config.json or set the createDomain flag to true.")
    sys.exit(1)

### 2. Form Payload for Creation of Insights DP ### 
dataProduct = dp.create_dataproduct(api_client, configs, domainId)

if dataProduct is None:
    print("Script execution failed. Failed to create Data Product correctly. Check Data Products page, delete and try again.")
    sys.exit(1)
else: 
    print("Data Product creation completed.")

### 3. Call publish if publish flag is true

if configs.get("publishDataProduct") is True:
    dpId = dataProduct.id 
    dataPublishDp = dp.publish_dataproduct(api_client, configs, dpId)
else: 
    print("Data product creation script completed.")
    sys.exit(0)

if(dataPublishDp.status == 'COMPLETED'):
    print("Data product publishing completed.")
    sys.exit(0)
else:
    print("Encountered the following errors publishing the data product:")
    for i in dataPublishDp.errors:
        print(f"{i.entity_type}: {i.entity_name}: Message: {i.message} ")
    print("Data product creation script completed with errors.")
    sys.exit(len(dataPublishDp.errors))



