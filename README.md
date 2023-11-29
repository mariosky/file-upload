# file-upload

## SQS 

### Ejemplo de Access Policy

Para permitir que S3 envíe eventos a SQS:
```json
{
  "Version": "2012-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__owner_statement",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<user_id>:root"
      },
      "Action": "SQS:*",
      "Resource": "arn:aws:sqs:us-east-1:<user_id>:MyQueue"
    },
    {
      "Sid": "example-statement-ID",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:us-east-1:<user_id>:MyQueue",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<user_id>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:s3:::<bucket_name>"
        }
      }
    }
  ]
}
```


### Redis CLI
Instalación
```
wget http://download.redis.io/redis-stable.tar.gz && tar xvzf redis-stable.tar.gz && cd redis-stable && make BUILD_TLS=yes
sudo yum install gcc openssl-devel
```

Conexión al endpoint o redis
```
src/redis-cli -h conn-string-elasticache.amazonaws.com -p 6379 --tls
```

## Algunos comandos para el contenedor de redis
```
docker run --name redis -d redis:alpine
docker ps 
docker kill redis
docker rm <contenedor>
docker stop <contenedor> 
docker run --name redis -p 6379:6379 redis:alpine
```

## docker-compose.yml 

```yaml
version: '3'

# definiciones de los servicios
services:
  redis:
    image: "redis:alpine"
    ports:
    - "6379:6379"
  worker:
    build: '.'
    depends_on:
      - redis
      #volumes:
       # - ./Worker:/code
    command: python worker.py
    environment:
      PYTHONUNBUFFERED: 1
      REDIS_HOST: redis
```