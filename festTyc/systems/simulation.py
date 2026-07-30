# SIMULA TUDO
from entities.staff import Services
from systems import finance
from entities.festival import FestivalStatus
from systems import reputation

#ORQUESTRA TUDO
def simulate_festival(player, festival):
    if not start_check(festival): return
    festival.status = FestivalStatus.SIMULATING
    hype = calculate_hype(festival)
    apply_results(player, festival, hype)
    festival.status = FestivalStatus.DONE


#CHECKER
def start_check (festival) -> bool:
    if festival.venue is None:
        festival.status = FestivalStatus.CANCELLED
        return False
    else:
        if len(festival.lineup) == 0:
            festival.status = FestivalStatus.CANCELLED
            return False
    return True



#SIM CALCULATIONS
def lineup_strength(festival) -> float:
    avg_popularity = 0
    avg_level = 0
    for artist in festival.lineup:
        avg_popularity += artist.reputation
        avg_level += artist.level
    if len(festival.lineup) == 0:
        return 0
    avg_popularity /= len(festival.lineup)
    avg_level /= len(festival.lineup)
    avg_lineup = avg_popularity + 5 * (avg_level - 1)
    return avg_lineup

#def calculate_genre_bonus(festival):

def calculate_hype (festival) -> int:
    bonus = 1
    avg_lineup = lineup_strength(festival)
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


def calculate_performance(festival) -> float:
    if not festival.lineup: return 0
    strength = lineup_strength(festival)
    #TODO aplicar penalidades de evento e outros ajustes depois
    return strength


def calculate_satisfaction(festival, hype) -> float:
    k = 0.7                          # do Cânone; depois vira constante nomeada
    expectation = hype * 100         # traz pra escala 0-100
    delivery = calculate_performance(festival)
    g = delivery - expectation
    s = 50 + k * g
    return min(max(s, 0), 100)       # clamp 0-100, o mesmo idioma do hype


def apply_results(player, festival, hype):
    festival.sold_tickets = calculate_sold_tickets(festival, hype)
    festival.total_earnings = finance.calculate_total_earnings(festival)
    festival.profit = finance.calculate_profit(festival)
    festival.crowd_satisfaction = calculate_satisfaction(festival, hype)
    #festival.genre_bonus
    reputation.update_artist_rep(festival)
    reputation.update_player_rep(player, festival)




