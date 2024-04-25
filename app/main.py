from fastapi import FastAPI, APIRouter
from app.routes import speedtest, whatsupdocker
from app.settings import settings
import uvicorn

settings.load_variables()

app = FastAPI()
api_router = APIRouter()

api_router.include_router(speedtest.router)
api_router.include_router(whatsupdocker.router)
app.include_router(api_router, prefix="/api/v1/notify")


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)