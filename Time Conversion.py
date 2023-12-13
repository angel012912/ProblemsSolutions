#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    dayTime = s[-2:]
    time = int(s[:2])
    if dayTime == 'AM' and time == 12:
        s = '00'+s[2:8]
    elif dayTime == 'PM' and time < 12:
        s=str(time+12)+s[2:8]  
    else:
        s=s[:8]
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
