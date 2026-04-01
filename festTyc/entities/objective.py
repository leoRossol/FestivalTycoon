from dataclasses import dataclass
from enum import Enum

class Types (Enum):
    PROFIT = "Profit"
    LINEUPSIZE = "Lineup size"
    LINEUPLEVEL = "Lineup level"
    LOCATION = "Location"
    GENRE = "Genre"

@dataclass
class Objective:
    type: Types
    target_value: float
    description: str
    fulfilled: bool
    max_reputation: int

    def __str__(self):
        return (
            f"Type: {self.type.value}\n"
            f"  Target Value: {self.target_value}\n"
            f"  Description: {self.description}\n"
            f"  Fulfilled: {self.fulfilled}\n"
            f"  Maximum Reputation: {self.max_reputation}\n"
        )