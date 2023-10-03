from fastapi import APIRouter, status

from src.core.db import session
from src.core.managers.user_manager import UserManager
from src.rest.schemas.user_schema import UserCreateSchema, UserListSchema, UserRetrieveSchema, UserUpdateResponseSchema, \
    UserUpdateInputSchema
from src.services.user_service import UserService

router = APIRouter()


@router.get('/users', response_model=list[UserListSchema], status_code=status.HTTP_200_OK)
def get_users():
    return UserManager.list(session=session)


@router.get('/users/{user_id}', response_model=UserRetrieveSchema, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    return UserManager.retrieve(pk=user_id, session=session)


@router.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateSchema):
    return UserService.create_user(user=user.__dict__, session=session)


@router.patch('/users/{user_id}', response_model=UserUpdateResponseSchema, status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: int, input_data: UserUpdateInputSchema):
    return UserManager.update(pk=user_id, input_data=input_data.__dict__, session=session)


@router.delete('/users/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    return UserManager.delete(pk=user_id, session=session)
