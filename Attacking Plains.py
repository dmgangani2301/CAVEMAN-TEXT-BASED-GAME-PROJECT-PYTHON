import random 
attacking_plains = ["You spot a rabbit", "You see a wounded deer", "You see a hedgehog" ]
random_number = random.randint(0, 2)
random_attacking_plains = attacking_plains[random_number]
print(f"You have arrived at the plains and {random_attacking_plains}!") 