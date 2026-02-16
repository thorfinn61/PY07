from ex0.CreatureCard import CreatureCard


def main() -> None:
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 4, "Common", 5, 5)
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print(f"CreatureCard Info: \n{dragon.get_card_info()}")
    print(f"\nPlaying {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")
    print(f"\n{dragon.name} attacks Goblin Warrior")
    print(f"Attack result: {dragon.attack_target(goblin.name)}")
    print("\nTesting insufficient mana (3 available)")
    print(f"Playable: {goblin.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
