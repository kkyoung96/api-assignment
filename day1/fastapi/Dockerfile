FROM python:latest

MAINTAINER kmpark

RUN mkdir -p /app
WORKDIR /app
RUN pip install fastapi
RUN pip install uvicorn

COPY main.py /app/main.py

CMD uvicorn main:app --reload --host=0.0.0.0 --port=8000

EXPOSE 8000
