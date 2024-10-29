from fastapi import HTTPException

from pydantic import BaseModel, EmailStr

from src.execptions.users import UserAlreadyExists
from src.main import app
from src.repository.redis_users_repositry import RedisUsersRepository
from src.services.sign_in_user import SignInUsers
from src.services.sign_up_user import SignUpUsers


class UserProfileCreate(BaseModel):
    username: str
    name: str
    age: int
    email: EmailStr
    address: str
    password: str


@app.post("/sign_up")
def sign_up(data: UserProfileCreate):
    users_repository = RedisUsersRepository()
    sign_up_service = SignUpUsers(users_repository=users_repository)
    try:
        sign_up_service.sign_up(data.username, data.password)
        return {"message": "Ваш профиль успешно создан"}
    except UserAlreadyExists:
        raise HTTPException(
            status_code=400, detail="Пользователь с таким именем уже существует."
        )


@app.post("/sign_in")
def sign_in(data: UserProfileCreate):
    users_repository = RedisUsersRepository()
    sign_in_user = SignInUsers(users_repository=users_repository)
    try:
        sign_in_user.sign_in(data.username, data.password)
        return {"message": "Вы вошли в свой профиль"}
    except HTTPException:
        raise HTTPException(
            status_code=400, detail="Неверное имя пользователя или пароль."
        )


@app.post("/profile/")
def create_profile(profile: UserProfileCreate):
    users_repository = RedisUsersRepository()
    if users_repository.exists(profile.username):
        raise HTTPException(
            status_code=400, detail="Пользователь с таким именем уже существует."
        )
    users_repository.create(profile)
    return {"message": "Профиль успешно создан."}
