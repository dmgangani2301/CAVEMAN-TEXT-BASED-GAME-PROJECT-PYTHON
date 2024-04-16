import random

class Animal:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

class AttackingRiverEasy:
    def __init__(self, player_health=100, num_animals=3):
        self.player_health = player_health
        self.num_animals = num_animals
        self.player_position = 0
        self.animals = [Animal("Wolf", 50, 10),
                        Animal("Bear", 80, 15),
                        Animal("Lion", 70, 12)]

    def encounter_animals(self):
        """Encounter random animals at the destination."""
        print("You have arrived at the destination and encounter some animals!")
        for _ in range(self.num_animals):
            animal = random.choice(self.animals)
            print(f"A wild {animal.name} appears!")
            while self.player_health > 0 and animal.health > 0:
                print(f"Your health: {self.player_health}")
                print(f"{animal.name}'s health: {animal.health}")
                action = input("Choose your action (attack/defend): ").lower()
                if action == "attack":
                    animal.health -= random.randint(5, 15)
                    print(f"You attack the {animal.name}!")
                    if animal.health > 0:
                        self.player_health -= animal.attack_power
                        print(f"The {animal.name} counterattacks!")
                    else:
                        print(f"You have defeated the {animal.name}!")
                elif action == "defend":
                    damage_blocked = random.randint(5, 10)
                    self.player_health -= max(animal.attack_power - damage_blocked, 0)
                    print(f"You defend against the {animal.name}!")
                else:
                    print("Invalid action. Try again.")
                if self.player_health <= 0:
                    print("You have been defeated!")
                    return
        print("You have successfully defeated all the animals and reached the destination!")


if __name__ == "__main__":
    game = AttackingRiverEasy()
    game.encounter_animals()

   