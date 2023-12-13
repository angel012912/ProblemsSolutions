#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    res = []
    i = 0
    dif = 0
    while i < len(a):
        if i > 0 and dif + a[i] - a[i-1] > 1:
           res.append(a[:i])
           a = a[i:]
           i = 0
           dif = 0
        else:
            if i > 0:
                dif += a[i] - a[i-1]
            i +=1  
    if len(a) > 0:
        res.append(a)
    max = float("-inf")
    for arr in res:
        if len(arr) > max:
            max = len(arr)    
    return max

if __name__ == '__main__':
    a = [1, 2, 2, 3, 1, 2]
    result = pickingNumbers(a)
    print(result)