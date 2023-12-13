#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    min_diff = float("inf")
    result = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
            result = [arr[i-1], arr[i]]
        elif diff == min_diff:
            result.extend([arr[i-1], arr[i]])
    return result

if __name__ == '__main__':
    arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
    result = closestNumbers(arr)
    print(result)