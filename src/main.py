import redis
import bcrypt

redis_connector = redis.Redis(host='localhost', port=6379,db=0)  # Подключение к Redis

def sign_up(username: str, password: str) -> None:
    """Регистрация пользователя"""
    if redis_connector.hexists("users",str(username)):
        print("Пользователь с таким именем уже существует.")
        return False
    

    hashed_passoword = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()) # Хешируем пароль и добавляем соль

    redis_connector.hset("users",username,hashed_passoword.decode('utf-8'))
    print(f'Пользователь {username} успешно зарегестрирован.')
    return True

def sign_in(username:str, password:str) -> None:
    '''Аутентификация пользователя'''
    if not redis_connector.exists("users",username):
        print('Пользователь не найден.')
        return False
    
    stored_password = redis_connector.hget("users",username)

    if bcrypt.checkpw(password.encode('utf-8'),stored_password.encode('utf-8')):
        print(f"Добро подаловать, {username}")
        return True
    else:
        print('Неверный пароль')
        return False


def menu():
    while True:
        print("1. Регистрация (sign-up)")
        print("2. Вход в систему (sign-in)")
        print("3. Выйти")

        menu = input('Введите номер действия: ')
        if menu == '1':
            username = print('Введите имя пользоватея: ')
            password = print('Введите пароль: ')
            sign_up(username,password)
        elif menu == '2':
            username = print('Введите имя пользоватея: ')
            password = print('Введите пароль: ')
            sign_in(username,password)
        elif menu == '3':
            print('Выход')
            break

if __name__ == "__main__":
    menu()
                









 