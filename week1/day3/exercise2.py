""" 
Author: Dylan Luttrell
Description: program to convert to and from celsius and fahrenheit
"""

def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32

def get_temp():
    temp = None
    
    while not temp:
        try:
            temp = float(input("enter a temp: "))
        except ValueError:
            print("invalid input")
            
    return temp

def main():
    print("1. convert celsius to fahrenheit")
    print("2. convert fahrenheit to celsius")
    
    mode = None
    while not mode:
        select = input("make a selection: ")
        if select in ("1", "2"):
            mode = select
        else:
            print("invalid input")
    
    if mode == "1":
        print(to_fahrenheit(f"{get_temp():.0f}"))
    else:
        print(to_celsius(f"{get_temp():.0f}"))
        
        
if __name__ == '__main__':
    main()