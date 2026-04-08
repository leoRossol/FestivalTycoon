# CONTROLA DINHEIRO DO JOGO
from entities.staff import Services

# called in planning
def player_pay(player, amount: float) -> bool:
    if player.money < amount:
        return False
    else: player.money -= amount
    return True

# called in planning
def player_get(player, amount: float) -> bool:
    player.money += amount
    return True

def set_ticket_price(festival, amount: float) -> bool:
    festival.ticket_price = amount
    return True

# called during simulation phase
def calculate_sold_tickets(festival) -> int:
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
    rate = score / 100
    sold = int(festival.venue.capacity * rate)
    return sold

# callled in result screen
def calculate_total_earnings(festival) -> float:
    total = calculate_sold_tickets(festival) * festival.ticket_price
    return total

# called in planning/result screen
def calculate_total_costs(festival):
    artist_cost = 0
    staff_cost = 0
    for artist in festival.lineup:
        artist_cost += artist.fee
    for staff in festival.hired_staff:
        staff_cost += staff.cost
    total_cost = artist_cost + staff_cost + festival.venue.rent
    return total_cost, artist_cost, staff_cost, festival.venue.rent

# called in result screen
def calculate_profit (festival) -> float:
    total_cost, artist_fee, staff_cost, venue_rent = calculate_total_costs(festival)
    profit = calculate_total_earnings(festival) - total_cost
    return profit

