from dataclasses import dataclass
from enum import Enum

class MusicGenre (Enum):
    ROCK = "Rock"
    POP = "Pop"
    RAP = "Rap"
    ELECTRONIC = "Electronic"
    COUNTRY = "Country"
    JAZZ = "Jazz"
    INDIE = "Indie"
    OTHER = "Other"

@dataclass
class Artist:
    name: str
    genre: MusicGenre
    reputation: int #DEFINE HYPE GERADO
    fee: float #AUMENTA DE ACORDO COM NIVEL / PROXIMIDADE DO FESTIVAL
    level: int #AUMENTA DE ACORDO COM REPUTACAO
    is_retired: bool

    def __str__(self):
        return(
            f"Name: {self.name}\n"
            f"  Genre: {self.genre.value}\n"
            f"  Reputation: {self.reputation}/100\n"
            f"  Fee: ${self.fee}\n"
            f"  Level: {self.level}/5\n"
            f"  Retired: {self.is_retired}\n"
        )