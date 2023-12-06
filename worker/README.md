
## Servidor FastAPI
Primero en el código de see-redis.py` cambiamos la variable:

```env
REDIS_HOST='172.31.76.34'
```
Agregamos el url del cliente a la lista `origins`, ejemplo:

```python
origins = [
    "http://44.219.209.251:8080",
    "http://ittweb.ddns.net:8080"
]
```
Por último agrega el nombre correcto de tu bucket en el método `s3_client.generate_presigned_post`. 

Como tarea esto se puede poner en variables de entorno o en un archivo de settings.
Ahora si corremos el server.
```bash
uvicorn sse-redis:app --reload --host 0.0.0.0 --port 8000
```

## React Client
```
export NODE_OPTIONS=--openssl-legacy-provider
REACT_APP_BACKEND_URL=http://44.219.209.251:8000 npm start
```

## Redis Container

El siguiente comando ejecuta el contenedor:
```
docker run redis:alpine  -p 6379:6379
```

## Worker Local
Exportamos las variables de entorno:
```
export REDIS_HOST=localhost
export QUEUE_URL=<QueueUrl>
```
```
python worker.py
```

## Worker Container
Desde el directorio worker, creamos la imagen:

```
docker build -t image-worker .
```
Modificamos el archivo env.list indicando las variables de entorno. En el caso
de REDIS_HOST es la dirección IP del host. Como la imágen corre en un contenedor 
este tiene su propia IP. 

Corremos el contenedor worker
```
docker run --env-file env.list --network host  image-worker python worker-redis.py
```

En caso de algún error o cambio en el código del worker podemos 
recrear la imagen.
```
docker build -t image-worker .
```

sudo mount /dev/sdf /var/lib/docker/
sudo systemctl stop docker
sudo systemctl start docker




source env.list.ex
docker run --env-file env.list image-worker python worker-redis.py
python worker-redis.py [stop]





