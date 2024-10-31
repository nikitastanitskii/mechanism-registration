from fastapi import Depends, HTTPException

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import RedisProfileRepository


class DeleteProfileService:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def delete_profile(self, username: str):
        # Пытаемся удалить профиль, если он существует
        if not self.__repository.delete(username):
            raise HTTPException(status_code=404, detail="Профиль не найден")
        return {"message": "Профиль успешно удалён"}


def get_profile_service(
    profile_repository: BaseProfileRepository = Depends(RedisProfileRepository),
) -> DeleteProfileService:
    return DeleteProfileService(profile_repository=profile_repository)
