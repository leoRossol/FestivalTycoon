import json
from pathlib import Path
from zoneinfo import available_timezones

from entities.artist import Artist, MusicGenre
from entities.venue import Venue, Locations
from entities.staff import Staff, Services
from entities.player import Player
from entities.festival import Festival, FestivalStatus

from systems import planning
from systems import finance
from systems import simulation


DATA_DIR = Path("data")

def load_artists() -> list[Artist]:
    path = DATA_DIR / "artists.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    artists: list[Artist] = []
    for item in raw_list:
        name = item["name"]
        genre_str = item["genre"]
        genre = MusicGenre[genre_str]
        reputation = item["reputation"]
        fee = item["fee"]

        artist = Artist(
            name=name,
            genre=genre,
            reputation=reputation,
            fee=fee
        )
        artists.append(artist)
        return artists


def load_venues() -> list[Venue]:
    path = DATA_DIR / "venues.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    venues: list[Artist] = []
    for item in raw_list:
        name = item["name"]
        quality = item["quality"]
        capacity = item["capacity"]
        rent = item["rent"]
        reputation = item["reputation"]
        location_str = item["location"]
        location = Locations[location_str]

        venue = Venue(
            name=name,
            quality=quality,
            capacity=capacity,
            rent=rent,
            reputation=reputation,
            location=location
        )
        venues.append(venue)
        return venues


def load_staff() -> list[Staff]:
    path = DATA_DIR / "staff.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    staff_list: list[Staff] = []
    for item in raw_list:
        type_str = item["type"]
        service_type = Services[type_str]
        level = item["level"]
        cost = item["cost"]
        effect_value = item["effect_value"]
        min_reputation = item["min_reputation"]

        staff_member = Staff(
            type=service_type,
            level=level,
            cost=cost,
            effect_value=effect_value,
            min_reputation=min_reputation
        )
        staff_list.append(staff_member)
        return staff_list

def create_initial_player() -> Player:
    return Player(
        name= "Crash T. Dummy",
        money= 10_000.00,
        reputation= 50,
    )

def create_empty_festival(name: str) -> Festival:
    return Festival(
        name=name,
        status=FestivalStatus.PLANNING,
        ticketPrice=0,
        venue=None,
        soldTickets=0,
        totalEarnings=0,
        profit=0,
        crowdSatisfaction=0,
        lineup=[],
        hiredStaff=[]
    )

def plan_festival(player: Player, festival: Festival,
                  artists: list[Artist],
                  venues: list[Venue],
                  staff_list: list[Staff]) -> None:

    # ESCOLHER VENUE
    available_venues = planning.get_available_venues(player, venues)
    if not available_venues:
        print("No available venues")
        return
    choosen_venue = available_venues[0]
    added = planning.add_venue(festival, choosen_venue, player)
    if not added:
        print("Nao foi possivel add venue")
        return

    # ESCOLHER ARTISTAS
    available_artists = planning.get_available_artists(player, artists)
    if not available_artists:
        print("No available artists")
        return
    for artist in available_artists[:2]:
        planning.add_artist(festival, artist, player)

    # contratar staff
    if staff_list:
        available_staff = planning.get_available_staff(player, staff_list)
        for staff_member in available_staff[:1]:
            planning.add_staff(festival, staff_member, player)

    # preço do ingresso
    finance.set_ticket_price(festival, price=100.0)


def main():
    # Carregar dados dos JSONs
    artists = load_artists()
    venues = load_venues()
    staff_list = load_staff()  # pode vir vazio se não tiver JSON

    #player e festival
    player = create_initial_player()
    festival = create_empty_festival("MVP Fest")

    #planejar o festival
    plan_festival(player, festival, artists, venues, staff_list)

    #rodar a simulação
    simulation.simulate_festival(player, festival)

    # 5) Mostrar resultados
    print("\n=== RESULTADO DA SIMULAÇÃO ===")
    print("\nPlayer:")
    print(player)

    print("\nFestival:")
    print(festival)


if __name__ == "__main__":
    main()