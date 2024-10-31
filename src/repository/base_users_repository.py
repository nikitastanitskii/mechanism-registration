from abc import ABC, abstractmethod


class BaseUsersRepository(ABC):
    @abstractmethod
    def exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def get(self, username: str) -> str | dict:
        pass

    @abstractmethod
    def create(self, username: str, password: str) -> dict:
        pass

    @abstractmethod
    def delete(self, username: str) -> dict:
        pass
