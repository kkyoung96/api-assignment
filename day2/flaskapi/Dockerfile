FROM python:latest

RUN mkdir -p /app
WORKDIR /app
RUN pip install Flask
RUN pip install mysql-connector

COPY main.py /app/main.py
COPY env.py /app/env.py

EXPOSE 5000

VOLUME ["/data/flask","/app"]

CMD python main.py
