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
    def get(self, username: str) -> dict:
        pass

    @abstractmethod
    def get_profile(self, profile: UserProfileCreate) -> dict:
        pass

    @abstractmethod
    def get_all_profiles(self, username: UserProfileCreate) -> dict:
        pass

    def delete(self, username: UserProfileCreate) -> None:
        pass
