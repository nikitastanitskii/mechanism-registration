from src.core.db.redis import redis_connector
from src.repository.profile_repository import BaseProfileRepository
from src.services.schemas import UserProfileCreate


class RedisProfileRepository(BaseProfileRepository):
    def exists(self, username: str) -> bool:
        return redis_connector.hexists("profiles", username)

    def create(self, profile: UserProfileCreate) -> None:
        redis_connector.hset("profiles", profile.username, profile.model_dump_json())

    def get_all(self) -> list:
        keys = redis_connector.hkeys("profiles")
        return [redis_connector.hget("profiles", key) for key in keys]


def get_profile_repository() -> BaseProfileRepository:
    return RedisProfileRepository()
