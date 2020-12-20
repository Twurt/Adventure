import random
import time

from classes import Fighter, Wizard
from enemies import Zombie, Orc

def combat(good_guy, bad_guy):
    # good_guy = player
    # bad_guy = current_enemy

    while not good_guy.is_dead() and not bad_guy.is_dead():
        good_guy.health -= bad_guy.attack(good_guy)
        if good_guy.special and good_guy.roll20() > 15:
            bad_guy.health -= good_guy.special(bad_guy)
        else: 
            bad_guy.health -= good_guy.attack(bad_guy)
        
        print(f"{good_guy.name}'s health is {good_guy.health}")
        print(f"{bad_guy.name}'s Health is {bad_guy.health}")
        time.sleep(2)

    print(f"{good_guy.name if bad_guy.is_dead() else bad_guy.name} has won")