from classes import Fighter, Wizard, Rogue
from enemies import Orc, Zombie
from combat import combat
import random
import time

print("Welcome to your adventure in Borovia.")

time.sleep(2)

print("First, tell me who you are")
name_input = input("What is your name? ")

time.sleep(2)

class_input = str(input("Are you a Fighter, Wizard, or Rogue? "))
class_dict = {
    "Fighter":Fighter(150, 50, 50, name_input, special=True), 
    "Wizard":Wizard(100, 20, 70, name_input, special=True), 
    "Rogue":Rogue(120, 40, 30, name_input, special=True)
}
while class_input not in class_dict:
    class_input = str(input("Sorry, I didn't catch that. Are you Fighter, Wizard, or Rogue? "))

player = class_dict.get(class_input)    

time.sleep(2)

print(f"I hope your adventure in Borovia fares well, {name_input} the {class_input}. ")

time.sleep(2)

print(f"""Here are your stats: 
    Health is {player.health}
    Attack is {player.attack_power}
    Defense is {player.defense}""")
    
time.sleep(2)

print("For reasons you can't remember, you are walking in the woods.")

time.sleep(2)

print("You come across an Orc. Scary! It attacks!")

time.sleep(2)

current_enemy = Orc(150, 10, 10, "Bregor the Stonebutt")

combat(player, current_enemy)
