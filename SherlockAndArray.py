#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    lastSumLeft = 0
    lastSumRight = 0
    for i in range(len(arr)):
        if i == 0:
            lastSumLeft = sum(arr[:i])
            lastSumRight = sum(arr[i+1:])
        else:
            lastSumLeft += arr[i-1]
            lastSumRight -= arr[i]
        if lastSumLeft == lastSumRight:
            return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
