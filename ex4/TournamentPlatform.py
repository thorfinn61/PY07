from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registry = {}
        self.matches_count = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.registry[card1_id]
        c2 = self.registry[card2_id]

        if c1.attack_power >= c2.attack_power:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_count += 1

        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.registry.values(),
            key=lambda x: x.rating,
            reverse=True
        )
        return sorted_cards

    def generate_tournament_report(self) -> dict:
        ratings = [c.rating for c in self.registry.values()]
        return {
            'total_cards': len(self.registry),
            'matches_played': self.matches_count,
            'avg_rating': sum(ratings) // len(ratings) if ratings else 0,
            'platform_status': 'active'
        }
