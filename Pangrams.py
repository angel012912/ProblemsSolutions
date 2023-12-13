#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    abc = [chr(x+96) for x in range (1, 27)]
    for c in s:
        if c.lower() in abc:
            abc.remove(c.lower())
            
    if len(abc)<= 0:
        return 'pangram'
    else:
        return 'not pangram'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
