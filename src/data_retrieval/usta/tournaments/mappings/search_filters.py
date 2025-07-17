from data_retrieval.usta.tournaments.models.category import Category
from data_retrieval.usta.tournaments.models.section import Section

CATEGORY_MAPPING = {
    Category.ADULT: "adult",
    Category.JUNIOR: "junior",
    Category.WHEELCHAIR: "wheelchair",
    Category.WTN: "wtnPlay",
}

SECTION_MAPPING = {
    Section.CARIBBEAN: "5aff543a-dd8f-466e-8848-499b5d92b5e0",
    Section.EASTERN: "2834c4a1-c49f-4fd5-a80e-5a3044260865",
    Section.FLORIDA: "8fe5a334-ff54-492d-a370-d6d9518c2ac1",
    Section.HAWAII_PACIFIC: "5e088f7b-9698-4d12-9340-3e7414e6d3f2",
    Section.INTERMOUNTAIN: "1005a927-0866-44ae-af99-868f7da5e0eb",
    Section.MID_ATLANTIC: "ad5323a2-ffa7-4aca-84e0-d02342b32376",
    Section.MIDDLE_STATES: "990eebd8-7c81-4d48-942f-47857fd97611",
    Section.MIDWEST: "53f40fbc-aebb-46e6-8ca3-128b37fd3404",
    Section.MISSOURI_VALLEY: "7a6b37de-f7a6-49fb-a7f9-131328770863",
    Section.NEW_ENGLAND: "e5b430e8-e07d-48a0-b688-72a147cf1803",
    Section.NORTHERN: "65b038b1-fad0-4ebb-b613-c17c0c2bfb8f",
    Section.NORTHERN_CALIFORNIA: "d2cb6550-b618-4e62-9a40-c798fbd18a35",
    Section.PACIFIC_NW: "0695853f-b87b-44a5-805d-a3c120dd5ea2",
    Section.SOUTHERN: "99c0f41c-0da5-4599-958f-cff312ab2fa2",
    Section.SOUTHERN_CALIFORNIA: "6f20620d-90b5-4a74-bf20-18b0cdd90f98",
    Section.SOUTHWEST: "021009d1-3994-4f79-a384-e6ee24b588a8",
    Section.TEXAS: "7472b77e-f9f3-45f9-9af6-d9ee5b89a866",
    Section.UNASSIGNED: "be33b626-8764-4472-b34f-a77c650e1771",
    Section.NATIONAL: "96a7c92e-92cb-4965-8284-8e5a33761130",
}
