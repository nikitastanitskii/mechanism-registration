from fastapi import Depends, HTTPException

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.model_data import UserProfileCreate


class UpdateProfile:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def update(self, username: str, profile_data: UserProfileCreate):
        if not self.__repository.exists(username):
            raise HTTPException(status_code=404, detail="Профиль не найден")

        current_profile = self.__repository.get(username)

        if current_profile is None:
            raise HTTPException(status_code=404, detail="Профиль не найден")

        updated_profile = current_profile.copy()
        for key, value in profile_data.model_dump(exclude_unset=True).items():
            updated_profile[key] = value

        self.__repository.update(username, updated_profile)
        return {"message": "Профиль успешно обновлен"}


def get_update_profile_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> UpdateProfile:
    return UpdateProfile(profile_repository=profile_repository)
