#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s)%2 != 0:
          return -1
    mid = len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]
    print(s1, s2)
    res = 0
    for i in s1:
        encontrado = False
        for a in range(len(s2)):
             if i == s2[a]:
                s2 = s2[:a]+s2[a+1:]
                encontrado = True
                break                          
        if not encontrado:
            res += 1
    return res

if __name__ == '__main__':
        s = 'hhpddlnnsjfoyxpciioigvjqzfbpllssuj'
        result = anagram(s)
        print(result)