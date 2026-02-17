from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int, rarity: str,
                 attack_power: int, hp: int):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack_power
        self.hp = hp

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    # Rankable
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {"rating": self.rating, "record": f"{self.wins}-{self.losses}"}

    # Combatable
    def attack(self, target) -> dict:
        return {"attacker": self.name, "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> dict:
        self.hp -= incoming_damage
        if self.hp < 0:
            self.hp = 0
        return {"damage_taken": incoming_damage, "remaining_hp": self.hp}

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "hp": self.hp
        }

    # Card
    def play(self, game_state: dict) -> dict:
        return {"played": self.name, "cost": self.cost}

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
