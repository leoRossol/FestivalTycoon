# SIMULA TUDO
from entities.staff import Services

#CHECKER
def start_check (festival) -> bool:
    if festival.venue is None:
        festival.status = "CANCELLED"
        return False
    else:
        if len(festival.lineup) == 0:
            festival.status = "CANCELLED"
            return False
    return True



#SIM CALCULATIONS
def calculate_hype (festival) -> int:
    avg_popularity = 0
    avg_level = 0
    bonus = 1
    for artist in festival.lineup:
        avg_popularity += artist.reputation
        avg_level += artist.level
    if len(festival.lineup) == 0:
        return 0

    avg_popularity /= len(festival.lineup)
    avg_level /= len(festival.lineup)
    avg_lineup = avg_popularity + 5*(avg_level -1)

    for staff in festival.hired_staff:
        if staff.type == Services.MARKETING:
            bonus = staff.effect_value

    raw_score  = avg_lineup * bonus
    score = min(max(raw_score, 0), 100)
    hype = score / 100
    return hype

def calculate_sold_tickets(festival, hype) -> int:
    sold = int(festival.venue.capacity * hype)
    return sold

#def calculate_performance(festival):


#def calculate_satisfaction(festival, hype):

#def calculate_genre_bonus(festival):


#def apply_results(player, festival):
