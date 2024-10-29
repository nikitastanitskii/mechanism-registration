from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

from src.main import app
from src.repository.redis_users_repositry import RedisUsersRepository


class UserProfileUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None

@app.patch("/profiles/{username}")
def update_profile(username: str, profile_data: UserProfileUpdate):
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
