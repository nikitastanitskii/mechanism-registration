from src.repository.redis_users_repositry import RedisUsersRepository
from src.services.sign_in_user import SignInUsers
from src.services.sign_up_user import SignUpUsers

if __name__ == "__main__":
    users_repository = RedisUsersRepository()
    sign_up_service = SignUpUsers(users_repository=users_repository)
    sign_in_user = SignInUsers(users_repository=users_repository)

    while True:
        print("\nВыберите действие:")
        print("1. Регистрация (sign-up)")
        print("2. Вход в систему (sign-in)")
        print("3. Выйти")

        menu = input("Введите номер действия: ")

        match menu:
            case "1":
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                sign_up_service.sign_up(username, password)

            case "2":
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                sign_in_user.sign_in(username, password)

            case "3":
                print("Выход.")
                break

            case _:
                print("Неверный ввод. Попробуйте снова.")
