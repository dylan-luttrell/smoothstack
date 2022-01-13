""" 
Author: Dylan Luttrell
Description: a set of functions with various utilities
"""
from typing import List

def func() -> None:
    """ prints 'Hello World' """
    print("Hello World")
    
def func1(name: str) -> None:
    """ prints hello with given name """
    print(f"Hi My name is {name}")
    
def func3(x: str, y: str, z: bool) -> str:
    """ returns x if z is true, else y """
    if z:
        return x
    
    return y

def func4(x: int, y: int) -> int:
    """ returns product of x and y """
    return x * y

def is_even(n: int) -> bool:
    """ returns True if n is even, else False """
    return n % 2 == 0

def x_is_greater(x: int, y: int) -> int:
    """ returns True if x is greater than y, else False """
    if x > y:
        return x
    
    return y

def sum_of_nums(*nums: int) -> int:
    """  """
    acc = 0
    for n in nums:
        acc += n
        
    return acc

def even_list_of_nums(*nums: int) -> List[int]:
    """  """
    return [n for n in nums if n % 2 == 0]

def even_odd(string: str) -> str:
    """ returns a string will all off letters in lowercase and all even in uppercase """
    results = ""
    
    for letter in string:
        if is_even(ord(letter) + 1):
            results += letter.upper()
        else:
            results += letter.lower()
    
    return results

def lesser_if_even(x:int, y: int) -> int:
    """ returns the lesser number if both numbers are even, otherwise returns greater number """
    if is_even(x) and is_even(y):
        return x if x < y else y
    
    return x if x > y else y

def square(n: int) -> int:
    """ returns the square of n """
    return n * n

def cap_first_and_fourth(string: str) -> str:
    """ returns string with first and fourth character capitalized """
    if len(string) == 0:
        """ if string is empty, return string """
        return string
    elif len(string) < 4:
        """ if string is less than four characters, only capitalize first character """
        return string[0].upper() + string[1:]

    return string[0].upper() + string[1:3] + string[3].upper() + string[4:]

