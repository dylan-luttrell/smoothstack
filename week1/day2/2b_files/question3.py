""" 
Author: Dylan Luttrell
Description: program takes a positive integer and produces a dictionary with the keys as 1..n, with n being the number given, and values being the respective key squared
"""

def n_squared(n: int) -> int:
    """ returns dictionary with 1...n as keys and key*key as the value """
    squares = {}
    for i in range(1, n + 1):
        squares[i] = i * i
    
    return squares

n = None

while not n:
    num = input("Enter an integer greater than 0: ")
    try:
        n = int(num)
        assert n > 0
    except:
        print("invalid input. Please enter an integer value of one or greater")
        
print(n_squared(n))