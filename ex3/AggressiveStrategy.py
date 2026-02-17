from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
            available_targets,
            key=lambda target: target.get_combat_stats()['hp']
        )

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_total = 5
        mana_used = 0
        played = []
        damage = 0

        playable_cards = sorted(hand, key=lambda c: c.mana)

        for card in playable_cards:
            if mana_used + card.mana <= mana_total:
                played.append(card.name)
                mana_used += card.mana

                stats = card.get_combat_stats()
                damage += stats.get('attack', 0)

        targets = ["Enemy Player"]
        if battlefield:
            sorted_enemies = self.prioritize_targets(battlefield)
            targets = [sorted_enemies[0].name]

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": played,
                "mana_used": mana_used,
                "targets_attacked": targets,
                "damage_dealt": damage
            }
        }
