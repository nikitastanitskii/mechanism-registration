from fastapi import Depends, HTTPException

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.model_data import UserProfileCreate


class GetProfileUsers:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def get_profile(self, username: str):
        profile_data = self.__repository.get(username)

        if profile_data is None:
            raise HTTPException(status_code=404, detail="Профиль не найден")

        profile_data = profile_data.get(username)

        # Возвращаем данные профиля
        return UserProfileCreate(**profile_data)


def get_profile_users_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> GetProfileUsers:
    return GetProfileUsers(profile_repository=profile_repository)
