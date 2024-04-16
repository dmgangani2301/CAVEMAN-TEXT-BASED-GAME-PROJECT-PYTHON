import random
import sys
from time import sleep
from colorama import init, Fore
init()


death_by_bush = ["You got tangled in the thorny embrace of the bush and succumbed to its prickly grasp.", "In your haste, you failed to notice the carnivorous nature of the bush, and it devoured you whole." , "You tripped over the roots of the bush and fell into its depths, never to emerge."]

random_number = random.randint(0, 2)

random_outcome = death_by_bush[ random_number ]

def tprint(words):
    for char in words:
        sleep(0.090)
        sys.stdout.write(char)
        sys.stdout.flush()

dead_by_bush = (Fore.RED + f"{random_outcome}")

tprint(dead_by_bush)