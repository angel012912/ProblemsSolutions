#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    sights = {}
    for i in arr:
        if i in sights:
            sights[i] += 1
        else:
            sights[i] = 1
    res = [float("inf"), float("-inf")]
    for key in sights:
        if sights[key] > res[1] or (sights[key] == res[1] and key < res[0]):
            res = [key, sights[key]]
    return res[0]            

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    result = migratoryBirds(arr)
    print(result)
