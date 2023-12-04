docker build -t image-worker .
docker image ls

source env.list.ex
docker run --env-file env.list image-worker python worker-redis.py
python worker-redis.py [stop]



uvicorn sse-redis:app --reload --host 0.0.0.0 --port 8000

