from fastapi import FastAPI
from app.utils.logger import logger
from app.routers import (
  auth as auth_router
)

logger.debug('hey')
app = FastAPI()

logger.debug('Initializing routers...')
app.include_router(auth_router.router)
