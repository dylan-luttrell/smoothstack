""" 
Author: Dylan Luttrell
Description: program to calculate total order value
"""
from typing import Iterable, List, Any, Tuple
import csv
import os
import sys

def total_price(data: List[List[Any]]) -> List[Tuple[int, int]]:
    """ returns a list of tuples containing order number and total price """
    if len(data) == 0:
        # if list is empty, return empty list
        return []
    
    orders = (line[0] for line in data)
    
    if isinstance(data[0][1], tuple):
        price_data = (line[1][1:] for line in data)
    else:
        price_data = (line[2:] for line in data)
    
    return list(zip(orders, 
                    map(lambda x: x[0] * x[1] + (10 if x[0] * x[1] <= 100 else 0),
                        price_data)))
                    
# #map(lambda x: ( x[0], (x[2] * x[3]) + (10 if x[2] * x[3] <= 100 else 0) ),
#                     data)))

def main():
    filename = os.path.join(sys.path[0], "data.tsv")
    if not os.path.exists(filename):
        print("file missing", file=sys.stderr)
        exit(1)
    
    data_a = []
    data_b = []
    
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for line in reader:
            data_a.append( [int(line[0]), line[1], int(line[2]), float(line[3]) ] ) 
            data_b.append( [int(line[0]), ( line[1], int(line[2]), float(line[3]) ) ] ) 

    # case a, data all in one list
    print(total_price(data_a))
    
    # case b, price data in tuple within list
    print(total_price(data_b))

if __name__ == '__main__':
    main()