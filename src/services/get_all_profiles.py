import json
from typing import List

from fastapi import Depends, HTTPException

from src.repository.base_profile_repository import BaseProfileRepository
from src.repository.redis_profile_repository import get_profile_repository
from src.services.model_data import UserProfileCreate


class GetAllProfile:
    def __init__(self, profile_repository: BaseProfileRepository):
        self.__repository = profile_repository

    def get_all_profiles(self) -> List[UserProfileCreate]:
        profile_keys = self.__repository.get_all_profiles()
        if not profile_keys:
            raise HTTPException(status_code=404, detail="Профили не найдены")

        all_profiles = []
        for key in profile_keys:
            profile_data = self.__repository.get(key)
            if profile_data:
                profile_dict = json.loads(profile_data)
                all_profiles.append(UserProfileCreate(**profile_dict))

        return all_profiles


def get_all_profile_users_service(
    profile_repository: BaseProfileRepository = Depends(get_profile_repository),
) -> GetAllProfile:
    return GetAllProfile(profile_repository=profile_repository)
