import redis

from src.core.config import get_settings

settings = get_settings()
redis_connector = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)
