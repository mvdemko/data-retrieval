from pydantic import BaseModel

from data_retrieval.usta.tournaments.models.format import Format
from data_retrieval.usta.tournaments.models.gender import Gender
from data_retrieval.usta.tournaments.models.rating import Rating

class Event(BaseModel):
    rating: Rating
    gender: Gender
    format: Format