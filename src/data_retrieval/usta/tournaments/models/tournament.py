"""A tennis event sponsored by USTA."""

import re

from pydantic import BaseModel

from data_retrieval.usta.tournaments.models.facility import Facility
from data_retrieval.usta.tournaments.models.player import Player
from data_retrieval.usta.tournaments.models.tournament_status import TournamentStatus


class Tournament(BaseModel):
    """
    A class to represent a tennis event sponsored by USTA.

    Attributes
    ----------
    name : str
        The name of the tournament.
    level : int
        The level of the tournament. Level is a number between 1 and 7 that dictates how many
        points are awarded to participants.
    facility : Facility
        An instance of the Facility class that describes where the event will occur.
    status : str
        Describes whether the tournament is still accepting registrations.
    dates : Dates
        An instance of the Dates class that describes when the event will occur.
    events : list[Events]
        A list of Event instances that provide more details on the events that make up the
        tournament.

    Methods
    -------
    __str__():
        Print the tournament information.
    """

    name: str  # TODO: Separate name and address
    url: str
    facility: Facility
    status: TournamentStatus
    dates: str  # TODO: Parse this and turn into a date object
    players: list[Player]

    def __init__(self, **data):
        super().__init__(**data)
        match = re.search(r"Level\s*(\d+)", self.name)
        if match:
            self.level = int(match.group(1))
