#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
def flip(s):
    res = ''
    for i in s:
        if i == '0':
            res += '1'
        else:
            res += '0'
    return res

def flippingBits(n):
    # Write your code here
    binary = flip(bin(n).split('b')[1])
    zeros = '1'*(32-len(binary))
    binary = zeros+binary
    integer = int(binary, 2)
    return integer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
