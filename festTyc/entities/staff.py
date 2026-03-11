from dataclasses import dataclass
from enum import Enum

class Services (Enum):
    MARKETING = "Marketing"
    EFFECTS = "Special Effects"
    SECURITY = "Security"
    CATERING = "Catering"

@dataclass
class Staff:
    type: Services
    level: str
    cost: float
    effect_value: int
    min_reputation: int

    def is_unlocked(self, player) -> bool:
        return player.reputation >= self.min_reputation

    def __str__(self):
        return(
            f"Service: {self.type.value}\n"
            f"  Level: {self.level}\n"
            f"  Cost: $ {self.cost:,}\n"
            f"  Effect Value: {self.effect_value}\n"
        )