from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from fastapi import HTTPException, Depends


from src.execptions.users import UserAlreadyExists
from src.repository.redis_profile_repository import RedisProfileRepository
from src.repository.redis_users_repositry import RedisUsersRepository
from src.services.create_profile import CreateProfile, get_create_profile_service
from src.services.exceptions import ProfileAlreadyExists
from src.services.schemas import UserProfileCreate
from src.services.sign_in_user import SignInUsers
from src.services.sign_up_user import SignUpUsers



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/profiles/")
def create_profile(
    profile: UserProfileCreate,
    create_profile_service: CreateProfile = Depends(get_create_profile_service),
):
    """Создание профиля пользователя"""
    try:
        create_profile_service.create(profile)
        return {"message": "Профиль успешно создан."}
    except ProfileAlreadyExists:
        raise HTTPException(status_code=400, detail="User already exists")

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
def get_all_profiles():
    return [UserProfileCreate.model_validate_json(profile) for   profile in RedisProfileRepository().get_all()]

@app.delete("/profiles/{username}")
def delete_profile(username: str):
    """Удаление профиля пользователя"""
    users_repository = RedisUsersRepository()


if __name__ == "__main__":
    uvicorn.run(app)
