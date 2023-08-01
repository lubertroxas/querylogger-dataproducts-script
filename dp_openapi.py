import swagger_client
from swagger_client.rest import ApiException
import base64
import json
import string

def create_api_client(configs):
    #print("----------- create_api_client ---------------------------")
    configuration = swagger_client.Configuration()
    configuration.host = configs.get("url")
    configuration.verify_ssl = configs.get("verify")
    configuration.debug = configs.get("debug")
    api_client = swagger_client.ApiClient(configuration)
    creds = base64.b64encode('{}:{}'.format(configs.get("user"), configs.get("password")).encode()).decode()
    for hkey, hvalue in configs.get("headers").items():
        api_client.set_default_header(hkey, hvalue)
    api_client.set_default_header('Authorization', 'Basic {}'.format(creds))
    return api_client

def get_domains(api_client):
    api_instance = swagger_client.DomainsApi(api_client)
    try:
        #api_response = api_instance.list_roles()
        #print(api_instance.list_domains())
        return api_instance.list_domains()
    except ApiException as e: 
        print("Exception when calling DomainsApi->list_domains: %s\n" %e)
        exit(e.status) 

def create_domain(api_client, configs):
    api_instance = swagger_client.DomainsApi(api_client)
    try: 
        #print("---- call create domain API ----")
        domainData = {} 
        domainData["name"] = configs.get("domain").get("domainName")
        domainData["description"] = configs.get("domain").get("domainDescription")
        domainData["schemaLocation"] = configs.get("domain").get("domainPath")
        domainId = api_instance.create_domain(body=domainData)
        return domainId 
    
    except ApiException as e: 
        print("Exception when calling DomainsApi->create_domain: %s\n" %e)
        exit(e.status) 


def create_dataproduct(api_client, configs, domainId):
    api_instance = swagger_client.DataProductsApi(api_client)
    try: 
        #print("------- call create data product API ---------\n")
        dpBody = configs.get('dataProduct')
        dpBody['owners'][0]['name'] = configs.get('dpOwnerName') 
        dpBody['owners'][0]['email'] = configs.get('dpOwnerEmail') 
        dpBody['dataDomainId'] = domainId
        dpBody['catalogName'] = configs.get('dpCatalogName')

        catalogSchema = configs.get('insightsCatalogName') + '.' + configs.get('insightsSchemaName')

        #### Update SQL queries with catalog and schema ####
        for i in dpBody['views']:
            i['definitionQuery'] = i['definitionQuery'].replace('##InsightsCatalog##.##InsightsSchema##', catalogSchema)

        dp = api_instance.create_data_product(body=dpBody)
        return dp
    
    except ApiException as e:
        print("Exception when calling DataProductsAPI->create_data_product: %s\n" %e)
        exit(e.status)


def publish_dataproduct(api_client, configs, dpId):
    api_instance = swagger_client.WorkflowsApi(api_client)
    
    try: 
        dpForce = configs.get('forceRepublish')
        publishDp = api_instance.publish_data_product(data_product_id=dpId, force=dpForce)
    except ApiException as e:
        print("Exception when calling DataProductsAPI->publish_data_product: %s\n" %e)
        exit(e.status)

    try:
        dpPublishStatus = api_instance.get_publish_data_product_status(data_product_id=dpId)
        while dpPublishStatus.is_final_status is False:
            dpPublishStatus = api_instance.get_publish_data_product_status(data_product_id=dpId)
            print("Data Product Publishing in progress...")
        return dpPublishStatus

    except ApiException as e:
        print("Exception when calling DataProductsAPI->get_publish_data_product_status: %s\n" %e)
        exit(e.status)
