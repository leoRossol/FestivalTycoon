from dataclasses import dataclass
from enum import Enum

class Services (Enum):
    MARKETING = "Marketing"
    EFFECTS = "Special Effects"
    SECURITY = "Security"
    CATERING = "Catering"
    PRODUCER = "Producer"
    MEDICAL = "Medical"
    TECHNICAL = "Technical"

@dataclass
class Staff:
    type: Services
    level: str
    cost: float
    effect_value: int
    min_reputation: int
    mitigation_value: int

    def __str__(self):
        return (
            f"Staff Type: {self.type.value}\n"
            f"  Level: {self.level}/5\n"
            f"  Cost: $ {self.cost:,}\n"
            f"  Effect Value: {self.effect_value}\n"
            f"  Minimal Reputation: {self.min_reputation}\n"
            f"  Mitigation Value: {self.mitigation_value}\n"
        )
