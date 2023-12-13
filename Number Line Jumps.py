#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 == x2:
        return "YES"
    elif x1 > x2 and v2 > v1:
        if (x1 - x2) % (v2-v1) == 0:
            return "YES"
        else:
            return "NO"
    elif x2 > x1 and v1 > v2:
        if (x2 - x1) % (v1-v2) == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    x1, v1, x2, v2 = 1571, 4240, 9023, 4234
    result = kangaroo(x1, v1, x2, v2)
    print(result)
