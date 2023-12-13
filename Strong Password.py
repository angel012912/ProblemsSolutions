#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    constraints = 4
    numbers = ["0123456789", False]
    lower_case = ["abcdefghijklmnopqrstuvwxyz", False]
    upper_case = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", False]
    special_characters = ["!@#$%^&*()-+", False]
    for i in password:
        if not numbers[1] and i in numbers[0]:
            numbers[1] = True
            constraints -= 1
        if not lower_case[1] and i in lower_case[0]:
            lower_case[1] = True
            constraints -= 1
        if not upper_case[1] and i in upper_case[0]:
            upper_case[1] = True
            constraints -= 1
        if not special_characters[1] and i in special_characters[0]:
            special_characters[1] = True
            constraints -= 1
    if n < 6 and 6-n > constraints:
        return 6-n
    else:
        return constraints


if __name__ == '__main__':
    n = 3
    password = "Ab1"
    answer = minimumNumber(n, password)
    print(answer)