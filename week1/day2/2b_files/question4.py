""" 
Author: Dylan Luttrell
Description: takes a series of comma seperated nubmers and converts them into a list and tuple
"""
print("please enter a series of numbers seperated by commas: ")
# getting input and striping each one so there are no spaces
nums = [n.strip() for n in input().split(",")] 
tuple_nums = tuple(nums)

print()
print("output")
print(nums)
print(tuple_nums)
