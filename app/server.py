from fastapi import FastAPI
from app.utils.logger import logger
from app.routers import (
  auth as auth_router
)

logger.debug('hey')
api = FastAPI()

logger.debug('Initializing routers...')
api.include_router(auth_router.router)
