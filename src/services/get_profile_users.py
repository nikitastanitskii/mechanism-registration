from fastapi import Depends

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.exceptions import ProfileNotFound
from src.services.model_data import UserProfileCreate


class GetProfileUsers:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def get_profile(self, username: str):
        profile_data = self.__repository.get_profile(username)

        if profile_data is None:
            raise ProfileNotFound("Профиль не найден")

        # Возвращаем данные профиля
        return UserProfileCreate(**profile_data)


def get_profile_users_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> GetProfileUsers:
    return GetProfileUsers(profile_repository=profile_repository)
