from typing import Optional, Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(
    title='My App',
    docs_url='/api/docs',

)


class User(BaseModel):
    name: Optional[str]
    age: int
    is_admin: bool
    email: str


class UserCreateSchema(BaseModel):
    pass


class UserUpdateSchema(BaseModel):
    name: Optional[str]
    age: int


class UserUpdateResponseSchema(BaseModel):
    name: Optional[str]
    age: int
    is_admin: bool


@app.get('/')
def read():
    return {'Hello': 'world'}


@app.get('/name/{firstname}')
def read_name(firstname: str, lastname: str = ''):
    return f'Hello {firstname} {lastname}'


@app.get('/user')
def update_user():
    return 'user'


@app.get('/user/{user_id}')
def update_user(user_id: int):
    return user_id


@app.put('/user/{user_id}', response_model=UserUpdateResponseSchema)
def update_user(user_id: int, user: UserUpdateSchema) -> UserUpdateResponseSchema:
    return {'name': user.name, 'age': user.age, 'is_admin': True, 'id': user_id}
    # user = UserManager.update(fwonvwf.wvmiwnv)
    # return UserUpdateResponseSchema(**(user.__dict__))
    #
    # return UserUpdateResponseSchema(
    #     name=user.name,
    #     age=user.age,
    #     is_admin=True
    # )


@app.post('/user')
def create_user(user: User):
    return user.__dict__
