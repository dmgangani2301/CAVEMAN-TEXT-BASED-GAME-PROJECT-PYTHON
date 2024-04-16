import random
import sys
from time import sleep
from colorama import init, Fore
init()


success_animal = ["You skillfully overcome the creature,\n emerging victorious with a sense of mastery over the wilderness.",
                  "You obliterate the creature with one fell swoop."]


random_number = random.randint(0, 1)

random_outcome = success_animal[ random_number ]

def tprint(words):
    for char in words:
        sleep(0.090)
        sys.stdout.write(char)
        sys.stdout.flush()

animal = (Fore.GREEN + f"{random_outcome}")

tprint(animal)