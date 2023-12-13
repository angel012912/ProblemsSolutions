#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    unfairness = float("inf")
    for a in range(len(arr)-k+1):
        posible = arr[a:a+k]
        posUn = posible[-1]-posible[0]
        if unfairness > posUn:
            unfairness = posUn
    return unfairness

if __name__ == '__main__':
    k = 3  
    arr = [100, 200, 300, 350, 400, 401, 402]
    result = maxMin(k, arr)
    print(result)