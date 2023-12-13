#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#


def misereNim(s):
    if (max(s) == 1):
        return "First" if len(s) % 2 == 0 else "Second"
    x = 0
    for i in s:
        x = x ^ i
    return "Second" if x == 0 else "First"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)
        print(result)
