from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from src.repository.redis_users_repositry import RedisUsersRepository

app = FastAPI()


class UserProfile(BaseModel):
    username: str
    name: str
    age: int
    email: EmailStr
    address: str


@app.get("/profiles/", response_model=List[UserProfile])
def get_all_profiles():
    users_repository = RedisUsersRepository()

    # Получаем список всех профилей
    all_profiles = users_repository.get_all_profiles()

    # Проверяем, есть ли профили в базе
    if not all_profiles:
        raise HTTPException(
            status_code=404, detail="Профили не найдены."
        )

    return [UserProfile(**profile) for profile in all_profiles]
