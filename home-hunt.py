import sys
from time import sleep
from colorama import init, Fore
init()


def tprint(words):
    for char in words:
        sleep(0.090)
        sys.stdout.write(char)
        sys.stdout.flush()

Hunt_Home = Fore.MAGENTA + "Would you like to go home\n or would you like to hunt more beasts." + Fore.RESET

tprint(Hunt_Home)  