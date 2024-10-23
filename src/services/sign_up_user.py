from src.repository.base_users_repository import BaseUsersRepository
from src.services.security import HashPassword


class SignUpUsers:
    def __init__(self, users_repository: BaseUsersRepository) -> None:
        self.__repository = users_repository
        self.__security = HashPassword()

    def sign_up(self, username: str, password: str) -> bool:
        """Реализация функции для регистрации пользователя"""
        # Проверяем, существует ли уже пользователь
        if self.__repository.exists(username):
            print("Пользователь с таким именем уже существует.")
            return False

        # Хешируем пароль
        hashed_password = self.__security.hash(password)

        # Сохраняем имя пользователя и хешированный пароль в Redis
        self.__repository.create(username, hashed_password.decode("utf-8"))
        print(f"Пользователь {username} успешно зарегистрирован!")
        return True
