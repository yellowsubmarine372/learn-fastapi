from fastapi import APIRouter
from pydantic import BaseModel

from user.application.user_service import UserService
from user.domain import user

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str

@router.post("", status_code=201)
def create_user(user: CreateUserBody):
    user_service = UserService()
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )
    
    return created_user