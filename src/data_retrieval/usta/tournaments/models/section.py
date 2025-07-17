"""Subdivisions of United States and its territories defined by USTA."""

from enum import Enum


class Section(Enum):
    """
    A subclass of enumeration used to represent a USTA section.

    Sections are defined by USTA.
    """

    CARIBBEAN = "Caribbean"
    EASTERN = "Eastern"
    FLORIDA = "Florida"
    HAWAII_PACIFIC = "Hawaii-Pacific"
    INTERMOUNTAIN = "Intermountain"
    MID_ATLANTIC = "Mid-Atlantic"
    MIDDLE_STATES = "Middle States"
    MIDWEST = "Midwest"
    MISSOURI_VALLEY = "Missouri Valley"
    NEW_ENGLAND = "New England"
    NORTHERN = "Northern"
    NORTHERN_CALIFORNIA = "Northwen California"
    PACIFIC_NW = "Pacific Northwest"
    SOUTHERN = "Southern"
    SOUTHERN_CALIFORNIA = "Southern California"
    SOUTHWEST = "Southwest"
    TEXAS = "Texas"
    UNASSIGNED = "Unassigned"
    NATIONAL = "National"
