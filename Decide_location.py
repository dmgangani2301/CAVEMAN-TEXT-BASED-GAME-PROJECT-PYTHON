def decide_location(player_choice):
    return player_choice

def main():
    print("Welcome to the decision maker!")
    print("Choose a location to go: Hunt, Gather, or Fish")
    
    while True:
        player_choice = input("Enter your choice: ").strip().capitalize()
        if player_choice in ['Hunt', 'Gather', 'Fish']:
            print("You have chosen to go", player_choice)
            break
        else:
            print("Invalid choice. Please choose from Hunt, Gather, or Fish.")
    
    location = decide_location(player_choice)
    print("You are going to:", location)

if __name__ == "__main__":
    main()