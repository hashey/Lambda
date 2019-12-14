import json

print("Starting new invocation")

def lambda_handler(event, context):
	# setting variables to equal values from the vent object passed in

	# set variable by parsing out JSON key value pairs from the s3 event triggering the function
	bucket = event['Records'][0]['s3']['bucket']['name']
	region = event['Records'][0]['awsRegion']
	object = event['Records'][0]['s3']['object']['key']
	user = event['Records'][0]['userIdentity']['principalId']

	print("Bucket: " + bucket)
	print("Region: " + region)
	print("User is: " + user)

	return(object)
