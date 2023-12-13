#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

#Function to check if s is is beautiful

def separateNumbers(s):
    mid = len(s)//2 + 1
    if s[0] == '0':
        print("NO")
        return
    for i in range(1, mid):
        first = int(s[:i])
        current = first
        j = i
        while j < len(s):
            current += 1
            posible = s[j:j+len(str(current))]
            if posible == str(current):
                j += len(str(current))
            else:
                break
        if j == len(s):
            print("YES", first)
            return
    print("NO")

if __name__ == '__main__':
    #58589967442418995858996744241900
    #58589967442418995858996744231900
    #56345303562552205634530356255221
    #56345303562552205634530356155221
    #26828966706901802682896670690181
    #26828966706901802682896679690181
    #29247155344093442924715534409345
    #29247155344093442924715524409345
    #76869698582486267686969858248627
    #76869698582486267686969758248627
    s = "56345303562552205634530356255221"
    separateNumbers(s)
