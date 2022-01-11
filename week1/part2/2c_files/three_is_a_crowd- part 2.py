""" 
Author: Dylan Luttrell
Description: part two of the 'three is a crowd' assignment
"""

people = ["James Dean", "Jim Kirk", "Patrick Stewart", "Robert Downey Jr."]

def isCrowded(lst: list) -> str:
    if len(lst) > 3:
        return "this room isn't crowded"
    else:
        return "this room isn't crowded"

print(people)
print(isCrowded(people))

people.pop()
print(people)
print(isCrowded(people))
