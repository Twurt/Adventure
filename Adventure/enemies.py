# All the enemies

from classes import Fighter
import random

def roll20(self):
        return random.randint(1, 20)

class Zombie(Fighter):

    health = 1 #figure out why I can't put roll20 here
    attack_power = 1
    defense = 1

    def is_dead(self):
        return False
        
class Orc(Fighter):

    def is_dead(self):
        return self.health < 1
        
    health = 10 #figure out why I can't put roll20 here
    attack_power = 5
    defense = 10