from abc import ABC, abstractmethod

from src.services.schemas import UserProfileCreate


class BaseProfileRepository(ABC):
    @abstractmethod
    def exists(self, username: str) -> bool:
        pass


    @abstractmethod
    def create(self, profile: UserProfileCreate) -> None:
        pass

    @abstractmethod
    def get_all(self, username: str) -> dict:
        pass
