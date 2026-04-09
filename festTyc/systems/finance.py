# CONTROLA DINHEIRO DO JOGO
from systems import simulation

#PLAYER MONEY
def player_pay(player, amount: float) -> bool:
    if player.money < amount:
        return False
    else: player.money -= amount
    return True

def player_get(player, amount: float) -> bool:
    player.money += amount
    return True



#TICKET PRICE
def set_ticket_price(festival, amount: float) -> bool:
    festival.ticket_price = amount
    return True



#CALCULATIONS
def calculate_total_earnings(festival) -> float:
    total = simulation.calculate_sold_tickets(festival) * festival.ticket_price
    return total

def calculate_total_costs(festival):
    artist_cost = 0
    staff_cost = 0
    for artist in festival.lineup:
        artist_cost += artist.fee
    for staff in festival.hired_staff:
        staff_cost += staff.cost
    total_cost = artist_cost + staff_cost + festival.venue.rent
    return total_cost, artist_cost, staff_cost, festival.venue.rent

def calculate_profit (festival) -> float:
    total_cost, artist_fee, staff_cost, venue_rent = calculate_total_costs(festival)
    profit = calculate_total_earnings(festival) - total_cost
    return profit

