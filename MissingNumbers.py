#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    # Write your code here
    result = []
    numbersInBrr = {}
    for number in brr:
        if number in numbersInBrr:
            numbersInBrr[number] += 1
        else:
            numbersInBrr[number] = 1
    for number in numbersInBrr:
        if number in arr:
            if numbersInBrr[number] > arr.count(number):
                result.append(number)
        else:
            result.append(number)
    result.sort()
    return result


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    print(result)
