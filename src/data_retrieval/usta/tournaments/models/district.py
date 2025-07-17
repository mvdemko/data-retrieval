"""The smallest subdivision of a region defined by USTA."""

from enum import Enum


class District(Enum):
    """
    A subclass of enumeration used to represent a USTA district.

    Districts are defined by USTA. Most, but not all (e.g., Texas), sections are subdivided into
    districts.
    """

    # Caribbean
    PUERTO_RICO = "Puerto Rico"
    VIRGIN_ISLANDS = "Virgin Islands"

    # Eastern
    LONG_ISLAND_REGION = "Long Island"
    METROPOLITAN_REGION = "Metropolitan"
    NEW_JERSEY_REGION = "New Jersey"
    NORTHERN_REGION = "Northern"
    SOUTHERN_REGION = "Southern"
    WESTERN_REGION = "Western"

    # Florida
    REGION_1 = "Region 1"
    REGION_2 = "Region 2"
    REGION_3 = "Region 3"
    REGION_4 = "Region 4"
    REGION_5 = "Region 5"
    REGION_6 = "Region 6"
    REGION_7 = "Region 7"
    REGION_8 = "Region 8"

    # Hawaii Pacific
    AMERICAN_SAMOA_GUAM = "American Samoa-Guam"
    EAST_HAWAII = "East Hawaii"
    KAUAI = "Kauai"
    MAUI = "Maui"
    OAHU = "Oahu"
    WEST_HAWAII = "West Hawaii"

    # Intermountain
    COLORADO = "Colorado"
    IDAHO = "Idaho"
    MONTANA = "Montana"
    NEVADA = "Nevada"
    UTAH = "Utah"
    WYOMING = "Wyoming"

    # Mid-Atlantic
    MARYLAND = "Maryland"
    VIRGINIA = "Virginia"
    WASHINGTON_DC = "Washington, DC"
    WEST_VIRGINIA = "West Virginia"

    # Middle States
    ALLEGHENY_MOUNTAIN = "Allegheny Mountain"
    CENTRAL_PENNSYLVANIA = "Central Pennsylvania"
    DELAWARE = "Delaware"
    EASTERN_PENNSYLVANIA = "Eastern Pennsylvania"
    NEW_JERSEY = "New Jersey"
    PHILADELPHIA = "Philadelphia"

    # Midwest
    CENTRAL_INDIANA = "Central Indiana"
    CHICAGO = "Chicago"
    MID_SOUTH_ILLINOIS_TENNIS_ASSOCIATION = "Mid-South Illinois Tennis Association"
    NE_MICHIGAN = "Northeast Michigan"
    NORTHEASTERN_OHIO = "Northeastern Ohio"
    NORTHERN_ILLINOIS = "Northern Illinois"
    NORTHERN_INDIANA = "Northern Indiana"
    NORTHERN_MICHIGAN = "Northern Michigan"
    NORTHWESTERN_OHIO = "Northwestern Ohio"
    OHIO_VALLEY = "Ohio Valley"
    SE_MICHIGAN = "Southeast Michigan"
    WESTERN_MICHIGAN = "Western Michigan"
    WISCONSIN = "Wisconsin"

    # Missouri Valley
    HEART_OF_AMERICA = "Heart of America"
    IOWA = "Iowa"
    KANSAS = "Kansas"
    MISSOURI = "Missouri"
    NEBRASKA = "Nebraska"
    OKLAHOMA = "Oklahoma"
    ST_LOUIS = "St. Louis"

    # New England
    CONNECTICUT = "Connecticut"
    EASTERN_MASSACHUSETTS = "Eastern Massachusetts"
    MAINE = "Maine"
    NEW_HAMPSHIRE = "New Hampshire"
    RHODE_ISLAND = "Rhode Island"
    VERMONT = "Vermont"
    WESTERN_MASSACHUSETTS = "Western Massachusetts"

    # Northern
    MEMBER = "Member"

    # Northern California
    NORTHERN_CALIFORNIA = "Northern California"

    # Pacific Northwest
    ALASKA = "Alaska"
    BRITISH_COLUMBIA = "British Columbia"
    EASTERN_WASHINGTON = "Eastern Washington"
    # IDAHO already defined
    NORTHERN_OREGON = "Northern Oregon"
    NORTHWEST_WASHINGTON = "Northwest Washington"
    SOUTHERN_OREGON = "Southern Oregon"
    SOUTHWEST_WASHINGTON = "Southwest Washington"

    # Southern
    ALABAMA = "Alabama"
    ARKANSAS = "Arkansas"
    GEORGIA = "Georgia"
    KENTUCKY = "Kentucky"
    LOUISIANA = "Louisiana"
    MISSISSIPPI = "Mississippi"
    NORTH_CAROLINA = "North Carolina"
    SOUTH_CAROLINA = "South Carolina"
    TENNESSEE = "Tennessee"

    # Southern California
    SAN_DIEGO = "San Diego"
    SOUTHERN_CALIFORNIA = "Southern California"

    # Southwest
    CENTRAL_ARIZONA = "Central Arizona"
    GREATER_EL_PASO = "Greater El Paso"
    NORTHERN_ARIZONA = "Northern Arizona"
    NORTHERN_NEW_MEXICO = "Northern New Mexico"
    SOUTHERN_ARIZONA = "Southern Arizona"
    SOUTHERN_NEW_MEXICO = "Southern New Mexico"

    # Unassigned
    UNASSIGNED = "Unassigned"

    # National
    NATIONAL = "National"
