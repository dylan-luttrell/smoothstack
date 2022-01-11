""" 
Author: Dylan Luttrell
Description: A demonstration of indexing strings, running loops, appending to lists
"""

print("Hello World"[-3])

print("thinker"[2:5])

S = "hello"

print(S[1])

print(S[2:])

print("".join(set("Mississippi")))

def isPalidrome(line: str) -> str:
    """ returns 'Y' if string is palindrome, else 'N' """
    left = 0
    right = len(line) - 1

    # remove cap letters to ensure match
    line = line.lower()
    while left < right:
        if not line[left].isalpha():
            left += 1
        elif not line[right].isalpha():
            right -= 1
        elif line[left] == line[right]:
            left += 1
            right -= 1
        else:
            return "N"
        
    return "Y"

print("input data:")
cnt = -1

while cnt <= 0:
    num = input()
    try:
        cnt = int(num)
    except:
        print("invalid input. Please enter integer value greater than 0")

strings = []
for _ in range(cnt):
    strings.append(input())
    
# create empty line after inputs
print()

print("anwser:")
for s in strings:
    print(isPalidrome(s), end=" ")
    
print()
