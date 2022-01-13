""" 
Author: Dylan Luttrell
Description: program that generates a list of numbers that are divisible by 7 and 5
"""

def magic_numbers(start: int, end: int) -> list:
    """ returns a list of numbers that are both divisible by 7 and a multiple of 5 """
    results = []
    
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            results.append(i)
            
    return results


S = 1500
E = 2700

print(magic_numbers(S, E))