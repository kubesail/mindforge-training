FROM python:3

ENV HTTP_PORT=9000
ENV REDIS_SERVER=redis

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD server.py .

CMD ["python", "-u", "server.py"]
