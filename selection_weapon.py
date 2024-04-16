selected_weapon = None

print("you see the club, it has a long, smooth brown handle, going up to a thicker end thats nobbled for extra damage. \nThis will be great for bashing an enemy")
print("you see the knife, its comprised of a sharpened stone, stuck, sturdily into a piece of wood for a handle. \nThis will be great for forraging")
print("you see the spear, its comprised of a sharpened stone, stuck, sturdily into a long piece of wood, around a meter long, that should be great for fishing")

weapons = ["club", "knife", "spear"]


def selection_weapon():
    selection = int(input("You have an option: 1 - for club, 2 - for knife, 3 - for spear. \nPlease, select the number: 1 or 2 or 3   "))

    if selection == 1:
        print(f"You have a {weapons[0]}!")
        return weapons[0]
    elif selection == 2:
        print(f"You have a {weapons[1]}!")
        return weapons[1]
    elif selection == 3:
        print(f"You have a {weapons[2]}!")
        return weapons[2]
    else:
        print("Try again! Please, select the number: 1 or 2 or 3")
        return None

selected_weapon = selection_weapon()
