"""The time period during which a tournament occurs."""

from datetime import datetime

from pydantic import BaseModel


class Dates(BaseModel):
    start_date: datetime.date
    end_date: datetime.date

    def __init__(self, **data):
        super().__init__(**data)
        if self.end_date < self.start_date:
            raise ValueError("End date must be after start date")

    def __str__(self):
        """
        Print the time period spanned by the event.

        Returns
        -------
        str
            The formatted string.
        """
        return f"{self.start_date} through {self.end_date}"
