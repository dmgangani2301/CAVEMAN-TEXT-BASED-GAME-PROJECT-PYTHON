import random

class Resource:
    def __init__(self, name, amount_range):
        self.name = name
        self.amount_range = amount_range

class ResourceLocation:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

class ResourceGatheringGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_inventory = {}
        self.locations = [
            ResourceLocation("Forest", [Resource("Wood", (1, 5))]),
            ResourceLocation("Mine", [Resource("Ore", (1, 3))])
        ]

    def gather_resources(self, location_index):
        location = self.locations[location_index]
        print(f"You're at {location.name}.")
        for resource in location.resources:
            amount = random.randint(*resource.amount_range)
            print(f"You've gathered {amount} {resource.name}.")
            if resource.name in self.player_inventory:
                self.player_inventory[resource.name] += amount
            else:
                self.player_inventory[resource.name] = amount

    def display_inventory(self):
        print(f"{self.player_name}'s Inventory:")
        for resource, amount in self.player_inventory.items():
            print(f"{resource}: {amount}")


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = ResourceGatheringGame(player_name)

    while True:
        print("\nLocations:")
        for i, location in enumerate(game.locations):
            print(f"{i + 1}. {location.name}")

        try:
            location_choice = int(input("Choose a location to gather resources: "))
            if 1 <= location_choice <= len(game.locations):
                game.gather_resources(location_choice - 1)
                game.display_inventory()
            else:
                print("Invalid choice. Please enter a valid location.")
        except ValueError:
            print("Invalid input. Please enter a number.")