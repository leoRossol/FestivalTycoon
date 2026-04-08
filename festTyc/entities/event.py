from dataclasses import dataclass
from enum import Enum

class Type(Enum):
    ARTIST = "Artist"
    VENUE = "Venue"
    STAFF = "Staff"
    OTHER = "Other"
class Mitigated(Enum):
    SECURITY = "Security"
    TECHNICAL = "Technical"
    PRODUCER = "Producer"
    MEDIC ="Medic"
class Target(Enum):
    PERFORMANCE = "Performance"
    PRODUCTION = "Production"
    SATISFACTION = "Satisfaction"
    PROFIT = "Profit"

@dataclass
class Event:
    id: int
    name: str
    description: str
    resolve_cost: float
    penalty_value: float
    penalty_from: Type
    penalty_target: Target
    mitigated: Mitigated | None
    resolved: bool
    is_positive: bool


    def __str__(self):
        return(
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"  Description: {self.description}\n"
            f"  Cost to Resolve: ${self.resolve_cost}\n"
            f"  Penalty Value: {self.penalty_value}/5\n"
            f"  Penalty From: {self.penalty_from.value}\n"
            f"  Penalty Target: {self.penalty_target.value}\n"
            f"  Mitigated By: {self.mitigated.value}\n"
            f"  Resolved: {self.resolved}\n"
            f"  Positive: {self.is_positive}\n"
        )