from fastapi import FastAPI, HTTPException
from src.repository.redis_users_repositry import RedisUsersRepository

app = FastAPI()


@app.delete("/profiles/{username}")
def delete_profile(username: str):
    users_repository = RedisUsersRepository()

    # Проверяем, существует ли профиль
    if not users_repository.exists(username):
        raise HTTPException(
            status_code=404, detail="Профиль не найден."
        )

    # Удаляем профиль
    users_repository.delete_profile(username)
    return {"message": "Profile deleted successfully."}