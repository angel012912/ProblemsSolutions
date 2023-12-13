#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    countValley = 0
    latitude = 0
    floor = True
    for step in path:
        if step == 'D':
            latitude -= 1
            if floor:
                countValley += 1
        elif step == 'U':
            latitude += 1
        if latitude == 0:
            floor = True
        else:
            floor = False
    return countValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
