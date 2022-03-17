import json
import logging
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):    
    client = boto3.client('sns')
        response = client.publish (
            TargetArn = "<ARN>",
            Message = json.dumps(event),
            MessageStructure = 'json'
        )