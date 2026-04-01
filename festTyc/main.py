from entities.artist import Artist, MusicGenre
from entities.venue import Venue, Locations
from entities.staff import Staff, Services
from entities.player import Player
from entities.festival import Festival, FestivalStatus

from systems import planning
from systems import finance
from systems import simulation

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