#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    values = [0, 0, 0]
    for i in arr:
        if i > 0:
            values[0] += 1
        elif i == 0:
            values[1] += 1
        elif i < 0:
            values[2] += 1
    print("{:.6f}".format(values[0]/len(arr)))
    print("{:.6f}".format(values[2]/len(arr)))
    print("{:.6f}".format(values[1]/len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
