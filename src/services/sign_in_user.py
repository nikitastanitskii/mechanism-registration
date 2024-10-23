import bcrypt

from src.repository.base_users_repository import BaseUsersRepository


class SignInUsers:
    def __init__(self, users_repository: BaseUsersRepository) -> None:
        self.__repository = users_repository

    def sign_in(self, username: str, password: str) -> bool:
        """Функция для входа пользователя"""
        if not self.__repository.exists(username):
            print("Пользователь не найден.")
            return False

        # Получаем хешированный пароль из Redis
        stored_password = self.__repository.get(username)

        # Проверяем пароль
        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            print(f"Добро пожаловать, {username}!")
            return True
        else:
            print("Неверный пароль.")
            return False
