from dataclasses import dataclass, field

@dataclass
class Player:
    name: str
    money: float = 10_000.0
    reputation: int = 10
    prev_fests: int = 0

    def enough_money(self, amount: float) -> bool:
        return self.money >= amount

    def pay(self, amount: float) -> bool:
        if self.enough_money(amount):
            self.money -= amount
            return True
        return False

    def earn(self, amount: float):
        self.money += amount

    def update_reputation(self, delta: int):
        self.reputation = max(0, min(100, self.reputation + delta))

    def __str__(self):
        return (
            f"{self.nome}\n"
            f"  Money: $  {self.money:,.2f}\n"
            f"  Reputation: {self.reputation}/100\n"
            f"  Previous Festivals {self.prev_fests}"
        )