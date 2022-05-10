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

def gridChallenge(grid, n):
    i = 0
    row_len = len(grid[0])
    gr_len = len(grid)
    while i < gr_len-1:
        row = sorted(grid[i])
        next_row = sorted(grid[i + 1])
        j = 0
        while j < row_len:
            if row[j] > next_row[j]:
                return "NO"
            j += 1
        i += 1
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid, t_itr)

        fptr.write(result + '\n')

    fptr.close()
