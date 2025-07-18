import logging
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from data_retrieval.usta.tournaments.mappings.search_filters import (
    CATEGORY_MAPPING,
    SECTION_MAPPING,
)
from data_retrieval.usta.tournaments.models.category import Category
from data_retrieval.usta.tournaments.models.facility import Facility
from data_retrieval.usta.tournaments.models.gender import Gender
from data_retrieval.usta.tournaments.models.player import Player
from data_retrieval.usta.tournaments.models.section import Section
from data_retrieval.usta.tournaments.models.tournament import Tournament
from data_retrieval.usta.tournaments.models.tournament_status import TournamentStatus

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


BASE_URL = "https://playtennis.usta.com"


def fetch_tournaments(category: Category, section: Section) -> list[Tournament]:
    driver = get_webdriver()
    search_url = construct_search_url(category, section)

    try:
        driver.get(search_url)
        click_search_button(driver)
        expand_search_results(driver)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        results = soup.find("div", class_="csa-results")
        tournaments = results.find_all("div", class_="csa-search-result-item")
        logging.info(f"{len(tournaments)} tournaments found")

        return get_tournaments(tournaments, driver)

    finally:
        # Close the WebDriver
        driver.quit()


def get_tournaments(
    search_results: list, driver: ChromeDriverManager
) -> list[Tournament]:
    tournaments = []
    for entry in search_results:
        descriptions = entry.find_all("div", class_="csa-description")
        title = descriptions[0].find("h3", class_="csa-title").text.strip()

        a_tag = entry.find("a")
        title = a_tag.text.strip()
        tournament_url = BASE_URL + a_tag["href"]

        address = descriptions[0].find("p", class_="csa-location").text.strip()
        facility = Facility.model_validate({"location": address})

        dates = descriptions[0].find("li", class_="csa-date-v2").text.strip()
        tournament_status = get_tournament_status(descriptions)

        if tournament_status == TournamentStatus.REGISTRATIONS_OPEN:
            tournament_players_url = tournament_url.replace("Overview", "Players")
            try:
                players = get_tournament_players(tournament_players_url, driver)
                tournament = Tournament.model_validate(
                    {
                        "name": title,
                        "url": tournament_url,
                        "facility": facility,
                        "status": tournament_status,
                        "dates": dates,
                        "players": players,
                    }
                )
                tournaments.append(tournament)
            except Exception as e:
                print(f"Failed to retrieve tournament data: {e}")


def get_tournament_players(
    tournament_players_url: str, driver: ChromeDriverManager
) -> list[Player]:
    driver.get(tournament_players_url)
    time.sleep(2)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    players = []
    player_table = soup.find("table", id="player-list")
    if player_table:
        for entry in player_table.find_all("tr"):
            table_data = entry.find("td", class_="_alignLeft_1nqit_268")
            if table_data:
                players.append(get_player_information(table_data))

    return players


# @TODO: Fix type declaration
def get_player_information(table_data) -> Player:
    strong = table_data.find("strong")
    if strong and strong.a:
        name = strong.a.text.strip()
        event_td = table_data.find_next_sibling("td", class_="_alignLeft_1nqit_268")
        events = event_td.get_text(separator=",", strip=True) if event_td else ""
        valid_events = get_valid_events(events)
        player = Player.model_validate({"name": name, "events": valid_events})

        return player


def get_tournament_status(descriptions: str) -> TournamentStatus:
    registration_info = descriptions[1].find("div", class_="csa-registration")
    registration_status = registration_info.find("p", class_="csa-status").text.strip()

    return TournamentStatus(registration_status)


def expand_search_results(driver: ChromeDriverManager) -> None:
    path = (
        "//div[@class='csa-show-more-wrap']//"
        "button[contains(text(), 'Show more results')]"
    )
    while True:
        try:
            show_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, path))
            )
            show_more_button.click()
            time.sleep(2)
        except Exception:
            break


def click_search_button(driver: ChromeDriverManager) -> None:
    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button-text"))
        )
        search_button.click()
        time.sleep(2)
    except Exception as e:
        print("Search button not found or error:", e)


def get_webdriver() -> ChromeDriverManager:
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_setting_values.geolocation": 2  # 1: allow, 2: block,
    }
    chrome_options.add_argument("--headless=new")
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def construct_search_url(category: Category, section: Section) -> str:
    return (
        BASE_URL + "/tournaments?panel=section"
        "&level-category="
        + CATEGORY_MAPPING[category]
        + "&organisation-group="
        + SECTION_MAPPING[section]
    )


def get_valid_events(events: str) -> list[str]:
    original_list = events.split(",")
    return [x for x in original_list if _is_valid_event(x)]


def _is_valid_event(text: str) -> bool:
    return (
        text.startswith(Gender.MEN.value)
        or text.startswith(Gender.WOMEN.value)
        or text.startswith(Gender.MIXED.value)
    )
