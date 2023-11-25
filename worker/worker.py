import boto3
import json

client = boto3.client('sqs')


while True:
    message = client.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/052353881089/MyQueue',
                    WaitTimeSeconds=2,
                    )
    if message and 'Messages' in message and message['Messages']:
        
        print(message['Messages'])
        

