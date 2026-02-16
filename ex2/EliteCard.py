from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.hp = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost
        }

    def attack(self, target) -> dict:
        target_name = target.name if hasattr(target, 'name') else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        block = 3
        damage_taken = max(0, incoming_damage - block)
        self.hp -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": block,
            "still_alive": self.hp > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "hp": self.hp
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        targets = [t.name if hasattr(t, 'name') else str(t) for t in targets]
        mana_cost = 4
        self.mana -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana
        }
