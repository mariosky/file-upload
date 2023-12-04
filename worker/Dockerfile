FROM python:3.8.16


COPY . /worker
WORKDIR /worker
RUN pip install -r requirements.txt
RUN chmod 644 worker-redis.py
