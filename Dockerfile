FROM python:3.9.6-alpine

WORKDIR /apiservice2gotify

COPY requirements.txt /apiservice2gotify/requirements.txt 
COPY app /apiservice2gotify/app

RUN apk add --update alpine-sdk

RUN pip install -r /apiservice2gotify/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/apiservice2gotify"
CMD [ "python", "-u", "app/main.py" ]
