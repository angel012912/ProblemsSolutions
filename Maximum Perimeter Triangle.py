#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
def non_degenerate(arr):
    if arr[0] + arr[1] > arr[2] and arr[1] + arr[2] > arr[0] and arr[2] + arr[0] > arr[1]:
        return True
    return False

def maximumPerimeterTriangle(sticks):
    # Write your code here
    posibles = []
    for l in range(len(sticks)):
       posible = [sticks[l]]
       for lR in range(l+1, len(sticks)):
            posible.append(sticks[lR])
            for lRR in range(lR+1, len(sticks)): 
                if posible + [sticks[lRR]] not in posibles and non_degenerate(posible + [sticks[lRR]]):
                    posibles.append(posible + [sticks[lRR]])
                posible = [sticks[l], sticks[lR]]
            posible = [sticks[l]]
    maximum = [float("-inf"), float("-inf")]
    if len(posibles) == 0:
        return [-1]
    for pos in posibles:
        if sum(pos) > maximum[1]:
            maximum = [pos, sum(pos)]
        elif sum(pos) == maximum[1] and max(pos) > max(maximum[0]):
            maximum = [pos, sum(pos)]
    maximum[0].sort()
    return maximum[0]

if __name__ == '__main__':
    sticks = [3900717, 53516059, 288589053, 23189292, 21487730, 94997775, 260173, 41298280, 47784002, 23032379, 67686298, 48162481, 44775136, 47340544, 2165965, 34202258, 81746554, 57179615, 6240306, 33110389, 7424599, 41389013, 480910581, 86150390, 13777985, 96265144, 89266112, 316419, 74896112, 192317271, 63729818, 40712188, 19111441, 25556170, 33808338, 96043868, 90508879, 88229925, 62520492, 49835454, 78096135, 54610351, 78888361, 10300724, 34843471, 38439667, 81892481, 16254176, 24261693, 84190486]
    # [94997775,96043868, 96265144]
    result = maximumPerimeterTriangle(sticks)
    print(result)
