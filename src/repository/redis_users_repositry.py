from src.core.db.redis import redis_connector
from src.repository.base_users_repository import BaseUsersRepository


class RedisUsersRepository(BaseUsersRepository):
    def exists(self, username: str) -> bool:
        return redis_connector.hexists("users", username)

    def create(self, username: str, password: str) -> None:
        redis_connector.hset("users", username, password)

    def get(self, username: str) -> str:
        return redis_connector.hget("users", username)

    def delete(self, username: str) -> dict:
        pass
