from dataclasses import dataclass, field
from enum import Enum
from entities.artist import Artist
from entities.venue import Venue

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

    # tbd after sim
    soldTickets: int
    totalEarnings: float
    profit: float
    crowdSatisfaction: int





