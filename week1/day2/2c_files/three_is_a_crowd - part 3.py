""" 
Author: Dylan Luttrell
Description: part three of the 'three is a crowd' assignment
"""

people = ["James Dean", "Jim Kirk", "Patrick Stewart",
          "Robert Downey Jr.", "Kent Clark", "Captain Disallusion"]

def isCrowded(lst: list) -> str:
    if len(lst) > 5:
        return "there is a mob of people in this room"
    elif len(lst) > 2:
        return "this room is crowded"
    elif len(lst) > 0:
        return "this room isn't crowded"
    else:
        return "this  room is empty"

while len(people) > 0:
    print(people)
    print(isCrowded(people))
    people.pop()
    
print(people)
print(isCrowded(people))

