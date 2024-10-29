from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from src.repository.redis_users_repositry import RedisUsersRepository

app = FastAPI()


class UserProfile(BaseModel):
    username: str
    name: str
    age: int
    email: EmailStr
    address: str


@app.get("/profiles/{username}", response_model=UserProfile)
def get_profile(username: str):
    users_repository = RedisUsersRepository()

    # Проверяем, существует ли профиль
    if not users_repository.exists(username):
        raise HTTPException(
            status_code=404, detail="Профиль не найден."
        )

    # Получаем профиль из базы данных
    profile_data = users_repository.get(username)

    # Возвращаем данные профиля
    return UserProfile(**profile_data)
