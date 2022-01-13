""" 
Author: Dylan Luttrell
Description: program that takes a series of weight, height pairs and calculates the bmi value
"""

def get_bmi(weight: int, height: int) -> str:
    """ returns string indicating weight category """
    bmi = weight / height ** 2
    
    if bmi < 18.5:
        return "under"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "over"
    else:
        return "obese"
    
def main():
    print("input data:")
     
    cnt = -1
    while cnt < 0:
        n = input()
        if n.isdigit():
            cnt = int(n)
        else:
            print("invalid input")
    
    data = []
    for _ in range(cnt):
        d = input().split()
        data.append( ( int(d[0]), float(d[1]) ) )
    
    print() # empty line
    print("answer:")
    
    for d in data:
        print(get_bmi(*d), end=" ")
    print()

if __name__ == '__main__':
    main()