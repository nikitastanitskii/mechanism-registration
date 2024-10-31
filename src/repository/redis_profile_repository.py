import json
from typing import List

from fastapi import HTTPException

from src.core.db.redis import redis_connector
from src.repository.base_profile_repository import BaseProfileRepository
from src.services.exceptions import ProfileAlreadyExists
from src.services.model_data import UserProfileCreate


class RedisProfileRepository(BaseProfileRepository):
    def exists(self, username: str) -> bool:
        return redis_connector.hexists("profiles", username)

    def create(self, profile: UserProfileCreate) -> None:
        redis_connector.hset("profiles", profile.username, profile.model_dump_json())

    def update(self, username: str, updated_data: dict) -> None:
        if not self.exists(username):
            raise HTTPException(status_code=404, detail="Профиль не найден")
        current_profile_data = redis_connector.hget("profiles", username)
        if current_profile_data is None:
            raise HTTPException(status_code=404, detail="Профиль не найден")
        else:
            profile_data = json.loads(current_profile_data)
            profile_data.update(updated_data)
            redis_connector.hset("profiles", username, json.dumps(profile_data))

    def get_profile(self, username: str) -> UserProfileCreate:
        profile_data = redis_connector.hget("profiles", username)
        if profile_data is None:
            raise HTTPException(status_code=404, detail="Профиль не найден")

        return UserProfileCreate(**profile_data)

    def get(self, key: str) -> str:
        profile_data = redis_connector.hget("profiles", key)
        if profile_data:
            return json.loads(profile_data)  # Преобразуем JSON-строку в словарь
        return None

    def get_all_profiles(self) -> list:
        keys = redis_connector.hkeys("profiles")
        return [json.loads(redis_connector.hget("profiles", key)) for key in keys]

    def delete(self, username: str) -> bool:
        result = redis_connector.hdel("profiles", username)
        return True


def get_profile_repository() -> BaseProfileRepository:
    return RedisProfileRepository()
