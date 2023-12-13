#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    res = ''
    for c in s:
        mayus = c.isupper()
        ascci = ord(c.lower())
        if 97 <= ascci <= 122:
            ascci = ascci - 96
            nC = ascci + k
            while nC > 26:
                nC = nC - 26
            res += chr(nC+96).upper() if mayus else chr(nC+96)
        else:
            res += c
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
