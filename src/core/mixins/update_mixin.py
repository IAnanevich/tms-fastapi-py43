from sqlalchemy import update, select
from sqlalchemy.orm import Session

from src.core.mixins.base_mixin import BaseMixin


class UpdateMixin(BaseMixin):

    @classmethod
    def update(cls, pk: int, input_data: dict, session: Session) -> list:
        query = update(cls.table).where(cls.table.id == pk).values(**input_data)
        cls.execute_commit(query=query, session=session)
        result = session.execute(select(cls.table).where(cls.table.id == pk))
        return result.scalars().first()
