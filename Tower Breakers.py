#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    return 2 if n % 2 == 0 or m == 1 else 1

if __name__ == '__main__':
    n = 2
    m = 2
    result = towerBreakers(n, m)
    print(result)
