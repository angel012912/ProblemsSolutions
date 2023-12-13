#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    res = []
    for i in range(len(s)):
        if len(s) - i >= m:
            a = [s[i]]
            for b in range(i+1, len(s)):
                if len(a) == m:
                    if sum(a) == d:
                        if a not in res:
                            res.append(a) 
                    a = []
                a.append(s[b])
            if len(a) == m:
                if sum(a) == d:
                    if a not in res:
                        res.append(a) 
    return len(res)

if __name__ == '__main__':
    s = [5, 1, 4, 1, 5, 4, 5, 1, 3, 5, 1, 1, 5, 1, 4, 2, 1, 1, 1, 2, 5]
    d = 15
    m = 7
    result = birthday(s, d, m)
    print("Result: ", result)