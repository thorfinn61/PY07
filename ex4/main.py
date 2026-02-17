from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=10,
        hp=20
    )

    wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack_power=5,
        hp=12
    )
    wizard.rating = 1150

    print("Registering Tournament Cards...")
    cards = [dragon, wizard]

    for card in cards:
        platform.register_card(card)
        stats = card.get_rank_info()

        interfaces = [cls.__name__ for cls in type(card).__bases__]

        print(f"{card.name} (ID: {card.card_id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {stats['record']}")

    # 2. Match
    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    # 3. Leaderboard
    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        stats = card.get_rank_info()
        print(f"{i}. {card.name} - Rating: {card.rating} ({stats['record']})")

    # 4. Rapport
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
