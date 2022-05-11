#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List


#
# Complete the '2legoblocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr: list, n: int):
    i, j,k, diag1, diag2 = 0, n-1, 0, 0, 0
    while i < n and k > -1:
        diag1 += arr[i][i]
        diag2 += arr[k][j]
        i += 1
        k += 1
        j -= 1
    return abs(diag1 - diag2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
