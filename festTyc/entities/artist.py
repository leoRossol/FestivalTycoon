from dataclasses import dataclass, field
from enum import Enum

class Genre(Enum):
    ROCK = "Rock"
    POP = "Pop"
    ELETRONIC = "Eletronic"
    RAP = "Rap"
    COUNTRY = "Country"

@dataclass
class Artist:
    name: str
    genre: Genre
    popularity: int
    cache: float

    def min_reputation(self) -> int:
        return self.popularity // 2

    def __str__(self):
        return(
            f"{self.name} ({self.genre.value})\n"
            f" Popularity: {self.popularity}/100\n"
            f" Cache: $ {self.cache:,.2f}"
        )