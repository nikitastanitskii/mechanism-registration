from typing import List

import uvicorn
from fastapi import FastAPI

app = FastAPI()
from http.client import HTTPException

from pydantic import BaseModel

from src.execptions.users import UserAlreadyExists
from src.repository.redis_users_repositry import RedisUsersRepository
from src.services.sign_in_user import SignInUsers
from src.services.sign_up_user import SignUpUsers


class UserProfileCreate(BaseModel):
    username: str
    name: str
    age: int
    email: str
    address: str
    password: str


@app.post("/profile/")
def create_profile(profile: UserProfileCreate):
    """Создание профиля пользователя"""
    users_repository = RedisUsersRepository()
    if users_repository.exists(profile.username):
        raise HTTPException(
            status_code=400, detail="Пользователь с таким именем уже существует."
        )
    else:
        users_repository.create(profile.username)
        return {"message": "Профиль успешно создан."}


@app.post("/sign_up")
def sign_up(profile: UserProfileCreate):
    """Регистрация пользователя"""
    users_repository = RedisUsersRepository()
    sign_up_service = SignUpUsers(users_repository=users_repository)
    try:
        sign_up_service.sign_up(profile.username, profile.password)
        return {"message": "Ваш профиль успешно создан"}
    except UserAlreadyExists:
        raise HTTPException(
            status_code=400, detail="Пользователь с таким именем уже существует."
        )


@app.post("/sign_in")
def sign_in(profile: UserProfileCreate):
    """Аутентификация пользователя"""
    users_repository = RedisUsersRepository()
    sign_in_user = SignInUsers(users_repository=users_repository)
    try:
        sign_in_user.sign_in(profile.username, profile.password)
        return {"message": "Вы вошли в свой профиль"}
    except HTTPException:
        raise HTTPException(
            status_code=400, detail="Неверное имя пользователя или пароль."
        )

@app.patch("/profiles/{username}")
def update_profile(username: str, profile_data: UserProfileCreate):
    """Обновление профиля пользователя"""
    users_repository = RedisUsersRepository()
    if not users_repository.exists(username):
        raise HTTPException(
            status_code=404,detail="Профиль не найден."
        )
    current_profile = users_repository.get(username)

    updated_profile = current_profile.copy()
    for field, value in profile_data.items():
        updated_profile[field] = value

    users_repository.update(username, updated_profile)
    return {"message": "Данные профиля успешно обновлены"}

@app.get("/profiles/{username}")
def get_profile(username: str):
    """Получение профиля пользователя"""
    users_repository = RedisUsersRepository()
    if not users_repository.exists(username):
        raise HTTPException (
            status_code = 404,detail = "Профиль не найден"
        )

    # Получаем профиль из базы данных
    profile_data = users_repository.get(username)

    # Возвращаем данные профиля
    return UserProfileCreate(**profile_data)

@app.get("/profiles/", response_model=List[UserProfileCreate])
def get_all_profiles(username: str, profile_data: UserProfileCreate):
    """Получение списка профилей пользователей."""
    users_repository = RedisUsersRepository()

    # Получаем список всех профилей
    all_profiles = users_repository.get(username)

    # Проверяем, есть ли профили в базе
    if not all_profiles:
        raise HTTPException(
            status_code=404, detail="Профили не найдены."
        )

    return [UserProfileCreate(**profile) for profile in all_profiles]

@app.delete("/profiles/{username}")
def delete_profile(username: str):
    """Удаление профиля пользователя"""
    users_repository = RedisUsersRepository()

    if not users_repository.exists(username):
        raise HTTPException(
            status_code=404, detail="Профиль не найден."
        )

    users_repository.delete(username)
    return {"message": "Профиль успешно удалён"}

if __name__ == "__main__":
    uvicorn.run(app)
