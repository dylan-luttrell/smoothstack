""" 
Author: Dylan Luttrell
Description: construct a pyramid of asterics of 5 width
"""

def build_pyramid(n: int) -> None:
    """ prints a pyramid that is n wide and 2n - 1 tall """
    structure = [""] * (n * 2 - 1)
    
    for i in range(n):
        for _ in range(i + 1):
            structure[i] += "* "
            
        structure[-(i+1)] = structure[i]
            
    print("\n".join(structure))
        
if __name__ == '__main__':
    build_pyramid(5)