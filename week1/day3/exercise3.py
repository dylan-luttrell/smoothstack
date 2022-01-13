""" 
Author: Dylan Luttrell
Description: program that generates a random number and continues to run until said number is guessed
"""
import random

def guess_a_number(start: int, end: int) -> None:
    print(f"guess a number between {start} and {end}")
    
    n = random.randint(start, end)
    guess = None
    
    while guess != n:
        try:
            guess = int(input("enter a number: "))
        except ValueError:
            print("invalid input")
    
    print("Well guessed!")
    
if __name__ == '__main__':
    guess_a_number(1, 9)