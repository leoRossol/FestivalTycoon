# GERENCIA O QUE CABE AO PLANEJAMENTO
from entities import festival
from systems import finance
from entities.artist import Artist
from entities.staff import Staff
from entities.venue import Venue

#LISTING
def get_available_artists(player, artists: list[Artist], festival) -> list[Artist]:
    available = []
    for artist in artists:
        if artist_booking(player, artist) and artist not in festival.lineup:
            available.append(artist)
    return available

def get_fixed(player, available_artists, festival) -> list[Artist]:
    available = get_available_artists(player, available_artists, festival)
    fixed = []
    for artist in available:
        if big_star(artist, player):
            fixed.append(artist)
    return fixed

def get_rotation(player, artists, festival) -> list[Artist]:
    available = get_available_artists(player, artists, festival)
    fixed = [a for a in available if big_star(a, player)]
    pool = [a for a in available if a not in fixed]
    return pool

def get_available_staff(player, staffs: list[Staff], festival) -> list[Staff]:
    available = []
    for staff in staffs:
        if staff_booking(player, staff) and staff not in festival.hired_staff:
            available.append(staff)
    return available

def get_available_venue(player, venues: list[Venue]) -> list[Venue]:
    available = []
    for venue in venues:
        if venue_booking(player, venue):
            available.append(venue)
    return available



#HIRING
def add_artist(player, artist, festival) -> bool:
    if not artist_booking(player, artist):
        return False
    elif artist in festival.lineup:
        return False
    if not finance.player_pay(player, artist.fee):
        return False
    festival.lineup.append(artist)
    return True

def add_venue (player, venue, festival) -> bool:
    if not venue_booking(player, venue):
        return False
    if festival.venue is not None:
        return False
    if not finance.player_pay(player, venue.rent):
        return False
    festival.venue = venue
    return True

def add_staff (player, staff, festival) -> bool:
    if not staff_booking(player, staff):
        return False
    for hired in festival.hired_staff:
        if hired.type == staff.type:
            return False
    if not finance.player_pay(player, staff.cost):
        return False
    festival.hired_staff.append(staff)
    return True



#REMOVING
def remove_artist(player, artist, festival) -> bool:
    if artist in festival.lineup:
        festival.lineup.remove(artist)
        finance.player_get(player, artist.fee)
        return True
    else:
        return False

def remove_venue(player, venue, festival) -> bool:
    if venue is festival.venue:
        festival.venue = None
        finance.player_get(player, venue.rent)
        return True
    else:
        return False

def remove_staff(player, staff, festival) -> bool:
    if staff in festival.hired_staff:
        festival.hired_staff.remove(staff)
        finance.player_get(player, staff.cost)
        return True
    else:
        return False



#INVESTING
def venue_invest(player, venue, amount: float) -> bool:
    if venue.quality < 5 and player.reputation >= 50:
        if finance.player_pay(player, amount):
            venue.reputation += amount * 0.50
            if venue.reputation >= 100:
                venue.reputation -= 100
                venue.quality += 1
            return True
    return False



#CANCELLING
def cancel_festival(festival):
    festival.status = "CANCELED"



#HELPERS
def artist_booking(player, artist) -> bool:
    if artist.is_retired: return False
    else:
        if artist.reputation > player.reputation: return False
    return True

def staff_booking(player, staff) -> bool:
    if staff.min_reputation > player.reputation: return False
    return True

def venue_booking(player, venue) -> bool:
    if venue.reputation > player.reputation: return False
    return True

def big_star(artist, player):
    if player.reputation <= 25:
        return artist.level >= 3
    elif player.reputation <= 50:
        return artist.level >= 4
    elif player.reputation <= 75:
        return artist.level >= 5
    else: return artist.level >= 5