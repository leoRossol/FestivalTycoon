from entities.festival import Festival
from entities.player import Player
from entities.staff import Staff, Services

# INGRESSOS VENDIDOS, APLICA LUCRO/PREJUIZO

def set_ticket_cost(festival, price: float):
    festival.ticketPrice = price

def calculate_ticket_sales(festival):
    avg_popularity = 0
    for artist in festival.lineup:
        avg_popularity += artist.popularity
    if len(festival.lineup) > 0:
        avg_popularity /= len(festival.lineup)

    bonus = 0
    for staff in festival.hiredStaff:
        if staff.type == Services.MARKETING:
            bonus += staff.effect_value

    sold = festival.venue.capacity * min((avg_popularity + festival.venue.popularity + bonus)/100, 1.0)
    return int(sold)

def apply_earnings(festival, player):
    festival.soldTickets = calculate_ticket_sales(festival)
    festival.totalEarnings = festival.calculate_earnings()
    festival.profit = festival.calculate_profit()
    if festival.profit >= 0:
        player.earn(festival.profit)
    elif festival.profit < 0:
        player.payment(abs(festival.profit))

def __str__ ():
    return(


    )