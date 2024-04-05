# apiservice2gotify

[![Build image and push to docker hub](https://github.com/PascalRomb/apiservice2gotify/actions/workflows/release.yml/badge.svg)](https://github.com/PascalRomb/apiservice2gotify/actions/workflows/release.yml)

A simple integration between another service using Rest API and [Gotify](https://gotify.net) Server.

At the moment the following API Services are supported:
- [X] [SpeedTestTracker](https://docs.speedtest-tracker.dev)


## How to configure
Please use the following docker-compose.yml file in order to run the container:
```yml
version: '3'
services:
  apiservice-2-gotify:
    restart: unless-stopped
    image: apiservice2gotify:latest
    ports: 
     - "8000:8000"
    volumes:
      - .env:/apiservice2gotify/app/.env
```

Then create a .env file with the following content:
```
SPEEDTEST_GOTIFY_APP_TOKEN = <app_token_from_gotify_server>
GOTIFY_SERVER_URL = <gotify_server_ip_address>
```

### Connect with other service
#### SpeedTestTracker
* Go to Admin page.
* Select notification under settings
* Enable webook notification and set http(s)://<ip-address:port>/api/v1/notify/speedtest as recipient url.
