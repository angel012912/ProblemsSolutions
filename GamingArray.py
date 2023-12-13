#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def gamingArray(arr):
    countMax = 0
    max = float("-inf")
    for n in arr:
        if n > max:
            max = n
            countMax += 1
    if countMax % 2 == 0:
        return "ANDY"
    return "BOB"


if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)
        print(result)
