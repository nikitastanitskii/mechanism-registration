from fastapi import HTTPException

import uvicorn
from src.execptions.users import UserAlreadyExists
from src.repository.redis_users_repositry import RedisUsersRepository
from src.services.sign_in_user import SignInUsers
from src.services.sign_up_user import SignUpUsers
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


class CreateUserModel(BaseModel):
    username: str
    password: str


@app.post("/sign_up")
def sign_up(data: CreateUserModel):
    users_repository = RedisUsersRepository()
    sign_up_service = SignUpUsers(users_repository=users_repository)
    try:
        sign_up_service.sign_up(data.username, data.password)
        return {"response": "OK"}
    except UserAlreadyExists:
        raise HTTPException(
            status_code=400, detail="Пользователь с таким именем уже существует."
        )


@app.post("/sign_in")
def sign_in(data: CreateUserModel):
    users_repository = RedisUsersRepository()
    sign_in_user = SignInUsers(users_repository=users_repository)
    sign_in_user.sign_in(data.username, data.password)
    return {"response": "OK"}


if __name__ == "__main__":
    uvicorn.run(app)
