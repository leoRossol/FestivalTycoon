# player reputation must go up or down depeding on the success of the festival
REP_GAIN = 5


def update_artist_rep(festival):
    s = festival.crowd_satisfaction
    for artist in festival.lineup:
        if s > 70:
            artist.reputation = min(artist.reputation + REP_GAIN, 100)
        elif s < 40:
            artist.reputation = max(artist.reputation - REP_GAIN, 0)
