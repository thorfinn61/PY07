from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    my_deck = Deck()

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn")

    my_deck.add_card(dragon)
    my_deck.add_card(bolt)
    my_deck.add_card(crystal)

    stats = my_deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    my_deck.shuffle()

    print("\nDrawing and playing cards:\n")

    for _ in range(3):
        card = my_deck.draw_card()
        if card:
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"Drew: {card.name} ({card_type})")
            print(f"Play result: {card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
