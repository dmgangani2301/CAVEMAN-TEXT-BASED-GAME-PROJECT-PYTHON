import random
import sys
from time import sleep
from colorama import init, Fore
init()


success_fish = ["With practiced skill, you cast your line\n and reel in your catch a shimmering fish gleaming in the sunlight,\n a testament to your resourcefulness in the wild.", "You deftly hook and reel in a lively fish,\n feeling a rush of triumph as it lands in your basket,\n a testament to your prowess in the wilderness."]


random_number = random.randint(0, 1)

random_outcome = success_fish[ random_number ]

def tprint(words):
    for char in words:
        sleep(0.090)
        sys.stdout.write(char)
        sys.stdout.flush()

fish = (Fore.GREEN + f"{random_outcome}")

tprint(fish)