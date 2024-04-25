import math
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union, List
from app.gotify.notifier import notify_to_gotify
from app.settings import settings

router = APIRouter(prefix="/whatsupdocker", tags=["whatsupdocker"])


class Registry(BaseModel):
    url: str
    name: str


class Tag(BaseModel):
    value: str
    semver: bool


class Digest(BaseModel):
    watch: bool
    repo: str
    value: str


class Image(BaseModel):
    id: str
    registry: Registry
    name: str
    tag: Tag
    digest: Digest
    architecture: str
    os: str
    created: str


class UpdateKind(BaseModel):
    kind: str
    localValue: str
    remoteValue: str


class Result(BaseModel):
    tag: str
    digest: str


class WhatsupDockerContainer(BaseModel):
    id: str
    name: str
    status: str
    watcher: str
    displayName: str
    displayIcon: str
    image: Image
    updateAvailable: bool
    updateKind: UpdateKind
    result: Result

    

@router.post("")
def notify_whatsupdocker(wud_containers: List[WhatsupDockerContainer]):
    title = "New docker container releases are available"
    message = ""
    for container in wud_containers:
        message += "Watcher" + container.watcher + ". Container: " + container.name + ".\n"
        

    notify_to_gotify(settings.WUD_GOTIFY_APP_TOKEN, title, message)


    