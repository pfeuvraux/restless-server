from redis import Redis
from app.config import settings
from app.utils.logger import logger

logger.info('Connecting to redis...')

redisclient = Redis(
  host=settings.cache.host,
  port=settings.cache.port
)
