import json
import os
import boto3


s3 = boto3.resource('s3')

def lambda_handler(event, context):
        filename = event['Records'][0]['s3']['object']['key']
        filetype = os.path.splitext(filename)[1]
        
        print("The object filetype is ", filetype)
        
        
        
        s3bucket = event['Records'][0]['s3']['bucket']['name']
        s3key = filename
        
        s3object = s3.Object(s3bucket, s3key)
        s3object.delete()
        
        #s3object = event['Records'][0]
    #return(json.dumps("test"))
    
    #return()
"""
    return {
        
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    bucket_key = event['bucket_key']
    body = event['body']

    put_object_into_s3(bucket_name, bucket_key, body)
    get_object_from_s3(bucket_name, bucket_key)

# Define subsegments manually
def put_object_into_s3(bucket_name, bucket_key, body):
    try:
        xray_recorder.begin_subsegment('put_object')
        response = s3_client.put_object(Bucket=bucket_name, Key=bucket_key, Body=body)
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        
"""
