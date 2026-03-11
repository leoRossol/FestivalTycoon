from entities.artist import Artist
from entities.venue import Venue

# PRECO DE ARTISTAS E VENUES + DISPO

def get_available_artists (player, all_artists):
    available = []
    for artist in all_artists:
        if artist.accepts_booking(player):
            available.append(artist)
    return available

def get_available_venues(all_venues):
    available = []
    for venue in all_venues:
        if venue.is_available():
            available.append(venue)
    return available

def get_available_staff(player, all_staff):
    available= []
    for staff in all_staff:
        if staff.is_unlocked(player):
            available.append(staff)
    return available