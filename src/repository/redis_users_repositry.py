from typing import Any

from src.core.db.redis import redis_connector
from src.repository.base_users_repository import BaseUsersRepository


class RedisUsersRepository(BaseUsersRepository):
    def exists(self, username: str) -> bool:
        return redis_connector.hexists("users", username)

    def create(self, username: str) -> None:
        redis_connector.hset("users", username)

    def get(self, username: str) -> Any | None:
        profile = redis_connector.hget("users", username)
        if profile:
            return profile
        else:
            return None

    def update(self, username: str) -> None:
        if self.exists(username):
            redis_connector.exists("users", username)

    def delete(self, username: str) -> None:
        if self.exists(username):
            redis_connector.hdel("users", username)

    def get_all_profile(self,username: str) -> list:
        keys = redis_connector.hkeys("users")
        return [redis_connector.hget("users", key) for key in keys]
