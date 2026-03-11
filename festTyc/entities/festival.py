from dataclasses import dataclass, field
from enum import Enum
from entities.artist import Artist
from entities.venue import Venue
from entities.player import Player
from entities.staff import Staff

class FestivalStatus (Enum):
    PLANNING = "Planning"
    DONE = "Done"
    CANCELLED = "Cancelled"

@dataclass
class Festival:
    name: str
    status: FestivalStatus
    ticketPrice: float
    venue: Venue
    lineup: list[Artist] = field(default_factory=list)
    hiredStaff: list[Staff] = field(default_factory=list)

    # tbd after sim
    soldTickets: int
    totalEarnings: float
    profit: float
    crowdSatisfaction: int

    def add_artist(self, artist, player) -> bool:
        if artist.accepts_booking(player):
            self.lineup.append(artist)
            return True
        return False

    def add_staff(self, staff, plaver) -> bool:
        if staff.is_unlocked(plaver):
            self.hiredStaff.append(staff)
            return True
        return False

    def calculate_costs(self) -> float:
        cost = 0
        for artist in self.lineup:
            cost += artist.fee
        cost += self.venue.rent
        return cost

    def calculate_earnings(self) -> float:
        earned = self.soldTickets * self.ticketPrice
        return earned

    def calculate_profit(self) -> float:
        profit = self.calculate_earnings() - self.calculate_costs()
        return profit

    def cancel(self):
        if self.status == FestivalStatus.DONE:
            return
        self.status = FestivalStatus.CANCELLED

    def __str__(self):
        return(
            f"Festival Name: {self.name}\n"
            f"  Status: {self.status.value}\n"
            f"  Ticket Price: $ {self.ticketPrice:,}\n"
            f"  Venue: {self.venue.name}\n"
            f"  Lineup: {self.lineup}\n"
        )