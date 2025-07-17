import argparse
import logging

from data_retrieval.usta.tournaments import client as tournament_client
from data_retrieval.usta.tournaments.models.category import Category
from data_retrieval.usta.tournaments.models.section import Section

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)

SUPPORTED_OPTIONS = ["tournaments"]


def main(args):
    if args.data == "tournaments":
        parameter_list = args.parameters[0].split(",")
        if len(parameter_list) != 2:
            raise ValueError(
                "Invalid number of parameters provided. Category and Section are expected."
            )
        try:
            category = Category(parameter_list[0])
        except ValueError:
            categories = [category.value for category in Category]
            logging.error(f"Invalid category provided. Valid options are: {categories}")
        else:
            try:
                section = Section(parameter_list[1])
            except ValueError:
                sections = [section.value for section in Section]
                logging.error(
                    f"Invalid section provided. Valid options are: {sections}"
                )
            else:
                return tournament_client.fetch_tournaments(category, section)
    else:
        raise ValueError(
            f"Function not supported. Valid options are: {SUPPORTED_OPTIONS.join(' ')}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="data_retrieval",
        description="Retrieve data from various sources.",
    )
    parser.add_argument(
        "data", help="The type of data to retrieve.", choices=SUPPORTED_OPTIONS
    )
    parser.add_argument(
        "parameters",
        nargs="*",
        help="A comma-separated list of parameters to use for data retrieval",
    )

    args = parser.parse_args()
    main(args)
