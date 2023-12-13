#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def all3x3PosibleMagicSquares():
    return [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]


def formingMagicSquare(s):
    posibles = all3x3PosibleMagicSquares()
    minTotalCost = float('inf')
    for i in range(len(posibles)):
        totalCost = 0
        for indexRow in range(len(s)):
            for indexCol in range(len(s[indexRow])):
                totalCost += abs(s[indexRow][indexCol] -
                                 posibles[i][indexRow][indexCol])
        if totalCost < minTotalCost:
            minTotalCost = totalCost
    return minTotalCost


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
