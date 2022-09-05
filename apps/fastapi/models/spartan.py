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

class Spartan(BaseModel):
    """ Spartan model. """
    uuid: typing.Optional[UUID] = Field(default_factory=uuid4)
    name: str
    age: int
    team: typing.Optional[Team] = Team.BLUE
