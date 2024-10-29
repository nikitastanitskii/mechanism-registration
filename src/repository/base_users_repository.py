from abc import ABC, abstractmethod


class BaseUsersRepository(ABC):
    @abstractmethod
    def exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def update(self, username: str) -> str:
        pass

    @abstractmethod
    def get(self, username: str) -> str:
        pass


    @abstractmethod
    def create(self, username: str) -> None:
        pass

    @abstractmethod
    def delete(self, username: str) -> dict:
        pass
