from pydantic import BaseModel


class RemoveNullableValueSchema(BaseModel):

    def __getattribute__(self, item):
        result = super().__getattribute__(item)
        if item == '__dict__':
            return {key: value for key, value in result.items() if value is not None}
        return result
