FROM  python:3.7-alpine
MAINTAINER cloudyrathor.com

ENV PYTHONUNBUFFERED 1
copy ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user