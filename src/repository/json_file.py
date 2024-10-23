import json

def write_to_json(username:str, password:str):
    """Реализация функции для записи данных пользователя"""
    try:
        with open('users_data.json', 'r') as json_file:
            users_data = json.load(json_file)   # Преобразуем их в Python-структуру
    except FileNotFoundError:
        users_data = {"users": []}

    users_data["users"].append({"username": username, "password": password.decode()})

    with open('users_data.json', 'w') as json_file:
        json.dump(users_data, json_file, indent=4)  # Записываем содержимое в формате JSON