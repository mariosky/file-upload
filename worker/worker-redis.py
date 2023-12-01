import asyncio
import boto3
import json
import s3image
import sys
import redis 

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/052353881089/MyQueue'
REDIS_URL = 'localhost'

client = boto3.client('sqs')


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
    
        

        
