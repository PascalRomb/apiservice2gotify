import math
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union, List
from app.gotify.notifier import notify_to_gotify
from app.settings import settings

router = APIRouter(prefix="/speedtest", tags=["speedtest"])


class SpeedTest(BaseModel):
    result_id: int
    site_name: str
    ping: float
    download: int
    upload: int
    

class SpeedThresholdFailureMetric(BaseModel):
    name: str
    threshold: str
    value: str

class SpeedThresholdFailure(BaseModel):
    result_id: int
    site_name: str
    metrics: List[SpeedThresholdFailureMetric]


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("bit/s", "Kbit/s", "Mbit/s", "Gbit/s")
   i = int(math.floor(math.log(size_bytes, 1000)))
   p = math.pow(1000, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

@router.post("")
def notify_speedtest_or_threshold_failure(notify_request: Union[SpeedTest, SpeedThresholdFailure]):
    title = ""
    message = ""
    if(isinstance(notify_request, SpeedTest)):
        title = "SpeedTest Run"
        message = "Site: " + notify_request.site_name + "\n" \
            + "Download: " + convert_size(notify_request.download) + "\n" \
            + "Upload: " + convert_size(notify_request.upload) + "\n" \
            + "Ping: " + str(notify_request.ping) + " ms"
    else: 
        title = "SpeedTest Threshold Failure"
        message = "Site: " + notify_request.site_name + "\n"
        message += "Thresholds:\n"
        for metric in notify_request.metrics:
            operator = ">" if metric.name == "Download" or metric.name == "Upload" else "<"
            message += "\t* " + metric.name + " must be " + operator + metric.threshold + " but is " + metric.value  + "\n" 
    
    notify_to_gotify(settings.SPEEDTEST_GOTIFY_APP_TOKEN, title, message)


    