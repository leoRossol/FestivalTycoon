from dataclasses import dataclass
from enum import Enum

class Locations(Enum):
    STADIUM = "Stadium"
    PARK = "Park"
    ISLAND = "Island"
    RACETRACK = "Racetrack"
    FOREST = "Forest"

@dataclass
class Venue:
    name: str
    quality: int
    capacity: int
    rent: float
    reputation: int
    location: Locations

    def update_reputation(self, delta: int):
        self.reputation = max(0, min(100, self.reputation + delta))

    def __str__(self):
        return(
            f"Venue Name: {self.name}\n"
            f"  Quality: {self.quality}/100\n"
            f"  Capacity: {self.capacity} People\n"
            f"  Rent: $ {self.rent:,}\n"
            f"  Popularity: {self.reputation}/100\n"
        )