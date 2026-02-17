class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory, strategy):
        self.factory = factory
        self.strategy = strategy

        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        print(f"Factory: {type(factory).__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {self.factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        print("\nSimulating aggressive turn...")

        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data['cards']
        self.cards_created += len(hand)

        print(f"Hand: [{', '.join(str(card) for card in hand)}]")
        turn_execution = self.strategy.execute_turn(hand, [])

        self.total_damage += turn_execution['actions']['damage_dealt']
        self.turns_simulated += 1

        print("\nTurn execution:")
        return turn_execution

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
