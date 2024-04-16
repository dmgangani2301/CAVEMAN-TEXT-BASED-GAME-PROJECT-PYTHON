from colorama import init, Fore
import sys
init()

def main():
    print(Fore.RED + "What is your name.")
    name = input(Fore.RED + "My name is "+ Fore.RESET)

    print(Fore.RED + "SO your name is " + Fore.RESET + Fore.BLUE + (name) + Fore.RESET + Fore.RED + " Exccelent")

main()