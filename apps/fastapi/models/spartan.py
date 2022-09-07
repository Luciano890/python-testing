""" Spartan Model """
# pylint: disable=import-error
from uuid import UUID, uuid4
import typing
from enum import Enum

from pydantic import BaseModel, Field

class Team(int, Enum):
    """ Enum for Spartan Team """
    RED = 1
    BLUE = 2
    BLACK = 3
    ORANGE = 4

class BaseSpartan(BaseModel):
    """ Base Spartan model. """
    name: str
    age: int
    team: typing.Optional[Team] = Team.BLUE


class CreateSpartan(BaseSpartan):
    """ Create Spartan model. """
    uuid: UUID = Field(default_factory=uuid4)


class UpdateSpartan(BaseSpartan):
    """ Update Spartan model. """
