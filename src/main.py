import uvicorn
from fastapi import Depends, FastAPI, HTTPException

from src.services.create_profile import CreateProfile, get_create_profile_service
from src.services.delete_users import DeleteProfileService, get_profile_service
from src.services.exceptions import ProfileAlreadyExists, ProfileNotFound
from src.services.get_all_profiles import GetAllProfile, get_all_profile_users_service
from src.services.get_profile_users import GetProfileUsers, get_profile_users_service
from src.services.model_data import UserProfileCreate
from src.services.update_profile import UpdateProfile, get_update_profile_service

app = FastAPI()


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
        raise HTTPException(status_code=404, detail="Такой пользователь уже есть")


@app.patch("/profiles/{username}")
def update_profile(
    username: str,
    profile: UserProfileCreate,
    update_profile_service: UpdateProfile = Depends(get_update_profile_service),
):
    """Обновление профиля пользователя"""
    try:
        update_profile_service.update(username, profile)
        return {"message": "Профиль успешно обновлен"}
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail="Профиль не найден")


@app.get("/profiles/{username}")
def get_profile(
    username: str,
    get_profile_service: GetProfileUsers = Depends(get_profile_users_service),
):
    """Получение профиля пользователя"""
    try:
        return get_profile_service.get_profile(username)
    except ProfileNotFound:
        return HTTPException(status_code=404, detail="Профиль не найден")


@app.get("/profiles/", response_model=list[UserProfileCreate])
def get_all_profiles(service: GetAllProfile = Depends(get_all_profile_users_service)):
    return service.get_all_profiles()


@app.delete("/profiles/{username}", status_code=204)
def delete_profile(
    username: str, service: DeleteProfileService = Depends(get_profile_service)
):
    try:
        return service.delete_profile(username)
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail="Профиль не найден")


if __name__ == "__main__":
    uvicorn.run(app)
