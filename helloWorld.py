import json

print('Loading your function') #this appears in the cloudwatch logs but not the immediate/console output because it is outside the scope of the handler function

def lambda_handler(event, context):
    print("message --> " + event['message'])
    
    return event['message'] #echo back the first key value
    raise Exception('Something went wrong!')
