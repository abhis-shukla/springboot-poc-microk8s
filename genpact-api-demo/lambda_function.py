
import json
import boto3
import csv

def lambda_handler(event, context):
    error = None
    try: 
        print("event printing")
        #import pprint 
        #pprint.pprint(event)
        #print(event)
        #print(context)
        #print("Hello")
    
        request_name = event['context']['resource-path']
        print(request_name ,"request_name")
        print("Hello1")
        # request_method = event[context][http-method]
        
        request_method = event['context']['http-method']
        print(request_method)
        # print(request_name, "resource_new")
        
        
        request_query_parameters = event['params']['querystring']
        # request_query_parameters = event['queryStringParameters'] 
        print(request_query_parameters)
        #read the configuration file to get the metadata of the requested resource
        config_file = open('./config.json',) 
        parameter_json_contents = json.load(config_file)
        try:
            input_config = parameter_json_contents[request_name]
            print(input_config)
            s3 = boto3.resource('s3')
            BUCKET_NAME = 'aws-coe'
            key = 'api-gateway-poc/covid-fci-data.csv'
            local_file_name = '/tmp/covid-fci-data.csv'
            s3.Bucket(BUCKET_NAME).download_file(key, local_file_name)
            data = []
            with open(local_file_name, encoding='ISO-8859-1') as csvf:
                csvReader = csv.DictReader(csvf)
                for rows in csvReader: 
                    jsonStr = json.dumps(rows)
                    data.append(jsonStr)
            returnVal = []
            for x in data:
                y = json.loads(x)
                finaldict = {}
                if y["Country"] == request_query_parameters["Country"]:
                    print("%s--%s" % (y["Country_Code"],y["Termination_Date"]))
                    finaldict["Country_Code"] = y["Country_Code"]
                    finaldict["Termination_Date"] = y["Termination_Date"]
                    returnVal.append(finaldict)
            return returnVal

        except Exception as ERROR:
            print("Connection Issue: " , ERROR)
            return " is not configured in DEP"
        for input in input_config:
            v_query_parameters = input['query_parameters']
            v_response_col_names = input['response_col_names']
    except Exception as ERROR:
        print("Connection Issue: " , ERROR)
        return " API is not working"
