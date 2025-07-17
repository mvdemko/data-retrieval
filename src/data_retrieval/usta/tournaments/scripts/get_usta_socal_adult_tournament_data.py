from data_retrieval.usta.tournaments import client as tournament_client
from data_retrieval.usta.tournaments.models.category import Category
from data_retrieval.usta.tournaments.models.section import Section


def main():
    return tournament_client.fetch_tournaments(Category.ADULT, Section.SOUTHERN_CALIFORNIA)