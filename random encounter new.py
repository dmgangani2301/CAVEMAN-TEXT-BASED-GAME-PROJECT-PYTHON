import random
from colorama import Fore

encounter_difficulty = None
good_weapon = None
bad_weapon = None
location = input(Fore.LIGHTGREEN_EX + "plains, forest, river " + Fore.RESET)

def gererate_random_encounter(location):
    global good_weapon
    global bad_weapon
    global encounter_difficulty

    encounter_difficulty = random.randint(0,2)

    if location == "plains":
        if encounter_difficulty > 1:
            good_weapon = Fore.GREEN + "spear" + Fore.RESET
            bad_weapon = Fore.RED + "club" + Fore.RESET
        else:
            good_weapon = Fore.GREEN + "club" + Fore.RESET
            bad_weapon = Fore.RED + "knife" + Fore.RESET

    elif location == "forest":
        if encounter_difficulty > 1:
            good_weapon = Fore.GREEN + "club" + Fore.RESET
            bad_weapon = Fore.RED + "knife" + Fore.RESET
        else:
            good_weapon = Fore.GREEN + "knife" + Fore.RESET
            bad_weapon = Fore.RED + "spear" + Fore.RESET

    elif location == "river":
        if encounter_difficulty > 1:
            good_weapon = Fore.GREEN + "knife" + Fore.RESET
            bad_weapon = Fore.RED + "spear" + Fore.RESET
        else:
            good_weapon = Fore.GREEN + "spear" + Fore.RESET
            bad_weapon = Fore.RED + "club" + Fore.RESET
        

gererate_random_encounter(location)