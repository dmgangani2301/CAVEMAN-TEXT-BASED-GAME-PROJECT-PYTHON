import random
import sys
from time import sleep
from colorama import init, Fore
init()


death_by_animal = ["The animal bested you. ", "You died from the ferocious bite of the animal" , "The saber tooth tiger devours your body"]

random_number = random.randint(0, 2)

random_outcome = death_by_animal[ random_number ]

def tprint(words):
    for char in words:
        sleep(0.090)
        sys.stdout.write(char)
        sys.stdout.flush()

dead = (Fore.RED + f"{random_outcome}")

tprint(dead)