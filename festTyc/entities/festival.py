from dataclasses import dataclass, field
from enum import Enum
from entities.artist import Artist
from entities.venue import Venue
from entities.staff import Staff
from entities.objective import Objective
from entities.event import Event

class FestivalStatus (Enum):
    PLANNING = "Planning"
    DONE = "Done"
    CANCELLED = "Cancelled"
    SIMULATING = "Simulating"

@dataclass
class Festival:
    name: str
    status: FestivalStatus
    ticket_price: float
    venue: Venue | None
    # tbd after sim
    sold_tickets: int
    total_earnings: float
    profit: float
    crowd_satisfaction: int
    genre_bonus: float
    # lists
    lineup: list[Artist] = field(default_factory=list)
    hired_staff: list[Staff] = field(default_factory=list)
    objectives: list[Objective] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)

    def __str__(self):
        return (
            f"Festival Name: {self.name}\n"
            f"  Status: {self.status.value}\n"
            f"  Ticket Price: $ {self.ticket_price:,}\n"
            f"  Venue: {self.venue.name}\n"
            f"  Lineup: {self.lineup}\n"
            f"  Hired Staff: {self.hired_staff}\n"
            f"  Sold Tickets: {self.sold_tickets}\n"
            f"  Total Earnings: ${self.total_earnings:,}\n"
            f"  Profit: ${self.profit:,}\n"
            f"  Crowd Satisfaction: {self.crowd_satisfaction}\n"
            f"  Genre Bonus: {self.genre_bonus}\n"
        )