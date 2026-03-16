from entities import player
from entities.player import Player
from entities.festival import Festival

# ATUALIZA REP DO PLAYER, POPULARIDADE DE ARTISTAS E VENUE
def apply_reputation(player, festival):
    satisfaction = festival.crowdSatisfaction
    delta = 0
    if satisfaction == 100: delta += 10
    elif satisfaction >= 80: delta += +5
    elif satisfaction >= 60: delta += 2
    elif satisfaction >= 50: delta += 0
    elif satisfaction >= 30: delta -= 2
    else: delta -= 5
    player.update_reputation(delta)
    artist_delta = round(delta * 0.75)
    venue_delta = round(delta * 0.50)
    for artist in festival.lineup:
        artist.change_popularity(artist_delta)
    festival.venue.change_popularity(venue_delta)
