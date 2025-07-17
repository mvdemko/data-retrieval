"""Information about where a tennis tournament occurs."""

from pydantic import BaseModel

from data_retrieval.usta.tournaments.models.district import District
from data_retrieval.usta.tournaments.models.section import Section

DISTRICT_SECTIONS = {
    District["PUERTO_RICO"]: Section["CARIBBEAN"],
    District["VIRGIN_ISLANDS"]: Section["CARIBBEAN"],
    District["LONG_ISLAND_REGION"]: Section["EASTERN"],
    District["METROPOLITAN_REGION"]: Section["EASTERN"],
    District["NEW_JERSEY_REGION"]: Section["EASTERN"],
    District["NORTHERN_REGION"]: Section["EASTERN"],
    District["SOUTHERN_REGION"]: Section["EASTERN"],
    District["WESTERN_REGION"]: Section["EASTERN"],
    District["REGION_1"]: Section["FLORIDA"],
    District["REGION_2"]: Section["FLORIDA"],
    District["REGION_3"]: Section["FLORIDA"],
    District["REGION_4"]: Section["FLORIDA"],
    District["REGION_5"]: Section["FLORIDA"],
    District["REGION_6"]: Section["FLORIDA"],
    District["REGION_7"]: Section["FLORIDA"],
    District["REGION_8"]: Section["FLORIDA"],
    District["AMERICAN_SAMOA_GUAM"]: Section["HAWAII_PACIFIC"],
    District["EAST_HAWAII"]: Section["HAWAII_PACIFIC"],
    District["KAUAI"]: Section["HAWAII_PACIFIC"],
    District["MAUI"]: Section["HAWAII_PACIFIC"],
    District["OAHU"]: Section["HAWAII_PACIFIC"],
    District["WEST_HAWAII"]: Section["HAWAII_PACIFIC"],
    District["COLORADO"]: Section["INTERMOUNTAIN"],
    District["IDAHO"]: Section["INTERMOUNTAIN"],
    District["MONTANA"]: Section["INTERMOUNTAIN"],
    District["NEVADA"]: Section["INTERMOUNTAIN"],
    District["UTAH"]: Section["INTERMOUNTAIN"],
    District["WYOMING"]: Section["INTERMOUNTAIN"],
    District["MARYLAND"]: Section["MID_ATLANTIC"],
    District["VIRGINIA"]: Section["MID_ATLANTIC"],
    District["WASHINGTON_DC"]: Section["MID_ATLANTIC"],
    District["WEST_VIRGINIA"]: Section["MID_ATLANTIC"],
    District["ALLEGHENY_MOUNTAIN"]: Section["MIDDLE_STATES"],
    District["CENTRAL_PENNSYLVANIA"]: Section["MIDDLE_STATES"],
    District["DELAWARE"]: Section["MIDDLE_STATES"],
    District["EASTERN_PENNSYLVANIA"]: Section["MIDDLE_STATES"],
    District["NEW_JERSEY"]: Section["MIDDLE_STATES"],
    District["PHILADELPHIA"]: Section["MIDDLE_STATES"],
    District["CENTRAL_INDIANA"]: Section["MIDWEST"],
    District["CHICAGO"]: Section["MIDWEST"],
    District["MID_SOUTH_ILLINOIS_TENNIS_ASSOCIATION"]: Section["MIDWEST"],
    District["NE_MICHIGAN"]: Section["MIDWEST"],
    District["NORTHEASTERN_OHIO"]: Section["MIDWEST"],
    District["NORTHERN_ILLINOIS"]: Section["MIDWEST"],
    District["NORTHERN_INDIANA"]: Section["MIDWEST"],
    District["NORTHERN_MICHIGAN"]: Section["MIDWEST"],
    District["NORTHWESTERN_OHIO"]: Section["MIDWEST"],
    District["OHIO_VALLEY"]: Section["MIDWEST"],
    District["SE_MICHIGAN"]: Section["MIDWEST"],
    District["WESTERN_MICHIGAN"]: Section["MIDWEST"],
    District["WISCONSIN"]: Section["MIDWEST"],
    District["HEART_OF_AMERICA"]: Section["MISSOURI_VALLEY"],
    District["IOWA"]: Section["MISSOURI_VALLEY"],
    District["KANSAS"]: Section["MISSOURI_VALLEY"],
    District["MISSOURI"]: Section["MISSOURI_VALLEY"],
    District["NEBRASKA"]: Section["MISSOURI_VALLEY"],
    District["OKLAHOMA"]: Section["MISSOURI_VALLEY"],
    District["ST_LOUIS"]: Section["MISSOURI_VALLEY"],
    District["CONNECTICUT"]: Section["NEW_ENGLAND"],
    District["EASTERN_MASSACHUSETTS"]: Section["NEW_ENGLAND"],
    District["MAINE"]: Section["NEW_ENGLAND"],
    District["NEW_HAMPSHIRE"]: Section["NEW_ENGLAND"],
    District["RHODE_ISLAND"]: Section["NEW_ENGLAND"],
    District["VERMONT"]: Section["NEW_ENGLAND"],
    District["WESTERN_MASSACHUSETTS"]: Section["NEW_ENGLAND"],
    District["MEMBER"]: Section["NORTHERN"],
    District["NORTHERN_CALIFORNIA"]: Section["NORTHERN_CALIFORNIA"],
    District["ALASKA"]: Section["PACIFIC_NW"],
    District["BRITISH_COLUMBIA"]: Section["PACIFIC_NW"],
    District["EASTERN_WASHINGTON"]: Section["PACIFIC_NW"],
    # District["IDAHO"]: Section["PACIFIC_NW"],
    District["NORTHERN_OREGON"]: Section["PACIFIC_NW"],
    District["NORTHWEST_WASHINGTON"]: Section["PACIFIC_NW"],
    District["SOUTHERN_OREGON"]: Section["PACIFIC_NW"],
    District["SOUTHWEST_WASHINGTON"]: Section["PACIFIC_NW"],
    District["ALABAMA"]: Section["SOUTHERN"],
    District["ARKANSAS"]: Section["SOUTHERN"],
    District["GEORGIA"]: Section["SOUTHERN"],
    District["KENTUCKY"]: Section["SOUTHERN"],
    District["LOUISIANA"]: Section["SOUTHERN"],
    District["MISSISSIPPI"]: Section["SOUTHERN"],
    District["NORTH_CAROLINA"]: Section["SOUTHERN"],
    District["SOUTH_CAROLINA"]: Section["SOUTHERN"],
    District["TENNESSEE"]: Section["SOUTHERN"],
    District["SAN_DIEGO"]: Section["SOUTHERN_CALIFORNIA"],
    District["SOUTHERN_CALIFORNIA"]: Section["SOUTHERN_CALIFORNIA"],
    District["CENTRAL_ARIZONA"]: Section["SOUTHWEST"],
    District["GREATER_EL_PASO"]: Section["SOUTHWEST"],
    District["NORTHERN_ARIZONA"]: Section["SOUTHWEST"],
    District["NORTHERN_NEW_MEXICO"]: Section["SOUTHWEST"],
    District["SOUTHERN_ARIZONA"]: Section["SOUTHWEST"],
    District["SOUTHERN_NEW_MEXICO"]: Section["SOUTHWEST"],
    District["UNASSIGNED"]: Section["UNASSIGNED"],
    District["NATIONAL"]: Section["NATIONAL"],
}


class Facility(BaseModel):
    location: str
    section: Section = None
    district: District = None

    def __init__(self, **data):
        """
        Construct all the necessary attributes for the facility object.

        Parameters
        ----------
        location : str
            The name and address of the facility.
        district : str
            The district in which the facility is located. District is subdivision of section.
            Texas is the only section that is not subdivided into smaller sections. Idaho
            is associated with two different sections (Pacific NW and Intermountain); we will
            assign Idaho to the Intermountain section.
        section : str
            The section in which the facility is located.

        Returns
        -------
        None
        """
        super().__init__(**data)
        if self.district is not None:
            self.section = DISTRICT_SECTIONS[self.district]

    def __str__(self):
        """
        Print the facility details.

        Returns
        -------
        str
            The facility details.
        """
        description = (
            f"Section: {self.section.value}\n"
            f"District: {self.district.value}\n"
            f"Facility: {self.name} {self.address}"
        )

        return description
