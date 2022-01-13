""" 
Author: Dylan Luttrell
Description: program for printing numbers 0 - 6 except 3 and 6
"""


from typing import Tuple


def print_such_except_thus(start: int, end: int, exception: Tuple[int]) -> None:
    """ prints a number between start and end, inclusive, unless it is in exception """
    
    for i in range(start, end + 1):
        if i in exception:
            continue
        
        print(i, end=" ")
    
    print()
    
def main() -> None:
    print_such_except_thus(0, 6, (3, 6))
    
if __name__ == '__main__':
    main()