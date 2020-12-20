import random

class Character(object):
    def __init__(self, health, attack_power, defense, name, special=False):
        self.health = health
        self.special = special
        self.attack_power = attack_power
        self.defense = defense
        self.name = name

# PC options

class Fighter(Character):
    
    def roll20(self):
        return random.randint(1, 20)
    
    def attack(self, character):
        damage = self.attack_power * self.roll20() / character.defense
        print(f"{self.name} punched {character.name} for {damage} damage")
        return damage
        
    def special(self, character):
        if self.special:
            damage = self.roll20() * 20
            print(f"{self.name} roundhouse kicked {character.name} for {damage} damage!")
            return damage
        return None
        
    def is_dead(self):
        return self.health < 1
        
class Wizard(Character):
        
    def roll20(self):
        return random.randint(1, 20)
        
    def attack(self, character):
        damage = self.attack_power * self.roll20() / character.defense
        print(f"{self.name} bonked {character.name} for {damage} damage")
        return damage
        
    def special(self, character):
        if self.special:
            damage = self.roll20() + 25
            print(f"{self.name} blasted {character.name} for {damage} damage!")
            return damage
        return None
        
    def is_dead(self):
        return self.health < 1
        
class Rogue(Character):

    def roll20(self):
        return random.randint(1, 20)
        
    def attack(self, character):
        damage = self.attack_power * self.roll20() / character.defense
        print(f"{self.name} stabbed {character.name} for {damage} damage")
        return damage
        
    def special(self, character):
        if self.special:
            damage = 20 * character.defense
            print(f"{self.name} backstabbed {character.name} for {damage} damage")
            return damage
        return None
        
    def is_dead(self):
        return self.health < 1   