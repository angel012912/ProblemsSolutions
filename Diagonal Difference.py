#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left = arr[0][0] + arr[len(arr)-1][len(arr)-1]
    right = arr[0][len(arr)-1] + arr[len(arr)-1][0]
    for a in range(1, len(arr)-1):
        left += arr[a][a]
        right += arr[a][len(arr)-a-1]
    return abs(left - right)
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
