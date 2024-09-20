#Task 1- Code correction
attendees = int(input("Enter number of attendees: "))
if attendees > 100: 
    venue = "large hall"
else:
    venue = "conference room"
print(venue)


#Task 2- Venue selection
attendees = int(input("Enter number of attendees: "))
if attendees > 100: 
    venue = "Large hall"
else:
    venue = "Conference room"
print(venue)
if venue == "Large hall":
    print("We suggest a sound system, which we can include for only $50 extra!")
elif venue == "Conference room":
    print("Maybe you'd like to include a projector for only $50 extra!")


#Task 3- Catering choices
food = input("Would you like a vegetarian meal to be served? ")
if food == "yes":
    print("We highly recommend Veggie Delight Caterers!")
if food == "no":
    print("In that case, we highly recommend Gourmet Meals Caterers!")