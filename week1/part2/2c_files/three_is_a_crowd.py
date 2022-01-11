""" 
Author: Dylan Luttrell
"""

people = ["James Dean", "Jim Kirk", "Patrick Stewart", "Robert Downey Jr."]

def isCrowded(lst: list) -> str:
    if len(lst) > 3:
        print("this room is crowded")


isCrowded(people)

people.pop()
isCrowded(people)
