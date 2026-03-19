from dataclasses import dataclass, field
from enum import Enum
from entities.artist import Artist
from entities.venue import Venue
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
    # tbd after sim
    soldTickets: int
    totalEarnings: float
    profit: float
    crowdSatisfaction: int
    # lists
    lineup: list[Artist] = field(default_factory=list)
    hiredStaff: list[Staff] = field(default_factory=list)

    def __str__(self):
        return(
            f"Festival Name: {self.name}\n"
            f"  Status: {self.status.value}\n"
            f"  Ticket Price: $ {self.ticketPrice:,}\n"
            f"  Venue: {self.venue.name}\n"
            f"  Lineup: {self.lineup}\n"
            f"  Sold Tickets: {self.soldTickets}\n"
            f"  Profit: $ {self.profit:,}\n"
        )