import requests
from app.settings import settings


def notify_to_gotify(app_token, title, message):
    requests.post('{0}/message?token={1}'.format(settings.GOTIFY_SERVER_URL, app_token), json={
    "message": message,
    "priority": 5,
    "title": title
})