from fastapi import Depends

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.model_data import UserProfileCreate


class GetAllProfile:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def get_all_profiles(self) -> list[UserProfileCreate]:
        all_profile_data = self.__repository.get_all_profiles()
        if not all_profile_data:
            return []

        all_profiles = []
        for profile_dict in all_profile_data:
            all_profiles.append(UserProfileCreate(**profile_dict))

        return all_profiles


def get_all_profile_users_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> GetAllProfile:
    return GetAllProfile(profile_repository=profile_repository)
