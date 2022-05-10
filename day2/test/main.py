#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix, q):
    n = 2*q
    i, res = 0, 0
    while(i<q):
        j = 0
        while(j<q):
            elem = matrix[i][j]
            sim_vert = matrix[i][n-1-j]
            sim_horiz = matrix[n-1-i][j]
            sim_diag = matrix[n-1-i][n-1-j]
            res += max([elem, sim_vert, sim_horiz, sim_diag])
            j+=1
        i+=1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix, n)
        fptr.write(str(result) + '\n')
    fptr.close()
