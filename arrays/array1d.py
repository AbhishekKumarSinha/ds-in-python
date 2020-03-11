"""
Array-1D Example in Python3

from array import *

arrayName = array(typecode, [Initializers])

typecode                Value
    b       Represents signed integer of size 1 byte/td>
    B       Represents unsigned integer of size 1 byte
    c       Represents character of size 1 byte
    i       Represents signed integer of size 2 bytes
    i       Represents unsigned integer of size 2 bytes
    f       Represents floating point of size 4 bytes
    d       Represents floating point of size 8 bytes
"""

from array import array

def disp_arr(arr, mesg="Array Elements :"):
    """
    Function to print array elements
    """
    print("%s [" %(mesg), end=' ')
    for ar_item in arr:
        print(ar_item, end=' ')
    print(']')

ARR = array('i', [10, 20, 30, 40, 50])

# Print Array Elements
disp_arr(ARR)

# Access Array Elements using Index
print("Array Value at 0 : %d "%(ARR[0]))
print("Array Value at 2 : %d "%(ARR[2]))

# Insertion Operation
ARR.insert(1, 100)
disp_arr(ARR, "Array Elements after inserting 100 at 1 position :")

# Deletion Operation
ARR.remove(100)
disp_arr(ARR, "After removing 100 : ")

# Search Operation
print(ARR.index(40))

# Update Operation
ARR[2] = 11
disp_arr(ARR, "After Update : ")
