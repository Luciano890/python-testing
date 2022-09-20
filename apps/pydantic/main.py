# pylint: disable=missing-docstring
# pylint: disable=import-error
from uuid import uuid4
from pydantic import UUID4, BaseModel, Field


class User(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    name: str


u = User(name='John', id=uuid4())
print(u)
