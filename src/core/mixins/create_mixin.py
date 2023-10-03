from sqlalchemy.orm import Session

from src.core.mixins.base_mixin import BaseMixin


class CreateMixin(BaseMixin):

    @classmethod
    def create(cls, input_data, session: Session):
        obj = cls.table(**input_data)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
