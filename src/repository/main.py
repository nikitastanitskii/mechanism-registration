from repository.users import sign_up
from repository.users import sign_in

if __name__ == "__main__":
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
                sign_up(username, password)
        
            case "2":
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                sign_in(username, password)
        
            case "3":
                print("Выход.")
                break
        
            case _:
                print("Неверный ввод. Попробуйте снова.")

