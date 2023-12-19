FROM python:3.11-alpine

MAINTAINER Vitaliy Demchyshyn

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev libpq-dev
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip && pip install pipenv

COPY requirements.txt /tmp

RUN pip install --upgrade pip
RUN cd /tmp && pip install -r requirements.txt
