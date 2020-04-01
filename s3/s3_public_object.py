# Trigger on S3 object put request events

import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
        bucketName = event['Records'][0]['s3']['bucket']['name']
        fileName = event['Records'][0]['s3']['object']['key']
        objectACL = s3.ObjectAcl(bucketName, fileName)
        
        for entry in objectACL.grants:
                try:
                        if entry['Grantee']['URI'] == "http://acs.amazonaws.com/groups/global/AllUsers":
                                print("Instance of public access found, overwriting object permissions to private")
                                objectACL.put(ACL='private')
                except:
                        print("Non-URI style grantee encountered (not a public grantee), ignoring")
