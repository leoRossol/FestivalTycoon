from systems import finance
from systems import reputation
from entities.festival import FestivalStatus

def simulate_festival(player, festival):

    if not venue_check(festival):
        festival.status = FestivalStatus.CANCELLED
        return

    calculate_crowd_satisfaction(festival)
    finance.apply_earnings(festival, player)
    reputation.apply_reputation(player, festival)
    festival.status = FestivalStatus.DONE

def calculate_crowd_satisfaction(festival):
    satisfaction = 0
    for artist in festival.lineup:
        satisfaction += artist.reputation
    satisfaction = satisfaction / len(festival.lineup)

    for staff in festival.hiredStaff:
        satisfaction += staff.effect_value

    satisfaction += festival.venue.reputation
    festival.crowdSatisfaction = min(max(satisfaction, 0), 100)

def venue_check(festival):
    if festival.venue is None:
        return False
    return True