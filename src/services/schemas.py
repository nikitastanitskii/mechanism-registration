from pydantic import BaseModel


class UserProfileCreate(BaseModel):
    username: str
    name: str
    age: int
    email: str
    address: str
    password: str
