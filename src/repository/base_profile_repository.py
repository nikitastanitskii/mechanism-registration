from abc import ABC, abstractmethod

from src.services.model_data import UserProfileCreate


class BaseProfileRepository(ABC):
    @abstractmethod
    def exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def create(self, profile: UserProfileCreate) -> None:
        pass

    @abstractmethod
    def update(self, username: str, updated_data: UserProfileCreate) -> None:
        pass

    @abstractmethod
    def get_profile(self, profile: UserProfileCreate) -> None:
        pass

    @abstractmethod
    def get_all_profiles(self, username: UserProfileCreate) -> list[UserProfileCreate]:
        pass

    @abstractmethod
    def get(self, username: str) -> UserProfileCreate:
        pass

    def delete(self, username: UserProfileCreate) -> bool:
        pass
