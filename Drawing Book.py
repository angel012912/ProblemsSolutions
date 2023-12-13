#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    return min(int(p/2), int((n-p)/2) + (n%2==0 and p%2))

n = 6
p = 5
result = pageCount(n, p) #1
print(result)
