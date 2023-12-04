import asyncio
import boto3
import json
import s3image
import sys
import redis 
import os

#import ssl
#print(ssl.OPENSSL_VERSION)

#import urllib3
#URL = 'https://localhost:4433/'

#http = urllib3.PoolManager(
#    ca_certs='cert.pem',
#    cert_reqs='CERT_REQUIRED',
#)
#r = http.request('GET', URL)
#print(r.data.decode('utf-8'))

session = boto3.Session()

# Access the credentials from the session
#credentials = session.get_credentials()
#current_credentials = credentials.get_frozen_credentials()

#print("Access Key:", current_credentials.access_key)
#print("Secret Key:", current_credentials.secret_key)
#print("Session Token:", current_credentials.token)

QUEUE_URL = os.environ['QUEUE_URL'] 
REDIS_URL = os.environ['REDIS_HOST']  

client = boto3.client('sqs', region_name='us-east-1')
#sts_client = boto3.client('sts') 
#assumed_role_object = sts_client.assume_role(
#    RoleArn="arn:aws:iam::052353881089:role/LabRole",
#    RoleSessionName="SessionName"
#)
#expiration = sts_client['Credentials']['Expiration']

#print(expiration)
#print(sts_client['Credentials'])



#print(sts_client.get_caller_identity())
#print(client._endpoint)
r = redis.Redis(host=REDIS_URL, decode_responses=True)

stop = len(sys.argv) > 1 and sys.argv[1] == 'stop'

run = True

while run:
    if stop: # El parámetro stop detiene el script despues de un loop
        run = False
    message = client.receive_message(QueueUrl=QUEUE_URL,
                    WaitTimeSeconds=2,
                    )
    if message and 'Messages' in message and message['Messages']:
        try:
            receipt_handle = message['Messages'][0]['ReceiptHandle']
            body =  json.loads(message['Messages'][0]['Body'])
            bucket_name = body['Records'][0]['s3']['bucket']['name']
            key = body['Records'][0]['s3']['object']['key']
            filename = key.split('/')[-1]
            message_id =  message['Messages'][0]['MessageId']
            print(message_id,bucket_name, key, receipt_handle)
            s3image.download_file(bucket_name, key, 'image.jpg')
            print('imagen recibida')
            s3image.resize_image('image.jpg','new.jpg')
            print('imagen transformada') 
            s3image.upload_file('new.jpg', bucket_name,
                     f'small/{filename}',  extra_args={'ACL': 'public-read'}) 
            print('imagen almacenada')
            client.delete_message( QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle )
            print('mensaje eliminado')
            ok = r.set(filename, "ok")
            #ok = r.set(filename, "ok", ex=2000)
            assert ok
        except Exception as e:
            print(e)
            client.delete_message( QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle )
    print('Waiting Loop')
    
        

        
