"""A tennis event sponsored by USTA."""

import re

from pydantic import BaseModel

from data_retrieval.usta.tournaments.models.facility import Facility
from data_retrieval.usta.tournaments.models.player import Player
from data_retrieval.usta.tournaments.models.tournament_status import TournamentStatus


class Tournament(BaseModel):
    name: str  # TODO: Separate name and address
    url: str
    facility: Facility
    status: TournamentStatus
    dates: str  # TODO: Parse this and turn into a date object
    players: list[Player]