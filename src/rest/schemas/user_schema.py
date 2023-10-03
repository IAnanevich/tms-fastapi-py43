import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, validator

from src.rest.schemas.remove_nullable_value_schema import RemoveNullableValueSchema


class UserListSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: Optional[int]
    email: EmailStr
    password: str
    is_admin: bool
    created_at: datetime
    updated_at: datetime


class UserRetrieveSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: Optional[int]
    email: EmailStr
    password: str
    is_admin: bool


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None
    email: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, value):
        pattern = r"^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:;<>,.?~-])[A-Za-z0-9!@#$%^&*()_+{}|:;<>,.?~-]{8,}$"

        if re.match(pattern, value):
            return value
        raise ValueError('The password must consist of one special character, one number and be 8 characters long.')


class UserUpdateInputSchema(RemoveNullableValueSchema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None


class UserUpdateResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: Optional[int]
    email: EmailStr
    password: str
    is_admin: bool
    created_at: datetime
    updated_at: datetime
