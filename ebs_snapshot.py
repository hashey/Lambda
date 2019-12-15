import json
import boto3

# setting ec2 client
ec2 = boto3.client('ec2')

# our lambda handler function
def lambda_handler(event, context):
    # Printing event received
    # print("Received event: " + json.dumps(event, indent=2))
    
    # Print the rule ARN to the logs to be able to differentiate cloudwatch rule sources
    rule_name = event['resources']
    print(rule_name)
    
    # Setting the variable to loop through later
    # Filtering by only looking for EBS volumes where status = 'in-use'
    total_ebs = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['in-use']}])
    
    # Looping through and collecting all EBS volumes
    for volume in total_ebs['Volumes']:
            # create snapshot for each volume within the region
            ec2.create_snapshot(VolumeId=volume['VolumeId'],Description=volume['Attachments'][0]['InstanceId'])
            
            print("Completed volume: " + volume['VolumeId'])
