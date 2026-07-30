# player reputation must go up or down depeding on the success of the festival
REP_GAIN = 5
MAX_GAIN = 10
MAX_LOSS = 20


def update_artist_rep(festival):
    s = festival.crowd_satisfaction
    for artist in festival.lineup:
        if s > 70:
            artist.reputation = min(artist.reputation + REP_GAIN, 100)
        elif s < 40:
            artist.reputation = max(artist.reputation - REP_GAIN, 0)


def update_player_rep(player, festival):
    s = festival.crowd_satisfaction
    if s >= 50:
        change = (s - 50) / 50 * MAX_GAIN
    else:
        change = (50 - s) / 50 * -MAX_LOSS
    player.reputation = min(max(player.reputation + change, 0), 100)