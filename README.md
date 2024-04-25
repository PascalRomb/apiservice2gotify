# apiservice2gotify

A simple integration between another service using Rest API and [Gotify](https://gotify.net) Server.

At the moment the following API Services are supported:
- [X] [SpeedTestTracker](https://docs.speedtest-tracker.dev)
- [X] [What's Up Docker](https://fmartinou.github.io/whats-up-docker/#/)


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
WUD_GOTIFY_APP_TOKEN = <app_token_from_gotify_server>
SPEEDTEST_GOTIFY_APP_TOKEN = <app_token_from_gotify_server>
GOTIFY_SERVER_URL = <gotify_server_ip_address>
```

### Connect with other service
#### SpeedTestTracker
* Go to Admin page.
* Select notification under settings
* Enable webook notification and set http(s)://<ip-address:port>/api/v1/notify/speedtest as recipient url.

#### SpeedTestTracker
Configure What's up Docker using the following docker environments:
- WUD_TRIGGER_HTTP_GOTIFY_URL=http(s)://<ip-address:port>/api/v1/notify/whatsupdocker
- WUD_TRIGGER_HTTP_GOTIFY_MODE=batch
- WUD_TRIGGER_HTTP_GOTIFY_ONCE=false
