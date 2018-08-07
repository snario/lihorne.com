FROM node:8-alpine

COPY . /home

WORKDIR /home

RUN apk update
RUN apk add --no-cache python py-pip docker
RUN npm i -g firebase-tools
RUN pip install -r scraper/requirements.txt
