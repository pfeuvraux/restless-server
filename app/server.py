import os
from fastapi import FastAPI
from app.utils.logger import logger
import app.routers

api = FastAPI()

logger.debug('Initializing routers...')
api.include_router(app.routers.auth.router)
