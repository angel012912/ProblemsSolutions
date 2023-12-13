#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    possiblesReArranges = [grid]
    for index in range(len(grid)):
        possibleReArrangedGrid = grid
        for indexGrid, row in enumerate(possibleReArrangedGrid):
            if indexGrid == index:
                newRow = ''
                for char in sorted(row):
                    newRow += char
                possibleReArrangedGrid[indexGrid] = newRow
        possiblesReArranges.append(possibleReArrangedGrid)
    for possibleReArrangedGrid in possiblesReArranges:
        for index in range(len(possibleReArrangedGrid[0])):
            col = ''
            for row in possibleReArrangedGrid:
                col += row[index]
            if col != ''.join(sorted(col)):
                break
        else:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
