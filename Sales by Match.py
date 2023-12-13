#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    res = 0
    restante = []
    for a in ar:
        if a in restante:
            res += 1
            restante.remove(a)
        else:
            restante.append(a)
    return res


if __name__ == '__main__':
    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(result)
