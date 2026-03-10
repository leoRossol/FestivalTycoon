from dataclasses import dataclass

@dataclass
class Player:
    name: str
    money: float
    reputation: int
    history: int

    def has_enough(self, amount: float) -> bool:
        return self.money >= amount

    def payment(self, amount:float) -> bool:
        if self.has_enough(amount):
            self.money -= amount
            return True
        return False

    def earn(self, amount: float):
        self.money += amount

    def update_reputation(self, delta: int):
        self.reputation = max(0, min(100, self.reputation + delta))

    def __str__(self):
        return(
            f"{self.name}\n"
            f"  Money: $ {self.money:,}\n"
            f"  Reputation: {self.reputation}/100\n"
            f"  Previous Festivals: {self.history}\n"
        )