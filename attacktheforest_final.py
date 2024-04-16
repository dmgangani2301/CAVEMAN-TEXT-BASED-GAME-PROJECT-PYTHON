import random

# Describe Attacking Forest Easy
attacking_forest_easy = ["Rabbit", "Forest Grouse", "Cottontail Hare", "Red Squirre"]
random_number = random.randint(0,2)
random_attacking_forest_easy = attacking_forest_easy[random_number]
print(f"You found a cute {random_attacking_forest_easy}. You are doing great!")


# Describe Attacking Forest Medium 

attacking_forest_medium = ["Bear", 'Deer', "Volf"]
random_number = random.randint(0,2)
random_attacking_forest_medium = attacking_forest_medium[random_number]
print(f"You are a great hunter. You came to the forest and you managed to find a {random_attacking_forest_medium}.")

# Describe Attacking Forest Hard 

attacking_forest_hard = ["Bear", 'Deer', "Volf"]
random_number = random.randint(0,2)
random_attacking_forest_hard = attacking_forest_hard[random_number]
print(f"It was a terrible day for you and a huge {random_attacking_forest_hard} striked you but you are fighting courageously.")