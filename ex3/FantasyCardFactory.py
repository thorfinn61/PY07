import random
from .CardFactory import CardFactory
from ex2.EliteCard import EliteCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.supported = {
            'creatures': ['Dragon', 'Goblin'],
            'spells': ['Fireball', 'Lightning Bolt'],
            'artifacts': ['Mana Ring']
        }

    def get_supported_types(self) -> dict:
        return self.supported

    def create_creature(self, name_or_power=None):
        if name_or_power == "Dragon":
            return EliteCard(
                "Fire Dragon", 5, "Legendary",
                attack_power=8, health=20, mana=20
            )
        return EliteCard(
            "Goblin Warrior", 2, "Common",
            attack_power=3, health=5, mana=2
        )

    def create_spell(self, name_or_power=None):
        if name_or_power == "Fireball":
            return EliteCard(
                "Fireball", 4, "Rare",
                attack_power=6, health=0, mana=3
            )
        return EliteCard(
            "Lightning Bolt", 3, "Rare",
            attack_power=5, health=0, mana=2
        )

    def create_artifact(self, name_or_power=None):
        return EliteCard(
            "Mana Ring", 1, "Common",
            attack_power=0, health=0, mana=10
        )

    def create_themed_deck(self, size: int) -> dict:
        creation_methods = {
            'creatures': self.create_creature,
            'spells': self.create_spell,
            'artifacts': self.create_artifact
        }

        deck = []
        categories = list(self.supported.keys())

        for _ in range(size):
            cat = random.choice(categories)
            name = random.choice(self.supported[cat])
            card = creation_methods[cat](name)
            deck.append(card)

        return {
            "cards": deck,
            "theme": "Fantasy"
        }

    def __str__(self):
        return f"{self.name} ({self.cost})"
