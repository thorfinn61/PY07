import random
from typing import List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise TypeError("Only objects inheriting from Card can be added.")

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            print("Deck is empty!")
            return None
        drawn_card = self.cards.pop()
        return drawn_card

    def get_deck_stats(self) -> dict:
        stats = {
            'total_cards': len(self.cards),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }
        if not self.cards:
            return stats

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                stats['creatures'] += 1
            elif isinstance(card, SpellCard):
                stats['spells'] += 1
            elif isinstance(card, ArtifactCard):
                stats['artifacts'] += 1

        stats['avg_cost'] = round(total_cost / stats['total_cards'], 1)
        return stats
