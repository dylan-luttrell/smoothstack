""" 
Author: Dylan Luttrell
Description: 
"""

varied_lst = [42, "life", 3.142]

print(varied_lst)

lst=['a','b','c']

print(lst[1:])

weekdays = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

print(weekdays)

d = {'k1':[1,2,3]}

# d[k1][1] would result in an error as k1 is not a variable. Assumed typo and added quotation marks
print(d['k1'][1])

lstA = [1,[2,3]]
tupleA = tuple(lstA)

print(tupleA)

letter_set = set("Mississippi")
print(letter_set)

letter_set.add('X')
print(letter_set)

print(set([1,1,2,3]))



########################################################################
# question 1

def div_seven_not_five(start: int, end: int) -> list:
    """ returns a list of numbers that are divisible by seven but not five """
    lst = []
    
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 > 0:
            lst.append(i)
    return lst

print("Numbers between 2000 an 3200, inclusive, that are divisible by 7")
print("but not a multiple of 5")
print(", ".join(str(i) for i in div_seven_not_five(2000, 3200)))

########################################################################
# question 2

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


########################################################################
# question 3

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


########################################################################
# question 4

print("please enter a series of numbers seperated by commas: ")
# getting input and striping each one so there are no spaces
nums = [n.strip() for n in input().split(",")] 
tuple_nums = tuple(nums)

print()
print("output")
print(nums)
print(tuple_nums)


########################################################################
# question 5

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
