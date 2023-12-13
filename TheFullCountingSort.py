#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    # Write your code here
    for index in range(len(arr)):
        if index < len(arr) // 2:
            arr[index][1] = '-'
    arr.sort(key=lambda x: int(x[0]))
    for element in arr:
        print(element[1], end=' ')


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
