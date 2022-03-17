import json
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        print(str(payload))
       
        client = boto3.client('sns')
        response = client.publish (
            TargetArn = "<ARN>",
            Message = json.dumps({'default': payload}),
            MessageStructure = 'json'
        )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }