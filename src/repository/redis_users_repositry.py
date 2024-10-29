from typing import Any

from src.core.db.redis import redis_connector
from src.repository.base_users_repository import BaseUsersRepository


class RedisUsersRepository(BaseUsersRepository):
    def exists(self, username: str) -> bool:
        return redis_connector.hexists("users", username)

    def create(self, username: str, profile_data: dict) -> None:
        redis_connector.hset("users", username,profile_data)

    def get(self, username: str) -> Any | None:
        profile = redis_connector.hget("users", username)
        if profile:
            return profile
        else:
            return None


    def update(self, username: str, updated_data: dict) -> None:
        if self.exists(username):
            redis_connector.exists("users", username, updated_data)

    def delete(self, username: str) -> None:
        if self.exists(username):
            redis_connector.delete("users", username)

    def get_all_profiles(self,username: str):
        pass
