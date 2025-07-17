"""The competitive format of an event at a tennis tournament."""

from enum import Enum


class Format(Enum):
    """
    A subclass of enumeration used to represent an event format.

    Format can be singles (1 v 1) or doubles (2 v 2).
    """

    SINGLES = "Singles"
    DOUBLES = "Doubles"
