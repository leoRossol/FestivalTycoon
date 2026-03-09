from dataclasses import dataclass

@dataclass
class Venue:
    name: str
    capacity: int
    rent: float
    quality: int

def __str__(self):
    return (
        f" {self.name}\n"
        f" Capacity: {self.capacity:,} people\n"
        f" Rent: $ {self.rent:,.2f}\n "
        f" Quality: {self.quality}/100"
    )