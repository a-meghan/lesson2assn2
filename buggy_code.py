#Task 1- Code correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


#Task 2- Setting the scene

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    second_action = input("Light a torch or proceed in the dark? ")
    if second_action == "light a torch":
        print("You have come accross a wagon full of supplies!")
    elif second_action == "proceed in the dark":
        print("Your next task is to find some supplies.")


#Task 3- Default path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!")
else:
    pass
    second_action = input("Light a torch or proceed in the dark? ")
    if second_action == "light a torch":
        print("You have come accross a wagon full of supplies!")
    elif second_action == "proceed in the dark":
        print("Your next task is to find some supplies.")
    else:
        pass