from dataclasses import dataclass, field
from enum import Enum
from entities.artist import Artist
from entities.venue import Venue

class FestivalStatus(Enum):
    PLANNING = "PLANNING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"

@dataclass
class Festival:
    name: str
    venue: Venue
    lineup: list[Artist] = field(default_factory=list)
    ticket_cost: float = 50.0
    status: FestivalStatus = FestivalStatus.PLANNING

    # filled after simulation
    sold_tickets: int =0
    total: float =0.0
    profit: float=0.0
    satisfaction: int =0

    def lineup_total_cost(self) -> float:
        return sum(a.cache for a in self.lineup)

    def total_cost(self) -> float:
        return self.venue.rent + self.lineup_total_cost()

    def add_artist(self, artist: Artist):
        self.lineup.append(artist)

    def __str__(self):
        artists =", ".join(a.name for a in self.lineup) or "None"
        return (
            f" Festival: {self.name}\n"
            f" Local: {self.venue.nome}\n"
            f" Lineup: {artists}\n"
            f" Ticket Price: $ {self.ticket_cost:.2f}\n"
            f" Total Cost: $ {self.total_cost():,.2f}"
        )