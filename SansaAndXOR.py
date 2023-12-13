#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def sansaXor(arr):
    # Write your code here
    result = 0
    n = len(arr)
    for i in range(n):
        freq = (i+1)*(n-i)
        if freq % 2 == 1:
            result ^= arr[i]
    return result


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        print(result)
