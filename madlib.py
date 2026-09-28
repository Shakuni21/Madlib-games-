print(" Mad Libs Game!")
print("Enter the words when asked.\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")

story = f"""
One day, {name} went to {place}.
There, {name} saw a very {adjective} {animal}.
The {animal} was eating {food}.
Suddenly, the animal started to {verb}!
{name} laughed and ran away.
"""

print("\n Your Mad Libs Story:")
print(story)