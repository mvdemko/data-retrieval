"""Participant groupings for tournament events."""

from enum import Enum


class Gender(Enum):
    """
    A subclass of enumeration used to represent the genders that participate in a tournament event.

    Mixed means men and women participate together.
    """

    MEN = "Men's"
    WOMEN = "Women's"
    MIXED = "Mixed"
