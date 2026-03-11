from dataclasses import dataclass
from enum import Enum
import random

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
    popularity: int
    location: Locations

    def raise_rent(self):
        i = self.popularity / 1000
        self.rent += self.rent * i

    #TODO undupe this code after testing
    def boost_popularity(self, festival):
        if festival.crowdSatisfaction == 100:
            self.popularity += 10
        elif festival.crowdSatisfaction >= 80:
            self.popularity += 5
        elif festival.crowdSatisfaction >= 60:
            self.popularity += 2
        elif festival.crowdSatisfaction >= 50:
            self.popularity += 0
        elif festival.crowdSatisfaction >= 30:
            self.popularity -= 2
        else:
            self.popularity -= 5
        self.popularity = max(0, min(100, self.popularity))

    #TODO add random events to this later
    def is_available(self):
        if self.location == Locations.STADIUM:
            return random.random()>0.25
        else:
            return True

    def __str__(self):
        return(
            f"Venue Name: {self.name}\n"
            f"  Quality: {self.quality}/100\n"
            f"  Capacity: {self.capacity} People\n"
            f"  Rent: $ {self.rent:,}\n"
            f"  Popularity: {self.popularity}/100\n"
        )