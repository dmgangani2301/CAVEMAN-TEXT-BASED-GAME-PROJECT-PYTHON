import random

class Bush:
    def __init__(self, health=100):
        self.health = health

    def attack(self, strategy):
        if strategy == "chop":
            damage = random.randint(10, 20)
        elif strategy == "burn":
            damage = random.randint(5, 15)
        elif strategy == "poison":
            damage = random.randint(15, 25)
        else:
            print("Invalid attack strategy!")
            return

        self.health -= damage
        print(f"Attacking with {strategy}! Caused {damage} damage.")
        if self.health <= 0:
            print("The bush has been cleared!")
        else:
            print(f"Bush health: {self.health}")

def main():
    bush = Bush()

    while bush.health > 0:
        print("\nChoose an attack strategy:")
        print("1. Chop")
        print("2. Burn")
        print("3. Poison")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bush.attack("chop")
        elif choice == "2":
            bush.attack("burn")
        elif choice == "3":
            bush.attack("poison")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()