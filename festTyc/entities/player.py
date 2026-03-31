from dataclasses import dataclass, field
from entities.venue import Venue

@dataclass
class Player:
    name: str
    money: float
    reputation: int
    consecutive_failures: int
    owned_venues: list[Venue] = field(default_factory=list)

    def __str__(self):
        return(
            f"{self.name}\n"
            f"  Money: $ {self.money:,}\n"
            f"  Reputation: {self.reputation}/1000\n"
            f"  Consecutive Failures: {self.consecutive_failures}\n"
            f"  Owned Venues: {self.owned_venues}\n"
        )