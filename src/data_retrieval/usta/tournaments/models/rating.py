"""USTA-defined NTRP ratings used to group participants in tournament events and leagues."""

from enum import Enum


class Rating(Enum):
    NTRP_1_5 = 1.5
    NTRP_2_0 = 2.0
    NTRP_2_5 = 2.5
    NTRP_3_0 = 3.0
    NTRP_3_5 = 3.5
    NTRP_4_0 = 4.0
    NTRP_4_5 = 4.5
    NTRP_5_0 = 5.0
    NTRP_5_5 = 5.5
    NTRP_6_0 = 6.0
    NTRP_6_5 = 6.5
    NTRP_7_0 = 7.0
