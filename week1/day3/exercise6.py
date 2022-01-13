""" 
Author: Dylan Luttrell
Description: program for counting number of even and odd numbers in a list
"""
from typing import Tuple

def count_even_odd(nums: list) -> Tuple[int, int]:
    """ returns number of even and odd values """
    even = 0
    odd = 0
    
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
            
    return even, odd

def main() -> None:
    print("input a series of comma-seperated numbers below (eg 1, 3, 4, 5")
    try:
        n = [int(n) for n in input().split(",")]
    except ValueError:
        print("invalid input")
        exit(1)
        
        
    even, odd = count_even_odd(n)
    
    print("Number of even numbers :", even)
    print("Number of odd numbers :", odd)
        

if __name__ == '__main__':
    main()