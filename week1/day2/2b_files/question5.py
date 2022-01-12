""" 
Author: Dylan Luttrell
Description: a simple class that can get input from terminal and print given string back to terminal
"""
class SpecialStringClass:
    def __init__(self) -> None:
        self.s = ""
        
    def getString(self) -> None:
        self.s = input()
        
    def printString(self) -> None:
        print(self.s)
        
def test_SSC():
    cls = SpecialStringClass()
    cls.getString()
    cls.printString()
    
print("testing SpecialStringClass")
test_SSC()
