from colorama import init, Fore
import random
import sys
from time import sleep
import os
init()

def tprint(words):
    for char in words:
        sleep(0.060)
        sys.stdout.write(char)
        sys.stdout.flush()


text = r"""
  ___   __   _  _  ____     __   _  _  ____  ____ 
 / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \
( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /
 \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)
      """



os.system("cls")
tprint(Fore.RED + text)


