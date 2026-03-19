## TUDO QUE ENVOLVEM DINHEIRO
from entities.staff import Services

## INGRESSOS
def set_ticket_price(festival, price: float):
    festival.ticketPrice = price

def calculate_ticket_sales(festival):
    avg_popularity = 0
    for artist in festival.lineup:
        avg_popularity += artist.reputation
    if len(festival.lineup) > 0:
        avg_popularity /= len(festival.lineup)
    bonus = 0
    for staff in festival.hiredStaff:
        if staff.type == Services.MARKETING:
            bonus += staff.effect_value
    sold = festival.venue.capacity * min((avg_popularity + festival.venue.reputation + bonus)/100, 1.0)
    return int(sold)



## CALCULOS DE CUSTOS
def calculate_earnings(festival) -> float:
    earned = festival.soldTickets * festival.ticketPrice
    return earned

def calculate_costs(festival) -> float:
    cost = 0
    for artist in festival.lineup:
        cost += artist.fee
    cost += festival.venue.rent
    return cost

def calculate_profit(festival) -> float:
    profit = calculate_earnings(festival) - calculate_costs(festival)
    return profit

def apply_earnings(festival, player):
    festival.soldTickets = calculate_ticket_sales(festival)
    festival.totalEarnings = calculate_earnings(festival)
    festival.profit = calculate_profit(festival)
    if festival.profit >= 0:
        player.earn(festival.profit)
    elif festival.profit < 0:
        player.payment(abs(festival.profit))
