import random

class Character:
    def __init__(self, name, hp, normal_attack_damage, dodge_chance, special_attack_damage):
        self.name = name
        self.hp = hp
        self.normal_attack_damage = normal_attack_damage
        self.dodge_chance = dodge_chance
        self.special_attack_damage = special_attack_damage

    def is_alive(self):
        return self.hp > 0

    def normal_attack(self, opponent):
        if random.random() > opponent.dodge_chance:
            opponent.hp -= self.normal_attack_damage
            print(f"{self.name} hit {opponent.name} for {self.normal_attack_damage} damage.")
        else:
            print(f"{opponent.name} dodged the attack!")

    def special_attack(self, opponent):
        opponent.hp -= self.special_attack_damage
        print(f"{self.name} hit {opponent.name} with a special attack for {self.special_attack_damage} damage.")

def combat_round(attacker, defender):
    # Determine if the attacker will use a normal attack or a special attack
    if random.random() < 0.8:  # 80% chance to use normal attack, 20% chance to use special attack
        attacker.normal_attack(defender)
    else:
        attacker.special_attack(defender)

def battle(character1, character2):
    round_number = 1
    while character1.is_alive() and character2.is_alive():
        print(f"--- Round {round_number} ---")
        combat_round(character1, character2)
        if character2.is_alive():
            combat_round(character2, character1)
        round_number += 1
        print(f"{character1.name} HP: {character1.hp}")
        print(f"{character2.name} HP: {character2.hp}\n")
    
    if character1.is_alive():
        print(f"{character1.name} wins!")
    else:
        print(f"{character2.name} wins!")

# Create characters
character1 = Character(name="Warrior", hp=100, normal_attack_damage=15, dodge_chance=0.2, special_attack_damage=30)
character2 = Character(name="Mage", hp=80, normal_attack_damage=20, dodge_chance=0.1, special_attack_damage=40)

# Start the battle
battle(character1, character2)
