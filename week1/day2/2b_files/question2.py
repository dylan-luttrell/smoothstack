""" 
Author: Dylan Luttrell
Description: this program takes a series of integers and calculates the factorial of each
"""
def factorial(n: int) -> int:
    if n < 0:
        # special case for negative factorials
        return -1 * factorial(-n)
    elif n < 2:
        # if n is 1 or 2
        return n
    
    return n * factorial(n-1)

cnt = -1
print("factorials")
while cnt <= 0:
    num = input("How many would you like to parse? ")
    try:
        cnt = int(num)
    except:
        print("invalid input. Please enter integer value greater than 0")
        
nums = []
while cnt > 0:
    num = input()
    try:
        nums.append(int(int(num)))
        cnt -= 1
    except:
        print("invalid number. Please enter integers only")

print()
print("output")
for i, n in enumerate(nums):
    if i > 0:
        print(", ", end="")
    print(factorial(n), end="")
print()
