""" 
Author: Dylan Luttrell
Description: exercises for assignment 2b
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
