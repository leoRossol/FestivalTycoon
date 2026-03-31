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
    capacity: int
    level: int #AUMENTA DE ACORDO COM QUALIDADE
    rent: float #AUMENTA DE ACORDO COM O NIVEL
    reputation: int #DEFINE HYPE GERADO
    quality: int #AUMENTA APENAS VIA INVESTIMENTO DO PLAYER
    is_owned: bool
    location: Locations

    def __str__(self):
        return (
            f"Venue Name: {self.name}\n"
            f"  Capacity: {self.capacity}\n"
            f"  Level: {self.level}/5\n"
            f"  Rent: ${self.rent:,}\n"
            f"  Reputation: {self.reputation}/100\n"
            f"  Quality: {self.quality}/100\n"
            f"  Is Owned: {self.is_owned}\n"
            f"  Location: {self.location.value}\n"
        )