from fastapi import Depends

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.exceptions import ProfileNotFound


class DeleteProfileService:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def delete_profile(self, username: str):
        if self.__repository.exists(username):
            self.__repository.delete(username)
        else:
            raise ProfileNotFound("Профиль не найден")


def get_profile_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> DeleteProfileService:
    return DeleteProfileService(profile_repository=profile_repository)
