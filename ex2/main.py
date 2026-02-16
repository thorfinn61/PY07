from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

def get_capabilities(cls):
    return [m for m in dir(cls) if not m.startswith('_')]

def main():
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {get_capabilities(Card)}")
    print(f"- Combatable: {get_capabilities(Combatable)}")
    print(f"- Magical: {get_capabilities(Magical)}")
    
    warrior = EliteCard("Arcane Warrior", 5, "Rare", attack_power=5, health=10, mana=8)
    
    print(f"\nPlaying {warrior.name} (Elite Card):\n")
    
    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")
    
    print("\nMagic phase:")
    print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")
    
    print("\nMultiple interface implementation successful!")

if __name__ == "__main__":
    main()