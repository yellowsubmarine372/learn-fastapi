from datetime import datetime
from typing import Annotated
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field

from containers import Container
from user.application.user_service import UserService

from common.auth import CurrentUser, get_current_user

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str = Field(min_length=2, max_length=32)
    email: EmailStr = Field(max_length=64)
    password: str = Field(min_length=8, max_length=32)
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

class UpdateUserBody(BaseModel):
    name: str | None = Field(min_length=2, max_length=32, default=None)
    password: str | None = Field(min_length=8, max_length=32, default=None)

class GetUserResponse(BaseModel):
    total_count: int
    page: int
    users: list[UserResponse]


@router.post("", status_code=201, response_model=UserResponse)
@inject
def create_user(
    user: CreateUserBody,
    background_tasks: BackgroundTasks,
    user_service: UserService = Depends(Provide[Container.user_service]),
    ) -> UserResponse:
    print("request:", user)
    created_user = user_service.create_user(
        background_tasks=background_tasks,
        name=user.name,
        email=user.email,
        password=user.password
    )
    print("created_user:", created_user)
    print("created_user type:", type(created_user))

    response = UserResponse(
        id=created_user.id,
        name=created_user.name,
        email=created_user.email,
        created_at=created_user.created_at,
        updated_at=created_user.updated_at
    )

    print("response:", response)
    return response

@router.put("", response_model=UserResponse)
@inject
def update_user(
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    body: UpdateUserBody,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    user = user_service.update_user(
        user_id = current_user.id,
        name = body.name,
        password = body.password
    )
    
    return user

@router.get("")
@inject
def get_users(
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    user_service: UserService = Depends(Provide[Container.user_service]),
    page: int = 1,
    items_per_page: int = 10,
) -> GetUserResponse:
    if current_user.role == "ADMIN":
        total_count, users = user_service.get_users(page, items_per_page)
    else:
        user = user_service.get_user_by_id(page, items_per_page)
        total_count, users = 1, [user]
       
    return {
        "total_count": total_count,
        "page": page,
        "users": users,
    }
    
@router.delete("", status_code=204)
@inject
def delete_user(
    current_user: Annotated[CurrentUser, Depends(get_current_user)],
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    user_service.delete_user(current_user.id)
    
@router.post("/login")
@inject
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    access_token = user_service.login(
        email = form_data.username,
        password = form_data.password
    )
    
    return {"access_token": access_token, "token_type": "bearer"}