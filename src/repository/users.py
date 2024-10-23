import bcrypt
from services.redis_connector import redis_connector


def sign_up(username:str, password:str) -> bool:
    """Реализация функции для регистрации пользователя"""
    # Проверяем, существует ли уже пользователь
    if redis_connector.hexists("users", username):
        print("Пользователь с таким именем уже существует.")
        return False
    
    # Хешируем пароль
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    
    # Сохраняем имя пользователя и хешированный пароль в Redis
    redis_connector.hset("users", username, hashed_password.decode('utf-8'))
    print(f"Пользователь {username} успешно зарегистрирован!")
    return True



def sign_in(username:str, password:str) -> bool:
    """Функция для входа пользователя"""
    if not redis_connector.hexists("users", username):
        print("Пользователь не найден.")
        return False
    
    # Получаем хешированный пароль из Redis
    stored_password = redis_connector.hget("users", username)
    
    # Проверяем пароль
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        print(f"Добро пожаловать, {username}!")
        return True
    else:
        print("Неверный пароль.")
        return False


