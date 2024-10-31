from pydantic import BaseModel, EmailStr


class UserProfileCreate(BaseModel):
    """Модель данных пользователя"""

    username: str
    name: str
    age: int
    email: str | EmailStr
    address: str
    password: str
