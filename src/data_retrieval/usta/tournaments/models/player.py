from pydantic import BaseModel


class Player(BaseModel):
    name: str
    events: list[str]
