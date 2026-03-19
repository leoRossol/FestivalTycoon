from dataclasses import dataclass
from enum import Enum

class MusicGenre (Enum):
    ROCK = "Rock"
    POP = "Pop"
    RAP = "Rap"
    ELECTRONIC = "Electronic"
    COUNTRY = "Country"
    OTHER = "Other"

@dataclass
class Artist:
    name: str
    genre: MusicGenre
    reputation: int
    fee: float

    def update_reputation(self, delta: int):
        self.reputation = max(0, min(100, self.reputation + delta))

    def __str__(self):
        return(
            f"Artist Name: {self.name}\n"
            f"  Genre: {self.genre.value}\n"
            f"  Reputation: {self.reputation}/100\n"
            f"  Fee: $ {self.fee}\n"
        )