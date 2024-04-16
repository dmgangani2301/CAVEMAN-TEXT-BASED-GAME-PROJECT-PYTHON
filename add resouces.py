resources = 0

def  add_resources(amount):
    global resources
    resources = resources + amount
    print ("well done" )
    print (f"You have recieved {amount} kg of food")
    print(f" You now have {resources} kg ")

add_resources(25)