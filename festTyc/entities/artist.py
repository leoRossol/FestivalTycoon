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
    popularity: int
    fee: float

    def accepts_booking(self, player):
        i = self.popularity // 2
        return i <= player.reputation

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

    def fee_rise(self):
        self.fee += self.fee * 0.10


    def __str__(self):
        return(
            f"Name: {self.name}\n"
            f"  Genre: {self.genre.value}\n"
            f"  Popularity: {self.popularity}/100\n"
            f"  Fee: $ {self.fee}\n"
        )