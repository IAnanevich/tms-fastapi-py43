from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from src.core.db import Base


class AbstractModel(Base):
    __abstract__ = True

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
