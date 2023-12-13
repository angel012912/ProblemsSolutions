#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here 
    res = arr[d:]+ arr[:d]
    return res

if __name__ == '__main__':
    d = 4
    arr = [1, 2, 3, 4, 5]
    result = rotateLeft(d, arr)
    print(result)