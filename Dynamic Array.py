#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    for query in queries:
        idx = ((query[1]^lastAnswer)%n)
        if query[0] == 1:
            arr[idx].append(query[2])
        elif query[0] == 2:
            lastAnswer = arr[idx][query[2]%len(arr[idx])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    n = 2
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    result = dynamicArray(n, queries)
    for answer in result:
        print(answer)

