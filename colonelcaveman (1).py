# Imports
import random
from colorama import init, Fore
import sys
from time import sleep
import os

# Global Variables
activity = None
selected_weapon = None
weapons = ["club", "knife", "spear"]
encounter_difficulty = None
best_weapon = None
medium_weapon = None
worst_weapon = None
resources = 0

# Functions

# Author: Rachael
def introduction():
    Introduction ="welcome to Caveman Game"
    print (f"{Introduction}, dear caveman has waking up hungry and nodoubt his family are hungry too, so what weapon would he take?")

def epilogue():
    Happy_Ending="happy ending,Caveman!"
    print (f" Hurray..... great fighter hunting mission completed, {Happy_Ending}:)")

# Author: Mohammed Islam
def decide_location():
    global activity
    print("Welcome to the decision maker!")
    print("Choose a location to go: Hunt, Gather, or Fish")
    
    while True:
        player_choice = input("Enter your choice: ").strip().capitalize()
        if player_choice in ['Hunt', 'Gather', 'Fish']:
            print("You have chosen to go", player_choice)
            break
        else:
            print("Invalid choice. Please choose from Hunt, Gather, or Fish.")
    
    activity = player_choice
    print("You are going to:", activity)

# Authors: Tetiana, Nick
def selection_weapon():
    while True:

        selection = input("You have an option: 1 - for club, 2 - for knife, 3 - for spear. \nPlease, select the number: 1 or 2 or 3   ")
        if selection.isnumeric():
            selection = int(selection)
        else:
            selection = None

        if selection == 1:
            print(f"You have a {weapons[0]}!")
            return weapons[0]
        elif selection == 2:
            print(f"You have a {weapons[1]}!")
            return weapons[1]
        elif selection == 3:
            print(f"You have a {weapons[2]}!")
            return weapons[2]
        else:
            print("Try again! Please, select the number: 1 or 2 or 3")

# Authors: Nick, Mohammed Islam, Muhammad Shuaib, Tetiana
def set_encounter_difficulty(scenario):
    global encounter_difficulty
    global best_weapon
    global medium_weapon
    global worst_weapon

    encounter_difficulty = random.randint(0,2)

    if scenario == "Hunt":
        if encounter_difficulty > 1:
            best_weapon = weapons[2]  # Spear is best for hard encounters here
            medium_weapon = weapons[1]  # Knife is medium for hard encounters here
            worst_weapon = weapons[0]  # Club is worst for hard encounters here
        else:
            best_weapon = weapons[0]  # Club is best for hunting
            medium_weapon = weapons[2]  # Spear is medium for hunting
            worst_weapon = weapons[1]  # Knife is worst for hunting
    elif scenario == "Fish":
        if encounter_difficulty > 1:
            best_weapon = weapons[1]  # Knife is best for hard encounters here
            medium_weapon = weapons[0]  # Club is medium for hard encounters here
            worst_weapon = weapons[2]  # Spear is worst for hard encounters here
        else:
            best_weapon = weapons[2]  # Spear is best for fishing
            medium_weapon = weapons[1]  # Knife is medium for fishing
            worst_weapon = weapons[0]  # Club is worst for fishing
    elif scenario == "Gather":
        if encounter_difficulty > 1:
            best_weapon = weapons[0]  # Club is best for hard encounters here
            medium_weapon = weapons[2]  # Spear is medium for hard encounters here
            worst_weapon = weapons[1]  # Knife is worst for hard encounters here
        else:
            best_weapon = weapons[1]  # Knife is best for gathering
            medium_weapon = weapons[0]  # Club is medium for gathering
            worst_weapon = weapons[2]  # Spear is worst for gathering

# Author: Muhammad Shuaib
def attack_or_flee():
    while True:
        attack_flee = input("Will you (A)ttack or (F)lee: ").strip().capitalize()
        if attack_flee in ['A', 'F']:
            if attack_flee == 'A':
                return True
            else:
                return False
        else:
            print("Invalid Text")

    # if attack_flee.strip().capitalize() == 'A':
    #     attack = ['you lose', 'you win']
    #     radndom_number = random.randint(0,1)
    #     random_attack = attack[radndom_number]
    #     print(random_attack)
    # elif attack_flee.strip().capitalize() == 'F':
    #     flee = ['You escpaped', 'You did not escape']
    #     radndom_number = random.randint(0,1)
    #     random_flee = flee[radndom_number]
    #     print(random_flee)
    # else:
    #     print("Invalid Text")

# Author: Matthew, Keith, Chris, Tetiana
def combat_outcome (difficulty, bonus):
    combat_score = random.randint (1, 10)
    weapon_score = combat_score + bonus
    if weapon_score > difficulty: 
        return True
    else: return False

# Authors: Mohammed Islam
def journey_to_plains():
    print("You set out on a journey to the Plains for hunting.")
    sleep(2)
    print("The sun is shining brightly as you traverse through lush forests and meandering rivers.")
    sleep(2)
    print("You hear the distant calls of birds and the rustle of leaves in the gentle breeze.")
    sleep(2)
    print("After a few hours of travel, you finally reach the vast open plains.")
    sleep(2)
    print("The grasslands stretch out before you, dotted with occasional trees and shrubs.")
    sleep(2)
    print("You feel a rush of excitement as you prepare your hunting gear and begin your hunt.")

# Author: Keith, Chris, Matthew
def attacking_plains_easy():
    attacking_plains = ["You spot a rabbit", "You see a wounded deer", "You see a hedgehog" ]
    random_number = random.randint(0, 2)
    random_attacking_plains = attacking_plains[random_number]
    print(f"You have arrived at the plains and {random_attacking_plains}!")

# Author: Keith, Chris, Matthew
def attacking_plains_medium():
    plains_medium = ["Wooly mamoth", "Sabre tooth tiger", "Wolf" ]
    random_number = random.randint(0, 2)
    random_plains_medium = plains_medium[random_number]
    print(f"You find yourself out on the plains and you spot a {random_plains_medium}!")

# Author: Keith, Chris, Matthew
def attacking_plains_hard():
    attacking_plains_hard = [" a Tyranasaurus Rex" , " a Terradactyl" , " an alien space ship" ]
    random_number = random.randint(0, 2)
    random_attacking_plains_hard = attacking_plains_hard [random_number]
    print(f"You find a opening onto the plains & suddenly you are confronted with{random_attacking_plains_hard}!")

# Author: Kieth, Chris, Matthew
def journey_to_river():
    journeys = ["windy", "sunny", "raining" ]
    random_number = random.randint(0, 2)
    random_journey = journeys[random_number]
    print(f"The weather is {random_journey}!")

def attacking_river_easy():
    print("TODO")

# Authors: Tetiana, Deepti
def attacking_river_medium():
    print("You are doing well. You found a giant fish.")

# Authors: Tetiana, Deepti
def attacking_river_hard():
    print("You came to the river and a crocodile attacked you.")
    print("You put all your efforts and fight with corocodile with bravery.")
    print("You are an incredible fighter!")

# Authors: Mohammad Islam
def journey_to_forest():
    print("You embark on a journey to the forest for gathering resources.")
    sleep(2)
    print("The path winds through dense foliage, the air thick with the scent of earth and greenery.")
    sleep(2)
    print("Sunlight filters through the canopy above, dappling the forest floor with golden hues.")
    sleep(2)
    print("You hear the chirping of birds and the gentle rustle of leaves as you make your way deeper into the woods.")
    sleep(2)
    print("The forest teems with life, from the smallest insects to the majestic trees towering above.")
    sleep(2)
    print("You feel a sense of tranquility and connection with nature as you gather herbs, berries, and other treasures.")


# Authors: Tetiana, Deepti
def attacking_forest_easy():
    # Describe Attacking Forest Easy
    attacking_forest_easy = ["Rabbit", "Forest Grouse", "Cottontail Hare", "Red Squirre"]
    random_number = random.randint(0,2)
    random_attacking_forest_easy = attacking_forest_easy[random_number]
    print(f"You found a cute {random_attacking_forest_easy}. You are doing great!")

# Authors: Tetiana, Deepti
def attacking_forest_medium():
    # Describe Attacking Forest Medium 
    attacking_forest_medium = ["Bear", 'Deer', "Volf"]
    random_number = random.randint(0,2)
    random_attacking_forest_medium = attacking_forest_medium[random_number]
    print(f"You are a great hunter. You came to the forest and you managed to find a {random_attacking_forest_medium}.")

# Authors: Tetiana, Deepti
def attacking_forest_hard():
    # Describe Attacking Forest Hard 
    attacking_forest_hard = ["Bear", 'Deer', "Volf"]
    random_number = random.randint(0,2)
    random_attacking_forest_hard = attacking_forest_hard[random_number]
    print(f"It was a terrible day for you and a huge {random_attacking_forest_hard} striked you but you are fighting courageously.")

def tprint(words):
    for char in words:
        sleep(0.060)
        sys.stdout.write(char)
        sys.stdout.flush()

def add_resources(amount):
    global resources
    resources = resources + amount
    print ( "well done!" )
    print (f"You have recieved {amount} kg of food")
    print (f"You now have {resources} kg ")

def carry_on_or_go_home_prompt():
    global resources

    # print("It's been a long day. Would you like to continue or go home ?")
    # SET UP A LOOP WHICH WILL ASK FOR INPUT UNTILL IT GETS VALIDATION.
    choice = 0
    # FOR LOOP IS BEST FOR A SPECIFIC RANGE OF DATA AND WHILE LOOP IS BETTER FOR LOOPING WHICH IS SOMETHING UNTILL IT IS COMPLETED.

    while choice == 0:
        choice_input = input("Press 1 if you want to go home, Press 2 to keep hunting: ")
        # INPUT WILL FOR WAITING FOR USERS TO TYPE SOME OF THE CHOICES OR OPTIONS.

        if choice_input == "1":
        # WE SHOULD DESCRIBE THE CHOICE TO GO HOME.
            
            print(f"It's been a long day, you've arrived home safely. Enjoy the rest of the day. You take home {resources}kg of food")
            choice = 1 

        elif choice_input == "2":
            print(f"You've decided to continue, you are carrying {resources}kg of food. Good luck on your next hunt.")
            choice = 2
        else:
            print("Invalid Key, Please try again.")

    return choice                           # RETURNING THE VALUE ACCORDING TO USER'S CHOICE.

# Start Game
    
# Init Colorama
init()

introduction()

while True:
    # Decide Location
    decide_location()

    # Choose Weapon
    print("you see the club, it has a long, smooth brown handle, going up to a thicker end thats nobbled for extra damage. \nThis will be great for bashing an enemy")
    print("you see the knife, its comprised of a sharpened stone, stuck, sturdily into a piece of wood for a handle. \nThis will be great for forraging")
    print("you see the spear, its comprised of a sharpened stone, stuck, sturdily into a long piece of wood, around a meter long, that should be great for fishing")

    selection_weapon()

    # Generate random encounter

    set_encounter_difficulty(activity)

    # Describe Attack Scene

    if activity == "Hunt":
        journey_to_plains()
        if encounter_difficulty == 0:
            attacking_plains_easy()
        elif encounter_difficulty == 1:
            attacking_plains_medium()
        elif encounter_difficulty == 2:
            attacking_plains_hard()
        else:
            print("Unknown Plains Difficulty")
    elif activity == "Fish":
        journey_to_river()
        if encounter_difficulty == 0:
            attacking_river_easy()
        elif encounter_difficulty == 1:
            attacking_river_medium()
        elif encounter_difficulty == 2:
            attacking_river_hard()
        else:
            print("Unknown River Difficulty")
    elif activity == "Gather":
        journey_to_forest()
        if encounter_difficulty == 0:
            attacking_forest_easy()
        elif encounter_difficulty == 1:
            attacking_forest_medium()
        elif encounter_difficulty == 2:
            attacking_forest_hard()
        else:
            print("Unknown Forest Difficulty")

    # Attack or Flee
    attacking = attack_or_flee()
    if attacking:
        # If Attacking
        difficulty_scores = [3, 5, 7]
        weapon_bonus = 0

        if selected_weapon == best_weapon:
            weapon_bonus = 2
        elif selected_weapon == worst_weapon:
            weapon_bonus = -2

        # Calculate Attack Result
        combat_result = combat_outcome(difficulty_scores[encounter_difficulty], weapon_bonus)

        if combat_result == False: # False = Dead
        # If the player dies
            tprint(f"Your foe has bested you. You died with {resources}kg of food.")
            tprint(Fore.RED + r"""
  ___   __   _  _  ____     __   _  _  ____  ____ 
 / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \
( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /
 \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)
""" + Fore.RESET)
            exit()

            # Game Over
        else: # Didn't die
        # If the player succeeds
            print("You manage to take down your foe, and collect the meat.")
            add_resources(random.randint(3, 7))
            # Keep going
    else:
        print(f"You think better of it, and run away. You have {resources}.")

    # Attack Succeeded or Player Fleeing

    # Choose to hunt or go home
    Hunt_Home = Fore.MAGENTA + "Would you like to go home\n or would you like to hunt more beasts.\n" + Fore.RESET
    tprint(Hunt_Home)

    carry_on = carry_on_or_go_home_prompt()

    if carry_on == 1: # 1 = Go Home, 2 = Carry On
        # If they choose to go home, Game Over
        epilogue()
        tprint(Fore.GREEN + r"""
 _  _  __   _  _    _  _  __  __ _ 
( \/ )/  \ / )( \  / )( \(  )(  ( \
 )  /(  O )) \/ (  \ /\ / )( /    /
(__/  \__/ \____/  (_/\_)(__)\_)__)
""" + Fore.RESET)
        exit()

    # End of main loop (loops if they continue)