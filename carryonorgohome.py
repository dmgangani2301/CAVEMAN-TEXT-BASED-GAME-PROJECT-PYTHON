score = 100      
def carry_on_or_go_home_prompt():
    global score

    print("It's been a long day. Would you like to continue or go home ?")
    # SET UP A LOOP WHICH WILL ASK FOR INPUT UNTILL IT GETS VALIDATION.
    choice = 0
    # FOR LOOP IS BEST FOR A SPECIFIC RANGE OF DATA AND WHILE LOOP IS BETTER FOR LOOPING WHICH IS SOMETHING UNTILL IT IS COMPLETED.

    while choice == 0:
        choice_input = input("Press 1 if you want to go home, Press 2 to keep hunting: ")
        # INPUT WILL FOR WAITING FOR USERS TO TYPE SOME OF THE CHOICES OR OPTIONS.

        if choice_input == "1":
        # WE SHOULD DESCRIBE THE CHOICE TO GO HOME.
            
            print(f"It's been a long day, you've arrived home safely. Enjoy the rest of the day. You have scored {score}")
            choice = 1 

        elif choice_input == "2":
            print(f"You've decided to continue, your current score is {score} Good luck on your next hunt.")
            choice = 2
        else:
            print("Invalid Key, Please try again.")

    return choice                           # RETURNING THE VALUE ACCORDING TO USER'S CHOICE.
print(carry_on_or_go_home_prompt())
