""" 
Author: Dylan Luttrell
Description: program that calculates numbers between 2000 and 3200, inclusive, that are divisible by 7 but not 5
"""

def div_seven_not_five(start: int, end: int) -> list:
    """ returns a list of numbers that are divisible by seven but not five """
    lst = []
    
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 > 0:
            lst.append(i)
    return lst

print("Numbers between 2000 an 3200, inclusive, that are divisible by 7")
print("but not a multiple of 5")
print(", ".join(str(i) for i in div_seven_not_five(2000, 3200)))