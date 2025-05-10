from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="CloudVision")

app.include_router(router)
