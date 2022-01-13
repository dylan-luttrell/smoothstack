""" 
Author: Dylan Luttrell
Description: program for reversing a word given
"""

def reverse_word(word: str) -> str:
    return word[::-1]

def main():
    word = input("enter a word to reverse:")
    print(reverse_word(word))
    
if __name__ == '__main__':
    main()