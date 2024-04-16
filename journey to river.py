# print ("Go to the river")
# print ("Your journey progress's quickly , you find yourself at an opening to a large lake ...")
# print ("")


import random

journeys = ["windy", "sunny", "raining" ]

random_number = random.randint(0, 2)

random_journey = journeys[random_number]

print(f"The weather is {random_journey}!")