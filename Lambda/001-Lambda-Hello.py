import json

print('Loading your function')
def lambda_handler(event,context):
    print("message-->" + event['message'])
    return event['message']
    raise Exception('Oh, no!! Something went wrong')
