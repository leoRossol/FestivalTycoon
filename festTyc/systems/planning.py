##TUDO QUE ACONTECE NA FASE DE PLANEJAMENTO
from entities.festival import FestivalStatus


##DISPONIBILIDADE
def get_available_artists (player, all_artists):
    available = []
    for artist in all_artists:
        if artist_booking(artist, player):
            available.append(artist)
    return available

def get_available_venues(player, all_venues):
    available = []
    for venue in all_venues:
        if venue_booking(venue, player):
            available.append(venue)
    return available

def get_available_staff(player, all_staff):
    available= []
    for staff in all_staff:
        if staff_booking(staff, player):
            available.append(staff)
    return available

##ADICIONAR AO FESTIVAL
def add_artist(festival, artist, player) -> bool:
    if artist_booking(artist, player):
        festival.lineup.append(artist)
        return True
    return False

def add_staff(festival, staff, player) -> bool:
    if staff_booking(staff, player):
        festival.hiredStaff.append(staff)
        return True
    return False

def add_venue(festival, venue, player) -> bool:
    if venue_booking(venue, player):
        festival.venue = venue
        return True
    return False

## CANCELAR
def cancel(festival):
    if festival.status == FestivalStatus.DONE:
        return
    festival.status = FestivalStatus.CANCELLED

## REGRAS
def artist_booking(artist, player) -> bool:
    if player.reputation <= artist.reputation // 2:
        return False
    return True

def venue_booking(venue, player) -> bool:
    if player.reputation <= venue.reputation // 2:
        return False
    return True

def staff_booking(staff, player) -> bool:
    if player.reputation < staff.min_reputation:
        return False
    return True
