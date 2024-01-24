The basic docker run command takes this form:

$ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]

The docker run command must specify an IMAGE

to derive the container from. An image developer can define image defaults related to:

    detached or foreground running
    container identification
    network settings
    runtime constraints on CPU and memory

```
docker run --env-file env.list image-worker python worker-redis.py
uvicorn sse-redis:app --reload --host 0.0.0.0 --port 8000
docker run --name redis -p 6379:6379 redis:alpine

docker run -p 6379:6379 redis:alpine

docker images
docker rmi -f  21d3e986b483

Reiniciar un contenedor:
docker start  `docker ps -q -l` # restart it in the background
docker attach `docker ps -q -l` # reattach the terminal & stdin

docker info
```

Caution - These steps depend on your current /var/lib/docker being an actual directory (not a symlink to another location).

Stop docker: service docker stop. Verify no docker process is running ps faux
Double check docker really isn’t running. Take a look at the current docker directory: ls /var/lib/docker/
2b) Make a backup - tar -zcC /var/lib docker > /mnt/pd0/var_lib_docker-backup-$(date +%s).tar.gz
Move the /var/lib/docker directory to your new partition: mv /var/lib/docker /mnt/pd0/docker
Make a symlink: ln -s /mnt/pd0/docker /var/lib/docker
Take a peek at the directory structure to make sure it looks like it did before the mv: ls /var/lib/docker/ (note the trailing slash to resolve the symlink)
Start docker back up service docker start
restart your containers

sudo systemctl stop docker.socket
