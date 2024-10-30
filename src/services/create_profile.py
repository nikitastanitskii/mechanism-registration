from fastapi import Depends
from src.repository.profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.exceptions import ProfileAlreadyExists
from src.services.schemas import UserProfileCreate


class CreateProfile:
    def __init__(self, profile_repository: BaseProfileRepository) -> None:
        self.__repository = profile_repository

    def create(self, data: UserProfileCreate) -> None:
        """Функция для входа пользователя"""
        if self.__repository.exists(data.username):
            raise ProfileAlreadyExists
        else:
            self.__repository.create(data)


def get_create_profile_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> CreateProfile:
    return CreateProfile(profile_repository=profile_repository)
