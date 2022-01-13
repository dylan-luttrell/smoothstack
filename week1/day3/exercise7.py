""" 
Author: Dylan Luttrell
Description: program for printing out data and its type from a given list
"""
from typing import List, Any

def print_data_and_type(data: List[Any]) -> None:
    """ prints out an item and its type from given list data """
    for item in data:
        print(item, type(item))
        
def main():
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    
    print_data_and_type(datalist)


if __name__ == '__main__':
    main()