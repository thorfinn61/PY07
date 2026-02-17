from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():
    engine = GameEngine()

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    turn_execution = engine.simulate_turn()

    print(f"Strategy: {turn_execution['strategy']}")
    print(f"Actions: {turn_execution['actions']}")

    print("\nGame Report:")
    report = engine.get_engine_status()
    print(report)

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
