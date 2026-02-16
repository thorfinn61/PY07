from ex0.Card import Card

class CreatureCard(Card):
	def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
		super().__init__(name, cost, rarity)

		if not isinstance(attack, int) or not isinstance(health, int):
			raise TypeError("Attack and Health must be integers")
		if not isinstance(attack, int) or attack < 0:
			raise ValueError("Attack must be a non-negative integer")
		if not isinstance(health, int) or health <= 0:
			raise ValueError("Health must be a positive integer")
	
		self.attack = attack
		self.health = health

	def play(self, game_state: dict) -> dict:
		return {"card_played": self.name,
				"mana_used": self.cost,
				"effect": "Creature summoned to battlefield"}

	def attack_target(self, target) -> dict:
		damage = self.attack if self.attack > 0 else 0
		if hasattr(target, 'name'):
			target_name = target.name
		else:
			target_name = str(target)
		return {
			"attacker": self.name,
			"target": target_name,
			"damage_dealt": damage,
			"combat_resolved": True
		}
	
	def get_card_info(self) -> dict:
		info = super().get_card_info()
		info.update({
			"type": "Creature",
			"attack": self.attack,
			"health": self.health
		})
		return info