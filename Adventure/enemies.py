# All the enemies

from classes import Fighter
import random

class Zombie(Fighter):

    def is_dead(self):
        return False
        
class Orc(Fighter):

    def is_dead(self):
        return self.health < 1