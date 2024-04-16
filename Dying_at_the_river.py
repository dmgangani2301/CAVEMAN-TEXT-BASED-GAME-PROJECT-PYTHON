import random


river_outcomes = ["death by falling into the river ", "death by crocodile bite" , "death by piranha disguised as a goldfish"]

random_number = random.randint(0, 2)

random_outcome = river_outcomes[ random_number ]
print(f"You have died.... {random_outcome}!!")