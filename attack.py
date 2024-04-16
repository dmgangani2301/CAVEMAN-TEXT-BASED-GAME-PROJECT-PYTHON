import random

def adventure():
    attack_flee = input("Will you (A)ttack or (F)lee: ")
    if attack_flee.strip().capitalize() == 'A':
        attack = ['you lose', 'you win']
        radndom_number = random.randint(0,1)
        random_attack = attack[radndom_number]
        print(random_attack)
    elif attack_flee.strip().capitalize() == 'F':
        flee = ['You escpaped', 'You did not escape']
        radndom_number = random.randint(0,1)
        random_flee = flee[radndom_number]
        print(random_flee)
    else:
        print("Invalid Text")

adventure()