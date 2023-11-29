# file-upload

### Redis CLI
Instalación
```
wget http://download.redis.io/redis-stable.tar.gz && tar xvzf redis-stable.tar.gz && cd redis-stable && make BUILD_TLS=yes
sudo yum install gcc openssl-devel
```

Conexión al endpoint
```
src/redis-cli -h conn-string-elasticache.amazonaws.com -p 6379 --tls
```

## Contenedor Docker
docker run --name redis -d redis:alpine
docker ps 
docker kill redis
docker rm <contenedor>
docker stop <contenedor> 
docker run --name redis -p 6379:6379 redis:alpine
