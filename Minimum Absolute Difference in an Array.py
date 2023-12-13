#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    minDifference = float("inf")
    for i in range(1, len(arr)):
        dif = abs(arr[i-1] - arr[i])
        if dif < minDifference:
            minDifference = dif
    return minDifference

if __name__ == '__main__':
    arr = [3, -7, 0]
    result = minimumAbsoluteDifference(arr)
    print(result)