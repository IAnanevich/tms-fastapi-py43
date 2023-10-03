from fastapi import HTTPException
from sqlalchemy import exists
from sqlalchemy.orm import Session
from fastapi import status

from src.core.managers.base_manager import BaseManager
from src.models.user_model import User


class UserManager(BaseManager):

    table = User

    @classmethod
    def create_user(cls, input_data, session: Session):
        email = input_data.get('email')
        if session.query(exists().where(cls.table.email == email)).scalar():
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'This {email=} already exists')
        return cls.create(input_data=input_data, session=session)

