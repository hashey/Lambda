# Trigger with S3 object creation events

import os
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
        fileName = event['Records'][0]['s3']['object']['key']
        fileType = os.path.splitext(fileName)[1]
        
        approvedFileTypes = ['.txt','.log']
        
        if fileType not in approvedFileTypes:
                try:
                        print("Automatically deleting unauthorized content  ", fileName, " - filetype ", fileType, " is not in approved list.")

                        s3bucket = event['Records'][0]['s3']['bucket']['name']
                        s3key = fileName
        
                        s3object = s3.Object(s3bucket, s3key)
                        s3object.delete()
                except:
                        print("Exception encountered attempting to delete ", fileName)
        else:
                print("File type ", fileType, " is approved, no action required.")
